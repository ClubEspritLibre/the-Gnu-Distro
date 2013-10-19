# -*- coding: utf-8 -*-
import os, shutil, subprocess
from utils import usbIsPresent

def copyDistribution(dist):
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb") != -1]
  print usb
  print usbIsPresent()
  if usbIsPresent() == True:
    homedir = os.environ['HOME']
    base = homedir+"/.the-gnu-distro/distribution/"+dist
    result = subprocess.Popen("udisks --show-info /dev/disk/by-id/usb*part1 | grep -i 'mount paths'",
                           stdout=subprocess.PIPE, shell=True).stdout.read()

    target = result[result.find("/"):-1]
    try:
      shutil.copy(base,target)
    except IOError, e:
      return "Erreur lors de la copie : %s" %e
    return "Copie terminée"
  else:
    return None
