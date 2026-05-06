# Write a function named get_end_coordinates(directions) that accepts a list of north, south, east, and west directions and returns a numeric pair of Cartesian coordinates.

# The first part of the program should repeatedly ask the user to enter N, S, E, or W (but should accept the lowercase n, s, e, and w as well) and should collect these inputs in a list. The loop should exit when the user enters a blank string. Next, the program should pass the list to the get_end_coordinates() function.

# Going north should increase the y-coordinate by one, while going south should decrease it by one. Likewise, going east should increase the x-coordinate by one, while going west should decrease it by one.

# You can represent the coordinates in another list. For example, the function call get_end_coordinates(['N', 'N', 'W']) should return the list [-1, 2], and the function call get_end_coordinates(['E', 'W', 'E', 'E']) should return the coordinates [2, 0]. Your program should print the list returned by get_end_coordinates().

# Save this program in a file named coordinateDirections.py.

def get_end_coordinates(directions):
    
    x=0
    y=0
    for index,value in enumerate(directions):
        if value == 'e':
            x+=1
        elif value == 'w':
            x-=1
        elif value == 'n':
            y+=1
        else:
            y -= 1
        
    return [x,y]

def get_user_input():
    direction_list = []
    valid_list = ['n', 'e', 's','w']
    while True:
        print('Please enter n or e or s or w.')
        user_input = input('>')
        
        if(user_input == ""):
            break
        
        if(user_input.lower() not in valid_list):
            continue
        
        direction_list.append(user_input.lower())
        
        print(direction_list)
        
    
    return direction_list

def main():
    directions = get_user_input()
    coordinate_result = get_end_coordinates(directions)
    
    print('Result:' + str(coordinate_result))
    

main()
        