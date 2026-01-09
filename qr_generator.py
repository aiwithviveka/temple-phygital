import qrcode

# URL to encode
url = "https://www.matashrichintpurni.com/"

# Create QR code
qr = qrcode.QRCode(
    version=1,  # size of the QR
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box
    border=4,  # white border
)

qr.add_data(url)
qr.make(fit=True)

# Generate a high-quality image
img = qr.make_image(fill_color="black", back_color="white")
img.save("temple_qr.png")  # save in /static folder
