import os,shutil, subprocess
from utils import usbIsPresent
def bootDistribution(dist):

  if usbIsPresent() == True:
    homedir = os.environ['HOME']
    base = homedir+"/.the-gnu-distro/distribution/"+dist
    result = subprocess.Popen("udisks --show-info /dev/disk/by-id/usb*part1 | grep -i 'mount paths'",
                           stdout=subprocess.PIPE, shell=True).stdout.read()
    target = result[result.find("/"):-1]
    subprocess.Popen("dd if="+base+" of="+target+" ibs=4b obs=1b conv=notrunc,noerror", shell=True)
    return True
  else:
    return False
