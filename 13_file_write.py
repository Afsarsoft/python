# pyright: strict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# let see if we try to write to a file opened for read
with open('test.txt', 'r') as f:
    f.write('Test')  # we get error "not writable"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Create a new file to write in
with open('test2.txt', 'w') as f:
    # be carefull if file already exist. it will owerite
    # jsut running as is with "pass" will create a file
    pass
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Now write to file
with open('test2.txt', 'w') as f:
    f.write('Test')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Write to file
with open('test2.txt', 'w') as f:

    f.write('Test')

    # With seek method to go to a specific location
    f.seek(0)

    f.write('Test')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading from a file and writing to anotehr file
# Here we are opening existing file for read and writing
# to a file line by line
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# We can do simillar approach for image files
with open('AzureArtifacts.png', 'rb') as rf:
    with open('AzureArtifacts_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Also, as before, we can control how much we copy. chuck by chunck
with open('AzureArtifacts.png', 'rb') as rf:
    with open('AzureArtifacts_copy.png', 'wb') as wf:
        chunk_size: int = 100
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
