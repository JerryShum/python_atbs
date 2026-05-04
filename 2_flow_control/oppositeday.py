todayIsOppositeDay = False

# Set sayItIsOppositeDay based on todayIsOppositeDay
if todayIsOppositeDay == True:
    sayItIsOppositeDay = True
else:
    sayItIsOppositeDay = False
    
# If it is opposite day, toggle sayItIsOppositeDay
if todayIsOppositeDay:
    sayItIsOppositeDay = not sayItIsOppositeDay

# Say what day it is
if sayItIsOppositeDay:
    print('Today is opposite day.')
else:
    print('Today is not opposite day.')