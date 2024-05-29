file_name = 'File_1.txt'
file = open(file_name, mode='r')
line = True
with file:
    for line in file:
        print(line)
print(file.closed)
'''file.close() окончательно и безповоротно закрывает фаил а with закрывает и открывет его 
когда нужно что нибудь добавить в фаил'''