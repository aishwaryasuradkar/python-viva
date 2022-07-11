print("Name- Aditya Motale")


def getLength(list):
    if not list:
        return 0
    return 1 + getLength(list[1::2]) + getLength(list[2::2])

print("Length of the list is:", getLength(listOfFruits))
