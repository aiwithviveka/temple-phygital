from gtts import gTTS
import os

os.makedirs("static/audio", exist_ok=True)

# Hindi history
hi_text = "जय माता दी। श्री चिंतपूर्णी माता मंदिर हिमाचल प्रदेश का प्रसिद्ध शक्तिपीठ है। कृपया परिसर को स्वच्छ रखें।"
hi_tts = gTTS(text=hi_text, lang="hi")
hi_tts.save("static/audio/history_hi.mp3")

# English history
en_text = "Jai Mata Di. Chintpurni Temple is a famous Shakti Peeth in Himachal Pradesh. Please keep the premises clean."
en_tts = gTTS(text=en_text, lang="en")
en_tts.save("static/audio/history_en.mp3")

print("✅ Hindi & English audio generated")
