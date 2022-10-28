# Write program to read and write csv file
'''Follow this requirements:
1. Get user input for 2 columns: name, age
2. Write CSV file name 'data.csv' with 2 columns: name, age
3. Write 5 rows of data
4. Read the file and print the data
5. Read the file and print the data in a list
6. Read the file and print the data in a dictionary
'''

from csv import writer, reader


def write_csv():
    with open('data.csv', 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['name', 'age'])
        for i in range(5):
            name = input('Enter name: ')
            age = input('Enter age: ')
            csv_writer.writerow([name, age])


def read_csv():
    with open('data.csv', 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            print(row)


def read_csv_list():
    with open('data.csv', 'r') as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        print(data)


def read_csv_dict():
    with open('data.csv', 'r') as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        for row in data:
            print(row)
            print(dict(zip(data[0], row)))


if __name__ == "__main__":
    write_csv()
    read_csv()
    read_csv_list()
    read_csv_dict()
