from cmath import sqrt


class point3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        temp = point3(self.x, self.y, self.z)
        if isinstance(other, point3):
            temp.x += other.x
            temp.y += other.y
            temp.z += other.z
        else:
            temp.x += other
            temp.y += other
            temp.z += other
        return temp

    def __radd__(self, other):
        temp = point3(self.x, self.y, self.z)
        if isinstance(other, point3):
            temp.x += other.x
            temp.y += other.y
            temp.z += other.z
        else:
            temp.x += other
            temp.y += other
            temp.z += other
        return temp

    def __sub__(self, other):
        temp = point3(self.x, self.y, self.z)
        if isinstance(other, point3):
            temp.x -= other.x
            temp.y -= other.y
            temp.z -= other.z
        else:
            temp.x -= other
            temp.y -= other
            temp.z -= other
        return temp

    def __rsub__(self, other):
        temp = point3(self.x, self.y, self.z)
        if isinstance(other, point3):
            temp.x -= other.x
            temp.y -= other.y
            temp.z -= other.z
        else:
            temp.x = other - temp.x
            temp.y = other - temp.y
            temp.z = other - temp.z
        return temp

    def __mul__(self, other):
        if isinstance(other, point3):
            temp = 0
            temp = self.x * other.x+self.y * other.y+self.z * other.z
        else:
            temp = point3(self.x, self.y, self.z)
            temp.x *= other
            temp.y *= other
            temp.z *= other
        return temp

    def __rmul__(self, other):
        if isinstance(other, point3):
            temp = 0
            temp = self.x * other.x+self.y * other.y+self.z * other.z
        else:
            temp = point3(self.x, self.y, self.z)
            temp.x *= other
            temp.y *= other
            temp.z *= other
        return temp

    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        return self * (1.0 / self.length())
