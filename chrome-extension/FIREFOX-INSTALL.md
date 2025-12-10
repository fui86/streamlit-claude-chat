# 🦊 Installazione Firefox - Karaoke Video Player

Guida completa per installare e usare l'estensione Karaoke Video Player su Firefox.

## 🔍 Differenze tra Chrome e Firefox

L'estensione è stata adattata per Firefox con le seguenti modifiche:

- **Manifest v2**: Firefox usa ancora Manifest v2 (Chrome usa v3)
- **API Display**: Firefox non ha `chrome.system.display`, quindi la finestra si apre massimizzata invece che su un monitor specifico
- **Browser API**: Usa `browser.*` invece di `chrome.*` quando disponibile
- **Posizionamento manuale**: Su Firefox dovrai spostare manualmente la finestra del player sul secondo monitor

## 📥 Download per Firefox

### Opzione 1: Download ZIP (Consigliato)

1. Scarica il branch completo:
   ```
   https://github.com/fui86/streamlit-claude-chat/archive/refs/heads/copilot/create-karaoke-player-extension.zip
   ```

2. Estrai il file ZIP

3. Naviga nella cartella `chrome-extension`

### Opzione 2: Git Clone

```bash
git clone https://github.com/fui86/streamlit-claude-chat.git
cd streamlit-claude-chat
git checkout copilot/create-karaoke-player-extension
cd chrome-extension
```

## 🔧 Preparazione File per Firefox

Dopo aver scaricato l'estensione, devi preparare i file per Firefox:

### Metodo Automatico (CONSIGLIATO) 🚀

Usa lo script di setup per preparare automaticamente l'estensione:

**Su Windows:**
```batch
cd chrome-extension
setup-firefox.bat
```

**Su Linux/Mac:**
```bash
cd chrome-extension
chmod +x setup-firefox.sh
./setup-firefox.sh
```

Lo script farà automaticamente:
- ✅ Backup dei file Chrome originali
- ✅ Copia dei file Firefox corretti
- ✅ Configurazione pronta per l'installazione

### Metodo Manuale

Se preferisci fare manualmente, nella cartella `chrome-extension`:

**Su Windows (PowerShell):**
```powershell
Copy-Item manifest.json manifest-chrome.json
Copy-Item background.js background-chrome.js
Copy-Item manifest-firefox.json manifest.json -Force
Copy-Item background-firefox.js background.js -Force
```

**Su Linux/Mac:**
```bash
cp manifest.json manifest-chrome.json
cp background.js background-chrome.js
cp manifest-firefox.json manifest.json
cp background-firefox.js background.js
```

**Manualmente (senza comandi):**
1. Copia `manifest.json` e rinominalo in `manifest-chrome.json` (backup)
2. Copia `background.js` e rinominalo in `background-chrome.js` (backup)
3. Copia `manifest-firefox.json` e rinominalo in `manifest.json` (sovrascrivendo)
4. Copia `background-firefox.js` e rinominalo in `background.js` (sovrascrivendo)

## 🚀 Installazione su Firefox

### Metodo 1: Installazione Temporanea (Sviluppatore)

1. Apri Firefox

2. Digita nella barra degli indirizzi:
   ```
   about:debugging
   ```

3. Clicca su "**Questo Firefox**" (This Firefox) nella barra laterale

4. Clicca sul pulsante "**Carica componente aggiuntivo temporaneo...**" (Load Temporary Add-on...)

5. Naviga alla cartella `chrome-extension`

6. Seleziona il file `manifest.json`

7. L'estensione verrà caricata e apparirà nella barra degli strumenti

**⚠️ Nota**: Le estensioni temporanee vengono rimosse quando chiudi Firefox

### Metodo 2: Installazione Permanente (Richiede firma)

Per un'installazione permanente, l'estensione deve essere:
1. Impacchettata come file `.xpi`
2. Firmata da Mozilla (o usare Firefox Developer Edition)

