import anthropic
import streamlit as st

# Configurazione pagina
st.set_page_config(
    page_title="747Disco - Marketing & Vendite Eventi", 
    page_icon="🎉",
    layout="wide"
)

st.title("🎉 747Disco - Assistant Marketing & Vendite Eventi")
st.caption("📍 Location: Ciampino (Roma) - Vicino al GRA | Specializzati in Eventi Privati")

# Sidebar per configurazioni
with st.sidebar:
    st.header("⚙️ Configurazioni")
    
    # Selezione del modello
    model_options = [
        "claude-3-5-sonnet-20241022",    # Claude 3.5 Sonnet (ottimo per marketing)
        "claude-sonnet-4-20250514",      # Claude Sonnet 4
        "claude-3-5-haiku-20241022",     # Claude 3.5 Haiku
        "claude-3-opus-20240229"         # Claude 3 Opus
    ]
    
    selected_model = st.selectbox(
        "Seleziona il modello:",
        model_options,
        index=0,
        help="Claude 3.5 Sonnet è ottimo per strategie di marketing"
    )
    
    # Parametri di configurazione
    max_tokens = st.slider("Max tokens:", 1000, 8000, 4096)
    temperature = st.slider("Temperature:", 0.0, 1.0, 0.7, help="Più alto = più creativo per marketing")
    
    st.markdown("---")
    
    # Template veloci per Marketing & Vendite
    st.subheader("🚀 Template Marketing & Vendite")
    
    templates = {
        "📧 Email Proposta": "Crea una email professionale per proporre un evento a un cliente:",
        "📱 Messaggio WhatsApp": "Scrivi un messaggio WhatsApp per contattare un cliente:",
        "📝 Preventivo Evento": "Crea un preventivo dettagliato per un evento:",
        "🎯 Strategia Marketing": "Suggerisci una strategia di marketing per:",
        "💬 Script Vendita": "Crea uno script di vendita telefonica per:",
        "📊 Analisi Cliente": "Analizza questo cliente e suggerisci approccio:",
        "🎉 Pitch Evento": "Crea un pitch convincente per vendere:",
        "📈 Piano Comunicazione": "Crea un piano di comunicazione per:"
    }
    
    for emoji_name, prompt_template in templates.items():
        if st.button(emoji_name, use_container_width=True):
            st.session_state.quick_template = prompt_template
    
    st.markdown("---")
    
    # Informazioni business
    st.subheader("ℹ️ Info 747Disco")
    st.info("""
    **📍 Location**: Ciampino (Roma)  
    **🚗**: Vicino al GRA  
    **🎯**: Eventi Privati  
    - Compleanni
    - Feste private
    - Eventi aziendali
    - Matrimoni
    """)
    
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
    st.caption(f"💼 Ruolo: **Esperto Marketing & Vendite Eventi**")
    
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
    st.subheader("📋 Informazioni Cliente/Evento")
    
    # Campi per informazioni evento
    event_type = st.selectbox(
        "Tipo di evento:",
        ["Compleanno", "Festa Privata", "Evento Aziendale", "Matrimonio", "Altro"],
        index=0
    )
    
    guest_count = st.number_input("Numero ospiti:", min_value=1, max_value=500, value=50)
    
    budget = st.text_input("Budget (€):", placeholder="Es: 2000-3000")
    
    event_date = st.date_input("Data evento:")
    
    client_info = st.text_area(
        "Info cliente (nome, contatto, preferenze, etc.):",
        height=150,
        placeholder="Es: Mario Rossi, tel: 333..., cerca location per compleanno 50 anni..."
    )
    
    if st.button("📤 Analizza Richiesta", use_container_width=True) and client_info.strip():
        analysis_message = f"""Analizza questa richiesta cliente per un evento 747Disco:

**Tipo Evento**: {event_type}
**Numero Ospiti**: {guest_count}
**Budget**: {budget}€
**Data**: {event_date}
**Info Cliente**: {client_info}

Suggerisci:
1. Strategia di vendita
2. Proposta personalizzata
3. Punti di forza da evidenziare
4. Eventuali obiezioni da gestire
"""
        st.session_state.messages.append({"role": "user", "content": analysis_message})
        st.rerun()
    
    st.markdown("---")
    
    # Upload file (per documenti, preventivi, etc.)
    st.subheader("📁 Upload Documenti")
    
    uploaded_files = st.file_uploader(
        "Carica documenti (PDF, TXT, DOCX):",
        type=["pdf", "txt", "docx", "doc"],
        accept_multiple_files=True,
        key="file_uploader"
    )
    
    if uploaded_files:
        st.write("**File caricati:**")
        for file in uploaded_files:
            st.write(f"📄 {file.name}")

