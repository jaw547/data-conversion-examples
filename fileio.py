with open('myfile.txt') as f:
    my_file_text = f.read()

full_text = my_file_text + '\nyo from fileio'

with open('testwrite.txt', 'w') as f:
    f.write(full_text)
