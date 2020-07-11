'''
https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?toc=%2Fpython%2Fazure%2FTOC.json
https://github.com/Azure-Samples/storage-blobs-python-quickstart/blob/master/example.py

Prerequisites:
Azure Storage SDK for Python
https://github.com/Azure/azure-storage-python

pip install azure-storage-blob
pip install azure-storage-file
pip install azure-storage-queue
'''

import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

# Create the BlockBlockService that is used to call the Blob service for the storage account
block_blob_service = BlockBlobService(account_name='storagepytest',
 account_key='YH1dFrPJh29cytJeHlJsVqzUDaPqnvR0BpCYkS8msmR3H9Q7gbym3pGIEcsAzoTOSKs53BgWNXKWau0DgUd05w==')

# Create a container called 'quickstartblobs'.
container_name ='quickstartblobs'
block_blob_service.create_container(container_name)

# Set the permission so the blobs are public.
block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)


# Create a file in Documents to test the upload and download.
local_path=os.path.expanduser('~/Documents')
#local_file_name ="QuickStart_" + str(uuid.uuid4()) + ".txt"
local_file_name = 'QuickStart.txt'
full_path_to_file = os.path.join(local_path, local_file_name)

# Write text to the file.
file = open(full_path_to_file,  'w')
file.write('Hello, World!')
file.close()

print(f'Temp file = {full_path_to_file}')
print(f'\nUploading to Blob storage as blob {local_file_name}')

# Upload the created file, use local_file_name for the blob name
block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

print(f'Uploaded to Blob storage as blob {local_file_name}')

 # List the blobs in the container
print('\nList blobs in the container')

generator = block_blob_service.list_blobs(container_name)

for blob in generator:
    print(f'\t Blob name: {blob.name}')

# Download the blob(s).
# Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name ,'.txt', '_DOWNLOADED.txt'))
print(f'\nDownloading blob to {full_path_to_file2}')
block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

sys.stdout.write('Sample finished running. When you hit <any key>, the sample will be deleted and the sample '
                    'application will exit.')
sys.stdout.flush()
input()

# Clean up resources. This includes the container and the temp files
block_blob_service.delete_container(container_name)
os.remove(full_path_to_file)
os.remove(full_path_to_file2)
