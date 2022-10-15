player_x = 4
player_y = 4
import logging

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



def renderables(worldState, sx, sy, w, h):
    sx = screen_x
    sy = screen_y

    for i in propcoords:
        if i.x < sx or i.x > (sx+w):
            continue
        elif i.y < sy or i.y > (sy+h):
            continue
        else:
            renderableprops.append(i)

def playeraction():
    print("Type your action:")
    answer = input()
    print(answer)

def render_x(m, xc, w):
    return m[xc:xc+w]

def render_y(screen_y, height, naytto):
    y_pos = screen_y + 1
    with open("Test.txt", "r") as a:
        for i in range(0, height):
            row = str((a.readlines(y_pos)))
            row = row.replace("[","").replace("]","").replace("'","")#.replace("n","")
            w = width
#            print(render_x(row, screen_x, w))
            y_pos = y_pos + 1
            naytto.append(render_x(row, screen_x, w))

def replace(s, index, c):
    chars = list(s)
    chars[index] = c
    res = "".join(chars)
    return res

def renderAll():
    for i in renderableprops:
        rivi = i.y
        x = i.x
        kirjain = i.character
        rivi = naytto[rivi]
        print(replace(rivi, x, kirjain))

    # for i in naytto:
    #     print(i)

def mainrender(worldState):
    renderables(worldState.screen_x, worldState.screen_y, worldState.width, worldState.height)
    render_y(worldState.screen_y, worldState.height, worldState.naytto)
    renderAll()
    playeraction()


class WorldState:
    '''Holds everything together'''
    screen_x = 1
    screen_y = 1
    width = 9 
    height = 7

    naytto = []
    propcoords = []
    renderableprops = []
    actions = ["attack", "defend", "move", "open chest", "open inventory", "flee", "heal", "eat", "potion"]

    def loadMap():
        kartta = []
        # load kartta 
        return kartta


    def loadProps():
        props = []
        #load props
        enemy1 = enemy("E", 4, 10, 2, 1, 1, "none", 2, 4)
        enemy1.getCoordinates()
        props.append(enemy1)
        return props


    def init(self):
        props = self.loadProps()
        kartta = self.loadMap()        
        logging.info('world initialized')


def main():
    worldState = WorldState()
    worldState.init()
    mainrender(worldState)


if __name__ == "__main__":
    main()