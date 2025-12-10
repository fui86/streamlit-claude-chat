# 🎤 Karaoke Video Player - Browser Extension

Una estensione per Google Chrome e Mozilla Firefox per scaricare e riprodurre video YouTube in modalità karaoke su un secondo monitor.

## 🌐 Compatibilità Browser

- ✅ **Google Chrome** / Chromium (Manifest V3) - Supporto completo con rilevamento automatico multi-monitor
- ✅ **Mozilla Firefox** (Manifest V2) - Supporto completo, spostamento manuale finestra su secondo monitor

**📖 Per installazione Firefox**: Vedi [FIREFOX-INSTALL.md](./FIREFOX-INSTALL.md)

## 📋 Funzionalità

- ✅ Aggiunta di link YouTube alla playlist
- ✅ Riproduzione automatica dei video in sequenza
- ✅ Visualizzazione a schermo intero sul secondo monitor
- ✅ Interfaccia di gestione sul monitor principale
- ✅ Richiesta di eliminazione file dopo la riproduzione
- ✅ Supporto per playlist multiple
- ✅ Interfaccia utente in italiano
- ✅ **Scelta della qualità video (360p, 480p, 720p, 1080p)**
- ✅ **Scelta della cartella di download personalizzata**

## 🚀 Installazione

### 📌 Scegli il tuo Browser

- **Chrome/Chromium**: Segui le istruzioni qui sotto
- **Firefox**: Vedi la [Guida Firefox](./FIREFOX-INSTALL.md)

### Prerequisiti (Chrome)
- Google Chrome o Chromium browser
- Due monitor collegati (opzionale, ma consigliato)

### Passaggi di Installazione

1. **Scarica l'estensione**
   ```bash
   # Se hai clonato il repository
   cd streamlit-claude-chat/chrome-extension
   ```

2. **Apri Chrome Extensions**
   - Apri Google Chrome
   - Vai a `chrome://extensions/`
   - Oppure: Menu → Altri strumenti → Estensioni

3. **Attiva la Modalità Sviluppatore**
   - Attiva l'interruttore "Modalità sviluppatore" nell'angolo in alto a destra

4. **Carica l'estensione**
   - Clicca su "Carica estensione non pacchettizzata"
   - Seleziona la cartella `chrome-extension`
   - L'estensione verrà installata e apparirà nella barra degli strumenti

## 📖 Come Usare

### 0. Configurazione (Prima volta)
- Clicca su "⚙️ Impostazioni" per espandere le opzioni
- Seleziona la qualità video desiderata (360p, 480p, 720p, 1080p)
- Specifica la cartella di download (es: "Downloads/Karaoke")
- Clicca su "💾 Salva Impostazioni"

### 1. Apertura dell'estensione
- Clicca sull'icona dell'estensione 🎤 nella barra degli strumenti di Chrome
- Si aprirà il pannello di gestione

