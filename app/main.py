import anthropic
import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="Claude Code Assistant", 
    page_icon="💻",
    layout="wide"
)

st.title("💻 Claude Code Assistant - PHP & WordPress")

# Sidebar per configurazioni
with st.sidebar:
    st.header("⚙️ Configurazioni")
    
    # Selezione del modello
    model_options = [
        "claude-3-5-sonnet-20241022",    # Claude 3.5 Sonnet (più stabile per coding)
        "claude-sonnet-4-20250514",      # Claude Sonnet 4
        "claude-3-5-haiku-20241022",     # Claude 3.5 Haiku
        "claude-3-opus-20240229"         # Claude 3 Opus
    ]
    
    selected_model = st.selectbox(
        "Seleziona il modello:",
        model_options,
        index=0,
        help="Claude 3.5 Sonnet è ottimo per il coding"
    )
    
    # Parametri di configurazione
    max_tokens = st.slider("Max tokens:", 1000, 8000, 4096)
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.1, help="Più basso = più preciso per il codice")
    
    st.markdown("---")
    
    # Template veloci per WordPress
    st.subheader("🚀 Template Veloci")
    
    templates = {
        "🔍 Debug PHP": "Analizza questo codice PHP e trova eventuali bug o problemi:",
        "🎨 Hook WordPress": "Crea un hook WordPress per:",
        "📝 Funzione PHP": "Scrivi una funzione PHP che:",
        "🔌 Plugin WordPress": "Crea un plugin WordPress che:",
        "⚡ Ottimizzazione": "Ottimizza questo codice per performance:",
        "🛡️ Sicurezza": "Controlla la sicurezza di questo codice:",
        "📱 Responsive": "Rendi questo CSS responsive:",
        "🎯 Query MySQL": "Scrivi una query MySQL per:"
    }
    
    for emoji_name, prompt_template in templates.items():
        if st.button(emoji_name, use_container_width=True):
            st.session_state.quick_template = prompt_template
    
    st.markdown("---")
    
    # Pulsante per pulire la chat
    if st.button("🗑️ Pulisci chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.files_processed = []
        if 'quick_template' in st.session_state:
            del st.session_state.quick_template
        st.rerun()

# Lettura delle chiavi dal secrets.toml
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
    
    # Verifica chiave caricata
    st.caption(f"🔑 API Key: {api_key[:10]}...*** ✅")
    st.caption(f"🤖 Modello: **{selected_model}**")
    
except KeyError as e:
    st.error(f"❌ Errore: Chiave API non trovata nei secrets: {e}")
    st.stop()

# Crea il client Claude
try:
    client = anthropic.Anthropic(api_key=api_key)
except Exception as e:
    st.error(f"❌ Errore nella creazione del client: {e}")
    st.stop()

# Inizializza la sessione
if "messages" not in st.session_state:
    st.session_state.messages = []

if "files_processed" not in st.session_state:
    st.session_state.files_processed = []

# Layout principale
col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("📁 Upload Codice")
    
    # Upload file
    uploaded_files = st.file_uploader(
        "Carica file di codice:",
        type=["php", "js", "css", "html", "py", "txt", "json", "xml", "sql"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    if uploaded_files:
        st.write("**File caricati:**")
        for file in uploaded_files:
            st.write(f"📄 {file.name}")
    
    st.markdown("---")
    
    # Box per inserimento codice manuale
    st.subheader("💾 Inserisci Codice")
    
    code_language = st.selectbox(
        "Linguaggio:",
        ["php", "javascript", "css", "html", "sql", "python", "text"],
        index=0
    )
    
    code_input = st.text_area(
        "Incolla il tuo codice qui:",
        height=200,
        placeholder="<?php\n// Il tuo codice PHP qui...\n?>"
    )
    
    if st.button("📤 Analizza Codice", use_container_width=True) and code_input.strip():
        code_message = f"Analizza questo codice {code_language.upper()}:\n\n```{code_language}\n{code_input}\n```"
        st.session_state.messages.append({"role": "user", "content": code_message})
        st.rerun()

with col1:
    st.subheader("💬 Chat con Claude")
    
    # Container per i messaggi
    chat_container = st.container(height=500)
    
    # Mostra messaggi precedenti
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                # Se il messaggio contiene codice, usa syntax highlighting
                if "```" in message["content"]:
                    st.markdown(message["content"])
                else:
                    st.markdown(message["content"])

# Processo i file caricati
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.name not in st.session_state.files_processed:
            try:
                file_content = uploaded_file.read().decode("utf-8")
                filename = uploaded_file.name
                
                # Determina il linguaggio dal file
                file_ext = filename.split('.')[-1].lower()
                
                # Limita la lunghezza
                max_content_length = 4000
                if len(file_content) > max_content_length:
                    file_content = file_content[:max_content_length] + "\n\n... [file troncato]"
                
                file_message = f"📄 **File: `{filename}`**\n\nAnalizza questo codice e dimmi se ci sono problemi, miglioramenti possibili o bug:\n\n```{file_ext}\n{file_content}\n```"
                
                st.session_state.messages.append({
                    "role": "user",
                    "content": file_message
                })
                
                st.session_state.files_processed.append(filename)
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Errore nel leggere {uploaded_file.name}: {e}")

# Gestione template veloci
if 'quick_template' in st.session_state:
    st.info(f"💡 Template selezionato: {st.session_state.quick_template}")

# Input manuale utente
prompt_placeholder = "Scrivi la tua domanda sul codice..."
if 'quick_template' in st.session_state:
    prompt_placeholder = st.session_state.quick_template

if prompt := st.chat_input(prompt_placeholder):
    # Se c'è un template, combinalo con l'input
    if 'quick_template' in st.session_state:
        full_prompt = f"{st.session_state.quick_template} {prompt}"
        del st.session_state.quick_template
    else:
        full_prompt = prompt
    
    # Aggiunge messaggio sistema per identificazione corretta del modello
    if len(st.session_state.messages) == 0:
        system_message = f"Sei Claude {selected_model.split('-')[1]} {'4' if 'sonnet-4' in selected_model else '3.5'}, un assistente AI specializzato in sviluppo PHP e WordPress. Quando ti viene chiesto quale modello sei, rispondi sempre con la versione corretta: {selected_model}."
        st.session_state.messages.append({"role": "assistant", "content": system_message})
    
    st.session_state.messages.append({"role": "user", "content": full_prompt})
    
    # Mostra il messaggio dell'utente
    with chat_container:
        with st.chat_message("user"):
            st.markdown(full_prompt)
    
    # Genera la risposta di Claude
    with chat_container:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Prepara i messaggi per l'API (escludi il messaggio sistema dalla chiamata)
                api_messages = []
                for msg in st.session_state.messages:
                    if msg["role"] in ["user", "assistant"] and "Sei Claude" not in msg["content"]:
                        api_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
                
                # Aggiunge system prompt come primo messaggio user
                system_prompt = f"Sei Claude, modello {selected_model}. Sei specializzato in sviluppo PHP, WordPress, debugging e ottimizzazione del codice. Rispondi sempre in modo tecnico e preciso."
                api_messages.insert(0, {"role": "user", "content": system_prompt})
                api_messages.insert(1, {"role": "assistant", "content": "Perfetto! Sono pronto ad aiutarti con PHP, WordPress e debugging. Dimmi pure cosa devi sviluppare o quale problema devo risolvere."})
                
                # Chiamata streaming all'API
                with st.spinner("Claude sta analizzando il codice..."):
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
                
                message_placeholder.markdown(full_response)
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": full_response
                })
                
            except anthropic.AuthenticationError:
                error_msg = "❌ **Errore di autenticazione**: Verifica l'API key nei secrets."
                message_placeholder.error(error_msg)
                
            except anthropic.NotFoundError as e:
                error_msg = f"❌ **Modello non trovato**: {e}"
                message_placeholder.error(error_msg)
                
            except Exception as e:
                error_msg = f"❌ **Errore**: {str(e)}"
                message_placeholder.error(error_msg)

# Footer con suggerimenti
st.markdown("---")
st.markdown("""
💡 **Suggerimenti per sviluppatori**:
- 🔍 **Debug**: Carica file o incolla codice per l'analisi automatica
- 🚀 **Template**: Usa i pulsanti nella sidebar per domande comuni
- 🛡️ **Sicurezza**: Chiedi sempre controlli di sicurezza per il codice WordPress
- ⚡ **Performance**: Ottimizza query e funzioni per migliori prestazioni
""")

# Debug info (nascosta di default)
with st.expander("🔍 Info Debug", expanded=False):
    st.write(f"**Modello selezionato**: {selected_model}")
    st.write(f"**Messaggi in sessione**: {len(st.session_state.messages)}")
    st.write(f"**File processati**: {st.session_state.files_processed}")
    if st.session_state.messages:
        st.json(st.session_state.messages[-1] if st.session_state.messages else {})
