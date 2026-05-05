import sys 

while True:
    print('Type exit to exit:')
    response = input('>')

    if response == 'exit':
        sys.exit()
        
    print('You did not type "exit". You typed:' + response )