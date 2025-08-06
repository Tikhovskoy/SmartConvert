from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def ocr_pdf_to_docx(pdf_path: str, docx_path: str):
    base_path = get_base_path()
    poppler_path = os.path.join(base_path, 'poppler')
    tesseract_path = os.path.join(base_path, 'tesseract', 'tesseract.exe')
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    images = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)
    
    doc = Document()
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='rus+eng')
        doc.add_paragraph(text)
        if i < len(images) - 1:
            doc.add_page_break()
    doc.save(docx_path)
