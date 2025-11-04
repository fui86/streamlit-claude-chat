import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
from typing import Dict, List, Optional

# Configurazione pagina
st.set_page_config(
    page_title="747Disco - Gestione Vendite & Marketing",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizzato per styling moderno
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .stButton>button {
        width: 100%;
        background-color: #667eea;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #5568d3;
    }
</style>
""", unsafe_allow_html=True)

# Inizializzazione session state
if "events" not in st.session_state:
    st.session_state.events = []
if "contacts" not in st.session_state:
    st.session_state.contacts = []
if "quotes" not in st.session_state:
    st.session_state.quotes = []
if "sales_data" not in st.session_state:
    st.session_state.sales_data = []

# Funzioni helper per gestione dati
def save_to_session(key: str, data: List):
    """Salva dati nella session state"""
    st.session_state[key] = data

def load_from_session(key: str) -> List:
    """Carica dati dalla session state"""
    return st.session_state.get(key, [])

def calculate_revenue(events: List) -> float:
    """Calcola il fatturato totale"""
    return sum(event.get("price", 0) for event in events if event.get("status") == "Confermato")

def calculate_conversion_rate(quotes: List, events: List) -> float:
    """Calcola il tasso di conversione"""
    if not quotes:
        return 0.0
    confirmed = len([e for e in events if e.get("status") == "Confermato"])
    return (confirmed / len(quotes)) * 100 if quotes else 0.0

# Header principale
st.markdown("""
<div class="main-header">
    <h1>🎉 747Disco - Gestione Vendite & Marketing</h1>
    <p style="margin: 0; font-size: 1.1rem;">Location Eventi Privati | Ciampino, Roma | Vicino al GRA</p>
</div>
""", unsafe_allow_html=True)

# Sidebar per navigazione
with st.sidebar:
    st.image("https://via.placeholder.com/200x100/667eea/ffffff?text=747Disco", use_container_width=True)
    
    st.markdown("---")
    
    page = st.radio(
        "📋 Menu Navigazione",
        ["🏠 Dashboard", "👥 Contatti & Lead", "📅 Calendario Eventi", "💰 Preventivi", "📧 Marketing", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.subheader("⚡ Azioni Rapide")
    
    if st.button("➕ Nuovo Contatto", use_container_width=True):
        st.session_state.show_new_contact = True
    
    if st.button("📝 Nuovo Preventivo", use_container_width=True):
        st.session_state.show_new_quote = True
    
    if st.button("🎉 Nuovo Evento", use_container_width=True):
        st.session_state.show_new_event = True
    
    st.markdown("---")
    
    st.subheader("ℹ️ Info Business")
    st.info("""
    **747Disco**
    
    📍 Ciampino, Roma
    🚗 Vicino al GRA
    
    **Specialità:**
    - Feste di compleanno
    - Eventi privati
    - Organizzazione eventi
    """)

# Pagina Dashboard
if page == "🏠 Dashboard":
    st.header("📊 Dashboard Vendite")
    
    # Metriche principali
    events = load_from_session("events")
    quotes = load_from_session("quotes")
    contacts = load_from_session("contacts")
    
    revenue = calculate_revenue(events)
    conversion_rate = calculate_conversion_rate(quotes, events)
    pending_quotes = len([q for q in quotes if q.get("status") == "In Attesa"])
    confirmed_events = len([e for e in events if e.get("status") == "Confermato"])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Fatturato Totale",
            value=f"€ {revenue:,.2f}",
            delta=f"{len([e for e in events if e.get('status') == 'Confermato'])} eventi"
        )
    
    with col2:
        st.metric(
            label="📈 Tasso Conversione",
            value=f"{conversion_rate:.1f}%",
            delta=f"{confirmed_events}/{len(quotes)} preventivi"
        )
    
    with col3:
        st.metric(
            label="⏳ Preventivi in Attesa",
            value=pending_quotes,
            delta="da seguire"
        )
    
    with col4:
        st.metric(
            label="✅ Eventi Confermati",
            value=confirmed_events,
            delta=f"Totale: {len(events)}"
        )
    
    st.markdown("---")
    
    # Grafici e statistiche
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Eventi Prossimi 30 Giorni")
        if events:
            now = datetime.now()
            future_events = [
                e for e in events 
                if e.get("status") == "Confermato" and 
                datetime.strptime(e.get("date", now.strftime("%Y-%m-%d")), "%Y-%m-%d") >= now
            ]
            
            if future_events:
                events_df = pd.DataFrame(future_events)
                events_df["date"] = pd.to_datetime(events_df["date"])
                events_df = events_df.sort_values("date").head(10)
                
                for _, event in events_df.iterrows():
                    st.write(f"📅 **{event['date'].strftime('%d/%m/%Y')}** - {event.get('client_name', 'N/A')}")
                    st.write(f"   🎉 {event.get('event_type', 'N/A')} - €{event.get('price', 0):,.2f}")
                    st.markdown("---")
            else:
                st.info("Nessun evento programmato nei prossimi 30 giorni")
        else:
            st.info("Nessun evento registrato")
    
    with col2:
        st.subheader("🔥 Lead da Contattare")
        if contacts:
            recent_contacts = [
                c for c in contacts 
                if c.get("status") == "Nuovo" or c.get("last_contact") is None
            ]
            
            if recent_contacts:
                for contact in recent_contacts[:5]:
                    st.write(f"👤 **{contact.get('name', 'N/A')}**")
                    st.write(f"   📞 {contact.get('phone', 'N/A')}")
                    st.write(f"   📧 {contact.get('email', 'N/A')}")
                    if st.button(f"Contatta {contact.get('name', '')}", key=f"contact_{contact.get('name', '')}"):
                        st.session_state.selected_contact = contact
                        st.rerun()
                    st.markdown("---")
            else:
                st.success("Tutti i lead sono stati contattati!")
        else:
            st.info("Nessun contatto registrato")

# Pagina Contatti & Lead
elif page == "👥 Contatti & Lead":
    st.header("👥 Gestione Contatti & Lead")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Form nuovo contatto
        if st.session_state.get("show_new_contact", False) or st.button("➕ Aggiungi Nuovo Contatto"):
            with st.form("new_contact_form"):
                st.subheader("📝 Nuovo Contatto")
                
                name = st.text_input("Nome Completo *", placeholder="Mario Rossi")
                email = st.text_input("Email *", placeholder="mario.rossi@email.com")
                phone = st.text_input("Telefono *", placeholder="+39 123 456 7890")
                event_type = st.selectbox(
                    "Tipo Evento Interessato",
                    ["Compleanno", "Festa Privata", "Evento Aziendale", "Altro"]
                )
                notes = st.text_area("Note", placeholder="Note aggiuntive sul contatto...")
                
                col_submit1, col_submit2 = st.columns(2)
                with col_submit1:
                    submit = st.form_submit_button("💾 Salva Contatto", use_container_width=True)
                with col_submit2:
                    cancel = st.form_submit_button("❌ Annulla", use_container_width=True)
                
                if submit and name and email and phone:
                    new_contact = {
                        "id": len(contacts) + 1,
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "event_type": event_type,
                        "notes": notes,
                        "status": "Nuovo",
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "last_contact": None
                    }
                    contacts.append(new_contact)
                    save_to_session("contacts", contacts)
                    st.success(f"✅ Contatto {name} aggiunto con successo!")
                    st.session_state.show_new_contact = False
                    st.rerun()
                elif cancel:
                    st.session_state.show_new_contact = False
                    st.rerun()
        
        st.markdown("---")
        
        # Lista contatti
        st.subheader("📋 Lista Contatti")
        
        if contacts:
            # Filtri
            filter_col1, filter_col2 = st.columns(2)
            with filter_col1:
                status_filter = st.selectbox(
                    "Filtra per Status",
                    ["Tutti", "Nuovo", "Contattato", "Interessato", "Convertito", "Perso"]
                )
            with filter_col2:
                search_term = st.text_input("🔍 Cerca contatto", placeholder="Nome, email o telefono...")
            
            filtered_contacts = contacts
            if status_filter != "Tutti":
                filtered_contacts = [c for c in filtered_contacts if c.get("status") == status_filter]
            if search_term:
                filtered_contacts = [
                    c for c in filtered_contacts 
                    if search_term.lower() in c.get("name", "").lower() or
                       search_term.lower() in c.get("email", "").lower() or
                       search_term.lower() in c.get("phone", "").lower()
                ]
            
            if filtered_contacts:
                for contact in filtered_contacts:
                    with st.expander(f"👤 {contact.get('name', 'N/A')} - {contact.get('status', 'N/A')}"):
                        col_info1, col_info2 = st.columns(2)
                        with col_info1:
                            st.write(f"**Email:** {contact.get('email', 'N/A')}")
                            st.write(f"**Telefono:** {contact.get('phone', 'N/A')}")
                        with col_info2:
                            st.write(f"**Tipo Evento:** {contact.get('event_type', 'N/A')}")
                            st.write(f"**Creato:** {contact.get('created_at', 'N/A')}")
                        
                        if contact.get('notes'):
                            st.write(f"**Note:** {contact.get('notes', '')}")
                        
                        col_actions1, col_actions2, col_actions3 = st.columns(3)
                        with col_actions1:
                            if st.button("📞 Contatta", key=f"call_{contact.get('id')}"):
                                contact["status"] = "Contattato"
                                contact["last_contact"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                save_to_session("contacts", contacts)
                                st.rerun()
                        with col_actions2:
                            if st.button("💰 Crea Preventivo", key=f"quote_{contact.get('id')}"):
                                st.session_state.selected_contact_for_quote = contact
                                st.session_state.show_new_quote = True
                                st.rerun()
                        with col_actions3:
                            new_status = st.selectbox(
                                "Cambia Status",
                                ["Nuovo", "Contattato", "Interessato", "Convertito", "Perso"],
                                index=["Nuovo", "Contattato", "Interessato", "Convertito", "Perso"].index(contact.get("status", "Nuovo")),
                                key=f"status_{contact.get('id')}"
                            )
                            if new_status != contact.get("status"):
                                contact["status"] = new_status
                                save_to_session("contacts", contacts)
                                st.rerun()
            else:
                st.info("Nessun contatto trovato con i filtri selezionati")
        else:
            st.info("Nessun contatto registrato. Aggiungi il primo contatto!")
    
    with col2:
        st.subheader("📊 Statistiche Contatti")
        if contacts:
            total = len(contacts)
            st.metric("Totale Contatti", total)
            
            status_counts = {}
            for contact in contacts:
                status = contact.get("status", "Nuovo")
                status_counts[status] = status_counts.get(status, 0) + 1
            
            st.markdown("---")
            for status, count in status_counts.items():
                percentage = (count / total) * 100 if total > 0 else 0
                st.write(f"**{status}:** {count} ({percentage:.1f}%)")

# Pagina Calendario Eventi
elif page == "📅 Calendario Eventi":
    st.header("📅 Calendario Eventi")
    
    events = load_from_session("events")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Form nuovo evento
        if st.session_state.get("show_new_event", False) or st.button("➕ Aggiungi Nuovo Evento"):
            with st.form("new_event_form"):
                st.subheader("🎉 Nuovo Evento")
                
                client_name = st.text_input("Nome Cliente *", placeholder="Mario Rossi")
                event_type = st.selectbox(
                    "Tipo Evento *",
                    ["Compleanno", "Festa Privata", "Evento Aziendale", "Matrimonio", "Altro"]
                )
                date = st.date_input("Data Evento *", min_value=datetime.now().date())
                time = st.time_input("Orario Evento", value=datetime.strptime("20:00", "%H:%M").time())
                guests = st.number_input("Numero Ospiti", min_value=1, value=50)
                price = st.number_input("Prezzo (€)", min_value=0.0, value=0.0, step=100.0)
                status = st.selectbox(
                    "Status",
                    ["In Attesa", "Confermato", "Completato", "Cancellato"]
                )
                notes = st.text_area("Note", placeholder="Note aggiuntive sull'evento...")
                
                col_submit1, col_submit2 = st.columns(2)
                with col_submit1:
                    submit = st.form_submit_button("💾 Salva Evento", use_container_width=True)
                with col_submit2:
                    cancel = st.form_submit_button("❌ Annulla", use_container_width=True)
                
                if submit and client_name and date:
                    new_event = {
                        "id": len(events) + 1,
                        "client_name": client_name,
                        "event_type": event_type,
                        "date": date.strftime("%Y-%m-%d"),
                        "time": time.strftime("%H:%M"),
                        "guests": guests,
                        "price": float(price),
                        "status": status,
                        "notes": notes,
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    events.append(new_event)
                    save_to_session("events", events)
                    st.success(f"✅ Evento per {client_name} aggiunto con successo!")
                    st.session_state.show_new_event = False
                    st.rerun()
                elif cancel:
                    st.session_state.show_new_event = False
                    st.rerun()
        
        st.markdown("---")
        
        # Lista eventi
        st.subheader("📋 Lista Eventi")
        
        if events:
            # Filtri
            filter_col1, filter_col2 = st.columns(2)
            with filter_col1:
                status_filter = st.selectbox(
                    "Filtra per Status",
                    ["Tutti", "In Attesa", "Confermato", "Completato", "Cancellato"],
                    key="event_status_filter"
                )
            with filter_col2:
                date_filter = st.date_input(
                    "Filtra per Data",
                    value=None,
                    key="event_date_filter"
                )
            
            filtered_events = events
            if status_filter != "Tutti":
                filtered_events = [e for e in filtered_events if e.get("status") == status_filter]
            if date_filter:
                filtered_events = [
                    e for e in filtered_events 
                    if e.get("date") == date_filter.strftime("%Y-%m-%d")
                ]
            
            # Ordina per data
            filtered_events = sorted(
                filtered_events,
                key=lambda x: x.get("date", "9999-99-99")
            )
            
            if filtered_events:
                for event in filtered_events:
                    event_date = datetime.strptime(event.get("date", "2000-01-01"), "%Y-%m-%d")
                    status_color = {
                        "Confermato": "🟢",
                        "In Attesa": "🟡",
                        "Completato": "🔵",
                        "Cancellato": "🔴"
                    }.get(event.get("status", ""), "⚪")
                    
                    with st.expander(f"{status_color} {event.get('event_type', 'N/A')} - {event.get('client_name', 'N/A')} ({event_date.strftime('%d/%m/%Y')})"):
                        col_info1, col_info2 = st.columns(2)
                        with col_info1:
                            st.write(f"**Cliente:** {event.get('client_name', 'N/A')}")
                            st.write(f"**Data:** {event_date.strftime('%d/%m/%Y')}")
                            st.write(f"**Orario:** {event.get('time', 'N/A')}")
                            st.write(f"**Ospiti:** {event.get('guests', 'N/A')}")
                        with col_info2:
                            st.write(f"**Status:** {event.get('status', 'N/A')}")
                            st.write(f"**Prezzo:** €{event.get('price', 0):,.2f}")
                            st.write(f"**Creato:** {event.get('created_at', 'N/A')}")
                        
                        if event.get('notes'):
                            st.write(f"**Note:** {event.get('notes', '')}")
                        
                        col_actions1, col_actions2 = st.columns(2)
                        with col_actions1:
                            new_status = st.selectbox(
                                "Cambia Status",
                                ["In Attesa", "Confermato", "Completato", "Cancellato"],
                                index=["In Attesa", "Confermato", "Completato", "Cancellato"].index(event.get("status", "In Attesa")),
                                key=f"event_status_{event.get('id')}"
                            )
                            if new_status != event.get("status"):
                                event["status"] = new_status
                                save_to_session("events", events)
                                st.rerun()
                        with col_actions2:
                            if st.button("🗑️ Elimina", key=f"delete_event_{event.get('id')}"):
                                events.remove(event)
                                save_to_session("events", events)
                                st.rerun()
            else:
                st.info("Nessun evento trovato con i filtri selezionati")
        else:
            st.info("Nessun evento registrato. Aggiungi il primo evento!")
    
    with col2:
        st.subheader("📊 Statistiche Eventi")
        if events:
            total = len(events)
            confirmed = len([e for e in events if e.get("status") == "Confermato"])
            total_revenue = calculate_revenue(events)
            
            st.metric("Totale Eventi", total)
            st.metric("Eventi Confermati", confirmed)
            st.metric("Fatturato Totale", f"€ {total_revenue:,.2f}")
            
            st.markdown("---")
            st.subheader("📅 Eventi del Mese")
            
            now = datetime.now()
            month_events = [
                e for e in events 
                if e.get("status") == "Confermato" and
                datetime.strptime(e.get("date", "2000-01-01"), "%Y-%m-%d").month == now.month and
                datetime.strptime(e.get("date", "2000-01-01"), "%Y-%m-%d").year == now.year
            ]
            
            if month_events:
                for event in sorted(month_events, key=lambda x: x.get("date", "")):
                    event_date = datetime.strptime(event.get("date", "2000-01-01"), "%Y-%m-%d")
                    st.write(f"📅 **{event_date.strftime('%d/%m')}**")
                    st.write(f"   {event.get('client_name', 'N/A')}")
                    st.write(f"   {event.get('event_type', 'N/A')}")
            else:
                st.info("Nessun evento questo mese")

# Pagina Preventivi
elif page == "💰 Preventivi":
    st.header("💰 Gestione Preventivi")
    
    quotes = load_from_session("quotes")
    contacts = load_from_session("contacts")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Form nuovo preventivo
        if st.session_state.get("show_new_quote", False) or st.button("➕ Crea Nuovo Preventivo"):
            with st.form("new_quote_form"):
                st.subheader("📝 Nuovo Preventivo")
                
                # Seleziona contatto esistente o inserisci nuovo
                use_existing = st.checkbox("Usa contatto esistente")
                
                if use_existing and contacts:
                    contact_options = [f"{c.get('name', 'N/A')} - {c.get('email', 'N/A')}" for c in contacts]
                    selected_contact_idx = st.selectbox(
                        "Seleziona Contatto",
                        range(len(contact_options)),
                        format_func=lambda x: contact_options[x]
                    )
                    selected_contact = contacts[selected_contact_idx]
                    client_name = selected_contact.get("name", "")
                    client_email = selected_contact.get("email", "")
                    client_phone = selected_contact.get("phone", "")
                else:
                    client_name = st.text_input("Nome Cliente *", placeholder="Mario Rossi")
                    client_email = st.text_input("Email Cliente", placeholder="mario.rossi@email.com")
                    client_phone = st.text_input("Telefono Cliente", placeholder="+39 123 456 7890")
                
                event_type = st.selectbox(
                    "Tipo Evento *",
                    ["Compleanno", "Festa Privata", "Evento Aziendale", "Matrimonio", "Altro"]
                )
                date = st.date_input("Data Evento Proposta *", min_value=datetime.now().date())
                guests = st.number_input("Numero Ospiti Previsti", min_value=1, value=50)
                
                st.subheader("Servizi Inclusi")
                col_services1, col_services2 = st.columns(2)
                with col_services1:
                    location = st.checkbox("Location", value=True)
                    sound_system = st.checkbox("Impianto Audio", value=True)
                    lighting = st.checkbox("Illuminazione", value=False)
                    dj = st.checkbox("DJ", value=False)
                with col_services2:
                    bar_service = st.checkbox("Servizio Bar", value=False)
                    catering = st.checkbox("Catering", value=False)
                    security = st.checkbox("Sicurezza", value=False)
                    decoration = st.checkbox("Decorazioni", value=False)
                
                base_price = st.number_input("Prezzo Base (€)", min_value=0.0, value=1000.0, step=100.0)
                discount = st.number_input("Sconto (%)", min_value=0.0, max_value=100.0, value=0.0, step=5.0)
                
                final_price = base_price * (1 - discount / 100)
                st.info(f"💰 **Prezzo Finale: €{final_price:,.2f}**")
                
                valid_until = st.date_input("Valido Fino", min_value=datetime.now().date(), value=(datetime.now() + timedelta(days=30)).date())
                notes = st.text_area("Note Aggiuntive", placeholder="Note sul preventivo...")
                
                col_submit1, col_submit2 = st.columns(2)
                with col_submit1:
                    submit = st.form_submit_button("💾 Salva Preventivo", use_container_width=True)
                with col_submit2:
                    cancel = st.form_submit_button("❌ Annulla", use_container_width=True)
                
                if submit and client_name and date:
                    new_quote = {
                        "id": len(quotes) + 1,
                        "client_name": client_name,
                        "client_email": client_email,
                        "client_phone": client_phone,
                        "event_type": event_type,
                        "date": date.strftime("%Y-%m-%d"),
                        "guests": guests,
                        "services": {
                            "location": location,
                            "sound_system": sound_system,
                            "lighting": lighting,
                            "dj": dj,
                            "bar_service": bar_service,
                            "catering": catering,
                            "security": security,
                            "decoration": decoration
                        },
                        "base_price": float(base_price),
                        "discount": float(discount),
                        "final_price": float(final_price),
                        "valid_until": valid_until.strftime("%Y-%m-%d"),
                        "status": "In Attesa",
                        "notes": notes,
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    quotes.append(new_quote)
                    save_to_session("quotes", quotes)
                    st.success(f"✅ Preventivo per {client_name} creato con successo!")
                    st.session_state.show_new_quote = False
                    st.rerun()
                elif cancel:
                    st.session_state.show_new_quote = False
                    st.rerun()
        
        st.markdown("---")
        
        # Lista preventivi
        st.subheader("📋 Lista Preventivi")
        
        if quotes:
            # Filtri
            status_filter = st.selectbox(
                "Filtra per Status",
                ["Tutti", "In Attesa", "Accettato", "Rifiutato", "Scaduto"],
                key="quote_status_filter"
            )
            
            filtered_quotes = quotes
            if status_filter != "Tutti":
                filtered_quotes = [q for q in filtered_quotes if q.get("status") == status_filter]
            
            # Controlla preventivi scaduti
            now = datetime.now().date()
            for quote in filtered_quotes:
                valid_until = datetime.strptime(quote.get("valid_until", "2000-01-01"), "%Y-%m-%d").date()
                if valid_until < now and quote.get("status") == "In Attesa":
                    quote["status"] = "Scaduto"
            
            if filtered_quotes:
                for quote in filtered_quotes:
                    quote_date = datetime.strptime(quote.get("date", "2000-01-01"), "%Y-%m-%d")
                    status_color = {
                        "Accettato": "🟢",
                        "In Attesa": "🟡",
                        "Rifiutato": "🔴",
                        "Scaduto": "⚫"
                    }.get(quote.get("status", ""), "⚪")
                    
                    with st.expander(f"{status_color} Preventivo #{quote.get('id', 'N/A')} - {quote.get('client_name', 'N/A')} (€{quote.get('final_price', 0):,.2f})"):
                        col_info1, col_info2 = st.columns(2)
                        with col_info1:
                            st.write(f"**Cliente:** {quote.get('client_name', 'N/A')}")
                            st.write(f"**Email:** {quote.get('client_email', 'N/A')}")
                            st.write(f"**Telefono:** {quote.get('client_phone', 'N/A')}")
                            st.write(f"**Tipo Evento:** {quote.get('event_type', 'N/A')}")
                            st.write(f"**Data Evento:** {quote_date.strftime('%d/%m/%Y')}")
                            st.write(f"**Ospiti:** {quote.get('guests', 'N/A')}")
                        with col_info2:
                            st.write(f"**Status:** {quote.get('status', 'N/A')}")
                            st.write(f"**Prezzo Base:** €{quote.get('base_price', 0):,.2f}")
                            st.write(f"**Sconto:** {quote.get('discount', 0):.1f}%")
                            st.write(f"**Prezzo Finale:** €{quote.get('final_price', 0):,.2f}")
                            valid_until = datetime.strptime(quote.get("valid_until", "2000-01-01"), "%Y-%m-%d")
                            st.write(f"**Valido Fino:** {valid_until.strftime('%d/%m/%Y')}")
                            st.write(f"**Creato:** {quote.get('created_at', 'N/A')}")
                        
                        st.write("**Servizi Inclusi:**")
                        services = quote.get("services", {})
                        services_list = [k.replace("_", " ").title() for k, v in services.items() if v]
                        if services_list:
                            st.write(", ".join(services_list))
                        else:
                            st.write("Nessun servizio selezionato")
                        
                        if quote.get('notes'):
                            st.write(f"**Note:** {quote.get('notes', '')}")
                        
                        col_actions1, col_actions2, col_actions3 = st.columns(3)
                        with col_actions1:
                            new_status = st.selectbox(
                                "Cambia Status",
                                ["In Attesa", "Accettato", "Rifiutato", "Scaduto"],
                                index=["In Attesa", "Accettato", "Rifiutato", "Scaduto"].index(quote.get("status", "In Attesa")),
                                key=f"quote_status_{quote.get('id')}"
                            )
                            if new_status != quote.get("status"):
                                quote["status"] = new_status
                                save_to_session("quotes", quotes)
                                st.rerun()
                        with col_actions2:
                            if st.button("📧 Invia Email", key=f"email_quote_{quote.get('id')}"):
                                st.info("💡 Funzionalità email da implementare con integrazione servizio email")
                        with col_actions3:
                            if st.button("🗑️ Elimina", key=f"delete_quote_{quote.get('id')}"):
                                quotes.remove(quote)
                                save_to_session("quotes", quotes)
                                st.rerun()
            else:
                st.info("Nessun preventivo trovato con i filtri selezionati")
        else:
            st.info("Nessun preventivo creato. Crea il primo preventivo!")
    
    with col2:
        st.subheader("📊 Statistiche Preventivi")
        if quotes:
            total = len(quotes)
            pending = len([q for q in quotes if q.get("status") == "In Attesa"])
            accepted = len([q for q in quotes if q.get("status") == "Accettato"])
            total_value = sum(q.get("final_price", 0) for q in quotes)
            
            st.metric("Totale Preventivi", total)
            st.metric("In Attesa", pending)
            st.metric("Accettati", accepted)
            st.metric("Valore Totale", f"€ {total_value:,.2f}")

# Pagina Marketing
elif page == "📧 Marketing":
    st.header("📧 Marketing & Comunicazioni")
    
    contacts = load_from_session("contacts")
    quotes = load_from_session("quotes")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📧 Template Email Marketing")
        
        template_type = st.selectbox(
            "Seleziona Template",
            ["Preventivo", "Follow-up", "Promozione", "Ringraziamento", "Personalizzato"]
        )
        
        if template_type == "Preventivo":
            st.markdown("""
            **Oggetto:** Preventivo Evento 747Disco - [Nome Cliente]
            
            **Messaggio:**
            
            Gentile [Nome Cliente],
            
            Grazie per il tuo interesse in 747Disco!
            
            Siamo lieti di presentarti il preventivo per il tuo evento del [Data Evento].
            
            **Dettagli Evento:**
            - Tipo: [Tipo Evento]
            - Data: [Data]
            - Ospiti: [Numero Ospiti]
            - Prezzo: €[Importo]
            
            Il preventivo è valido fino al [Data Scadenza].
            
            Siamo a tua disposizione per qualsiasi domanda o personalizzazione.
            
            A presto,
            Il Team 747Disco
            📍 Ciampino, Roma - Vicino al GRA
            """)
        
        elif template_type == "Follow-up":
            st.markdown("""
            **Oggetto:** Ricordiamo il tuo evento con 747Disco
            
            **Messaggio:**
            
            Gentile [Nome Cliente],
            
            Ti scriviamo per ricordarti della possibilità di organizzare il tuo evento con noi.
            
            Siamo specializzati in:
            - 🎉 Feste di compleanno
            - 🎊 Eventi privati
            - 🏢 Eventi aziendali
            
            La nostra location è facilmente raggiungibile a Ciampino, vicino al GRA.
            
            Contattaci per un preventivo personalizzato!
            
            Cordiali saluti,
            Il Team 747Disco
            """)
        
        elif template_type == "Promozione":
            st.markdown("""
            **Oggetto:** 🎉 Promozione Speciale 747Disco!
            
            **Messaggio:**
            
            Gentile [Nome Cliente],
            
            Abbiamo una promozione speciale per te!
            
            **Sconto del [X]%** su tutti gli eventi prenotati entro [Data].
            
            Prenota ora e risparmia!
            
            La nostra location offre:
            - Impianti audio professionali
            - Illuminazione d'effetto
            - Servizio bar completo
            - Spazio per [X] ospiti
            
            Contattaci per maggiori informazioni!
            
            Promozione valida fino al [Data].
            
            A presto,
            Il Team 747Disco
            """)
        
        elif template_type == "Ringraziamento":
            st.markdown("""
            **Oggetto:** Grazie per aver scelto 747Disco!
            
            **Messaggio:**
            
            Gentile [Nome Cliente],
            
            Grazie per aver scelto 747Disco per il tuo evento!
            
            Siamo stati felici di averti come nostro ospite e speriamo che tu abbia trascorso una serata indimenticabile.
            
            Ci piacerebbe ricevere il tuo feedback per migliorare sempre di più i nostri servizi.
            
            Se hai bisogno di organizzare altri eventi in futuro, siamo a tua completa disposizione!
            
            Grazie ancora,
            Il Team 747Disco
            """)
        
        else:
            custom_subject = st.text_input("Oggetto Email", placeholder="Oggetto dell'email...")
            custom_message = st.text_area("Messaggio", height=300, placeholder="Scrivi il tuo messaggio personalizzato...")
        
        st.markdown("---")
        
        # Selezione destinatari
        st.subheader("📮 Destinatari")
        
        recipient_type = st.radio(
            "Seleziona destinatari",
            ["Tutti i contatti", "Contatti non contattati", "Preventivi in attesa", "Selezione manuale"]
        )
        
        if recipient_type == "Selezione manuale" and contacts:
            selected_contacts = st.multiselect(
                "Seleziona contatti",
                [f"{c.get('name', 'N/A')} - {c.get('email', 'N/A')}" for c in contacts]
            )
        
        if st.button("📧 Invia Email", use_container_width=True):
            st.success("✅ Email inviate! (Funzionalità da implementare con servizio email)")
    
    with col2:
        st.subheader("📊 Campagne Marketing")
        
        st.metric("Contatti Totali", len(contacts))
        st.metric("Preventivi Attivi", len([q for q in quotes if q.get("status") == "In Attesa"]))
        
        st.markdown("---")
        
        st.subheader("💡 Suggerimenti Marketing")
        
        st.info("""
        **Strategie Consigliate:**
        
        1. **Follow-up Automatici**
           - Contatta i lead entro 24h
           - Follow-up dopo 3-5 giorni
        
        2. **Personalizzazione**
           - Usa il nome del cliente
           - Riferimenti al tipo evento
        
        3. **Call-to-Action**
           - Chiamaci ora
           - Richiedi preventivo
           - Visita la location
        
        4. **Social Proof**
           - Condividi testimonianze
           - Mostra eventi passati
        """)
        
        st.markdown("---")
        
        st.subheader("📅 Calendario Campagne")
        
        campaign_date = st.date_input("Data Campagna", value=datetime.now().date())
        campaign_type = st.selectbox(
            "Tipo Campagna",
            ["Email", "Social Media", "Promozione", "Evento"]
        )
        
        if st.button("➕ Crea Campagna", use_container_width=True):
            st.success("✅ Campagna creata! (Funzionalità da implementare)")

# Pagina Analytics
elif page == "📊 Analytics":
    st.header("📊 Analytics & Report")
    
    events = load_from_session("events")
    quotes = load_from_session("quotes")
    contacts = load_from_session("contacts")
    
    # Metriche principali
    col1, col2, col3, col4 = st.columns(4)
    
    total_revenue = calculate_revenue(events)
    conversion_rate = calculate_conversion_rate(quotes, events)
    avg_event_price = total_revenue / len([e for e in events if e.get("status") == "Confermato"]) if len([e for e in events if e.get("status") == "Confermato"]) > 0 else 0
    
    with col1:
        st.metric("💰 Fatturato Totale", f"€ {total_revenue:,.2f}")
    with col2:
        st.metric("📈 Tasso Conversione", f"{conversion_rate:.1f}%")
    with col3:
        st.metric("💵 Prezzo Medio Evento", f"€ {avg_event_price:,.2f}")
    with col4:
        st.metric("👥 Contatti Totali", len(contacts))
    
    st.markdown("---")
    
    # Analisi per tipo evento
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Eventi per Tipo")
        if events:
            event_types = {}
            for event in events:
                if event.get("status") == "Confermato":
                    event_type = event.get("event_type", "Altro")
                    event_types[event_type] = event_types.get(event_type, 0) + 1
            
            if event_types:
                event_df = pd.DataFrame(list(event_types.items()), columns=["Tipo Evento", "Quantità"])
                st.bar_chart(event_df.set_index("Tipo Evento"))
            else:
                st.info("Nessun evento confermato per l'analisi")
        else:
            st.info("Nessun dato disponibile")
    
    with col2:
        st.subheader("📅 Fatturato Mensile")
        if events:
            monthly_revenue = {}
            for event in events:
                if event.get("status") == "Confermato":
                    event_date = datetime.strptime(event.get("date", "2000-01-01"), "%Y-%m-%d")
                    month_key = event_date.strftime("%Y-%m")
                    monthly_revenue[month_key] = monthly_revenue.get(month_key, 0) + event.get("price", 0)
            
            if monthly_revenue:
                revenue_df = pd.DataFrame(list(monthly_revenue.items()), columns=["Mese", "Fatturato"])
                revenue_df = revenue_df.sort_values("Mese")
                st.line_chart(revenue_df.set_index("Mese"))
            else:
                st.info("Nessun dato disponibile")
        else:
            st.info("Nessun dato disponibile")
    
    st.markdown("---")
    
    # Report dettagliato
    st.subheader("📋 Report Dettagliato")
    
    report_type = st.selectbox(
        "Seleziona Report",
        ["Vendite", "Lead", "Preventivi", "Performance"]
    )
    
    if report_type == "Vendite":
        if events:
            confirmed_events = [e for e in events if e.get("status") == "Confermato"]
            if confirmed_events:
                sales_df = pd.DataFrame(confirmed_events)
                st.dataframe(
                    sales_df[["client_name", "event_type", "date", "guests", "price", "status"]],
                    use_container_width=True
                )
            else:
                st.info("Nessun evento confermato")
        else:
            st.info("Nessun evento registrato")
    
    elif report_type == "Lead":
        if contacts:
            contacts_df = pd.DataFrame(contacts)
            st.dataframe(
                contacts_df[["name", "email", "phone", "event_type", "status", "created_at"]],
                use_container_width=True
            )
        else:
            st.info("Nessun contatto registrato")
    
    elif report_type == "Preventivi":
        if quotes:
            quotes_df = pd.DataFrame(quotes)
            # Espandi i servizi per la visualizzazione
            display_quotes = []
            for quote in quotes:
                display_quote = {
                    "ID": quote.get("id"),
                    "Cliente": quote.get("client_name"),
                    "Tipo Evento": quote.get("event_type"),
                    "Data": quote.get("date"),
                    "Ospiti": quote.get("guests"),
                    "Prezzo Finale": quote.get("final_price"),
                    "Status": quote.get("status")
                }
                display_quotes.append(display_quote)
            
            quotes_display_df = pd.DataFrame(display_quotes)
            st.dataframe(quotes_display_df, use_container_width=True)
        else:
            st.info("Nessun preventivo creato")
    
    else:  # Performance
        st.subheader("🎯 KPI Performance")
        
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        
        with kpi_col1:
            if quotes:
                avg_quote_value = sum(q.get("final_price", 0) for q in quotes) / len(quotes)
                st.metric("Valore Medio Preventivo", f"€ {avg_quote_value:,.2f}")
        
        with kpi_col2:
            if contacts:
                conversion_rate_contacts = (len([c for c in contacts if c.get("status") == "Convertito"]) / len(contacts)) * 100
                st.metric("Tasso Conversione Contatti", f"{conversion_rate_contacts:.1f}%")
        
        with kpi_col3:
            if events:
                completed_events = len([e for e in events if e.get("status") == "Completato"])
                st.metric("Eventi Completati", completed_events)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p><strong>747Disco</strong> - Gestione Vendite & Marketing | 📍 Ciampino, Roma | 🚗 Vicino al GRA</p>
    <p>© 2024 - Sistema di gestione eventi privati</p>
</div>
""", unsafe_allow_html=True)
