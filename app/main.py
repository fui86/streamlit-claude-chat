import anthropic
import streamlit as st
from datetime import datetime

# Configurazione pagina
st.set_page_config(
    page_title="747Disco - Assistente Vendite Eventi", 
    page_icon="🎉",
    layout="wide"
)

st.title("🎉 747Disco - Assistente Vendite Eventi")
st.caption("📍 Ciampino, vicino al GRA - Roma")

# Sidebar per configurazioni
with st.sidebar:
    st.header("⚙️ Configurazioni")
    
    # Logo/Info Location
    st.markdown("""
    ### 🏢 747Disco
    **Location per eventi privati**
    
    📍 Ciampino (RM) - GRA  
    🎊 Feste private  
    🎂 Compleanni  
    🎉 Eventi aziendali  
    💒 Cerimonie  
    """)
    
    st.markdown("---")
    
    # Selezione del modello
    model_options = [
        "claude-3-5-sonnet-20241022",    # Claude 3.5 Sonnet
        "claude-sonnet-4-20250514",      # Claude Sonnet 4
        "claude-3-5-haiku-20241022",     # Claude 3.5 Haiku
        "claude-3-opus-20240229"         # Claude 3 Opus
    ]
    
    selected_model = st.selectbox(
        "Modello AI:",
        model_options,
        index=0,
        help="Modello Claude per assistenza vendite"
    )
    
    # Parametri di configurazione
    max_tokens = st.slider("Max tokens:", 1000, 8000, 4096)
    temperature = st.slider("Creatività:", 0.0, 1.0, 0.7, help="Più alto = risposte più creative")
    
    st.markdown("---")
    
    # Template veloci per vendite eventi
    st.subheader("🚀 Azioni Rapide")
    
    templates = {
        "💰 Preventivo Rapido": "Genera un preventivo per un evento con:",
        "🎂 Festa Compleanno": "Cliente interessato a organizzare una festa di compleanno:",
        "🏢 Evento Aziendale": "Richiesta per evento aziendale con:",
        "💍 Cerimonia": "Preventivo per cerimonia privata:",
        "📧 Email Commerciale": "Scrivi un'email commerciale per follow-up cliente che:",
        "📱 Risposta WhatsApp": "Risposta professionale WhatsApp per cliente che chiede:",
        "🎯 Proposta Personalizzata": "Crea proposta commerciale dettagliata per:",
        "📊 Confronto Pacchetti": "Spiega differenze tra i nostri pacchetti per:"
    }
    
    for emoji_name, prompt_template in templates.items():
        if st.button(emoji_name, use_container_width=True):
            st.session_state.quick_template = prompt_template
    
    st.markdown("---")
    
    # Informazioni utili
    st.subheader("📋 Info Veloci")
    st.caption("**Capienza**: 200-300 persone")
    st.caption("**Parcheggio**: Disponibile")
    st.caption("**Servizi**: DJ, catering, allestimenti")
    
    st.markdown("---")
    
    # Pulsante per pulire la chat
    if st.button("🗑️ Nuova conversazione", use_container_width=True):
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
    st.subheader("📋 Informazioni Evento")
    
    # Form per raccolta info evento
    with st.form("event_info_form"):
        st.write("**Dettagli Cliente/Evento:**")
        
        cliente_nome = st.text_input("Nome cliente:", placeholder="Mario Rossi")
        tipo_evento = st.selectbox(
            "Tipo di evento:",
            ["Compleanno", "Evento Aziendale", "Cerimonia", "Festa Privata", "Altro"]
        )
        
        data_evento = st.date_input("Data evento:", datetime.now())
        num_persone = st.number_input("Numero persone:", min_value=10, max_value=300, value=50)
        
        servizi = st.multiselect(
            "Servizi richiesti:",
            ["DJ/Musica", "Catering", "Allestimenti", "Illuminazione", "Fotografo", "Bartender", "Sicurezza"]
        )
        
        note_aggiuntive = st.text_area(
            "Note aggiuntive:",
            placeholder="Esigenze particolari, budget, preferenze...",
            height=100
        )
        
        submit_button = st.form_submit_button("📤 Genera Preventivo", use_container_width=True)
        
        if submit_button:
            # Crea messaggio strutturato
            servizi_text = ", ".join(servizi) if servizi else "da definire"
            event_message = f"""Genera un preventivo dettagliato per:

**Cliente**: {cliente_nome if cliente_nome else 'Da definire'}
**Tipo evento**: {tipo_evento}
**Data**: {data_evento.strftime('%d/%m/%Y')}
**Numero persone**: {num_persone}
**Servizi richiesti**: {servizi_text}
**Note**: {note_aggiuntive if note_aggiuntive else 'Nessuna nota particolare'}

Crea una proposta commerciale professionale e persuasiva."""
            
            st.session_state.messages.append({"role": "user", "content": event_message})
            st.rerun()
    
    st.markdown("---")
    
    # Upload documenti (preventivi, contratti, etc)
    st.subheader("📎 Upload Documenti")
    
    uploaded_files = st.file_uploader(
        "Carica documenti evento:",
        type=["pdf", "doc", "docx", "txt", "jpg", "png"],
        accept_multiple_files=True,
        key="file_uploader",
        help="Carica preventivi esistenti, foto location, contratti, ecc."
    )
    
    if uploaded_files:
        st.write("**File caricati:**")
        for file in uploaded_files:
            st.write(f"📄 {file.name}")

