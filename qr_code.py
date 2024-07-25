import qrcode

data = input("Enter hyperlink or Any data to display:")

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

save_img = input("Please enter file name you want to save:")
img.save(f"{save_img}.png")
