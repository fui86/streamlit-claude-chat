@echo off
REM Setup script to prepare extension for Firefox installation

echo 🦊 Preparazione estensione per Firefox
echo ========================================
echo.

REM Check if we're in the chrome-extension directory
if not exist "manifest.json" (
    echo ❌ Errore: Devi eseguire questo script dalla cartella chrome-extension
    exit /b 1
)

echo 📋 Backup dei file Chrome originali...
REM Backup Chrome files if not already done
if not exist "manifest-chrome-backup.json" (
    copy manifest.json manifest-chrome-backup.json >nul
    echo ✅ Backup manifest.json -^> manifest-chrome-backup.json
)

if not exist "background-chrome-backup.js" (
    copy background.js background-chrome-backup.js >nul
    echo ✅ Backup background.js -^> background-chrome-backup.js
)

echo.
echo 🔄 Applicazione configurazione Firefox...

REM Replace files with Firefox versions
copy /Y manifest-firefox.json manifest.json >nul
echo ✅ Copiato manifest-firefox.json -^> manifest.json

copy /Y background-firefox.js background.js >nul
echo ✅ Copiato background-firefox.js -^> background.js

echo.
echo ✅ Preparazione completata!
echo.
echo 📖 Prossimi passi per installare in Firefox:
echo 1. Apri Firefox
echo 2. Vai a: about:debugging
echo 3. Clicca 'Questo Firefox'
echo 4. Clicca 'Carica componente aggiuntivo temporaneo...'
echo 5. Seleziona il file manifest.json in questa cartella
echo.
echo 💡 Per ripristinare i file Chrome:
echo    copy manifest-chrome-backup.json manifest.json
echo    copy background-chrome-backup.js background.js
echo.
pause
