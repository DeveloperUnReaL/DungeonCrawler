#!/usr/bin/env python3

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

player_x = 4
player_y = 4
screen_x = 1
screen_y = 1
width = 9 
height = 7

actions = ["attack", "defend", "move", "open chest", "open inventory", "flee", "heal", "eat", "potion"]



def filterLocations(inputList, x0, y0, w, h):
    outlist = []
    logging.info('filtering for area x0, y0 to x1, y1')
    logging.info('%s, %s to %s, %s', x0, y0, x0+w, y0+h)
    for i in inputList:
        if i['x'] < x0 or i['x'] > (x0+w):
            continue
        if i['y'] < y0 or i['y'] > (y0+h):
            continue
        outlist.append(i)
        logging.info('match x=%s y=%s', i['x'], i['y'] )
    return outlist

def playerAction():
    print("Type your action:")
    answer = input()
    print(answer)

def render_x(m, x, w):
    return m[x:x+w]

def render_y(screen_y, height):
    y_pos = screen_y + 1
    with open("TestC.txt", "r") as a:
        for i in range(0, height):
            row = str((a.readlines(y_pos)))
            row = row.replace("[","").replace("]","").replace("'","").replace("n","")
            w = width
            print(render_x(row, screen_x, w))
            y_pos = y_pos + 1

def mainRender():
    render_y(screen_y, height)
    playerAction()

def testFiltering():
    e1 = {
        'v' : 'D',  # visual
        'x' : 2,  # x-coord
        'y' : 4   # y-coord
    }
    e2 = {
        'v' : 'L',  # visual
        'x' : 7,  # x-coord
        'y' : 8   # y-coord
    }
    vihollislista = []
    vihollislista.append(e1)
    vihollislista.append(e2)

    printtilista = filterLocations(vihollislista, 1, 2, 3, 3)
    logging.info('printtilista len:%s :\n %s', len(printtilista), printtilista)

    printtilista = filterLocations(vihollislista, 0, 0, 10, 10)
    logging.info('printtilista len:%s :\n %s', len(printtilista), printtilista)

def main():
    testFiltering()
    mainRender()


if __name__ == "__main__":
    main()
