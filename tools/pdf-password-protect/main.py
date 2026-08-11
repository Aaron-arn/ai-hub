import argparse
from pypdf import PdfReader, PdfWriter

def protect(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password, algorithm="AES-256")
    with open(output_pdf, "wb") as fh:
        writer.write(fh)
    print(f"Encrypted: {output_pdf}")

def unlock(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    if reader.is_encrypted:
        reader.decrypt(password)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_pdf, "wb") as fh:
        writer.write(fh)
    print(f"Decrypted: {output_pdf}")

def main():
    ap = argparse.ArgumentParser(description="Encrypt or decrypt a PDF")
    ap.add_argument("action", choices=["encrypt", "decrypt"])
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("password")
    args = ap.parse_args()
    if args.action == "encrypt":
        protect(args.input, args.output, args.password)
    else:
        unlock(args.input, args.output, args.password)

if __name__ == "__main__":
    main()
