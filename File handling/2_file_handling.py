f = open('my_file.txt','r')
while True:
    line = f.readline()
    print(line)
    if not line:
       print(line, type(line))
       break