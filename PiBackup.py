# Include the Dropbox SDK
import dropbox
import os

dbx = dropbox.Dropbox('GUcbLvxGy4YAAAAAAABnMMLbZlv5AeNOH3MnsXpx_gNmc9izMspOSf9g-CyR5Fyw')

# x = dbx.users_get_current_account()

# print x


client = dropbox.client.DropboxClient('GUcbLvxGy4YAAAAAAABnMMLbZlv5AeNOH3MnsXpx_gNmc9izMspOSf9g-CyR5Fyw')
# f = open('/home/pi/RetroPie/roms/gba/', 'rb')
# response = client.put_file('/test.txt', f)
# print 'uploaded: ', response

# folder_metadata = client.metadata('/')
# print 'metadata: ', folder_metadata

# f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
# out = open('magnum-opus.txt', 'wb')
# out.write(f.read())
# out.close()
# print metadata

for root, dirs, files in os.walk("/home/pi/RetroPie/roms"):
    for name in files:
        if name.endswith((".state", ".htm")):
            print name
			
			
			
response = client.put_file('dir/name', f)