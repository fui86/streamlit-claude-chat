# 747Disco - Sistema Gestione Vendite & Marketing

Sistema completo di gestione vendite e marketing per eventi privati sviluppato con Streamlit.

![747Disco](./image/screen_shot_1.gif)

## 🎉 747Disco

**Location Eventi Privati**  
📍 Ciampino, Roma  
🚗 Vicino al GRA

Specializzato in:
- Feste di compleanno
- Eventi privati
- Organizzazione eventi

## 🚀 Funzionalità

Il sistema include:

- **🏠 Dashboard Vendite**: Metriche e statistiche in tempo reale
- **👥 Gestione Contatti & Lead**: CRM completo per tracciare tutti i contatti
- **📅 Calendario Eventi**: Gestione eventi con calendario e disponibilità
- **💰 Preventivi**: Sistema completo per creare e gestire preventivi
- **📧 Marketing**: Template email e campagne marketing
- **📊 Analytics**: Report dettagliati e analisi performance

## 📋 Requisiti

- Python 3.10+
- Streamlit
- Pandas

## 🛠️ Installazione

### Clona il repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Installa le dipendenze

```bash
pip install -r requirements.txt
```

## 🚀 Esecuzione

### Esegui localmente

```bash
streamlit run app/main.py
```

L'applicazione sarà disponibile su `http://localhost:8501`

### Build e deploy con Docker

#### Build container

```bash
docker build ./ -t 747disco-app
```

#### Deploy locale con Docker Compose

```bash
docker compose up -d
```

L'applicazione sarà disponibile su `http://localhost:8501`

## 📖 Utilizzo

1. **Dashboard**: Visualizza metriche e statistiche principali
2. **Contatti**: Aggiungi e gestisci contatti e lead
3. **Eventi**: Crea e gestisci eventi nel calendario
4. **Preventivi**: Crea preventivi personalizzati per i clienti
5. **Marketing**: Usa template email e campagne marketing
6. **Analytics**: Analizza performance e genera report

## 🎯 Caratteristiche Principali

- **Gestione Contatti Completa**: CRM integrato per tracciare tutti i lead
- **Sistema Preventivi**: Creazione preventivi con servizi personalizzabili
- **Calendario Eventi**: Visualizzazione e gestione eventi
- **Template Marketing**: Template email predefiniti per comunicazioni
- **Analytics Avanzati**: Report e metriche per ottimizzare le vendite
- **Interfaccia Moderna**: UI intuitiva e responsive

## 📝 Note

- I dati sono salvati nella session state di Streamlit (temporanei)
- Per produzione, integrare con database (PostgreSQL, MySQL, etc.)
- Per email marketing, integrare con servizio email (SendGrid, Mailchimp, etc.)

## 📄 Licenza

Vedi il file LICENSE per i dettagli.
