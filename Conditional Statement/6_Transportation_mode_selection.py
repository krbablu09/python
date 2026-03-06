distance = int(input("Enter the distance: ",))

if distance < 3:
    transport = "Walk"

elif distance <= 15:
    transport = "Bike"

else:
    transport = "car"

print("transpotation medium is ",transport)    

