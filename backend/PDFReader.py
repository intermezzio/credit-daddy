import fitz  # PyMuPDF

def read_pdf_content(pdf_path):
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    page_content = {}
    
    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        pdf_page = pdf_document.load_page(page_number)
        page_text = pdf_page.get_text()
        # Replace double quotes in the page text
        page_text_sanitized = page_text.replace('"', "")
        page_text_sanitized = page_text_sanitized.replace("\n", "")
        page_content[page_number + 1] = page_text_sanitized
    
    # Close the PDF document
    pdf_document.close()
    
    result_text = ""
    
    # Concatenate the sanitized page content
    for page_num, content in page_content.items():
        result_text += content
        
    return result_text