import os
import shutil
from tqdm import tqdm

cameraSD = 'ZV1'
savingPath = '/Users/yehdar/Pictures/ZV1/CLIPS/'

def checkVolume() :
    if cameraSD in os.listdir("/Volumes") :
        absPath = "/Volumes/"+cameraSD+"/PRIVATE/M4ROOT/CLIP"
        return absPath
    else :
        return False


def copy_with_progress(src, dst):
    # Get the size of the source file
    total_size = os.path.getsize(src)

    # Open the source file in binary mode
    with open(src, 'rb') as fsrc:
        # Open the destination file in binary mode
        with open(dst, 'wb') as fdst:
            # Create a progress bar with total size
            progress = tqdm(total=total_size, unit='B', unit_scale=True)

            # Copy the file chunk by chunk
            while True:
                # Read a chunk of data from the source file
                chunk = fsrc.read(1024)

                # If no more data is available, break the loop
                if not chunk:
                    break
                
                # Write the chunk to the destination file
                fdst.write(chunk)

                # Update the progress bar with the chunk size
                progress.update(len(chunk))
            
            # Close the progress bar
            progress.close()


def clipManager() :
    if not checkVolume() :
        return False
    
    try :
        for clip in os.listdir(checkVolume()) :
            if os.path.basename(clip)[-4:].lower() == '.mp4' and os.path.basename(clip)[0] != '.' :
                clipAbsPath = checkVolume()+"/"+clip
                print ("CLIP FOUND :",clip)
                if not os.path.exists(savingPath+clip) :
                    copy_with_progress(clipAbsPath, savingPath+clip)
                    print("File copied successfully")
                else :
                    print ("File already exist")

    except Exception as e :
        print ('Something went wrong :',e)


clipManager()
