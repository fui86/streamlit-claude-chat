# 🔍 Verifica Installazione Firefox

Usa questa guida per verificare che l'estensione sia configurata correttamente per Firefox.

## ✅ Checklist Rapida

### 1. Verifica File Manifest

Apri il file `manifest.json` con un editor di testo e controlla:

**✅ CORRETTO per Firefox:**
```json
{
  "manifest_version": 2,
  "name": "Karaoke Video Player",
  ...
  "background": {
    "scripts": ["background-firefox.js"],
    "persistent": false
  }
}
```

**❌ SBAGLIATO (questo è Chrome):**
```json
{
  "manifest_version": 3,
  ...
  "background": {
    "service_worker": "background.js"
  }
}
```

### 2. Verifica File Background

Controlla che esista il file `background.js` e che contenga:

```javascript
// All'inizio del file dovrebbe esserci:
// Background script for Firefox extension
// Firefox doesn't have chrome.system.display API...

const browserAPI = typeof browser !== 'undefined' ? browser : chrome;
```

Se il file inizia con `// Background service worker for Chrome extension`, hai il file sbagliato!

### 3. Verifica Struttura File

Nella cartella `chrome-extension` devono esserci:

```
✅ manifest.json (Manifest V2 - Firefox)
✅ manifest-firefox.json (copia originale)
✅ manifest-chrome.json o manifest-chrome-backup.json (backup Chrome)
✅ background.js (Firefox version)
✅ background-firefox.js (copia originale)
✅ background-chrome.js o background-chrome-backup.js (backup Chrome)
✅ popup.html, popup.css, popup.js
✅ player.html, player.js
✅ delete-prompt.html, delete-prompt.js
✅ icons/ (cartella con icon16.png, icon48.png, icon128.png)
```

## 🛠️ Come Correggere

Se hai il manifest sbagliato:

### Opzione 1: Usa lo Script (PIÙ FACILE)

**Windows:**
```batch
setup-firefox.bat
```

**Linux/Mac:**
```bash
./setup-firefox.sh
```

### Opzione 2: Copia Manuale

```bash
# Backup Chrome (se non fatto)
cp manifest.json manifest-chrome-backup.json
cp background.js background-chrome-backup.js

# Installa Firefox
cp manifest-firefox.json manifest.json
cp background-firefox.js background.js
```

### Opzione 3: PowerShell (Windows)

```powershell
# Backup Chrome
Copy-Item manifest.json manifest-chrome-backup.json
Copy-Item background.js background-chrome-backup.js

# Installa Firefox
Copy-Item manifest-firefox.json manifest.json -Force
Copy-Item background-firefox.js background.js -Force
```

## 🔄 Per Tornare a Chrome

Se vuoi tornare alla versione Chrome:

```bash
cp manifest-chrome-backup.json manifest.json
cp background-chrome-backup.js background.js
```

## 🧪 Test di Verifica

1. **Apri Firefox**
2. **Vai a**: `about:debugging`
3. **Clicca**: "Questo Firefox"
4. **Clicca**: "Carica componente aggiuntivo temporaneo..."
5. **Seleziona**: `manifest.json` nella cartella chrome-extension

### Risultato Atteso:

**✅ Successo:**
- L'estensione appare nella lista
- Vedi "Karaoke Video Player" installato
- Nessun errore rosso

**❌ Errore:**
- `background.service_worker is currently disabled`
  → **Hai il manifest Chrome! Devi usare manifest-firefox.json**
- `Error processing background.scripts`
  → **Verifica che background-firefox.js esista**

## 📞 Ancora Problemi?

Se continui ad avere problemi:

1. **Cancella tutto e ricomincia**:
   - Riscarica l'estensione
   - Estrai in una nuova cartella
   - Esegui lo script setup-firefox

2. **Verifica la versione Firefox**:
   - Deve essere Firefox 91 o superiore
   - Controlla: Menu → Aiuto → Informazioni su Firefox

3. **Controlla i permessi file**:
   - Tutti i file devono essere leggibili
   - Gli script .sh devono essere eseguibili (Linux/Mac)

## 📋 Comando Diagnosi Rapida

**Linux/Mac:**
```bash
cd chrome-extension
echo "=== Verifica Manifest ==="
head -5 manifest.json
echo ""
echo "=== Verifica Background ==="
head -3 background.js
```

**Output atteso:**
```
=== Verifica Manifest ===
{
  "manifest_version": 2,
  "name": "Karaoke Video Player",
  ...

=== Verifica Background ===
// Background script for Firefox extension
// Firefox doesn't have chrome.system.display API...
```

Se vedi `manifest_version": 3` o `service_worker`, hai ancora i file Chrome!

---

**🦊 Buona installazione su Firefox!**
