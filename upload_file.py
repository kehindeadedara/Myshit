from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os
import sys
import getopt

CLIENT_SECRECT_FILE =  'secret_client.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRECT_FILE, API_NAME, API_VERSION, SCOPES)
folder_id = '/0Bwd0VOuQpxHdfnZ0Rk8xdmwxOGw1ZTR1U1BlWWNQZTQxQkVuY0ZkeGFqRnFmdlloMnl6NVU'
mime_types = 'text/plain'

directory = 'TXDATA'
erase = 'no'

def upload_file(name, file_name):
    global mime_types, folder_id
    file_metadata = {
        'name' : name,
        'parents': folder_id,
        'mimeType': mime_types
        }
    media = MediaFileUpload(file_name, mimetype= mime_types)
    service.files().create(
        body = file_metadata,
        media_body = media,
        fields = 'id',
        ).execute()

def usage():
    print("-f - file path to upload")
    print("-e chose to wipe folder afterwards")

def Erase_data(file_path):
    for f in os.listdir(file_path):
        os.remove(os.path.join(file_path, f))
    
def main(argv):
    global directory, erase
    try:
        opts, args = getopt.getopt(argv, "hf:e:", ["file=", "erase="])
    except getopt.GetoptError as err:
        usage()
        print("stopping...")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-f', '--file'):
            directory = arg
        elif opt in ('-e', '--erase'):
            erase = (arg)
    
    navigate = "DataLog/{}".format(directory)
    file_names = os.listdir(navigate)
    try:
        for name in file_names:
            file_path = "DataLog/{}/{}".format(directory, name)
            upload_file(name, file_path)
        print('Data transfered successfully.')
    except:
        print("Check Google Drive OAuth or filepath does not exist...")

    if erase == "yes":
        Erase_data(navigate)
        print("Files erased from directory")
    else:
        print("Files not removed from directory")

    
if __name__ == "__main__":
    main(sys.argv[1:])
