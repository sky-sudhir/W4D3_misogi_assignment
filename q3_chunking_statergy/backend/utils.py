
from PyPDF2 import PdfReader
from io import BytesIO

def extract_text_from_pdf(file) -> str:
    pdf_stream = BytesIO(file)
    reader = PdfReader(pdf_stream)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
