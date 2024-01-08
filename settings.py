import os
import json

### Returns a dict object containing the current content of settings.json ###

def load():
    try:
        # Get the absolute path of the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        settings_path = os.path.join(script_dir, 'settings.json')

        with open(settings_path) as map:
            settings = json.load(map)
            return settings
    except FileNotFoundError as e:
        print("File not found:", e)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
    except Exception as e:
        print("Other error:", e)



### Volume Checker, if a SD card is currently mounted, it will return the dict object of the SD card mappings ###
def checkVolume() :
    settings = load()
    result = []
    
    try :
        for mapping in settings["sdCards"] :
            if os.path.exists(mapping["sourcePath"]) :
                result.append(mapping)
        
        if len(result) == 0 :
            return False
        else :
            return result

    except Exception as e :
        print("Something wrong happened : ",e)
        return (e)


### Boolean value for the showDialog option ###
        
def showDialog() :
    settings = load()
    if settings["showDialog"] == "true" :
        return True
    else :
        return False

