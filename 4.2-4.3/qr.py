import pyqrcode
import random

def data_to_qrcode(data, name, scale = 8):
    qr = pyqrcode.create(data)
    qr.png(name, scale = scale)

def data_to_qrcode_with_random_color(data, name, scale = 8):
    c1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    c2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    qr = pyqrcode.create(data)
    qr.png(name, scale = scale, module_color = c1, background = c2)


if __name__ == '__main__':
    text = 'AnotherStudent'
    data_to_qrcode(text, '1.png')
    data_to_qrcode_with_random_color(text, '2.png')