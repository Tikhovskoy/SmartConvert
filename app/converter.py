import os
from datetime import datetime
from app.file_utils import is_scanned_pdf
from app.ocr_utils import ocr_pdf_to_docx
from pdf2docx import Converter


def convert_pdf(pdf_path: str) -> str:
    file_dir = os.path.dirname(pdf_path)
    filename_wo_ext = os.path.splitext(os.path.basename(pdf_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(file_dir, f"{filename_wo_ext}_converted_{timestamp}.docx")

    if is_scanned_pdf(pdf_path):
        print("PDF определён как скан. Используется OCR.")
        ocr_pdf_to_docx(pdf_path, output_path)
    else:
        print("PDF содержит текст. Используется прямое преобразование.")
        cv = Converter(pdf_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()

    return output_path
