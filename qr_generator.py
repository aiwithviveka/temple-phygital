import qrcode

url = "https://www.matashrichintpurni.com/index.php"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("static/temple_qr.png")

print("QR Code Generated Successfully")
