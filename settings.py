import os
import json

### Returns a dict object containing the current content of settings.json ###

def load() :
    try :
        with open('settings.json') as map:
            settings = json.load(map)
            return settings
    except Exception as e :
        print ("Error : ",e)



### Volume Checker, if a SD card is currently mounted, it will return the dict object of the SD card mappings ###
def checkVolume() :
    try :
        
        settings = load()
        result = []
        for card in settings["sdCards"] :
            if os.path.exists(card["sourcePath"]) :
                result.append(card)
            
        if result == [] :
            return False
        
        return result

    except Exception as e :
        print("Something wrong happened : ",e)


### Boolean value for the showDialog option ###
        
def showDialog() :
    settings = load()
    if settings["showDialog"] == "true" :
        return True
    else :
        return False

