print("Name- Aditya Motale")
file = open(".\p10.txt", "r")

for line in file:
    titled_line = line.title()
    print(titled_line)

file.close()