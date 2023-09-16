import fitz  # PyMuPDF
import re

pdf_path = "Capital.pdf"

# Open the PDF file
pdf_document = fitz.open(pdf_path)

page_content = {}

# Iterate through each page in the PDF
for page_number in range(pdf_document.page_count):
    pdf_page = pdf_document.load_page(page_number)
    page_text = pdf_page.get_text()
    # Replace double quotes in the page text
    page_text_sanitized = page_text.replace('"', "")
    page_text_sanitized = page_text_sanitized.replace("\n", " ")
    page_content[page_number + 1] = page_text_sanitized

# Close the PDF document
pdf_document.close()

result_text = ""

# Print the sanitized page content
for page_num, content in page_content.items():
    result_text += content



#--------------------------------------------------------------------------------------

def extract_context(page_text_sanitized, target_word):
    # Split the text into words
    words = re.findall(r'\w+', page_text_sanitized)
    
    # Find the index of the target word
    try:
        target_index = words.index(target_word)
    except ValueError:
        return "Target word not found in the text."

    # Get the previous 10 words
    prev_words = words[max(0, target_index - 10):target_index]

    # Get the next 10 words
    next_words = words[target_index + 1:target_index + 11]

    return {
        'previous_words': ' '.join(prev_words),
        'next_words': ' '.join(next_words)
    }


# Target word
target_word = "annual fee"

# Extract context
context = extract_context(result_text, target_word)

# Print the context
print(context)


# print(result_text)