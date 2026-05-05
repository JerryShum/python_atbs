while True:
    print('Who are you?')
    name = input('>')
    if name != 'joe':
        # if the input != joe --> break out of the current loop iteration
        continue
    
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break


print('Access granted.')