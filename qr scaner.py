import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr= qrcode.make("https://www.youtube.com/channel/UC1ZQFzviYThWqyXbw4UoFkw")
myqr1= qrcode.make("https://codegnan.com/python-projects/#h-python-projects-for-beginners")
myqr.save("myqr.png")
myqr1.save("myqr1.png")

b= decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))