#### Creazione file XPI:

1. Assicurati che i file siano pronti (manifest-firefox.json rinominato)

2. Crea un file ZIP di tutta la cartella chrome-extension

3. Rinomina l'estensione da `.zip` a `.xpi`

**Su Linux/Mac:**
```bash
cd chrome-extension
zip -r ../karaoke-player.xpi *
```

**Su Windows:**
- Seleziona tutti i file nella cartella chrome-extension
- Clic destro → Invia a → Cartella compressa
- Rinomina il file da `.zip` a `.xpi`

#### Installazione XPI:

**Opzione A - Firefox Developer Edition (No firma richiesta):**
1. Scarica Firefox Developer Edition: https://www.mozilla.org/it/firefox/developer/
2. Apri `about:config`
3. Cerca `xpinstall.signatures.required`
4. Imposta su `false`
5. Trascina il file `.xpi` nella finestra di Firefox

**Opzione B - Firefox normale (Firma richiesta):**
1. Vai su: https://addons.mozilla.org/developers/
2. Crea un account Mozilla
3. Carica e firma l'estensione
4. Installa dal file firmato

**Opzione C - Usa installazione temporanea (più semplice per uso personale)**

## 📱 Uso dell'Estensione su Firefox

### 1. Apertura

- Clicca sull'icona 🎤 nella barra degli strumenti
- Oppure usa il menu Estensioni

### 2. Configurazione (Prima volta)

1. Espandi "⚙️ Impostazioni"
2. Seleziona qualità video (360p/480p/720p/1080p)
3. Imposta cartella download (es: "Downloads/Karaoke")
4. Clicca "💾 Salva Impostazioni"

### 3. Aggiunta Video

1. Copia un link YouTube
2. Incollalo nel campo
3. Clicca "➕ Aggiungi Video"

### 4. Riproduzione

1. Clicca "▶️ Riproduci Tutti"
2. La finestra del player si aprirà massimizzata
3. **⚠️ Su Firefox**: Sposta manualmente la finestra sul secondo monitor se necessario
4. Usa F11 per schermo intero

### 5. Gestione Multi-Monitor su Firefox

Poiché Firefox non ha l'API per rilevare automaticamente i monitor:

1. Quando si apre il player, la finestra sarà massimizzata sul monitor principale
2. Trascina manualmente la finestra sul secondo monitor
3. Premi F11 per attivare la modalità schermo intero
4. Oppure usa le opzioni della finestra per "Sposta su schermo 2"

## 🔄 Differenze Funzionali Firefox vs Chrome

| Funzionalità | Chrome | Firefox |
|--------------|---------|---------|
| Manifest Version | V3 | V2 |
| Multi-monitor automatico | ✅ Sì | ❌ No (manuale) |
| Qualità video | ✅ Sì | ✅ Sì |
| Cartella download | ✅ Sì | ✅ Sì |
| Playlist | ✅ Sì | ✅ Sì |
| Schermo intero | ✅ Auto | 🔄 Manuale (F11) |
| Eliminazione file | ✅ Sì | ✅ Sì |

## 🐛 Risoluzione Problemi Firefox

### ❌ Errore: "background.service_worker is currently disabled"

**Problema**: Questo errore appare quando Firefox sta cercando di caricare il manifest di Chrome invece di quello di Firefox.

**Causa**: Non hai sostituito correttamente i file. Firefox sta leggendo `manifest.json` che contiene la configurazione Chrome (Manifest V3 con service_worker).

**Soluzione**:
1. **Esegui lo script di setup**:
   - Windows: `setup-firefox.bat`
   - Linux/Mac: `./setup-firefox.sh`
2. **Oppure verifica manualmente**:
   - Apri `manifest.json` con un editor di testo
   - Controlla che contenga `"manifest_version": 2` (NON 3)
   - Controlla che la sezione background sia:
     ```json
     "background": {
       "scripts": ["background-firefox.js"],
       "persistent": false
     }
     ```
   - Se vedi `"service_worker"` nel manifest, NON è quello corretto per Firefox!
