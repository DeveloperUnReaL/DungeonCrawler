import logging

def render_y(screen_y, screen_x, height, width, naytto):
    y_pos = screen_y + 2
    with open("Test.txt", "r") as a:
        for i in range(screen_y, height):
            row = str((a.readlines(y_pos)))
            row = row.replace("[","").replace("]","").replace("'","").replace("n","")
            y_pos = y_pos + 1
            #append every row to list named naytto
            naytto.append(row[screen_x:screen_x+width])

def filterProps(propcoords, screen_x, screen_y, width, height):
    for i in propcoords:
        if i.x < screen_x or i.x > (screen_x + width):
            continue
        elif i.y < screen_y or i.y > (screen_y + height):
            continue
        else:
            return i

def replace(s, index, c):
    chars = list(s)
    chars[index] = c
    res = "".join(chars)
    return res

def renderAll(worldState):
    worldState.renderableprops.append(filterProps(worldState.propcoords, worldState.screen_x, worldState.screen_y, worldState.width, worldState.height)) ###filter which props from propcoords get rendered, add them to list renderableprops
    render_y(worldState.screen_y, worldState.screen_x, worldState.height, worldState. width, worldState.naytto) ###adds the part of the map which will be rendered to a list called naytto so replace() can put the props in

    ###go through every filtered prop (=every prop that is rendered) and replace every character with the props character. If no props are going to be rendered, continue to the next step
    if len(worldState.renderableprops) != 0:
        for i in worldState.renderableprops:
            rivinumero = i.y
            x = i.x
            kirjain = i.character
            rivi = worldState.naytto[rivinumero]
            worldState.naytto[rivinumero] = replace(rivi, x, kirjain)
    else:
        pass
    
#    replace()

    ###print every item in naytto
    for i in range(len(worldState.naytto)):
        print(worldState.naytto[i])



###EVERY CLASS START


class WorldState:
    '''Holds everything together'''
    screen_x = 0
    screen_y = 2
    width = 9 
    height = 7

    naytto = []
    #every props coordinates
    propcoords = []
    #every props coordinates inside the screen (so every prop that is going to be rendered)
    renderableprops = []

    def loadMap():
        kartta = []
        # load kartta 
        return kartta


    def loadProps(self):
        #the fuck is this shit, just replace this function when you like with something that reads props and their coordinates from a .txt or a .json
        props = []
        #load props
        enemy1 = enemy("E", 4, 10, 2, 4, 1, "none", 2, 4)
        props.append(enemy1)
        for i in props:
            self.propcoords.append(i)
    
    
    def loadPlayer(self):
        player = hero("@", 3, 20, 4, 3, 1, "none")
        self.renderableprops.append(player)


    def init(self):
        self.loadProps()
#        kartta = self.loadMap()        
        logging.info('world initialized')


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


###EVERY CLASS START


def main():
    worldState = WorldState()
    worldState.init()

    renderAll(worldState)

if __name__ == "__main__":
    main()