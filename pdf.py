import PyPDF2
import sys

inputs = sys.argv[1:]

# pdf merger function


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    # looping through all the pdfs that need to be combined
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('final.pdf')


pdf_merger(inputs)