3. **Se necessario, ricopia i file**:
   ```bash
   cp manifest-firefox.json manifest.json
   cp background-firefox.js background.js
   ```
4. **Ricarica l'estensione** in `about:debugging`

### L'estensione non si carica

**Problema**: Errore generico durante il caricamento

**Soluzione**:
1. Verifica di aver copiato (NON rinominato) `manifest-firefox.json` in `manifest.json`
2. Verifica di aver copiato `background-firefox.js` in `background.js`
3. Controlla la console errori in `about:debugging`
4. Assicurati che tutti i file siano presenti (icone, popup.html, ecc.)

### La finestra non si apre sul secondo monitor

**Problema**: Il player si apre sempre sul monitor principale

**Soluzione**:
- Su Firefox questo è normale (manca l'API system.display)
- Soluzione: Sposta manualmente la finestra
- Usa Windows + Shift + Freccia per spostare tra monitor (Windows)
- Usa Ctrl + Alt + Freccia su alcuni sistemi Linux

### I video non vanno a schermo intero automaticamente

**Problema**: La finestra è massimizzata ma non a schermo intero

**Soluzione**:
- Premi F11 nella finestra del player
- Oppure clicca sul pulsante schermo intero nel player YouTube

### L'estensione scompare dopo il riavvio

**Problema**: Le estensioni temporanee vengono rimosse

**Soluzione**:
- Usa Firefox Developer Edition e installa da file XPI
- Oppure ricarica l'estensione temporanea ogni volta
- Oppure firma l'estensione su addons.mozilla.org

## 📋 Checklist Installazione Firefox

- [ ] Download estensione da GitHub
- [ ] **Esegui `setup-firefox.bat` (Windows) o `setup-firefox.sh` (Linux/Mac)**
- [ ] Oppure copia manualmente i file Firefox
- [ ] Verifica che `manifest.json` contenga `"manifest_version": 2`
- [ ] Apri `about:debugging` su Firefox
- [ ] Clicca "Questo Firefox"
- [ ] Carica estensione temporanea
- [ ] Seleziona `manifest.json`
- [ ] Verifica che l'estensione sia caricata senza errori
- [ ] Configura impostazioni (qualità, percorso)
- [ ] Testa con un video
- [ ] Sposta manualmente su secondo monitor
- [ ] Premi F11 per schermo intero

## 🔗 Link Utili

- **Firefox Add-ons**: https://addons.mozilla.org/developers/
- **Firefox Developer Edition**: https://www.mozilla.org/firefox/developer/
- **Documentazione WebExtensions**: https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions
- **about:debugging**: Pagina debug estensioni Firefox

## 💡 Suggerimenti

1. **Firefox Developer Edition**: Se usi spesso estensioni non firmate, usa Firefox Developer Edition
2. **Shortcut Spostamento**: Impara le scorciatoie del tuo OS per spostare finestre tra monitor
3. **Profilo Separato**: Crea un profilo Firefox dedicato per uso karaoke
4. **Auto-firma**: Considera di creare un certificato di auto-firma per uso locale

## 🆚 Chrome vs Firefox: Quale Usare?

**Usa Chrome se:**
- ✅ Vuoi rilevamento automatico multi-monitor
- ✅ Vuoi schermo intero automatico
- ✅ Preferisci meno configurazione manuale

**Usa Firefox se:**
- ✅ Preferisci Firefox come browser
- ✅ Non ti dispiace spostare manualmente la finestra
- ✅ Vuoi più controllo sulla privacy
- ✅ Hai Firefox Developer Edition

## 📞 Supporto

Per problemi specifici di Firefox:
- Controlla i log in `about:debugging`
- Verifica la console del browser (F12)
- Assicurati di usare Firefox 91 o superiore

---

**Buon karaoke su Firefox! 🦊🎤🎵**
