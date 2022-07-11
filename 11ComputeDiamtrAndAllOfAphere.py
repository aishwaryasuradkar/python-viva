print("Name- Aditya Motale")
PI = 3.14

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getDiameter(self):
        return self.radius*2

    def getCircumference(self):
        return PI*(self.radius**2)

    def getVolume(self):
        return (4 / 3) * PI * self.radius**3


sphere_1 = Sphere(radius=4)

sphere_1.getDiameter(), sphere_1.getCircumference(), sphere_1.getVolume()
