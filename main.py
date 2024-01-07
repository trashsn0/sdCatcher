import opsys,settings


def main() :
    
    try :    

        mappings = settings.checkVolume()


        ### SD card not plugged
    
        if not mappings :
            print("Volume not attached")
            opsys.volumeNotFound()
            return False
        
        ### SD card plugged 
        
        
        if settings.showDialog() :
            userInterraction = opsys.dialog(mappings) 
            
            if not userInterraction :
                print ("User declined")
                return False
            
            if userInterraction == "button returned:Sync Photos" :
                opsys.execute(True,False,mappings)

            elif userInterraction == "button returned:Sync Videos" :
                opsys.execute(False,True,mappings)

            elif userInterraction == "button returned:Sync Both" :
                opsys.execute(True,True,mappings)

        else :
            opsys.execute(True,True,mappings)
                
        
    
        opsys.show_notification("SD Card Processed","Files have been properly copied to their locations.")

    except Exception as e :
        print ('Something went wrong :',e)



if __name__ == '__main__' :

    main()
    
