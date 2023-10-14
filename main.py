from pypdf import PdfReader, PdfWriter

# open original pdf
with open('Gram_145.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    # create pdf writer for part_1
    part1_pdf_writer = PdfWriter()

    # add firs two pages to part_1
    for page_num in range(2):  # first two pages are at positions 0 and 1
        page = pdf_reader.pages[page_num]
        part1_pdf_writer.add_page(page)

    # create pdf writer for part_1
    part2_pdf_writer = PdfWriter()

    # add rest of pages to part_2
    for page_num in range(2, len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        part2_pdf_writer.add_page(page)

    # save part_1 to file
    with open('part_1.pdf', 'wb') as part1_file:
        part1_pdf_writer.write(part1_file)

    # save part_2 to file
    with open('part_2.pdf', 'wb') as part2_file:
        part2_pdf_writer.write(part2_file)

print("PDF soubory byly rozděleny.")