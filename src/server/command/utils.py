import os

def usbIsPresent():
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb") != -1]
  if len(usb) != 0:
    return True
  else:
    return False