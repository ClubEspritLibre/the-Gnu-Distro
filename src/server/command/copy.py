import os
import getpass

def copyDistribution(dist):
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb")!= -1 ]
  if(len(usb)!=0):
    result= os.popen("udisks --show-info /dev/disk/by-id/usb*part1|grep -i 'mount paths'").read()
    target=result[result.find("/"):]
    return True
  else:
    return False
