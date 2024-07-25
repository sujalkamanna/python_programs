import qrcode
from PIL import Image

# Input UPI ID
upi_id = input("Enter your UPI ID: ")

# Test values
name = "Test Name"
amount = "10.00"
currency = "INR"
message = "Payment for test"

# Construct UPI URLs for different payment systems
phone_pe = f"upi://pay?pa={upi_id}&pn={
    name}&am={amount}&cu={currency}&tn={message}"
googlepay = f"upi://pay?pa={upi_id}&pn={
    name}&am={amount}&cu={currency}&tn={message}"
paytm = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}&tn={message}"

# Generate QR codes
phone_pe_qr = qrcode.make(phone_pe)
googlepay_qr = qrcode.make(googlepay)
paytm_qr = qrcode.make(paytm)

# Save QR codes as images
phone_pe_qr.save("phone_pe.png")
googlepay_qr.save("gpay.png")
paytm_qr.save("paytm.png")

# Display QR codes
phone_pe_qr.show()
googlepay_qr.show()
paytm_qr.show()
