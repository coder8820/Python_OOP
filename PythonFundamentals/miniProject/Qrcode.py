import qrcode

# Input your URL or text
data = input("https://github.com/coder8820?tab=overview&from=2025-06-01&to=2025-06-04")

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
