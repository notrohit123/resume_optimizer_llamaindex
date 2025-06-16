from PyPDF2 import PdfReader
from docx import Document
import os

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() or "" for page in reader.pages])

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text_from_txt(file):
    return file.read().decode("utf-8")

def parse_resume(file):
    ext = os.path.splitext(file.name)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file)
    elif ext == ".docx":
        return extract_text_from_docx(file)
    elif ext == ".txt":
        return extract_text_from_txt(file)
    else:
        raise ValueError("Unsupported file type")
