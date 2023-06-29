from curses.ascii import isdigit


string = "deepak1234"
result = ""
for i in range(len(string)):
    if string[i].isdigit():
        result = result + string[i]
print(result)