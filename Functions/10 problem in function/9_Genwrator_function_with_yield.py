def even_generator(limit):
    vlaue = 0
    for i in range(2, limit + 1, 2):
        value = i
        print(value)

even_generator(10)    

def even_generator(limit):
    for i in range(2, limit + 1 , 2):
        yield i

for num in even_generator(10):
    print(num)