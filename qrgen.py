import qrcode
'''qr = qrcode.make("9182002801")
qr.save("phnumqr.png")
qr.show()'''



# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box/pixel
    border=4,  # Border size (number of boxes around the QR code)
)

# Get user input: text or URL
user_input = input("Enter the text or URL to generate a QR code: ")


qr.add_data(user_input)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save( "qrcode.png")
img.show()
