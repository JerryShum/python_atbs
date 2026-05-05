def collatz(number):
    if number % 2 == 0:
        # number is even
        result = number //2
        print(result)
        return result
    
    else:
        result = 3 * number + 1
        print(result)
        return result

# main program
def main():
    userInput = 0
    # user input --> number
    while not userInput:
        try: userInput = int(input('Please insert a number >'))
        except ValueError:
            print('The input must be a number.')
    
    collatzValue = userInput
    
    while collatzValue != 1:
        collatzValue = collatz(collatzValue)

main()
    