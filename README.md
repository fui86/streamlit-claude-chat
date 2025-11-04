# 747Disco - Assistente Vendite Eventi AI 🎉

Applicazione Streamlit con intelligenza artificiale Claude per la gestione delle vendite di eventi presso **747Disco** - Location per eventi privati a Ciampino (Roma).

![screen_shot](./image/screen_shot_1.gif)

## 🎯 Caratteristiche Principali

- **Generazione automatica di preventivi** personalizzati per eventi
- **Template veloci** per risposte immediate a richieste comuni
- **Assistente AI** specializzato in vendita e marketing di eventi
- **Form interattivo** per raccolta dettagli cliente ed evento
- **Upload documenti** per gestione preventivi e contratti
- **Comunicazione professionale** - email, WhatsApp, proposte commerciali

## 📍 Informazioni Location

**747Disco** - Ciampino (Roma)
- 📍 Posizione: Vicino al GRA
- 👥 Capienza: 200-300 persone
- 🚗 Parcheggio disponibile
- 🎊 Specializzazioni: Compleanni, eventi aziendali, cerimonie, feste private

## 🚀 Installazione e Utilizzo

### Requisiti

- Docker e Docker Compose
- Chiave API Anthropic Claude

### 1. Clone del Repository

```bash
git clone <repository-url>
cd streamlit-claude-chat
```

### 2. Configurazione Secrets

Crea un file `.streamlit/secrets.toml` con la tua chiave API Anthropic:

```toml
ANTHROPIC_API_KEY = "sk-ant-xxxxx..."
```

### 3. Build Container

```bash
docker build ./ -t 747disco-sales-assistant
```

### 4. Avvio Applicazione

```bash
docker compose up -d
```

L'applicazione sarà disponibile su `http://localhost:8501`

## 💼 Come Utilizzare l'Assistente

### Generazione Preventivi
1. Compila il form laterale con i dettagli dell'evento
2. Seleziona i servizi richiesti
3. Clicca "Genera Preventivo"
4. L'AI creerà una proposta commerciale completa

### Template Veloci
Usa i pulsanti nella sidebar per:
- 💰 Preventivi rapidi
- 🎂 Feste di compleanno
- 🏢 Eventi aziendali
- 📧 Email commerciali
- 📱 Risposte WhatsApp

### Chat Libera
Scrivi direttamente nella chat per:
- Gestire obiezioni clienti
- Creare proposte personalizzate
- Ottenere consigli di marketing
- Preparare presentazioni commerciali

## 🛠️ Tecnologie Utilizzate

- **Streamlit** - Framework per l'interfaccia web
- **Anthropic Claude** - Modelli AI avanzati
- **Python 3.x**
- **Docker** - Containerizzazione

## 📝 Modelli Claude Disponibili

- Claude 3.5 Sonnet (consigliato)
- Claude Sonnet 4
- Claude 3.5 Haiku
- Claude 3 Opus

## 📞 Supporto

Per domande o supporto tecnico, contatta il team di sviluppo.

