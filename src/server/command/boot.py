import os,shutil

def bootDistribution(dist):
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb")!= -1 ]
  if(len(usb)!=0):
    result= os.popen("udisks --show-info /dev/disk/by-id/usb*|grep -i 'device-file'").read()
    target=result[result.find("/"):len(result)-1]
    return True
  else:
    return False
