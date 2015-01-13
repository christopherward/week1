#solution_8.py
#Christopher Ward
#MPCS 50101, Winter 2015
#This program converts a Fahrenheit temperature to Celsius
#and reports the temperature as a rounded whole number
def FtoC():
    try:
        fahrenheit = eval(input("What is the Fahrenheit temperature? "))
        celsius = int(round(((fahrenheit - 32) * 5/9),0))
        if celsius == 1 or celsius == -1:
            print("\nThe temperature is", celsius, "degree Celsius.")
        else:
            print("\nThe temperature is", celsius, "degrees Celsius.")

    except NameError:
        print("\nYou didn't enter a number.")
    except SyntaxError:
        print("\nYour input was not in the correct form.")
    except:
        print("\nSomething went terribly, terribly wrong.")
FtoC()
