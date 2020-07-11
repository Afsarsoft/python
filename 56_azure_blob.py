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
import datetime, time
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def setup_blob_storage(account, key):
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        blob_service = BlockBlobService(account_name = account, account_key = key)

        return blob_service

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def create_container(blob_service, container_name):
    try:
        blob_service.create_container(container_name)

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def set_permission(blob_service, container_name):
    try:
        # Set the permission so the blobs are public.
        blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_local_path(file_location):
    try:
        path=os.path.expanduser(file_location)
        
        return path

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_full_path(path, file_name):
    try:
        full_path = os.path.join(path, file_name)
        
        return full_path

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def write_to_file(path, message):
    try:
        # Write text to the file.
        file = open(path,  'w')
        file.write(message)
        file.close()

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def upload_file(blob_service, container_name, file_name, path):
    try:
        # Upload the created file, use local_file_name for the blob name
        blob_service.create_blob_from_path(container_name, file_name, path)

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def blobs_in_container(blob_service, container_name):
    try:
        generator = blob_service.list_blobs(container_name)
        
        for blob in generator:
            print(f'Blob name: {blob.name}')

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def download_file(blob_service, container_name, local_path, file_name):
    try:
        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        full_path_download_file = os.path.join(local_path, str.replace(file_name ,'.txt', '_DOWNLOADED.txt'))
        blob_service.get_blob_to_path(container_name, file_name, full_path_download_file)

        return full_path_download_file

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def clean_up(blob_service, container_name, full_path_to_file, full_path_download_file):
    try:
        # Clean up resources. This includes the container and the temp files
        blob_service.delete_container(container_name)
        os.remove(full_path_to_file)
        os.remove(full_path_download_file)

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def process_time(start_time):
    try:
        # sleeping 
        #time.sleep(2)
        end_time = time.time()
        duration = end_time - start_time

        return duration

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def notify_user(msg):
    try:
        sys.stdout.write(msg)
        sys.stdout.flush()
        input()

    except Exception as e:
        print(f'Error -> {e}')        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def clean_up_time(start_time):
    try:
        end_time = time.time()
        duration = end_time - start_time

        return duration

    except Exception as e:
        print(f'Error -> {e}')        

''' 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Main 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
start_time = time.time()

storage_account = 'storagepytest'
storage_key = 'YH1dFrPJh29cytJeHlJsVqzUDaPqnvR0BpCYkS8msmR3H9Q7gbym3pGIEcsAzoTOSKs53BgWNXKWau0DgUd05w=='
container_name ='quickstartblobs'
local_file_name = 'QuickStart.txt'
file_location = '~/Documents'
file_info = 'Hello, World!'
user_message = 'Sample finished running. When you hit <any key>, the sample will be deleted.' 

block_blob_service = setup_blob_storage(storage_account, storage_key)
print(f'Completed, setup blob storage -> {storage_account}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

create_container(block_blob_service, container_name)
print(f'Completed, create container -> {container_name}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

set_permission(block_blob_service, container_name)
print(f'Completed, set permission -> {container_name}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

local_path = get_local_path(file_location)
print(f'Completed, get local path -> {local_path}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

full_path_to_file = get_full_path(local_path, local_file_name)
print(f'Completed, get full path -> {full_path_to_file}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

write_to_file(full_path_to_file, file_info)
print(f'Completed, write to file -> {full_path_to_file}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

upload_file(block_blob_service, container_name, local_file_name, full_path_to_file)
print(f'Completed, uploading to Blob storage as blob {local_file_name}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

blobs_in_container(block_blob_service, container_name)
print(f'Completed, blobs_in_container -> {container_name}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

full_path_download_file = download_file(block_blob_service, container_name, local_path, local_file_name)
print(f'Completed, downloading -> {full_path_download_file}, @{datetime.datetime.now().strftime("%H:%M:%S.%f")}')

duration = process_time(start_time)
print(f'Processing time -> {duration}')

notify_user(user_message)

start_time_clean_up = time.time()
clean_up(block_blob_service, container_name, full_path_to_file, full_path_download_file)
clean_up_duration = clean_up_time(start_time_clean_up)
print(f'Clean up time -> {clean_up_duration}')