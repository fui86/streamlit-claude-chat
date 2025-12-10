#!/bin/bash
# Setup script to prepare extension for Firefox installation

echo "🦊 Preparazione estensione per Firefox"
echo "========================================"
echo ""

# Check if we're in the chrome-extension directory
if [ ! -f "manifest.json" ]; then
    echo "❌ Errore: Devi eseguire questo script dalla cartella chrome-extension"
    exit 1
fi

echo "📋 Backup dei file Chrome originali..."
# Backup Chrome files if not already done
if [ ! -f "manifest-chrome-backup.json" ]; then
    cp manifest.json manifest-chrome-backup.json
    echo "✅ Backup manifest.json → manifest-chrome-backup.json"
fi

if [ ! -f "background-chrome-backup.js" ]; then
    cp background.js background-chrome-backup.js
    echo "✅ Backup background.js → background-chrome-backup.js"
fi

echo ""
echo "🔄 Applicazione configurazione Firefox..."

# Replace files with Firefox versions
cp manifest-firefox.json manifest.json
echo "✅ Copiato manifest-firefox.json → manifest.json"

cp background-firefox.js background.js
echo "✅ Copiato background-firefox.js → background.js"

echo ""
echo "✅ Preparazione completata!"
echo ""
echo "📖 Prossimi passi per installare in Firefox:"
echo "1. Apri Firefox"
echo "2. Vai a: about:debugging"
echo "3. Clicca 'Questo Firefox'"
echo "4. Clicca 'Carica componente aggiuntivo temporaneo...'"
echo "5. Seleziona il file manifest.json in questa cartella"
echo ""
echo "💡 Per ripristinare i file Chrome:"
echo "   cp manifest-chrome-backup.json manifest.json"
echo "   cp background-chrome-backup.js background.js"
echo ""
