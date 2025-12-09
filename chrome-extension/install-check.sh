#!/bin/bash
# Installation verification script for Karaoke Video Player Chrome Extension

echo "🎤 Karaoke Video Player - Chrome Extension Installer"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -f "manifest.json" ]; then
    echo "❌ Error: manifest.json not found"
    echo "Please run this script from the chrome-extension directory"
    exit 1
fi

echo "✅ Extension directory found"

# Validate manifest.json
if python3 -m json.tool manifest.json > /dev/null 2>&1; then
    echo "✅ manifest.json is valid"
else
    echo "❌ manifest.json has JSON errors"
    exit 1
fi

# Check required files
required_files=(
    "popup.html"
    "popup.js"
    "popup.css"
    "background.js"
    "player.html"
    "player.js"
    "delete-prompt.html"
    "delete-prompt.js"
    "icons/icon16.png"
    "icons/icon48.png"
    "icons/icon128.png"
)

missing_files=0
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ Missing: $file"
        missing_files=$((missing_files + 1))
    fi
done

echo ""
if [ $missing_files -eq 0 ]; then
    echo "✅ All required files present"
    echo ""
    echo "📋 Installation Instructions:"
    echo "1. Open Chrome and navigate to: chrome://extensions/"
    echo "2. Enable 'Developer mode' (toggle in top right)"
    echo "3. Click 'Load unpacked'"
    echo "4. Select this directory: $(pwd)"
    echo ""
    echo "🎉 Ready to install!"
else
    echo "❌ $missing_files file(s) missing"
    echo "Please ensure all files are present before installation"
    exit 1
fi
