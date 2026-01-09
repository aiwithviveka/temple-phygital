# Temple Phygital Page

A simple Flask-based web page for temples that integrates **QR codes** and **audio messages** to guide visitors. This project is designed for temples like **Chintpurni Mata**, allowing visitors to scan QR codes for more information and listen to important audio messages in Hindi.

---

## Features Project Structure

- **QR Code Integration:** Visitors can scan the QR code to visit the temple’s official website.
- **Audio Message:** Plays a Hindi message guiding visitors to keep the premises clean.
- **Responsive Layout:** Works on desktops, tablets, and mobile devices.
- **Easy Customization:** Update QR image or audio file as needed.
- **Simple Flask Setup:** Easy to deploy locally or on a web server.

---

## Project Structure


<img width="457" height="301" alt="image" src="https://github.com/user-attachments/assets/84d66b36-608f-4341-a473-a74a5d3a0e81" />


---

## Setup Instructions Customization

1. Clone the repository
git clone https://github.com/aiwithviveka/temple-phygital.git
cd temple-phygital

2. Install dependencies
pip install flask gTTS

3. Run the Flask app
flask run --host=0.0.0.0 --port=5000

4. Open in browser
http://127.0.0.1:5000/


Note:
For phone scanning, make sure your phone is connected to the same Wi-Fi network as your computer, or deploy the app to a public server.

## Customization License

Change Audio Message
Replace the file:

static/audio/radhasoami_message.mp3


Update QR Code
Replace the QR image:

static/temple_qr.png


Modify Text or Design
Edit the HTML file:

templates/index.html

## License

This project is open source and free to use for educational and devotional purposes.

👤 Author

Viveka Sharma



