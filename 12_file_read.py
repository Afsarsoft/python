# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# This is NOT recomended way
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading mode
# If we do not specify. is reading mode
# The recommended way to specify it
f = open('test.txt', 'r')

# Writing mode
f = open('test.txt', 'w')

# Appending mode
f = open('test.txt', 'a')

# Reading and writing
f = open('test.txt', 'r+')

# Name of the file
print(f.name)

# Making sure have the code close the file explicity
# Before running your code to avoid memory leak
f.close()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# The recomended way, best practice, # using content manager
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# the benifit here is that it allows to work with in the block
# When exit from the block, it automatically close the file
# Also, it automatically close the file if exception occured during our block of code
with open('test.txt', 'r') as f:
    pass

# we can get to the mode outside of the block
print(f.mode)

# But, the file is close
print(f.closed)

# if we try to ready the file, we get
# "I/O operation on closed file." error
print(f.read())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# let's read the content. This is OK for a small file for our
# sample file in here and no issue with memory issues
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# for a large file, there are different methods
with open('test.txt', 'r') as f:
    # Getting all the lines
    # a little weird because of new line charaters
    f_contents = f.readlines()
    print(f_contents)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# we could read just one line at a time
with open('test.txt', 'r') as f:
    # to remove blank lines adding "end=''"
    f_contents = f.readline()
    print(f_contents, end='')

    # Everytime, we use readline, it gets next line
    f_contents = f.readline()
    print(f_contents, end='')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To read all lines from very big file
# This is all we want most of the time
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To have more control in reading from very big file
with open('test.txt', 'r') as f:
    # Reading from the file every 100 character
    f_contents = f.read(100)
    print(f_contents, end='')

    # The following reads another 100 character
    f_contents = f.read(100)
    print(f_contents, end='')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Now, put the above approach in a loop
with open('test.txt', 'r') as f:
    # to see how it works in our example
    # let's go with 10 charactr and have end='*'
    size_to_read: int = 10

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To see the currect position in file
with open('test.txt', 'r') as f:
    size_to_read: int = 10

    f_contents = f.read(size_to_read)
    print(f.tell())
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# We can manipulate our current position in file
# using seek method, first take a look at
# below
with open('test.txt', 'r') as f:
    size_to_read: int = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)
    print(f_contents)

    # here we did read 20 characters
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Now we want go back to begining afer frist read
# using seek method
with open('test.txt', 'r') as f:
    size_to_read: int = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    # Here, we go back to read at the begining
    # but, we go to any location we want
    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Top 10 most common words, v1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
with open('testl.txt', 'r') as f:
    lcount: int = 0
    counts: dict = {}

    for line in f:
        words: List[str] = line.split()
        lcount += 1
        for word in words:
            counts[word] = counts.get(word, 0) + 1

# Short cut approach
# print(sorted([(v,k) for k,v in counts.items()]))

# Complete list of counts
# for (key, val) in counts.items():
#    print(f'for {key} ->', val)

# all_words = list()
all_words: list = []
for (key, val) in counts.items():
    # Create a temp tuple
    temp: tuple = (val, key)
    # Add to it
    all_words.append(temp)

all_words = sorted(all_words, reverse=True)

print(f'Top 10 words in file {f}:')

# Get top 10
for (val, key) in all_words[:10]:
    print(f'{key} -> {val}')

print(f'Total number of rows in file {f} -> {lcount}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Top 10 most common words, v2
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#from typing import List
with open('testl.txt', 'r') as f:
    lcount: int = 0
    counts: dict = {}
    # counts = dict()

    for line in f:
        words: List[str] = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

all_words: list = []
all_words = [(v, k) for (k, v) in counts.items()]

all_words = sorted(all_words, reverse=True)

print(f'Top 10 words in file {f}:')

# Get top 10
for (val, key) in all_words[:10]:
    print(f'{key} -> {val}')

print(f'Total number of rows in file {f} -> {lcount}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Show start with
with open('testl.txt', 'r') as f:
    for line in f:
        line: str = line.rstrip()
        if line.startswith('How'):
            print(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Skip start with
with open('testl.txt', 'r') as f:
    for line in f:
        line: str = line.rstrip()
        if line.startswith('How'):
            # skips it and sends it to for
            continue
        print(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Skip in
with open('testl.txt', 'r') as f:
    for line in f:
        line: str = line.rstrip()
        if 'stuff' in line:
            # skips it and sends it to for
            continue
        print(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Navigate through email
with open('email.txt', 'r') as f:
    for line in f:
        line: str = line.rstrip()
        if not line.startswith('From'):
            continue
        words: List[str] = line.split()
        print(words[2])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# count the words in a line
# counts = dict()
#from typing import List
counts: dict = {}
print('Enter a line of text:')
line: str = str(input(''))

words: List[str] = line.split()
print('Words:', words)

print('Counting ...')

for word in words:
    counts[word] = counts.get(word, 0) + 1

if len(counts) == 0:
    print('Did not enter info!')
else:
    print('Counts', counts)

print('Completed ...')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
search: str = input('Enter something to search: ')
fname: str = input('Enter the file name: ')
try:
    f1 = open(fname, 'r')
except:
    print(f'File cannot be opened! {fname}')
    quit()

count: int = 0
for line in f1:
    if search in line:
        count += 1

print(f'There were {count}, "{search}" lines in {fname}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
