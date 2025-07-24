import anthropic
import streamlit as st

st.set_page_config(page_title="Chat Claude", page_icon="🤖")
st.title("🤖 Claude AI con Upload File - Versione 3.5/4")

# ✅ Lettura delle chiavi dal secrets.toml
api_key = st.secrets["ANTHROPIC_API_KEY"]
ai_model = st.secrets["AI_MODEL"]

# 🔐 Verifica chiave caricata
st.caption(f"🔑 Chiave API caricata (prime 6 cifre): {api_key[:6]}******")
st.caption(f"🤖 Modello attivo: {ai_model}")

# 👉 Crea il client Claude
client = anthropic.Anthropic(api_key=api_key)

# 💾 Inizializza sessione se serve
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

        # 💬 Aggiunge alla cronologia chat
        st.session_state.messages.append({
            "role": "user",
            "content": f"Analizza questo file chiamato `{filename}`:\n\n```php\n{file_content[:4000]}\n```"
        })

        with st.chat_message("user"):
            st.markdown(f"📄 Hai caricato il file: `{filename}`")
            st.code(file_content[:2000], language="php")

# 💬 Input manuale utente
if prompt := st.chat_input("Scrivi qui la tua domanda o richiesta"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 🧠 Risposta AI streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with client.messages.stream(
            max_tokens=4096,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            model=st.session_state["ai_model"],
        ) as stream:
            for text in stream.text_stream:
                if text:
                    full_response += str(text)
                    message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
