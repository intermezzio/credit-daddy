import pdfplumber

def pdf_to_text(pdf_file: str) -> str:
    """Extract text and statement dates from the PDF"""

    with pdfplumber.open(pdf_file) as pdf:
        all_text = "\n".join(
            page.extract_text(x_tolerance=1)
            for page in pdf.pages
        )
    
    return all_text