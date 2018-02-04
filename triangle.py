def triangle():
    print('  .  ');
    print(' ... ');
    print('.....');

def drawTriangle3():
    tranglesToDraw = int(input("enter triangle count to draw:"))
    for myTriangles in range(tranglesToDraw):
        triangle()
    

drawTriangle3()

