import fitz  # PyMuPDF

pdf_path = "../data/Apple-Card-Customer-Agreement.pdf"

def pdf_to_text(filename: str):

    # Open the PDF file
    with fitz.open(pdf_path) as pdf_document:

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
    
    return result_text

if __name__ == "__main__":
    text = pdf_to_text(pdf_path)
    print(text)