with col1:
    st.subheader("💬 Assistente Vendite AI")
    
    # Container per i messaggi
    chat_container = st.container(height=500)
    
    # Mostra messaggi precedenti
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Processo i file caricati
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.name not in st.session_state.files_processed:
            try:
                # Tenta di leggere come testo
                file_content = uploaded_file.read().decode("utf-8")
                filename = uploaded_file.name
                
                # Limita la lunghezza
                max_content_length = 4000
                if len(file_content) > max_content_length:
                    file_content = file_content[:max_content_length] + "\n\n... [documento troncato]"
                
                file_message = f"📄 **Documento caricato: `{filename}`**\n\nAnalizza questo documento e fornisci suggerimenti per la gestione dell'evento:\n\n{file_content}"
                
                st.session_state.messages.append({
                    "role": "user",
                    "content": file_message
                })
                
                st.session_state.files_processed.append(filename)
                st.rerun()
                
            except Exception as e:
                # Se non è un file di testo, semplicemente registra il caricamento
                filename = uploaded_file.name
                file_message = f"📄 **File caricato**: `{filename}` (file binario - immagine/documento)"
                st.session_state.messages.append({
                    "role": "user",
                    "content": file_message
                })
                st.session_state.files_processed.append(filename)
                st.rerun()

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
        system_message = f"Sei un esperto assistente AI per la vendita di eventi presso 747Disco, location per eventi privati a Ciampino (Roma)."
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
                    if msg["role"] in ["user", "assistant"] and "Sei un esperto assistente" not in msg["content"]:
                        api_messages.append({
                            "role": msg["role"],
                            "content": msg["content"]
                        })
                
                # Aggiunge system prompt come primo messaggio user
                system_prompt = f"""Sei un grande esperto di marketing e vendite, un commerciante di successo. Ti occupi di vendita di eventi privati per la location 747Disco a Ciampino, vicino al GRA di Roma.

**INFORMAZIONI SULLA LOCATION:**
- Nome: 747Disco
- Ubicazione: Ciampino (Roma), vicino al GRA
- Tipologia: Location per eventi privati
- Specializzazioni: Feste di compleanno, eventi aziendali, cerimonie, feste private
- Capienza: 200-300 persone
- Servizi disponibili: DJ/Musica, Catering, Allestimenti, Illuminazione, Fotografo, Bartender, Sicurezza
- Parcheggio: Disponibile e comodo

**TUO RUOLO:**
- Assistere nella vendita e gestione di eventi
- Creare preventivi dettagliati e persuasivi
- Rispondere a domande sui servizi
- Gestire obiezioni e negoziazioni
- Scrivere email e messaggi commerciali professionali
- Proporre soluzioni creative per ogni tipo di evento

**STILE DI COMUNICAZIONE:**
- Professionale ma caloroso e accogliente
- Entusiasta e positivo
- Orientato alla soluzione
- Attento alle esigenze del cliente
- Persuasivo senza essere invadente

Rispondi sempre in italiano e fornisci informazioni concrete e pratiche."""
                
                api_messages.insert(0, {"role": "user", "content": system_prompt})
                api_messages.insert(1, {"role": "assistant", "content": "Perfetto! Sono pronto ad assisterti nella vendita e gestione degli eventi per 747Disco. Come posso aiutarti oggi? Vuoi creare un preventivo, rispondere a un cliente, o gestire una trattativa?"})
                
                # Chiamata streaming all'API
                with st.spinner("Sto preparando la risposta..."):
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
💡 **Suggerimenti per la vendita di eventi**:
- 📋 **Preventivi**: Usa il form laterale per generare preventivi completi in pochi secondi
- 🚀 **Template Veloci**: Utilizza i pulsanti nella sidebar per risposte rapide a richieste comuni
- 💬 **Comunicazione**: Chiedi assistenza per email, WhatsApp e messaggi commerciali
- 🎯 **Personalizzazione**: Ogni evento è unico - descrivi le esigenze specifiche del cliente
- 📊 **Confronti**: Aiuta i clienti a scegliere tra diverse opzioni di pacchetti
""")

# Debug info (nascosta di default)
with st.expander("🔍 Info Debug", expanded=False):
    st.write(f"**Modello selezionato**: {selected_model}")
    st.write(f"**Messaggi in sessione**: {len(st.session_state.messages)}")
    st.write(f"**File processati**: {st.session_state.files_processed}")
    if st.session_state.messages:
        st.json(st.session_state.messages[-1] if st.session_state.messages else {})
