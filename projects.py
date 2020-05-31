print("Hello there!")
print("This program prints what you have typed.")
print("If you want to stop, just type 'x'.")
abc = str(input("What do you want to print? :  "))
while True:
    print(abc)
    abc = str(input("What do you want to print? :  "))
    if(abc == "x"):
        break
    