### 2. Aggiunta di video alla playlist
- Copia un link YouTube (esempio: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
- Incolla il link nel campo "Link YouTube"
- Clicca su "➕ Aggiungi Video"
- Il video verrà aggiunto alla playlist

### 3. Riproduzione
- Aggiungi tutti i video che desideri
- Clicca su "▶️ Riproduci Tutti"
- I video verranno riprodotti nella qualità selezionata
- Ogni video si aprirà a schermo intero sul secondo monitor (se disponibile)

### 4. Gestione dei file
- Dopo ogni video, ti verrà chiesto se vuoi eliminare il file
- Scegli "💾 Mantieni" per conservare il video nella cartella specificata
- Scegli "🗑️ Elimina" per rimuovere il file

### 5. Gestione della playlist
- Usa il pulsante "✖" accanto a ogni video per rimuoverlo
- Usa "🗑️ Pulisci Playlist" per cancellare tutti i video

## ⌨️ Scorciatoie da Tastiera

Durante la riproduzione:
- `F11` - Attiva/disattiva schermo intero
- `ESC` - Esci dallo schermo intero o chiudi il player
- `Delete` - Elimina il file (nella finestra di conferma)
- `ESC` - Mantieni il file (nella finestra di conferma)

## 🎯 Requisiti Tecnici

### Permessi dell'estensione
L'estensione richiede i seguenti permessi:

- **downloads**: Per scaricare i video da YouTube
- **storage**: Per salvare la playlist
- **tabs**: Per gestire le schede del browser
- **activeTab**: Per interagire con YouTube
- **system.display**: Per rilevare il secondo monitor

### Formati supportati
- Video YouTube con qualità 480p
- Tutti i formati di link YouTube:
  - `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - `https://www.youtube.com/embed/VIDEO_ID`

## 🔧 Configurazione Multi-Monitor

Per utilizzare al meglio l'estensione con due monitor:

1. **Setup Fisico**
   - Collega un secondo monitor al computer
   - Configura il secondo monitor come "Estendi" nelle impostazioni display

2. **Posizionamento**
   - Monitor 1 (Principale): Interfaccia di gestione
   - Monitor 2 (Secondario): Player a schermo intero

3. **Durante l'uso**
   - Il player si aprirà automaticamente sul secondo monitor
   - Puoi controllare la riproduzione dal monitor principale
   - Le finestre di dialogo appariranno sul monitor principale

## ⚠️ Limitazioni e Note

### Limitazioni tecniche
- **Download YouTube**: A causa delle restrizioni di Google, l'estensione utilizza l'embed di YouTube invece del download diretto. Questo significa:
  - I video vengono riprodotti tramite YouTube Player
  - È necessaria una connessione internet attiva
  - La qualità dipende dalla connessione

### Note importanti
- L'estensione rispetta i termini di servizio di YouTube
- Per download reali, considera l'uso di servizi esterni (non inclusi)
- Assicurati di avere i diritti per riprodurre i video

## 🐛 Risoluzione dei Problemi

### Il video non si apre
- Verifica che il link YouTube sia valido
- Controlla la connessione internet
- Prova a ricaricare l'estensione

### Il secondo monitor non viene rilevato
- Verifica che il secondo monitor sia collegato e attivo
- Riavvia Chrome dopo aver collegato il monitor
- Controlla le impostazioni display del sistema

### L'estensione non funziona
- Verifica che la modalità sviluppatore sia attiva
- Ricarica l'estensione da `chrome://extensions/`
- Controlla la console per errori (Tasto destro → Ispeziona → Console)

## 📁 Struttura del Progetto

```
chrome-extension/
├── manifest.json          # Configurazione dell'estensione
├── popup.html            # Interfaccia di gestione
├── popup.css             # Stili dell'interfaccia
├── popup.js              # Logica dell'interfaccia
├── background.js         # Service worker principale
├── player.html           # Pagina del player video
├── player.js             # Logica del player
├── delete-prompt.html    # Finestra di conferma eliminazione
├── delete-prompt.js      # Logica conferma eliminazione
├── icons/                # Icone dell'estensione
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
└── README.md            # Questa guida
```

## 🔄 Aggiornamenti Futuri

Possibili miglioramenti:

- [ ] Download reale dei video in 480p
- [ ] Supporto per altre piattaforme video
- [ ] Controlli avanzati del player (pausa, avanti, indietro)
- [ ] Salvataggio automatico della playlist
- [ ] Importazione/esportazione playlist
- [ ] Sottotitoli e lyrics sincronizzati
- [ ] Effetti karaoke avanzati

## 📄 Licenza

Questa estensione è parte del progetto `streamlit-claude-chat`.
Vedi LICENSE nel repository principale.

## 👨‍💻 Autore

Creato per il progetto streamlit-claude-chat

## 🆘 Supporto

Per problemi, bug o richieste di funzionalità:
- Apri una issue nel repository GitHub
- Controlla la documentazione
- Verifica i log della console dell'estensione

---

**Buon Karaoke! 🎤🎵**
