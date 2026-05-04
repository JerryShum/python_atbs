# Learning about boolean expressions and comparison operators
comp1 = 4 < 5
comp2 = 5 > 4

# true AND true = true
print(comp1 and comp2)

# false OR true = true
print((1 == 2) or (2== 2))

# ---------------------------------------------------------
# Flow Control in python (if, else, elif)
name = input("Please input your name:")
if(name.lower() == "alice"):
    print("Hi, Alice.")
elif (name.lower() == "jerry"):
    print("Hi, Jerry!")
else:
    print("Your name is not Alice.")