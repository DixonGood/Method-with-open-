string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
string3 = input("Введите третью строку: ")
string4 = input("Введите четвертую строку: ")

with open("homework.txt", "w") as f:
    f.write(string1 + "\n" + string2 + "\n")


with open("homework.txt", "a") as f:
    f.write(string3 + "\n" + string4)