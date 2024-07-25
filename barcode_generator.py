from barcode_generator import Code128
from barcode.writer import ImageWriter

def generate_barcode(data):
    # Generate Code128 barcode
    code128 = Code128(data, writer=ImageWriter())

    # Save the barcode image
    filename = code128.save('barcode')

    print(f"Barcode saved as {filename}")

data = "1234-5678-9012"
generate_barcode(data)
