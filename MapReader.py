player_x = 4
player_y = 4
screen_x = 1
screen_y = 1
width = 9 
height = 7

actions = ["attack", "defend", "move", "open chest", "open inventory", "flee", "heal", "eat", "potion"]

def playeraction():
    print("Type your action:")
    answer = input()
    print(answer)

def render_x(m, x, w):
    return m[x:x+w]

def render_y(screen_y, height):
    y_pos = screen_y + 1
    with open("D:\kamat\python\MapTest\Test.txt", "r") as a:
        for i in range(0, height):
            row = str((a.readlines(y_pos)))
            row = row.replace("[","").replace("]","").replace("'","").replace("n","")
            w = width
            print(render_x(row, screen_x, w))
            y_pos = y_pos + 1

def mainrender():
    render_y(screen_y, height)
    playeraction()

mainrender()