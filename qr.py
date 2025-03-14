import qrcode

data = input("Enter the file name: ").strip()
file_name = input("Enter the file_name: ").strip()

qr = qrcode.QRCode(box_size= 10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = 'black', back_color = 'white ')

image.save(file_name)
print("Image saved.....")