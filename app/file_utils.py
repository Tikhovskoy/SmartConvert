from PyPDF2 import PdfReader


def is_scanned_pdf(pdf_path: str) -> bool:
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            if page.extract_text():
                return False
        return True
    except Exception:
        return True
