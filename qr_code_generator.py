"""
qrcode==7.3.1
"""
import qrcode


img = qrcode.make('https://www.google.com.br/')
img.save("terapia-qr-code.png")
