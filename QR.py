import qrcode # Import the qrcode library to generate QR codes

data = input("Enter text or URL: ")

img = qrcode.make(data) # Generate the QR code image based on the input data

img.save("qrcode.png") # Save the QR code image as qrcode.png

img.show()  # Display the QR code image

print("QR Code saved as qrcode.png")