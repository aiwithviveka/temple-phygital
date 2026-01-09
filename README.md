# Temple Phygital Page

A simple Flask-based web page for temples that integrates **QR codes** and **audio messages** to guide visitors. This project is designed for temples like **Chintpurni Mata**, allowing visitors to scan QR codes for more information and listen to important audio messages in Hindi.

---

## Features

- **QR Code Integration:** Visitors can scan the QR code to visit the temple’s official website.
- **Audio Message:** Plays a Hindi message guiding visitors to keep the premises clean.
- **Responsive Layout:** Works on desktops, tablets, and mobile devices.
- **Easy Customization:** Update QR image or audio file as needed.
- **Simple Flask Setup:** Easy to deploy locally or on a web server.

---

## Project Structure

temple-phygital/
│
├── static/
│ ├── audio/
│ │ └── radhasoami_message.mp3
│ └── temple_qr.png
│
├── templates/
│ └── index.html
│
├── app.py
└── README.md


---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/aiwithviveka/temple-phygital.git
cd temple-phygital

2. **Install dependencies:**

pip install flask gTTS


3. **Run the Flask app:**

flask run --host=0.0.0.0 --port=5000


4. **Open in browser:**

http://127.0.0.1:5000/


Note: For phone scanning, make sure your phone is on the same Wi-Fi as your computer, or deploy to a public server.

**Customization**

Replace static/audio/radhasoami_message.mp3 with your own audio message.

Replace static/temple_qr.png with a new QR code image.

Update templates/index.html to change headings, text, or styling.

**License**

This project is open source and free to use for educational and devotional purposes.

**Author**

Viveka Sharma



