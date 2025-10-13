# from gamemodel import *
# from graphics import *


# # Skapa fönstret (600x400 pixlar)
# win = GraphWin("Testfönster", 600, 400)

# # Skapa en rektangel
# rect = Rectangle(Point(100, 300), Point(200, 200))  # två hörnpunkter
# rect.setFill("blue")   # färg
# rect.draw(win)         # ritas i fönstret

# # Vänta på musklick innan rutan stängs
# win.getMouse()
# win.close()

from graphics import GraphWin, Point, Rectangle

win = GraphWin("Testfönster", 600, 400)
rect = Rectangle(Point(100,300), Point(200,200))
rect.draw(win)
win.getMouse()
win.close()