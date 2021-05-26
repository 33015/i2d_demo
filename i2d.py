from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import tesseract
from os import listdir

def i2s(filename):
    templates = read_templates('templates/')
    result = extract_data(filename, templates=templates)
    # if extract_data cant extract from the invoice, result is false and tries it again with OCR
    if not result:
        result = extract_data(filename, templates=templates, input_module=tesseract)
    if result:
        print_data(result)

def print_data(result):
    print(result)
    for r in result:
        if r != "lines":
            print(f"{r}: {result[r]}")
        else:
            for lines in result[r]:
                for l in lines:
                    print(f"{r} - {l}: {lines[l]}")




if __name__ == "__main__":
    files = listdir(".")
    for f in files:
        if ".pdf" in f:
            print(f"\nFilename: {f}")
            i2s(f)
