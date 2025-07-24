import streamlit as st
import anthropic

# ⛽ Leggi API key e modello dai secrets (più sicuro e senza errori)
api_key = st.secrets["ANTHROPIC_API_KEY"]
ai_model = st.secrets["AI_MODEL"]

# 🧠 Inizializza client Claude
client = anthropic.Anthropic(api_key=api_key)

# 🎯 Titolo e setup iniziale
st.title("💬 Chat con Claude via API (Streamlit + Anthropic)")

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
            model=st.session_state["ai_model"],
            max_tokens=4096,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        ) as stream:
            for text in stream.text_stream:
                full_response += str(text) if text is not None else ""
                message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
