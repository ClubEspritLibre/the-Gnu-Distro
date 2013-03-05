import os
import getpass

def copyDistribution(dist):
  target="/media/"+getpass.getuser()+"/"+os.listdir("/media/"+getpass.getuser()+"/")[0]
  
