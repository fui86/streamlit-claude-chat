import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
from typing import Dict, List, Optional
import uuid

# Configurazione pagina
st.set_page_config(
    page_title="747Disco - Gestione Vendite Eventi",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizzato per branding 747Disco
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #0f3460;
        margin: 0.5rem 0;
    }
    .event-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .success-badge {
        background-color: #28a745;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
    }
    .warning-badge {
        background-color: #ffc107;
        color: black;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
    }
    .danger-badge {
        background-color: #dc3545;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Inizializzazione session state
if "eventi" not in st.session_state:
    st.session_state.eventi = []
if "clienti" not in st.session_state:
    st.session_state.clienti = []
if "preventivi" not in st.session_state:
    st.session_state.preventivi = []
if "current_date" not in st.session_state:
    st.session_state.current_date = datetime.now().date()

# Funzioni di utilità
def generate_id() -> str:
    """Genera un ID univoco"""
    return str(uuid.uuid4())[:8]

def formatta_euro(importo: float) -> str:
    """Formatta un importo in euro"""
    return f"€ {importo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def get_stato_badge(stato: str) -> str:
    """Restituisce il badge HTML per lo stato"""
    stati = {
        "Confermato": "success-badge",
        "In attesa": "warning-badge",
        "Annullato": "danger-badge",
        "Completato": "success-badge"
    }
    classe = stati.get(stato, "warning-badge")
    return f'<span class="{classe}">{stato}</span>'

# Header principale
st.markdown("""
<div class="main-header">
    <h1>🎉 747Disco - Gestione Vendite Eventi</h1>
    <p style="margin: 0; font-size: 1.1rem;">Location Eventi Privati - Ciampino (Roma) - Vicino al GRA</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Menu principale
with st.sidebar:
    st.image("https://via.placeholder.com/200x100/0f3460/ffffff?text=747Disco", use_container_width=True)
    
    st.markdown("---")
    st.header("📊 Menu")
    
    pagina = st.radio(
        "Seleziona sezione:",
        [
            "🏠 Dashboard",
            "📅 Calendario Eventi",
            "➕ Nuovo Evento",
            "👥 Gestione Clienti",
            "💰 Preventivi",
            "📈 Analytics Vendite",
            "⚙️ Configurazioni"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Quick Actions")
    
    if st.button("📊 Report Mensile", use_container_width=True):
        st.session_state.quick_action = "report_mensile"
    
    if st.button("📞 Lista Contatti", use_container_width=True):
        st.session_state.quick_action = "lista_contatti"
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.85rem;">
        <p><strong>747Disco</strong></p>
        <p>Ciampino, Roma</p>
        <p>📍 Vicino al GRA</p>
    </div>
    """, unsafe_allow_html=True)

# Pagina Dashboard
if pagina == "🏠 Dashboard":
    st.header("📊 Dashboard Vendite")
    
    # Statistiche principali
    col1, col2, col3, col4 = st.columns(4)
    
    eventi_confermati = [e for e in st.session_state.eventi if e.get("stato") == "Confermato"]
    eventi_mese = [e for e in eventi_confermati 
                   if datetime.strptime(e["data"], "%Y-%m-%d").month == datetime.now().month]
    
    fatturato_totale = sum(float(e.get("prezzo_totale", 0)) for e in eventi_confermati)
    fatturato_mese = sum(float(e.get("prezzo_totale", 0)) for e in eventi_mese)
    
    with col1:
        st.metric(
            "💰 Fatturato Totale",
            formatta_euro(fatturato_totale),
            delta=formatta_euro(fatturato_mese) + " questo mese"
        )
    
    with col2:
        st.metric(
            "📅 Eventi Confermati",
            len(eventi_confermati),
            delta=f"{len(eventi_mese)} questo mese"
        )
    
    with col3:
        clienti_attivi = len(set(e.get("cliente_id") for e in eventi_confermati))
        st.metric(
            "👥 Clienti Attivi",
            clienti_attivi
        )
    
    with col4:
        eventi_prossimi = [e for e in eventi_confermati 
                          if datetime.strptime(e["data"], "%Y-%m-%d").date() >= datetime.now().date()]
        st.metric(
            "⏭️ Prossimi Eventi",
            len(eventi_prossimi)
        )
    
    st.markdown("---")
    
    # Prossimi eventi
    st.subheader("📅 Prossimi Eventi")
    
    if eventi_prossimi:
        eventi_prossimi_sorted = sorted(
            eventi_prossimi,
            key=lambda x: datetime.strptime(x["data"], "%Y-%m-%d")
        )[:5]
        
        for evento in eventi_prossimi_sorted:
            cliente = next((c for c in st.session_state.clienti if c["id"] == evento.get("cliente_id")), None)
            nome_cliente = cliente["nome"] if cliente else "Cliente non trovato"
            
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.write(f"**{evento.get('tipo_evento', 'N/A')}**")
                st.caption(f"👤 {nome_cliente}")
            with col2:
                data_evento = datetime.strptime(evento["data"], "%Y-%m-%d")
                st.write(f"📅 {data_evento.strftime('%d/%m/%Y')}")
                st.caption(f"🕐 {evento.get('ora_inizio', 'N/A')} - {evento.get('ora_fine', 'N/A')}")
            with col3:
                st.write(f"**{formatta_euro(float(evento.get('prezzo_totale', 0)))}**")
            with col4:
                st.markdown(get_stato_badge(evento.get("stato", "In attesa")), unsafe_allow_html=True)
            
            st.markdown("---")
    else:
        st.info("Nessun evento in programma. Aggiungi un nuovo evento!")
    
    # Grafico vendite mensili (simplificato)
    st.subheader("📈 Andamento Vendite")
    
    if eventi_confermati:
        df_vendite = pd.DataFrame([
            {
                "Mese": datetime.strptime(e["data"], "%Y-%m-%d").strftime("%Y-%m"),
                "Importo": float(e.get("prezzo_totale", 0))
            }
            for e in eventi_confermati
        ])
        
        vendite_mensili = df_vendite.groupby("Mese")["Importo"].sum().reset_index()
        vendite_mensili["Mese"] = pd.to_datetime(vendite_mensili["Mese"])
        vendite_mensili = vendite_mensili.sort_values("Mese")
        
        st.line_chart(vendite_mensili.set_index("Mese"))

# Pagina Calendario Eventi
elif pagina == "📅 Calendario Eventi":
    st.header("📅 Calendario Disponibilità")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.subheader("Filtri")
        tipo_filtro = st.selectbox(
            "Tipo evento:",
            ["Tutti", "Compleanno", "Matrimonio", "Festa Privata", "Evento Aziendale", "Altro"]
        )
        
        stato_filtro = st.selectbox(
            "Stato:",
            ["Tutti", "Confermato", "In attesa", "Annullato", "Completato"]
        )
        
        data_inizio = st.date_input(
            "Data inizio:",
            value=datetime.now().date(),
            min_value=datetime.now().date()
        )
        
        data_fine = st.date_input(
            "Data fine:",
            value=datetime.now().date() + timedelta(days=30)
        )
    
    with col2:
        st.subheader("Eventi Programmati")
        
        eventi_filtrati = st.session_state.eventi.copy()
        
        if tipo_filtro != "Tutti":
            eventi_filtrati = [e for e in eventi_filtrati if e.get("tipo_evento") == tipo_filtro]
        
        if stato_filtro != "Tutti":
            eventi_filtrati = [e for e in eventi_filtrati if e.get("stato") == stato_filtro]
        
        eventi_periodo = [
            e for e in eventi_filtrati
            if data_inizio <= datetime.strptime(e["data"], "%Y-%m-%d").date() <= data_fine
        ]
        
        if eventi_periodo:
            for evento in sorted(eventi_periodo, key=lambda x: datetime.strptime(x["data"], "%Y-%m-%d")):
                cliente = next((c for c in st.session_state.clienti if c["id"] == evento.get("cliente_id")), None)
                nome_cliente = cliente["nome"] if cliente else "Cliente non trovato"
                
                with st.expander(f"📅 {evento.get('tipo_evento', 'N/A')} - {datetime.strptime(evento['data'], '%Y-%m-%d').strftime('%d/%m/%Y')}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Cliente:** {nome_cliente}")
                        st.write(f"**Data:** {datetime.strptime(evento['data'], '%Y-%m-%d').strftime('%d/%m/%Y')}")
                        st.write(f"**Orario:** {evento.get('ora_inizio', 'N/A')} - {evento.get('ora_fine', 'N/A')}")
                        st.write(f"**Ospiti:** {evento.get('numero_ospiti', 'N/A')}")
                    with col2:
                        st.write(f"**Prezzo:** {formatta_euro(float(evento.get('prezzo_totale', 0)))}")
                        st.markdown(f"**Stato:** {get_stato_badge(evento.get('stato', 'In attesa'))}", unsafe_allow_html=True)
                        st.write(f"**Note:** {evento.get('note', 'Nessuna nota')}")
                    
                    if st.button(f"✏️ Modifica", key=f"edit_{evento['id']}"):
                        st.session_state.edit_evento_id = evento["id"]
                        st.rerun()
        else:
            st.info("Nessun evento trovato per i filtri selezionati.")

# Pagina Nuovo Evento
elif pagina == "➕ Nuovo Evento":
    st.header("➕ Nuovo Evento")
    
    with st.form("nuovo_evento_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_evento = st.selectbox(
                "Tipo Evento *",
                ["Compleanno", "Matrimonio", "Festa Privata", "Evento Aziendale", "Altro"]
            )
            
            data_evento = st.date_input(
                "Data Evento *",
                value=datetime.now().date(),
                min_value=datetime.now().date()
            )
            
            ora_inizio = st.time_input("Ora Inizio *", value=datetime.strptime("20:00", "%H:%M").time())
            ora_fine = st.time_input("Ora Fine *", value=datetime.strptime("02:00", "%H:%M").time())
            
            numero_ospiti = st.number_input("Numero Ospiti *", min_value=1, max_value=500, value=50)
        
        with col2:
            # Selezione cliente esistente o nuovo
            opzione_cliente = st.radio(
                "Cliente:",
                ["Cliente esistente", "Nuovo cliente"]
            )
            
            if opzione_cliente == "Cliente esistente":
                if st.session_state.clienti:
                    cliente_selezionato = st.selectbox(
                        "Seleziona cliente:",
                        [f"{c['nome']} - {c['telefono']}" for c in st.session_state.clienti],
                        key="cliente_select"
                    )
                    cliente_id = st.session_state.clienti[
                        [f"{c['nome']} - {c['telefono']}" for c in st.session_state.clienti].index(cliente_selezionato)
                    ]["id"]
                else:
                    st.warning("Nessun cliente disponibile. Crea prima un cliente.")
                    cliente_id = None
            else:
                nome_cliente = st.text_input("Nome Cliente *")
                telefono_cliente = st.text_input("Telefono *")
                email_cliente = st.text_input("Email")
                
                if nome_cliente and telefono_cliente:
                    nuovo_cliente_id = generate_id()
                    cliente_id = nuovo_cliente_id
            
            prezzo_totale = st.number_input(
                "Prezzo Totale (€) *",
                min_value=0.0,
                value=1000.0,
                step=50.0
            )
            
            stato = st.selectbox(
                "Stato *",
                ["Confermato", "In attesa", "Annullato"]
            )
        
        note = st.text_area("Note aggiuntive", height=100)
        
        submitted = st.form_submit_button("💾 Salva Evento", use_container_width=True)
        
        if submitted:
            if cliente_id is None and opzione_cliente == "Nuovo cliente":
                if nome_cliente and telefono_cliente:
                    nuovo_cliente = {
                        "id": nuovo_cliente_id,
                        "nome": nome_cliente,
                        "telefono": telefono_cliente,
                        "email": email_cliente if email_cliente else "",
                        "data_registrazione": datetime.now().strftime("%Y-%m-%d")
                    }
                    st.session_state.clienti.append(nuovo_cliente)
                else:
                    st.error("Compila tutti i campi obbligatori del cliente.")
                    submitted = False
            
            if submitted and cliente_id:
                nuovo_evento = {
                    "id": generate_id(),
                    "tipo_evento": tipo_evento,
                    "data": data_evento.strftime("%Y-%m-%d"),
                    "ora_inizio": ora_inizio.strftime("%H:%M"),
                    "ora_fine": ora_fine.strftime("%H:%M"),
                    "numero_ospiti": numero_ospiti,
                    "cliente_id": cliente_id,
                    "prezzo_totale": prezzo_totale,
                    "stato": stato,
                    "note": note,
                    "data_creazione": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                st.session_state.eventi.append(nuovo_evento)
                st.success(f"✅ Evento '{tipo_evento}' creato con successo!")
                st.balloons()

# Pagina Gestione Clienti
elif pagina == "👥 Gestione Clienti":
    st.header("👥 Gestione Clienti")
    
    tab1, tab2 = st.tabs(["📋 Lista Clienti", "➕ Nuovo Cliente"])
    
    with tab1:
        if st.session_state.clienti:
            st.subheader(f"Totale Clienti: {len(st.session_state.clienti)}")
            
            # Filtro ricerca
            ricerca = st.text_input("🔍 Cerca cliente (nome, telefono, email)")
            
            clienti_filtrati = st.session_state.clienti
            if ricerca:
                ricerca_lower = ricerca.lower()
                clienti_filtrati = [
                    c for c in st.session_state.clienti
                    if ricerca_lower in c.get("nome", "").lower() or
                       ricerca_lower in c.get("telefono", "").lower() or
                       ricerca_lower in c.get("email", "").lower()
                ]
            
            for cliente in clienti_filtrati:
                eventi_cliente = [e for e in st.session_state.eventi if e.get("cliente_id") == cliente["id"]]
                eventi_confermati_cliente = [e for e in eventi_cliente if e.get("stato") == "Confermato"]
                fatturato_cliente = sum(float(e.get("prezzo_totale", 0)) for e in eventi_confermati_cliente)
                
                with st.expander(f"👤 {cliente.get('nome', 'N/A')} - 📞 {cliente.get('telefono', 'N/A')}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Nome:** {cliente.get('nome', 'N/A')}")
                        st.write(f"**Telefono:** {cliente.get('telefono', 'N/A')}")
                        st.write(f"**Email:** {cliente.get('email', 'N/A') if cliente.get('email') else 'Non fornita'}")
                        st.write(f"**Registrato il:** {cliente.get('data_registrazione', 'N/A')}")
                    with col2:
                        st.write(f"**Eventi totali:** {len(eventi_cliente)}")
                        st.write(f"**Eventi confermati:** {len(eventi_confermati_cliente)}")
                        st.write(f"**Fatturato totale:** {formatta_euro(fatturato_cliente)}")
        else:
            st.info("Nessun cliente registrato. Aggiungi il primo cliente!")
    
    with tab2:
        st.subheader("➕ Nuovo Cliente")
        
        with st.form("nuovo_cliente_form"):
            nome = st.text_input("Nome *")
            telefono = st.text_input("Telefono *")
            email = st.text_input("Email")
            indirizzo = st.text_input("Indirizzo")
            note_cliente = st.text_area("Note", height=100)
            
            submitted = st.form_submit_button("💾 Salva Cliente", use_container_width=True)
            
            if submitted:
                if nome and telefono:
                    nuovo_cliente = {
                        "id": generate_id(),
                        "nome": nome,
                        "telefono": telefono,
                        "email": email if email else "",
                        "indirizzo": indirizzo if indirizzo else "",
                        "note": note_cliente if note_cliente else "",
                        "data_registrazione": datetime.now().strftime("%Y-%m-%d")
                    }
                    st.session_state.clienti.append(nuovo_cliente)
                    st.success(f"✅ Cliente '{nome}' aggiunto con successo!")
                    st.balloons()
                else:
                    st.error("Compila tutti i campi obbligatori (Nome e Telefono).")

# Pagina Preventivi
elif pagina == "💰 Preventivi":
    st.header("💰 Gestione Preventivi")
    
    tab1, tab2 = st.tabs(["📋 Lista Preventivi", "➕ Nuovo Preventivo"])
    
    with tab1:
        if st.session_state.preventivi:
            for preventivo in st.session_state.preventivi:
                cliente = next((c for c in st.session_state.clienti if c["id"] == preventivo.get("cliente_id")), None)
                nome_cliente = cliente["nome"] if cliente else "Cliente non trovato"
                
                with st.expander(f"💰 Preventivo #{preventivo.get('id', 'N/A')} - {nome_cliente}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**Cliente:** {nome_cliente}")
                        st.write(f"**Tipo Evento:** {preventivo.get('tipo_evento', 'N/A')}")
                        st.write(f"**Data Evento:** {preventivo.get('data_evento', 'N/A')}")
                        st.write(f"**Numero Ospiti:** {preventivo.get('numero_ospiti', 'N/A')}")
                    with col2:
                        st.write(f"**Importo:** {formatta_euro(float(preventivo.get('importo', 0)))}")
                        st.write(f"**Stato:** {preventivo.get('stato', 'In attesa')}")
                        st.write(f"**Scadenza:** {preventivo.get('scadenza', 'N/A')}")
        else:
            st.info("Nessun preventivo disponibile.")
    
    with tab2:
        st.subheader("➕ Nuovo Preventivo")
        
        with st.form("nuovo_preventivo_form"):
            if st.session_state.clienti:
                cliente_selezionato = st.selectbox(
                    "Cliente *",
                    [f"{c['nome']} - {c['telefono']}" for c in st.session_state.clienti]
                )
                cliente_id = st.session_state.clienti[
                    [f"{c['nome']} - {c['telefono']}" for c in st.session_state.clienti].index(cliente_selezionato)
                ]["id"]
            else:
                st.warning("Crea prima un cliente.")
                cliente_id = None
            
            tipo_evento = st.selectbox(
                "Tipo Evento *",
                ["Compleanno", "Matrimonio", "Festa Privata", "Evento Aziendale", "Altro"]
            )
            
            col1, col2 = st.columns(2)
            with col1:
                data_evento = st.date_input("Data Evento Prevista", value=datetime.now().date())
                numero_ospiti = st.number_input("Numero Ospiti *", min_value=1, max_value=500, value=50)
            with col2:
                importo = st.number_input("Importo Preventivo (€) *", min_value=0.0, value=1000.0, step=50.0)
                scadenza = st.date_input("Scadenza Preventivo", value=datetime.now().date() + timedelta(days=7))
            
            servizi_inclusi = st.multiselect(
                "Servizi Inclusi",
                ["Location", "Audio/Sound System", "Luci", "Bar", "Catering", "Sicurezza", "Parcheggio"]
            )
            
            note_preventivo = st.text_area("Note", height=100)
            
            submitted = st.form_submit_button("💾 Crea Preventivo", use_container_width=True)
            
            if submitted and cliente_id:
                nuovo_preventivo = {
                    "id": generate_id(),
                    "cliente_id": cliente_id,
                    "tipo_evento": tipo_evento,
                    "data_evento": data_evento.strftime("%Y-%m-%d"),
                    "numero_ospiti": numero_ospiti,
                    "importo": importo,
                    "scadenza": scadenza.strftime("%Y-%m-%d"),
                    "servizi_inclusi": servizi_inclusi,
                    "note": note_preventivo,
                    "stato": "In attesa",
                    "data_creazione": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.preventivi.append(nuovo_preventivo)
                st.success(f"✅ Preventivo creato con successo!")
                st.balloons()

# Pagina Analytics Vendite
elif pagina == "📈 Analytics Vendite":
    st.header("📈 Analytics e Report Vendite")
    
    tab1, tab2, tab3 = st.tabs(["📊 Dashboard Analytics", "📅 Report Mensile", "🎯 KPIs"])
    
    with tab1:
        eventi_confermati = [e for e in st.session_state.eventi if e.get("stato") == "Confermato"]
        
        if eventi_confermati:
            # Grafico per tipo evento
            st.subheader("Vendite per Tipo Evento")
            tipo_eventi = {}
            for evento in eventi_confermati:
                tipo = evento.get("tipo_evento", "Altro")
                tipo_eventi[tipo] = tipo_eventi.get(tipo, 0) + float(evento.get("prezzo_totale", 0))
            
            df_tipo = pd.DataFrame(list(tipo_eventi.items()), columns=["Tipo Evento", "Fatturato"])
            st.bar_chart(df_tipo.set_index("Tipo Evento"))
            
            # Top clienti
            st.subheader("Top 5 Clienti per Fatturato")
            fatturato_per_cliente = {}
            for evento in eventi_confermati:
                cliente_id = evento.get("cliente_id")
                if cliente_id:
                    fatturato_per_cliente[cliente_id] = fatturato_per_cliente.get(cliente_id, 0) + float(evento.get("prezzo_totale", 0))
            
            top_clienti = sorted(fatturato_per_cliente.items(), key=lambda x: x[1], reverse=True)[:5]
            
            for cliente_id, fatturato in top_clienti:
                cliente = next((c for c in st.session_state.clienti if c["id"] == cliente_id), None)
                nome_cliente = cliente["nome"] if cliente else "Cliente non trovato"
                st.write(f"**{nome_cliente}:** {formatta_euro(fatturato)}")
        else:
            st.info("Nessun dato disponibile per l'analisi.")
    
    with tab2:
        st.subheader("Report Mensile")
        
        mese_selezionato = st.selectbox(
            "Seleziona mese:",
            [
                (datetime.now() - timedelta(days=30*i)).strftime("%Y-%m")
                for i in range(6)
            ]
        )
        
        eventi_mese = [
            e for e in st.session_state.eventi
            if e.get("stato") == "Confermato" and
            datetime.strptime(e["data"], "%Y-%m-%d").strftime("%Y-%m") == mese_selezionato
        ]
        
        if eventi_mese:
            fatturato_mese = sum(float(e.get("prezzo_totale", 0)) for e in eventi_mese)
            numero_eventi = len(eventi_mese)
            media_evento = fatturato_mese / numero_eventi if numero_eventi > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Fatturato", formatta_euro(fatturato_mese))
            with col2:
                st.metric("Numero Eventi", numero_eventi)
            with col3:
                st.metric("Media per Evento", formatta_euro(media_evento))
        else:
            st.info(f"Nessun evento confermato per {mese_selezionato}.")
    
    with tab3:
        st.subheader("🎯 Key Performance Indicators")
        
        eventi_confermati = [e for e in st.session_state.eventi if e.get("stato") == "Confermato"]
        preventivi = st.session_state.preventivi
        
        if eventi_confermati:
            fatturato_totale = sum(float(e.get("prezzo_totale", 0)) for e in eventi_confermati)
            numero_eventi = len(eventi_confermati)
            ticket_medio = fatturato_totale / numero_eventi if numero_eventi > 0 else 0
            
            conversion_rate = (numero_eventi / len(preventivi) * 100) if preventivi else 0
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("💰 Fatturato Totale", formatta_euro(fatturato_totale))
                st.metric("📊 Ticket Medio", formatta_euro(ticket_medio))
            with col2:
                st.metric("📅 Eventi Confermati", numero_eventi)
                st.metric("🎯 Conversion Rate", f"{conversion_rate:.1f}%")

# Pagina Configurazioni
elif pagina == "⚙️ Configurazioni":
    st.header("⚙️ Configurazioni")
    
    st.subheader("💾 Gestione Dati")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Esporta Dati**")
        if st.button("📥 Esporta Eventi (JSON)", use_container_width=True):
            json_data = json.dumps(st.session_state.eventi, indent=2, ensure_ascii=False)
            st.download_button(
                "⬇️ Scarica JSON",
                json_data,
                file_name=f"eventi_747disco_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
        
        if st.button("📥 Esporta Clienti (JSON)", use_container_width=True):
            json_data = json.dumps(st.session_state.clienti, indent=2, ensure_ascii=False)
            st.download_button(
                "⬇️ Scarica JSON",
                json_data,
                file_name=f"clienti_747disco_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        st.write("**Importa Dati**")
        uploaded_file = st.file_uploader("Carica file JSON", type=["json"])
        
        if uploaded_file:
            try:
                data = json.load(uploaded_file)
                if isinstance(data, list):
                    if st.button("📤 Importa Dati", use_container_width=True):
                        if "eventi" in uploaded_file.name.lower():
                            st.session_state.eventi.extend(data)
                            st.success(f"✅ Importati {len(data)} eventi!")
                        elif "clienti" in uploaded_file.name.lower():
                            st.session_state.clienti.extend(data)
                            st.success(f"✅ Importati {len(data)} clienti!")
                        else:
                            st.warning("Nome file non riconosciuto. Usa 'eventi' o 'clienti' nel nome.")
            except Exception as e:
                st.error(f"Errore nell'importazione: {e}")
    
    st.markdown("---")
    
    st.subheader("📊 Statistiche Database")
    st.write(f"**Eventi totali:** {len(st.session_state.eventi)}")
    st.write(f"**Clienti totali:** {len(st.session_state.clienti)}")
    st.write(f"**Preventivi totali:** {len(st.session_state.preventivi)}")
    
    if st.button("🗑️ Reset Database (ATTENZIONE!)", use_container_width=True, type="primary"):
        st.warning("⚠️ Questa azione eliminerà tutti i dati!")
        if st.button("✅ Conferma Reset", use_container_width=True):
            st.session_state.eventi = []
            st.session_state.clienti = []
            st.session_state.preventivi = []
            st.success("Database resettato.")
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.85rem; padding: 1rem;">
    <p><strong>747Disco</strong> - Gestione Vendite Eventi Privati</p>
    <p>Location Eventi - Ciampino, Roma - Vicino al GRA</p>
    <p>© 2024 - Sistema di Gestione Vendite</p>
</div>
""", unsafe_allow_html=True)
