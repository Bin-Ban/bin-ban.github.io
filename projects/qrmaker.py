import os
try:
  import qrcode.main
  from qrcode.main import make
except:
  os.system("pip install qrcode")
  import qrcode.main
  from qrcode.main import make

qrcode.main.make(input("Text: ").replace("\n", "")).show()
