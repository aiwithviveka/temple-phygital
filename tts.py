from gtts import gTTS

# Your Hindi message
message = "Jai Mata Di. कृपया परिसर को स्वच्छ रखें और प्लास्टिक का उपयोग न करें।"

# Generate TTS in Hindi
tts = gTTS(text=message, lang='hi')  # 'hi' for Hindi

# Save audio file in your Flask static folder
tts.save("static/audio/message.mp3")

print("Audio generated successfully!")

