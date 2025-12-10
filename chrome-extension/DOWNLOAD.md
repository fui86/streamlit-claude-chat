# 📦 Download Estensione Karaoke Video Player

## 🔗 Link per il Download

### Opzione 1: Download diretto dal Repository GitHub

Puoi scaricare l'estensione completa direttamente dal repository GitHub:

**Link diretto alla cartella dell'estensione:**
```
https://github.com/fui86/streamlit-claude-chat/tree/copilot/create-karaoke-player-extension/chrome-extension
```

**Per scaricare tutto il branch:**
1. Vai a: `https://github.com/fui86/streamlit-claude-chat`
2. Clicca sul menu "Branch" e seleziona `copilot/create-karaoke-player-extension`
3. Clicca sul pulsante verde "Code" → "Download ZIP"
4. Estrai il file ZIP
5. Naviga nella cartella `chrome-extension`

### Opzione 2: Clone con Git

```bash
git clone https://github.com/fui86/streamlit-claude-chat.git
cd streamlit-claude-chat
git checkout copilot/create-karaoke-player-extension
cd chrome-extension
```

### Opzione 3: Download manuale dei file

Scarica individualmente tutti i file dalla cartella:
```
https://github.com/fui86/streamlit-claude-chat/tree/copilot/create-karaoke-player-extension/chrome-extension
```

Clicca su ogni file e usa il pulsante "Raw" o "Download" per salvarlo.

## 📋 File necessari per l'estensione

Assicurati di avere tutti questi file nella cartella `chrome-extension`:

```
chrome-extension/
├── manifest.json              ← OBBLIGATORIO
├── popup.html                 ← OBBLIGATORIO
├── popup.css                  ← OBBLIGATORIO
├── popup.js                   ← OBBLIGATORIO
├── background.js              ← OBBLIGATORIO
├── player.html                ← OBBLIGATORIO
├── player.js                  ← OBBLIGATORIO
├── delete-prompt.html         ← OBBLIGATORIO
├── delete-prompt.js           ← OBBLIGATORIO
├── icons/
│   ├── icon16.png            ← OBBLIGATORIO
│   ├── icon48.png            ← OBBLIGATORIO
│   └── icon128.png           ← OBBLIGATORIO
├── install-check.sh           (opzionale - per verifica)
├── README.md                  (opzionale - documentazione)
├── EXAMPLES.md                (opzionale - esempi)
└── IMPLEMENTATION.md          (opzionale - dettagli tecnici)
```

**File obbligatori:** 12 file
**File opzionali:** 4 file (documentazione)

## 🚀 Installazione dopo il Download

### Passo 1: Verifica i file (opzionale)
```bash
cd chrome-extension
./install-check.sh
```

### Passo 2: Installa in Chrome

1. Apri Chrome e vai a: `chrome://extensions/`
2. Attiva "**Modalità sviluppatore**" (interruttore in alto a destra)
3. Clicca su "**Carica estensione non pacchettizzata**"
4. Seleziona la cartella `chrome-extension` dove hai scaricato i file
5. L'estensione verrà installata e apparirà nella barra degli strumenti

### Passo 3: Configurazione (prima volta)

1. Clicca sull'icona 🎤 dell'estensione
2. Espandi "⚙️ Impostazioni"
3. Configura:
   - **Qualità Video**: Scegli tra 360p/480p/720p/1080p
   - **Cartella Download**: Es. "Downloads/Karaoke"
4. Clicca "💾 Salva Impostazioni"

## 🎯 Link Rapidi

| Risorsa | URL |
|---------|-----|
| Repository GitHub | https://github.com/fui86/streamlit-claude-chat |
| Branch estensione | https://github.com/fui86/streamlit-claude-chat/tree/copilot/create-karaoke-player-extension |
| Cartella estensione | https://github.com/fui86/streamlit-claude-chat/tree/copilot/create-karaoke-player-extension/chrome-extension |
| README estensione | https://github.com/fui86/streamlit-claude-chat/blob/copilot/create-karaoke-player-extension/chrome-extension/README.md |

## ⚙️ Link Diretti ai File Principali

### File Core (copia questi URL nel browser per il download diretto)

**manifest.json:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/manifest.json
```

**popup.html:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.html
```

**popup.css:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.css
```

**popup.js:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.js
```

**background.js:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/background.js
```

**player.html:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/player.html
```

**player.js:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/player.js
```

**delete-prompt.html:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/delete-prompt.html
```

**delete-prompt.js:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/delete-prompt.js
```

### Icone

**icon16.png:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon16.png
```

**icon48.png:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon48.png
```

**icon128.png:**
```
https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon128.png
```

## 💡 Suggerimenti

### Download Veloce con wget/curl

Se hai `wget` o `curl` installato, puoi scaricare tutti i file con uno script:

```bash
mkdir -p chrome-extension/icons
cd chrome-extension

# Scarica i file principali
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/manifest.json
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.html
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.css
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/popup.js
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/background.js
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/player.html
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/player.js
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/delete-prompt.html
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/delete-prompt.js

# Scarica le icone
cd icons
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon16.png
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon48.png
wget https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension/icons/icon128.png

cd ../..
echo "✅ Download completato!"
```

### Script PowerShell per Windows

```powershell
$baseUrl = "https://raw.githubusercontent.com/fui86/streamlit-claude-chat/copilot/create-karaoke-player-extension/chrome-extension"
New-Item -ItemType Directory -Force -Path "chrome-extension\icons"

$files = @(
    "manifest.json",
    "popup.html",
    "popup.css",
    "popup.js",
    "background.js",
    "player.html",
    "player.js",
    "delete-prompt.html",
    "delete-prompt.js"
)

foreach ($file in $files) {
    Invoke-WebRequest -Uri "$baseUrl/$file" -OutFile "chrome-extension\$file"
}

$icons = @("icon16.png", "icon48.png", "icon128.png")
foreach ($icon in $icons) {
    Invoke-WebRequest -Uri "$baseUrl/icons/$icon" -OutFile "chrome-extension\icons\$icon"
}

Write-Host "✅ Download completato!"
```

## ❓ Problemi?

Se hai problemi con il download:

1. **Verifica di essere sul branch corretto**: `copilot/create-karaoke-player-extension`
2. **Controlla che tutti i 12 file obbligatori siano presenti**
3. **Assicurati che la struttura delle cartelle sia corretta** (icons/ deve essere una sottocartella)
4. **Usa lo script `install-check.sh` per verificare** che tutti i file siano presenti

## 📞 Supporto

Per problemi o domande:
- Apri una issue su GitHub
- Controlla la documentazione in `README.md`
- Verifica gli esempi in `EXAMPLES.md`

---

**Buon karaoke! 🎤🎵**
