from pypdf import PdfReader, PdfWriter

# Otevření původního PDF souboru
with open('Gram_145.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    # Vytvoření PDF writeru pro part_1
    part1_pdf_writer = PdfWriter()

    # Přidání první a druhé stránky do part_1
    for page_num in range(2):  # První dvě stránky jsou na pozicích 0 a 1
        page = pdf_reader.pages[page_num]
        part1_pdf_writer.add_page(page)

    # Vytvoření PDF writeru pro part_2
    part2_pdf_writer = PdfWriter()

    # Přidání zbylých stránek do part_2
    for page_num in range(2, len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        part2_pdf_writer.add_page(page)

    # Uložení part_1 do souboru
    with open('part_1.pdf', 'wb') as part1_file:
        part1_pdf_writer.write(part1_file)

    # Uložení part_2 do souboru
    with open('part_2.pdf', 'wb') as part2_file:
        part2_pdf_writer.write(part2_file)

print("PDF soubory byly rozděleny.")