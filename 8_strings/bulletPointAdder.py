import pyperclip

# get the text from a clipboard
text = pyperclip.paste()
print(text)
start = "* "

# modify the text

# 1. separate the text by \n chars
separated = text.split("\n")
clean = []
for sentence in separated:
    formatted = start + sentence
    clean.append(formatted)

print(clean)
print("\n".join(clean))
pyperclip.copy("\n".join(clean))
