"""import qrcode

url="https://www.tops-int.com/"

qr=qrcode.make(url)
qr.save("tops.png")"""


import pyqrcode

url="https://www.tops-int.com/"

qr=pyqrcode.create(url)
qr.png("newtops.png")