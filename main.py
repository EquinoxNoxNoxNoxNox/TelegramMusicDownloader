import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
    from telethon import errors
except:
    print("WE HAVE TO INSTALL SOME LIBRARIES FIRST")
    input("press Enter to continue...")
    os.system('pip3 install telethon')
    os.system("pip3 install cryptg")
    os.system("cls")
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
    from telethon import errors
print("run on python " + os.sys.version)
sessionName = "MainSession"
api_id = 2496
api_hash = "8da85b0d5bfe62527e5b244c209159c3"
client = TelegramClient(sessionName,api_id,api_hash)
client.start()

if __name__=="__main__":
    username = str(input("Enter user/channel username : "))
    try:
        ent = client.get_entity(username.split("/")[-1])
    except:
        print("Entity not found , try again")
        username = str(input("Enter user/channel username : "))
        ent = client.get_entity(username)
    print("\n "+ str(ent.id) +" entered \n")
    path = 'TelegramMusics-'+username
    downloadCounter = 1
    if(not os.path.isdir(path)):
        os.makedirs(path)
    for msg in client.iter_messages(ent):
        if(msg.audio):
            if(os.path.exists(path + "/" + msg.file.name)):
                continue
            try:
                print("Downloading the song : " + msg.file.name)
                downloadpath = client.download_media(msg.media, path)
            except errors.rpcerrorlist.FileReferenceExpiredError:
                continue
            print('File saved to', downloadpath +"\n")  # printed after a download is done
            downloadCounter += 1
        else:
            continue
    print("**************Download Finished - "+ str(downloadCounter) +" songs saved **************")
