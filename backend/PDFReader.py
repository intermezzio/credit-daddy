import fitz  # PyMuPDF

pdfpath = "C:/Users/USER/Desktop/Project/Project/backend/1.pdf"

def pdf_to_text(filepath: str):

    # Open the PDF file

    print(filepath)

    with fitz.open(filepath) as pdf_document:

        page_content = {}

        # Iterate through each page in the PDF
        for page_number in range(pdf_document.page_count):
            pdf_page = pdf_document.load_page(page_number)
            page_text = pdf_page.get_text()
            # Replace double quotes in the page text
            page_text_sanitized = page_text.replace('"', "")
            page_text_sanitized = page_text_sanitized.replace("\n", "")
            page_content[page_number + 1] = page_text_sanitized


    result_text = ""

    # Print the sanitized page content
    for page_num, content in page_content.items():
        result_text += content

    print(result_text)
    
    return result_text

if __name__ == "__main__":
    text = pdf_to_text(pdf_path)
    print(text)
