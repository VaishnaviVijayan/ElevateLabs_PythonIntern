import fitz  # PyMuPDF
import pyttsx3
import os

def pdf_to_audio(pdf_path, output_audio):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Open the PDF
    doc = fitz.open(pdf_path)
    full_text = ""

    # Extract text from each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text().strip()
        if text:
            full_text += text + " "

    doc.close()

    if not full_text:
        print("No readable text found in the PDF.")
        return

    # Save extracted text as audio
    engine.save_to_file(full_text, output_audio)
    engine.runAndWait()

    print("Audiobook created successfully!")

# -------- MAIN --------
if __name__ == "__main__":
    pdf_file = "sample.pdf"
    output_file = "output_audio.mp3"

    if os.path.exists(pdf_file):
        pdf_to_audio(pdf_file, output_file)
    else:
        print("PDF file not found. Please check the file name.")
