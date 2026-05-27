import re 
from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document
from rich.console  import Console

def search_files(directory,keyword):
    results=[]
    for file in Path(directory).rglob("*"):
        if file.is_file() and re.search(keyword,file.name,re.IGNORECASE):
            results.append(str(file))
    return results

def search_in_content(directory, keyword):

    results = []

    for file in Path(directory).rglob("*"):

        if file.is_file():

            try:

                text = ""

                # TXT FILES
                if file.suffix.lower() == ".txt":
                    text = file.read_text(errors="ignore")

                # PDF FILES
                elif file.suffix.lower() == ".pdf":

                    reader = PdfReader(file)

                    for page in reader.pages:
                        text += page.extract_text() or ""
                
                 # DOCX FILES
                elif file.suffix.lower() == ".docx":

                    doc = Document(file)

                    for para in doc.paragraphs:
                        text += para.text + "\n"

                # SEARCH KEYWORD
                if re.search(keyword, text, re.IGNORECASE):
                    results.append(str(file))

            except Exception as e:
                print(f"Error reading {file}: {e}")

    return results

