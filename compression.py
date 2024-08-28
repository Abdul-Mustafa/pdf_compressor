from PyPDF2 import PdfReader, PdfWriter

def compress_pdf(input_file, output_file, compression_level):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    if compression_level == 'normal':
        compression_factor = 0.8  # Example: Reduce size by 20%
    elif compression_level == 'standard':
        compression_factor = 0.7  # Example: Reduce size by 30%
    elif compression_level == 'advanced':
        compression_factor = 0.5  # Example: Reduce size by 50%
    else:
        compression_factor = 1.0

    # Here we assume that we have a function to compress pages, 
    # but you need to implement it based on your exact requirements
    for i in range(len(pdf_writer.pages)):
        page = pdf_writer.pages[i]
        # Example: page.compress(compression_factor)
        # You would need to use an actual compression method or library

    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
