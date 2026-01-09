import os
from pypdf import PdfReader
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a single PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text, or None if an error occurs.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        logging.error(f"Error reading PDF file {pdf_path}: {e}")
        return None

def main():
    """
    Main function to extract text from all PDFs in the data/raw_pdfs directory.
    """
    # Note: This script is intended to be run from the root of the project.
    # We will need to adjust the paths if we run it from a different location.
    pdf_dir = "data/raw_pdfs"
    output_dir = "data/extracted_text"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            logging.info(f"Extracting text from {pdf_path}...")
            text = extract_text_from_pdf(pdf_path)
            if text:
                output_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(output_dir, output_filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                logging.info(f"Saved extracted text to {output_path}")

if __name__ == "__main__":
    main()
