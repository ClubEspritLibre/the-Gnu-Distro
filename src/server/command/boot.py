import os,shutil

def bootDistribution(dist):
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb")!= -1 ]
  if(len(usb)!=0):
    homedir = os.environ['HOME']
    base=homedir+"/.the-gnu-distro/distribution/"+dist
    
