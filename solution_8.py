#solution_8.py
#Christopher Ward
#MPCS 50101, Winter 2015
#This program converts a Fahrenheit temperature to Celsius
#and reports the temperature as a whole number
def FtoC():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = int(round(((fahrenheit - 32) * 5/9),0))
    if celsius == 1:
        print("The temperature is", celsius, "degree Celsius.")
    else:
        print("The temperature is", celsius, "degrees Celsius.")

FtoC()
