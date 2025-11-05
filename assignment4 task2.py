with open("output.txt", 'wt') as fh:
    content = input("Enter text to write to the file: ")
    fh.write(content)
    print("Data successfully written to output.txt")
print("\n\n")
with open("output.txt", 'at') as fh:
    appending_content = input("Enter additional text to append: ")
    fh.write(appending_content)
    print("Data successfully appended to output.txt")
with open("output.txt", 'rt') as fh:
    content = fh.read()
    print("final content of output.txt is: ", content)
print("Learning file handling in python")