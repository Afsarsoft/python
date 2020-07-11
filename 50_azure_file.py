'''
https://docs.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage

Prerequisites:
Azure Storage SDK for Python
https://github.com/Azure/azure-storage-python

pip install azure-storage-blob
pip install azure-storage-file
pip install azure-storage-queue
'''

# Set up your application to use Azure Files
from azure.storage.file import FileService
print('Completed-> Set up your application to use Azure Files')

# Set up a connection to Azure storage account
#file_service = FileService(account_name='myaccount', account_key='mykey')
try:
    file_service = FileService(account_name='storagepytest',
     account_key='YH1dFrPJh29cytJeHlJsVqzUDaPqnvR0BpCYkS8msmR3H9Q7gbym3pGIEcsAzoTOSKs53BgWNXKWau0DgUd05w==')

except Exception as e:
    print(f'not able connect to storage account! {e}')    

else:
    # ToDoList, not able to catch the error!
    print('Completed-> Set up a connection to Azure Files')

'''
# If already exists, not erroring out
# Create an Azure file share
try:
    file_service.create_share('myshare')

except Exception as e:
    print(f'not able to create share! {e}')    

else:
    print('Completed-> Create an Azure file share')
'''

'''
# If already exists, not erroring out
try:
    file_service.create_directory('myshare', 'sampledir')

except Exception as e:
    print(f'not able to create directory! {e}')    

else:
    print ('Completed-> Create a directory')
'''

'''
# Enumerate files and directories in an Azure file share
try:
    generator = file_service.list_directories_and_files('myshare/sampledir') # to go to the sub
    # generator = file_service.list_directories_and_files('myshare')
    for file_or_dir in generator:
        print(file_or_dir.name)

except Exception as e:
    print(f'Issue connection to share! {e}')    

else:
    print ('Completed-> Enumerate files and directories in an Azure file share')
'''

'''
# Delete a file
try:
    file_service.delete_file('myshare', None, 'Paas Cube On ADLS.docx')

except Exception as e:
    print(f'Issue deleting the file from share! {e}')    

else:
    print ('Completed-> Delete a file')
'''

'''
# Delete an Azure file share
try:
    file_service.delete_share('myshare')

except Exception as e:
    print(f'Issue deleting the share! {e}')    

else:
    print('Completed-> Delete an Azure file share')

'''

'''
try:
# Delete a file
    file_service.delete_file('myshare/sampledir', None, 'Paas Cube On ADLS.docx')
    print ('Completed-> Delete a file')

except Exception as e:
    print(f'Issue deleting the file from share! {e}')    

else:
    print("Deleted the file OK ...")    

finally:
    print("Executing finally...")          
'''

'''
# Delete an Azure file share
# Should be empty
try:
    file_service.delete_directory('myshare', 'sampledir')

except Exception as e:
    print(f'Issue deleting the directory! {e}')    

else:
    print('Completed-> Delete a directory')
'''

'''
# Delete an Azure file share
try:
    file_service.delete_share('myshare')

except Exception as e:
    print(f'Issue deleting the share! {e}')    

else:
    print('Completed-> Delete an Azure file share')
'''

