# pyright: strict

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Read, parse, and write CSV files
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import csv

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Looking at the file, using reader
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
with open(read_file, 'r') as csv_file:
    # with open('C:/scyrus/py/py/csv/names.csv', 'r') as csv_file:
    # by default open as "," delimiter. Good practice always specify
    csv_reader = csv.reader(csv_file, delimiter=',')

    print(csv_reader)

    # next(csv_reader) # to skip the first row, the header

    for line in csv_reader:
        print(line)
        # print(line[2]) # to see just e-mails
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Looking at the file, using DictReader, better approach
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
with open(read_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    print(csv_reader)

    # do not skip since it is buit in for DictReader to remove the header
    # next(csv_reader)

    for line in csv_reader:
        # print(line)
        print(line['email'])  # to see just e-mails

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using reader, pipe line
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_pipe.csv'
with open(read_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='|')  # using pipe line

        for line in csv_reader:
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using reader, tab
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_tab.csv'
with open(read_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')  # using tab

        for line in csv_reader:
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using reader, comma
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_comma.csv'
with open(read_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')  # using comma

        for line in csv_reader:
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using DictReader, comma
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_Dict_comma.csv'
with open(read_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        f_names = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=f_names)  # using comma

        # to get the header
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using DictReader, pipe line 1
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_Dict_pipe.csv'

with open(read_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        f_names = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=f_names, delimiter='|')

        # to get the header
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# writing to another CSV file, using DictReader, pipe line 2
#import csv
read_file: str = 'C:/scyrus/py/py/csv/names.csv'
write_file: str = 'C:/scyrus/py/py/csv/new_names_Dict_pipe2.csv'

with open(read_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(write_file, 'w', newline='') as new_file:
        f_names = ['first_name', 'email']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=f_names, delimiter='|')

        # to get the header
        csv_writer.writeheader()

        for line in csv_reader:
            del line['last_name']
            csv_writer.writerow(line)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
