import plistlib
import os
from opsys import getPlatform


def checkInstall() :
    if getPlatform() == "Darwin" and os.path.exists(os.path.join(os.environ.get("HOME"),"Library","LaunchAgents","com.sdcatcher.insert.plist")):
        return True
    return False
        

def install() :
    if getPlatform() == "Darwin" :

        pythonBin = "/usr/bin/python3"
        scriptLocation = os.path.join(os.path.dirname(__file__),'main.py')
        
        pl_path = os.path.join(os.environ.get("HOME"),"Library","LaunchAgents","com.sdcatcher.insert.plist")
        pl = {
            'Label': 'com.sdcatcher.sdcards',
            'ProgramArguments': [pythonBin, scriptLocation],
            'WatchPaths': ['/Volumes']
        }
    
        try :
            with open(pl_path, 'wb') as f:
                plistlib.dump(pl,f)
            print (pl_path, "created")
            return True

        except Exception as e:
            print ('Something went wrong :',e)
        
print(install())