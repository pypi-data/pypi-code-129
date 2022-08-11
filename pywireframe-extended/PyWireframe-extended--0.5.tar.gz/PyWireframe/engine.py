import sys
try:
    import turtle
except ImportError:
    print("PyWireframe: Error importing modules. Make sure you have the Turtle module installed.")
    sys.exit()

#Define 3D Rendering Variables
global CameraX, CameraY, CameraZ, FocalLength, doPrint

FocalLength = 100
CameraX = 0
CameraY = 0
CameraZ = 0
Objects = []
_Dict={}
doPrint = True
drawing=False
fast=True
_curPos=(0,0,0)
autoPrintPos=False
_points=set()

def printMode(mode):
    global doPrint

    if mode == "on":
        doPrint = True
    elif mode == "off":
        doPrint = False
    else:
        print("'" + mode + "' is not a valid printMode value.")
    

def start():

    if doPrint == True:
        print("Starting PyWireframe")

    if doPrint == True:    
        print("Defining render")

    #Define render
    global render
    
    render=turtle.Turtle()
    render.speed(0)
    render.hideturtle()
    render.screen.title("PyWireframe")
    if doPrint == True:
        print("PyWireframe has started succesfully!")

#Redraw all predefined objects
def refresh():
    if fast:turtle.tracer(False)
        
    render.clear()

    for a in Objects:
        render.pencolor(a[1])
        try:
            exec(a[0],_Dict)
        except TypeError: # a is a function
            a()
        if fast:turtle.update()
    _points.clear()
    render.pencolor('black')
    turtle.tracer(True)

def exit():
    render.bye()

def __formatkw(kw):
    return ''.join("{}={},".format(key,kw[key]) for key in kw.keys())
def addObject(shape, *args, color='black', **kw):
    Objects.append(["{}({}{})".format(shape.__name__,
                                       ','.join(str(a) for a in args),
                                       ','+__formatkw(kw) if kw else ''),
                    color])
    if doPrint == True:
        print("Added object {} as object # {} color: {}" \
              .format(Objects[-1][0], str(len(Objects)),color))
    _Dict[shape.__name__]=shape

def addDynamicObject(function):
    if doPrint == True:
        print("Added '" + function + "' object as object #" + str(len(Objects)))
    Objects.append(function)

def deleteObject(value):
    Objects.pop(value)
    if doPrint == True:
        print("Deleted object #" + value)

def printObject(value):
    if doPrint == True:
        print(str(value) + ": " + str(Objects[value]))
    else:
        raise Exception("Cannot print object as printing is disabled.")
    

#Define some shapes
def cube(x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x + size, y, z, x + size, y + size, z)
    line(x + size, y + size, z, x, y + size, z)
    line(x, y + size, z, x, y, z)

    line(x, y, z + size, x + size, y, z + size)
    line(x + size, y, z + size, x + size, y + size, z + size)
    line(x + size, y + size, z + size, x, y + size, z + size)
    line(x, y + size, z + size, x, y, z + size)

    line(x, y, z, x, y, z + size)
    line(x + size, y, z, x + size, y, z + size)
    line(x + size, y + size, z, x + size, y + size, z + size)
    line(x, y + size, z, x, y + size, z + size)

def pyramid3 (x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x, y, z, x + size / 2, y + size, z)
    line(x, y, z, x + size / 2, y, z + size)

    line(x + size, y, z, x + size / 2, y + size, z)
    line(x + size, y, z, x + size / 2, y, z + size)

    line(x + size / 2, y, z + size, x + size / 2, y + size, z)

def pyramid4 (x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x, y, z, x, y, z + size)

    line(x + size, y, z + size, x + size, y, z)
    line(x + size, y, z + size, x, y, z + size)

    line(x, y, z, x + size / 2, y + size, z + size / 2)
    line(x + size, y, z, x + size / 2, y + size, z + size / 2)
    line(x, y, z + size, x + size / 2, y + size, z + size / 2)
    line(x + size, y, z + size, x + size / 2, y + size, z + size / 2)

#Renders a line in 3d space
def line(x1, y1, z1, x2, y2, z2, pos=False):
    global drawing, _curPos
    if drawing:
        return
    drawing=True

    _curPos=(x2,y2,z2)
    try:
        ScaleFactor = FocalLength/(z1 - CameraZ + FocalLength)
    except ZeroDivisionError:
        ScaleFactor = 0

    X = (x1 - CameraX) * ScaleFactor
    Y = (y1 - CameraY) * ScaleFactor

    render.goto(X, Y)
    render.pendown()

    try:
        ScaleFactor = FocalLength/(z2 - CameraZ + FocalLength)
    except ZeroDivisionError:
        ScaleFactor = 0

    if ScaleFactor > 0:
        X = (x2 - CameraX) * ScaleFactor
        Y = (y2 - CameraY) * ScaleFactor
        #print(X,Y,ScaleFactor)
        render.goto(X, Y)
        
        if pos or autoPrintPos:printPos()

    #print(ScaleFactor)
    render.penup()
    drawing=False

def ball(x,y,z,size,pos=False):
    # size: radius of the ball
    global _curPos
    _curPos = (x, y, z)

    try:
        ScaleFactor = FocalLength/(z - CameraZ + FocalLength)
    except ZeroDivisionError:
        ScaleFactor = 0
    if ScaleFactor > 0:
        X = (x - CameraX) * ScaleFactor
        Y = (y - CameraY) * ScaleFactor
        size *= ScaleFactor

        #render.penup()
        render.setheading(0)
        render.goto(X, Y - size)
        render.pendown()
        render.circle(size)
        render.penup()
        if pos or autoPrintPos:
            render.goto(X, Y)
            # center
            render.dot(3)
            printPos()

def text(arg,align='left',font=('Arial', 8, 'normal')):
    render.write(str(arg),align=align,font=font)


def printPos():
    # don't write down position repeatly
    if _curPos not in _points:
            text(_curPos)
            _points.add(_curPos)
    
def getPos():
    return _curPos

def moveCamera(axis, amount, _refresh=False):
    global CameraX
    global CameraY
    global CameraZ

    if axis == "X":
        CameraX += amount
    elif axis == "Y":
        CameraY += amount
    elif axis == "Z":
        CameraZ += amount
    else:
        raise Exception(axis +" is not a valid axis")

    if _refresh:refresh()

def setCameraPos(x=None,y=None,z=None, _refresh=False):
    global CameraX,CameraY,CameraZ
    if x:CameraX=x
    if y:CameraY=y
    if z:CameraZ=z
    if _refresh:refresh()

def setFocalLen(newFocalLen=None,amount=None,_refresh=False):
    global FocalLength
    if newFocalLen:FocalLength=newFocalLen
    elif amount:FocalLength+=amount
    if _refresh:refresh()

def reset():
    global CameraX, CameraY, CameraZ, FocalLength
    CameraX=CameraY=CameraZ=0
    FocalLength=0

def debug():
    print("CameraX = " + str(CameraX))
    print("CameraY = " + str(CameraY))
    print("CameraZ = " + str(CameraZ))
    print("FocalLength = " + str(FocalLength))
    print("objects: ")
    print(Objects)

def mode(*posarg, doPrint = doPrint, drawing=drawing, fast=fast,
         autoPrintPos=autoPrintPos):
    if posarg:raise TypeError("Keyword arguments only")
    globals().update(locals())
def getCanvas():
    return render.screen.getcanvas()
def getRender():
    return render