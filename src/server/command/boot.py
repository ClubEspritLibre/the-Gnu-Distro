import os,shutil
from utils import usbIsPresent
def bootDistribution(dist):

  if usbIsPresent() == True:
    homedir = os.environ['HOME']
    base=homedir+"/.the-gnu-distro/distribution/"+dist
    result= os.popen("udisks --show-info /dev/disk/by-id/usb*|grep -i 'device-file'").read()
    target=result[result.find("/"):len(result)-1]
    os.popen("dd if="+base+" of="+target+" ibs=4b obs=1b conv=notrunc,noerror").read()
    return True
  else:
    return False
