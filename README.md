# 747Disco - Sistema di Gestione Vendite Eventi

Sistema completo di gestione vendite per eventi privati della location **747Disco** a Ciampino, Roma (vicino al GRA).

## 🎉 Caratteristiche

- **📊 Dashboard Vendite**: Overview completa delle vendite con statistiche in tempo reale
- **📅 Calendario Eventi**: Visualizzazione e gestione calendario disponibilità location
- **➕ Gestione Eventi**: Creazione e modifica eventi (compleanni, matrimoni, feste private, eventi aziendali)
- **👥 CRM Clienti**: Gestione completa anagrafica clienti con storico eventi
- **💰 Preventivi**: Creazione e gestione preventivi per potenziali clienti
- **📈 Analytics**: Report dettagliati e analisi delle vendite con grafici e KPIs

## 🚀 Installazione

### Prerequisiti

- Docker e Docker Compose installati
- Python 3.10+ (per sviluppo locale)

### Setup con Docker

1. **Clona il repository**
```bash
git clone <repository-url>
cd 747disco-gestione-vendite
```

2. **Build del container**
```bash
docker build ./ -t 747disco-app
```

3. **Avvia l'applicazione**
```bash
docker compose up -d
```

4. **Accedi all'applicazione**
Apri il browser e vai su: `http://localhost:8501`

### Setup Locale (Sviluppo)

1. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

2. **Avvia Streamlit**
```bash
streamlit run app/main.py
```

## 📋 Funzionalità Principali

### Dashboard
- Fatturato totale e mensile
- Numero eventi confermati
- Clienti attivi
- Prossimi eventi in programma
- Grafico andamento vendite mensili

### Gestione Eventi
- Creazione eventi con dettagli completi
- Calendario disponibilità
- Filtri per tipo evento e stato
- Gestione orari e numero ospiti
- Tracking prezzi e pagamenti

### CRM Clienti
- Anagrafica completa clienti
- Storico eventi per cliente
- Fatturato per cliente
- Ricerca clienti avanzata

### Preventivi
- Creazione preventivi personalizzati
- Gestione scadenze
- Servizi inclusi configurabili
- Tracking stato preventivi

### Analytics
- Report mensili dettagliati
- Grafici vendite per tipo evento
- Top clienti per fatturato
- KPIs e conversion rate

## 🏢 Informazioni Location

**747Disco**
- 📍 **Posizione**: Ciampino, Roma
- 🛣️ **Vicino al**: GRA (Grande Raccordo Anulare)
- 🎉 **Tipologia**: Location per eventi privati

## 💾 Gestione Dati

I dati vengono salvati nella sessione Streamlit. Per persistenza permanente, puoi:
- Esportare i dati in formato JSON dalla sezione Configurazioni
- Importare dati da file JSON
- Implementare un database esterno (PostgreSQL, MySQL, ecc.)

## 🔧 Tecnologie Utilizzate

- **Streamlit**: Framework web per applicazioni Python
- **Pandas**: Analisi e manipolazione dati
- **Python 3.10+**: Linguaggio di programmazione

## 📝 Note

- I dati sono salvati in memoria durante la sessione
- Per produzione, implementare un database persistente
- Aggiungere autenticazione utenti per sicurezza
- Implementare backup automatici dei dati

## 📞 Supporto

Per supporto o domande relative al sistema di gestione vendite 747Disco, contattare l'amministratore.

---

© 2024 747Disco - Sistema di Gestione Vendite Eventi Privati
