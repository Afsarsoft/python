# pyright: strict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# OS internal module allows us to access underlying
# Operating System functionality
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime
import os

# Lets take a look at all the attributes and methods
# print(dir(os))

# Let's take a look at the few most common used
# Current directory
print(os.getcwd())  # C:\scyrus\py\py
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

# Let's see what files and folders we have
print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Let's create a new folder
# if there is only one level without any sub directory
# we can use

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

os.mkdir('demo1')

print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# if there are several level deep and have some directories
# we can use

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

os.makedirs('demo1/sub1/sub2')

print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# if there are several level deep and have some directories
# we can use

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

# to keep things eaier we can always use makedirs even for creating one diectory
os.makedirs('demo2')

print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for removing folders can use

print(os.getcwd())

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

# For one directory.
# please note directory need to be empty
# os.rmdir('demo2')

# For several
os.removedirs('demo1/sub1')

print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for renaming a file

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

os.rename('test.txt', 'demo.txt')

print(os.listdir())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for getting info about a file

# Let's change the working directory
os.chdir('C:/scyrus/py')

print(os.getcwd())

# Get all info about a file
# print(os.stat('demo.txt'))

# Get size info
# print(os.stat('demo.txt').st_size)

# Get the last modification time
# This gives the time stamp
# To be able to have it as actual date time format
# , we need to use datetime module
print(os.stat('demo.txt').st_mtime)

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To learn about the info on your desktop

for dirpath, dirnames, filenames in os.walk('C:/scyrus/py/py'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To gt to the directory home path

# the following is for mac
# print(os.environ.get('HOME'))

# My user directory
print(os.environ.get('USERPROFILE'))

# to get the path to a file we need to create in future
file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(file_path)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To gt the file path name

# The following gives the file name any path we are working on
# regardless the following path exist or not
print(os.path.basename('/temp/test.txt'))  # test.txt

# To get the directory
print(os.path.dirname('/temp/test.txt'))

# To get the both names
print(os.path.split('/temp/test.txt'))

# To check the path exist
print(os.path.exists('/temp/test.txt'))

# To check the folder exist
print(os.path.isdir('C:/scyrus/py'))

# To check the file exist
print(os.path.isfile('C:/scyrus/py/demo.txt'))

# To get the file extension. usful for file manipulation
print(os.path.splitext('C:/scyrus/py/demo.txt'))

# To  see everything is available for os.path module
print(dir(os.path))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Chek out the video "autoamted parsing and renaming of multiple files"
# Renaming files so, the numbers in the file comes at the begining

# Let's change the working directory
# I took the backup to the test_orig folder
os.chdir('C:/scyrus/py/py/test')

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    # print(file_name)
    # print(file_name.split('-'))

    f_name, f_num = f_name.split('-')
    # print(f_name)
    # print(f_num)
    f_name = f_name.strip()  # remove spaces
    f_num = f_num.strip()

    # print(f'{f_num}-{f_name}{f_ext}')

    new_name = f'{f_num}-{f_name}{f_ext}'
    os.rename(f, new_name)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
