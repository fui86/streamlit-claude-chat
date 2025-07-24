import os
import anthropic
import streamlit as st

st.title("Claude 3 by Streamlit")

ai_model = os.environ.get("AI_MODEL")
api_key = os.environ.get("API_KEY")

client = anthropic.Anthropic(api_key=api_key)

# 🔍 Mostra modelli disponibili con la tua API key
if st.button("🎯 Mostra modelli disponibili"):
    try:
        models_response = client.models.list()
        st.subheader("Modelli disponibili:")
        for model in models_response["data"]:
            st.markdown(f"- `{model['id']}`")
    except Exception as e:
        st.error(f"Errore nel recupero dei modelli: {e}")

if "ai_model" not in st.session_state:
    st.session_state["ai_model"] = ai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔁 Mostra messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 📂 Caricamento multiplo file
uploaded_files = st.file_uploader(
    "📁 Carica uno o più file da analizzare",
    type=["php", "txt", "html", "js", "css", "md", "json", "csv"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_content = uploaded_file.read().decode("utf-8")
        filename = uploaded_file.name

        # 💬 Aggiungiamo alla conversazione la richiesta per ogni file
        st.session_state.messages.append({
            "role": "user",
            "content": f"Ecco il file `{filename}`. Analizzalo:\n\n```php\n{file_content[:4000]}\n```"
        })

        with st.chat_message("user"):
            st.markdown(f"📄 Hai caricato il file: `{filename}`")
            st.code(file_content[:2000], language="php")

# 💬 Input da chat utente
if prompt := st.chat_input("Scrivi qui la tua domanda o richiesta"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 🤖 Risposta AI
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with client.messages.stream(
            max_tokens=4096,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            model=st.session_state["ai_model"],
        ) as stream:
            for text in stream.text_stream:
                full_response += str(text) if text is not None else ""
                message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
