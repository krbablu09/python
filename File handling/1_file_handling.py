# REading a file
# f = open ("my_file.txt","r")
# print(f)
# text = f.read()
# print(text)
# f.close()

# Writting a file

# f = open('my_file.txt','w')
# f.write('hello,world!')

# f.close()

# with open('my_file.txt','a') as f:
#     f.write("he bablu what happend")

# f = open('my_file.txt','r') 
# print("Filename: ", f.name)
# print("Mode: ", f.mode)
# print("Is Closed?: ", f.closed)

# f.close()
# print("Is Closed?: ", f.closed)

file = open("my_file.txt", "r")
content = file.read()
print(content)
file.close()