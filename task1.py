user = input('Enter the text: ')
text = list(user)
capital = 0
small = 0

for i in text:
    if i.islower():
        capital = capital + 1
    elif i.isupper():
        small = small + 1
    else:
        continue
sum = capital + small
print(f"capital letters: {int((capital * 100) / sum)}%")
print(f"small letters: {int((small * 100) / sum)}%")