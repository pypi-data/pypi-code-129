import sys
from PyWireframe.engine import *

#Define some shapes
def cube(x, y, z, size):
    line(x, y, z, size, y, z)
    line(size, y, z, size, size, z)
    line(size, size, z, y, size, z)
    line(x, size, z, x, y, z)

    line(x, y, size, size, y, size)
    line(size, y, size, size, size, size)
    line(size, size, size, x, size, size)
    line(x, size, size, x, y, size)

    line(x, y, z, x, y, size)
    line(size, y, z, size, y, size)
    line(size, size, z, size, size, size)
    line(x, size, z, x, size, size)

def pyramid3 (x, y, z, size):
    line(x, y, z, size, y, z)
    line(x, y, z, size / 2, size, z)
    line(x, y, z, size / 2, y, size)

    line(size, y, z, size / 2, size, z)
    line(size, y, z, size / 2, y, size)

    line(size / 2, y, size, size / 2, size, z)

def pyramid4 (x, y, z, size):
    line(x, y, z, size, y, z)
    line(x, y, z, x, y, size)

    line(size, y, size, size, y, z)
    line(size, y, size, x, y, size)

    line(x, y, z, size / 2, size, size / 2)
    line(size, y, z, size / 2, size, size / 2)
    line(x, y, size, size / 2, size, size / 2)
    line(size, y, size, size / 2, size, size / 2)

def horizon(distance=3000,length=80000):
    line(-length/2,0,distance,length/2,0,distance)

def __move(event,axis,amount):
    name="<Key-%s>"%event.keysym
    #print(name,event)
    #cv.unbind(name)
    moveCamera(axis,amount)
    refresh()
    #debug()
    __bind()

def __bind():
    cv=getCanvas()
    cv.bind_all("<Key-Up>",lambda event:__move(event,'Z',15))
    cv.bind_all("<Key-Down>",lambda event:__move(event,'Z',-15))
    cv.bind_all("<Control-Key-Down>",lambda event:__move(event,'Y',-15))
    cv.bind_all("<Control-Key-Up>",lambda event:__move(event,'Y',15))
    cv.bind_all("<Key-Left>",lambda event:__move(event,'X',-15))
    cv.bind_all("<Key-Right>",lambda event:__move(event,'X',15))
    cv.bind_all("<Key-equal>",lambda event:setFocalLen(amount=5,_refresh=True))
    cv.bind_all("<Key-minus>",lambda event:setFocalLen(amount=-5,_refresh=True))

def main():
    start()
    mode(autoPrintPos=True)
    __bind()
    addObject(horizon,color='#bbbbbb')
    addObject(cube,0,0,0,100)
    addObject(pyramid4,100,100,100,160,color='green')
    addObject(ball,50,50,0,50,color='purple')
    refresh()
    turtle.mainloop()

if __name__=="__main__":main()