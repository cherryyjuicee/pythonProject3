import sys


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isIntersect(self, otherCircle):
        l = ((otherCircle.x - self.x) ** 2 + (otherCircle.y - self.y) ** 2) ** 0.5
        rad = self.r + otherCircle.r
        if l < rad:
            return True
        return False


def newCircle(m):
    a = []
    for i in range(len(m)):
        if proverka(m, i):
            a.append(i)
    return a


def proverka(m, i):
    n = 0
    for j in range(len(m)):
        if m[i].isIntersect(m[j]) and i != j:
            n += 1
    return n == 0


def cic(k):
    ln =[]
    i = 0
    for i in range(len(k)):
        lp = Circle(k[i][0], k[i][1], k[i][2])
        ln.append(lp)
    return ln


def readToFile(file):
    matrix = [[int(n) for n in x.split()] for x in file]
    return matrix


def writeToFile(rez):
    f_end = open(sys.argv[2], "w+")
    s = str(rez)
    f_end.write(s + ' ')
    f_end.close()


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        f = file.readlines()
        matrix = readToFile(f)

    m = []
    m = cic(matrix)

    writeToFile(newCircle(m))



