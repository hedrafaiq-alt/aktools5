#!/bin/bash

echo ""
echo " =========================================="
echo "   AK TOOL - YouTube Downloader Backend"
echo " =========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo " [ERROR] Python3 install nahi hai!"
    echo " Mac: brew install python3"
    echo " Linux: sudo apt install python3 python3-pip"
    exit 1
fi

echo " [OK] Python mila!"
echo ""

# Install dependencies
echo " Dependencies install ho rahi hain..."
pip3 install -r requirements.txt --quiet
echo " [OK] Dependencies ready!"
echo ""

# Run server
echo " Backend start ho raha hai..."
echo " Browser mein AK-YouTube-Downloader.html open karo"
echo ""
echo " =========================================="
echo "  Server: http://localhost:5000"
echo "  Band karne ke liye: Ctrl+C"
echo " =========================================="
echo ""

python3 app.py
