# Assignment4
TASK1

README

Python File Reader

This is a simple Python program that opens and reads a text file named sample.txt, prints its output line by line, and handles errors gracefully if the file does not exist.

Features

Reads a text file named sample.txt

Prints the file's contents line by line

Handles errors gracefully if the file is missing

Requirements

Python 3.x

Usage

Ensure you have Python installed on your system.

Place a text file named sample.txt in the same directory as the script.

Run the script using the following command:

python file_reader.py

Error Handling

If sample.txt does not exist, the program prints an error message instead of crashing.

Code Example

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

TASK2
README

Python File Writer and Reader

This Python program takes user input, writes it to a file named output.txt, appends additional data to the same file, and then reads and displays the final content.

Features

Accepts user input and writes it to output.txt

Appends additional user input to the same file

Reads and displays the final content of the file

Requirements

Python 3.x

Usage

Ensure you have Python installed on your system.

Run the script using the following command:

python file_writer_reader.py

Enter text when prompted. The input will be written and appended to output.txt.

The program will then read and display the complete contents of output.txt.
code:
string = input("enter text to write to the file:")
file1 = open('output.txt','w')
file1.write("\n"+string)
print("Data successfully written to output.txt ")
file1.close()

string2 = input("enter additional text to append:")
file2 = open('output.txt','a')
file2.write("\n"+ string2)
print("Data successfully appended. ")
file2.close()
file2 = open('output.txt','r')
reading_file = file2.read()

print("Final content of output.txt:",reading_file)
file2.close()