with col1:
    st.subheader("💬 Assistant Marketing & Vendite")
    
    # Container per i messaggi
    chat_container = st.container(height=600)
    
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
                
                # Determina il tipo dal file
                file_ext = filename.split('.')[-1].lower()
                
                # Limita la lunghezza
                max_content_length = 4000
                if len(file_content) > max_content_length:
                    file_content = file_content[:max_content_length] + "\n\n... [file troncato]"
                
                file_message = f"📄 **File: `{filename}`**\n\nAnalizza questo documento e suggerisci strategie di marketing/vendita o miglioramenti:\n\n```{file_ext}\n{file_content}\n```"
                
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
prompt_placeholder = "Chiedi consigli su marketing, vendite, eventi, preventivi..."
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
        system_message = f"Sei Claude {selected_model.split('-')[1]} {'4' if 'sonnet-4' in selected_model else '3.5'}, un assistente AI specializzato in marketing e vendite per eventi privati. Sei un esperto di marketing e vendite, un grande commerciante. Ti occupi di vendita di eventi privati, come feste di compleanno, eventi di ogni genere. In particolare sei proprietario di una location di nome 747Disco a Ciampino, vicino al GRA, di Roma."
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
                system_prompt = f"""Sei Claude, modello {selected_model}. 

Sei un GRANDE ESPERTO di marketing e vendite, un grande commerciante. Ti occupi di vendita di eventi privati, come feste di compleanno, eventi di ogni genere. 

In particolare sei proprietario di una location di nome 747Disco a Ciampino, vicino al GRA, di Roma.

Le tue competenze:
- Marketing strategico per eventi
- Tecniche di vendita e chiusura contratti
- Comunicazione efficace con clienti
- Creazione di proposte e preventivi vincenti
- Gestione obiezioni comuni
- Strategie di follow-up e lead nurturing
- Personalizzazione di offerte per ogni tipo di evento

La location 747Disco:
- Si trova a Ciampino (Roma)
- Vicino al GRA (facilmente raggiungibile)
- Specializzata in eventi privati: compleanni, feste private, eventi aziendali, matrimoni

Rispondi sempre in modo professionale, strategico e orientato alle vendite. Usa tecniche di persuasione efficaci ma etiche."""
                api_messages.insert(0, {"role": "user", "content": system_prompt})
                api_messages.insert(1, {"role": "assistant", "content": "Perfetto! Sono il tuo assistente esperto di marketing e vendite per 747Disco. Sono specializzato in aiutarti a vendere eventi privati, creare proposte vincenti, gestire clienti e chiudere contratti. Come posso aiutarti oggi? 🎉"})
                
                # Chiamata streaming all'API
                with st.spinner("Claude sta preparando la strategia di marketing/vendita..."):
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
💡 **Suggerimenti per Marketing & Vendite**:
- 📧 **Email**: Usa i template per creare email professionali e convincenti
- 💬 **Script Vendita**: Prepara script per chiamate e presentazioni
- 📊 **Analisi Cliente**: Inserisci info cliente per strategie personalizzate
- 🎯 **Preventivi**: Crea preventivi dettagliati e competitivi
- 📱 **WhatsApp**: Usa template per comunicazioni veloci e efficaci
- 🎉 **Pitch Eventi**: Sviluppa pitch convincenti per ogni tipo di evento
""")

# Debug info (nascosta di default)
with st.expander("🔍 Info Debug", expanded=False):
    st.write(f"**Modello selezionato**: {selected_model}")
    st.write(f"**Messaggi in sessione**: {len(st.session_state.messages)}")
    st.write(f"**File processati**: {st.session_state.files_processed}")
    if st.session_state.messages:
        st.json(st.session_state.messages[-1] if st.session_state.messages else {})
