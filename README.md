# 🎬 AK Tool — YouTube Downloader

> Download YouTube videos in 1080p, 720p, 480p, 360p and MP3 audio

---

## 📁 Files Ki List

```
AK-Tool/
├── app.py                      ← Backend server (Python)
├── AK-YouTube-Downloader.html  ← Website (frontend)
├── requirements.txt            ← Python packages
├── START-BACKEND.bat           ← Windows ke liye (double-click)
├── start-backend.sh            ← Mac/Linux ke liye
└── README.md                   ← Yeh file
```

---

## 🚀 Kaise Chalayein (Step by Step)

### ✅ Step 1 — Python Install Karo (Pehli baar sirf)

Python download karo: https://www.python.org/downloads/

> ⚠️ Install karte waqt "Add Python to PATH" ka checkmark ZAROOR lagao!

---

### ✅ Step 2 — Backend Start Karo

#### 🪟 Windows Users:
  START-BACKEND.bat  double-click karo
  Bas itna hi! Sab automatically install aur start ho jayega.

#### 🍎 Mac / 🐧 Linux Users:
  Terminal mein yeh likho:
  chmod +x start-backend.sh
  ./start-backend.sh

#### 💻 Manual (Kisi bhi OS):
  pip install -r requirements.txt
  python app.py

---

### ✅ Step 3 — Website Open Karo

AK-YouTube-Downloader.html double-click karke browser mein kholein.
Header mein [Server Online] green dikhega jab sab sahi ho.

---

### ✅ Step 4 — Use Karo!

1. YouTube video ka link paste karo
2. GET button dabao
3. Quality choose karo (1080p / 720p / MP3 etc.)
4. Download shuru!

---

## ⚠️ Zaroori Baat

- Backend (app.py) HAMESHA chal raha hona chahiye jab website use karo
- Browser aur Backend dono ek saath kholne hain
- Agar "Server Offline" dikhe → pehle backend start karo

---

## ❓ Problem Aa Rahi Hai?

Problem                  | Solution
-------------------------|------------------------------------------
"Python nahi mila"       | python.org se install karo, PATH add karo
"Server Offline"         | START-BACKEND.bat dobara chalao
Video nahi aayi          | pip install -U yt-dlp
Private video error      | Wo video download nahi hogi

---

Made with AK Tool
