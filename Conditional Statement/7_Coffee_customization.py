order_size = input("order size (small/ medium/ large ): ")
extra_shot = input("You need extra shot (true or false): ")

if extra_shot == "true" :
    coffe = order_size + " coffe with an extra shot"

else:
    coffe = order_size + " coffe"

print(coffe)    
