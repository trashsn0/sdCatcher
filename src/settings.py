import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

### Returns a dict object containing the current content of settings.json ###
def load():
    try:
        # Get the absolute path of the directory where this script is located
        script_dir = os.path.dirname(__file__)
        print (script_dir)
        settings_path = os.path.join(script_dir, '../settings.json')

        with open(settings_path) as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError as e:
        logger.error("File not found: %s", e)
    except json.JSONDecodeError as e:
        logger.error("Error parsing JSON: %s", e)
    except Exception as e:
        logger.error("Other error: %s", e)
    return {}

### Volume Checker, if a SD card is currently mounted, it will return the dict object of the SD card mappings ###
def checkVolume():
    settings = load()
    result = []

    try:
        for mapping in settings.get("mappings", []):
            if os.path.exists(mapping["sourcePath"]):
                result.append(mapping)
        
        return result if result else False

    except Exception as e:
        logger.error("Something wrong happened: %s", e)
        return e

### Boolean value for the showDialog option ###
def showDialog():
    settings = load()
    return settings.get("showDialog", "false").lower() == "true"



print(load())