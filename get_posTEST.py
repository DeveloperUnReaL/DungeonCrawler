file = "abcdefghijklmnopqrstuvwxyzo"
row1 = False
row2 = False
row3 = False

with open("D:\kamat\python\MapTest\MapTest.txt", "r") as f:
    Map = str(f.readlines(1))
    print(type(Map))

def get_pos(Map, SX, width):
    return (Map)[SX + 1, SX + width]

def rows():
    pos = 8
    Lista = []
    for i in range(0, 5):
        bring_pos = get_pos(Map, pos)
        Lista.append(bring_pos)
        pos = pos + 1
    print(*Lista, sep=" ")

rows()
#print(*lines, sep=" ")