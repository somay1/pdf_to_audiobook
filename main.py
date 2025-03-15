import pdfplumber
import os
from gtts import gTTS

desktop_path=os.path.join(os.path.expanduser("~"),'Desktop','audio.mp3')
def extract_text(pdf_path):
    """Extract text from a PDF file."""
    text = ""

    if not os.path.exists(pdf_path):
        return "⚠️ Error: PDF file not found."

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Avoid adding 'None' values
                text += page_text + '\n'

    return text.strip() if text else "⚠️ Error: No readable text found in the PDF."


def text_to_speech(output, audio_path=desktop_path, lang='en'):
    """Convert text to speech and save as MP3."""

    tts = gTTS(output, lang=lang)
    tts.save(audio_path)
    print(f"✅ Audio saved: {audio_path}")


# --- Main Execution ---
pdf_path = "C:\\Users\\Hp-pc\\Documents\\Fightclub.pdf"

output = extract_text(pdf_path)

if "⚠️ Error" not in output:
    text_to_speech(output)
    print("🎧 Audio ready!")
else:
    print(output)  # Print error message if PDF is empty or missing
