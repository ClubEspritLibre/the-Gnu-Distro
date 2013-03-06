import os
import getpass

def copyDistribution(dist):
  result= os.popen("udisks --show-info /dev/disk/by-id/usb*part1|grep -i 'mount paths'").read()
  target=result[result.find("/"):]  
