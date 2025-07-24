import anthropic
import streamlit as st

st.set_page_config(page_title="Chat Claude", page_icon="🤖")
st.title("🤖 Claude AI con Upload File - Versione 3.5/4")

# ✅ Lettura delle chiavi dal secrets.toml
api_key = st.secrets["ANTHROPIC_API_KEY"]
ai_model = st.secrets["AI_MODEL"]

# 🔐 Verifica chiave caricata
st.caption(f"🔑 Chiave API caricata (prime 6 cifre): {api_key[:6]}******")
st.caption(f"🤖 Modello attivo: {ai_model}")import anthropic
import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Chat Claude", 
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Claude AI con Upload File - Versione 4")

# Sidebar per configurazioni
with st.sidebar:
    st.header("⚙️ Configurazioni")
    
    # Selezione del modello
    model_options = [
        "claude-sonnet-4-20250514",      # Claude Sonnet 4
        "claude-3-5-sonnet-20241022",    # Claude 3.5 Sonnet
        "claude-3-5-haiku-20241022",     # Claude 3.5 Haiku
        "claude-3-opus-20240229"         # Claude 3 Opus
    ]
    
    selected_model = st.selectbox(
        "Seleziona il modello:",
        model_options,
        index=0
    )
    
    # Parametri di configurazione
    max_tokens = st.slider("Max tokens:", 100, 8000, 4096)
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7)
    
    # Pulsante per pulire la chat
    if st.button("🗑️ Pulisci chat"):
        st.session_state.messages = []
        st.session_state.files_processed = []
        st.rerun()

# Lettura delle chiavi dal secrets.toml
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
    
    # Verifica chiave caricata (solo prime 10 caratteri per sicurezza)
    st.caption(f"🔑 API Key: {api_key[:10]}...*** ✅")
    st.caption(f"🤖 Modello selezionato: **{selected_model}**")
    
except KeyError as e:
    st.error(f"❌ Errore: Chiave API non trovata nei secrets. Controlla la configurazione: {e}")
    st.stop()

# Crea il client Claude
try:
    client = anthropic.Anthropic(api_key=api_key)
except Exception as e:
    st.error(f"❌ Errore nella creazione del client Anthropic: {e}")
    st.stop()

# Inizializza la sessione
if "messages" not in st.session_state:
    st.session_state.messages = []

if "files_processed" not in st.session_state:
    st.session_state.files_processed = []

# Area principale
col1, col2 = st.columns([3, 1])

with col2:
    st.subheader("📁 Upload File")
    # Caricamento file
    uploaded_files = st.file_uploader(
        "Carica file da analizzare:",
        type=["php", "py", "txt", "html", "js", "css", "md", "json", "csv", "xml"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    # Mostra file caricati
    if uploaded_files:
        st.write("**File caricati:**")
        for file in uploaded_files:
            st.write(f"📄 {file.name}")

with col1:
    st.subheader("💬 Chat")
    
    # Container per i messaggi
    chat_container = st.container(height=400)
    
    # Mostra messaggi precedenti
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Processo i file caricati
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Evita di processare lo stesso file più volte
        if uploaded_file.name not in st.session_state.files_processed:
            try:
                # Legge il contenuto del file
                file_content = uploaded_file.read().decode("utf-8")
                filename = uploaded_file.name
                
                # Limita la lunghezza del contenuto per evitare token eccessivi
                max_content_length = 3000
                if len(file_content) > max_content_length:
                    file_content = file_content[:max_content_length] + "\n\n... [file troncato]"
                
                # Aggiunge alla cronologia chat
                file_message = f"📄 **File caricato: `{filename}`**\n\n```\n{file_content}\n```\n\nPuoi analizzare questo file e rispondere alle mie domande su di esso."
                
                st.session_state.messages.append({
                    "role": "user",
                    "content": file_message
                })
                
                # Segna il file come processato
                st.session_state.files_processed.append(filename)
                
                # Ricarica la pagina per mostrare il nuovo messaggio
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Errore nel leggere il file {uploaded_file.name}: {e}")

# Input manuale utente
if prompt := st.chat_input("Scrivi qui la tua domanda..."):
    # Aggiunge il messaggio dell'utente
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostra il messaggio dell'utente
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)
    
    # Genera la risposta di Claude
    with chat_container:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Prepara i messaggi per l'API
                api_messages = []
                for msg in st.session_state.messages:
                    if msg["role"] in ["user", "assistant"]:
                        api_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
                
                # Chiamata streaming all'API
                with st.spinner("Claude sta pensando..."):
                    with client.messages.stream(
                        model=selected_model,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        messages=api_messages
                    ) as stream:
                        for text in stream.text_stream:
                            if text:
                                full_response += text
                                message_placeholder.markdown(full_response + "▌")
                
                # Rimuove il cursore e mostra la risposta finale
                message_placeholder.markdown(full_response)
                
                # Aggiunge la risposta alla sessione
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": full_response
                })
                
            except anthropic.AuthenticationError:
                error_msg = "❌ **Errore di autenticazione**: Verifica che l'API key sia corretta nei secrets di Streamlit Cloud."
                message_placeholder.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": error_msg
                })
                
            except anthropic.NotFoundError as e:
                error_msg = f"❌ **Modello non trovato**: {e}. Verifica il nome del modello."
                message_placeholder.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": error_msg
                })
                
            except Exception as e:
                error_msg = f"❌ **Errore**: {str(e)}"
                message_placeholder.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": error_msg
                })

# Footer
st.markdown("---")
st.markdown("""
💡 **Suggerimenti**:
- Puoi caricare file di codice per farli analizzare da Claude
- Usa la sidebar per cambiare modello e parametri
- Claude Sonnet 4 è il modello più performante disponibile
""")

# Info di debug (opzionale - rimuovi se non serve)
if st.checkbox("🔍 Mostra info debug", value=False):
    st.write("**Messaggi in sessione:**", len(st.session_state.messages))
    st.write("**File processati:**", st.session_state.files_processed)
    if st.session_state.messages:
        st.json(st.session_state.messages[-1])  # Ultimo messaggio

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
