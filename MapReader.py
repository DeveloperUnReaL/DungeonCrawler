player_x = 4
player_y = 4
screen_x = 1
screen_y = 1
width = 9 
height = 7

propcoords = []
renderableprops = []
actions = ["attack", "defend", "move", "open chest", "open inventory", "flee", "heal", "eat", "potion"]


class hero():
    def __init__(self, character, damage, hp, x, y, size, loot):
        self.character = character
        self.damage = damage
        self.hp = hp
        self.x = x
        self.y = y
        self.size = size
        self.loot = loot


class enemy(object):
    def __init__(self, character, damage, hp, x, y, size, loot, spawnx, spawny):
        self.character = character
        self.damage = damage
        self.hp = hp
        self.x = x
        self.y = y
        self.size = size
        self.loot = loot
        self.spawnx = spawnx
        self.spawny = spawny
    
    def getCoordinates(self):
        propcoords.append(self)


enemy1 = enemy("e", 4, 10, 2, 4, 1, "none", 2, 4)
enemy1.getCoordinates()

def renderables(sx, sy, w, h):
    sx = screen_x
    sy = screen_y

    for i in propcoords:
        if i.x < sx or i.x > (sx+w):
            continue
        elif i.y < sy or i.y > (sy+h):
            continue
        else:
            renderableprops.append(i)
            for i in renderableprops:
                print(i.x, i.y)

def playeraction():
    print("Type your action:")
    answer = input()
    print(answer)

def render_x(m, xc, w): ###xc = x coordinate so I can use x for searching from the list renderableprops.

    for i in renderableprops:
        if i.x == xc:
            print("joo")
        else:
            continue
    
    return m[xc:xc+w]

def render_y(screen_y, height):
    y_pos = screen_y + 1
    with open("Test.txt", "r") as a:
        for i in range(0, height):
            row = str((a.readlines(y_pos)))
            row = row.replace("[","").replace("]","").replace("'","").replace("n","")
            w = width
            print(render_x(row, screen_x, w))
            y_pos = y_pos + 1

def mainrender():
    renderables(screen_x, screen_y, width, height)
    render_y(screen_y, height)
    playeraction()

def main():
    mainrender()

if __name__ == "__main__":
    main()