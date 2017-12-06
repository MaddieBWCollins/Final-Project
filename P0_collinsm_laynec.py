######################################################################
# Author: Cameron Layne and Maddie Collins
# Username: laynec and collinsm
#
# Assignment: P0
#
######################################################################
import random
import turtle

class Shapes:


    def __init__(self, prim, secon, col):
        """
         Initialize a shape with random kaleidoscopic qualities.
        :param prim: This was originally 's' in the previous code. It is the primary number in out algorithm. It is user input.
        :param secon: Also used to be a part of 's'. It is the secondary number to make the shapes. Also user input.
        :param col: Sets the color of the shape. User can pick a color or it can be random.
        :param coord: Sets the coordinates of the shape.
        """

        self.prim = prim
        self.secon = secon
        self.col = col
        # self.coord = coord

    def draw_random(self, prim, secon, col):
        turt = turtle.Turtle()
        wn = turtle.Screen()
        wn.setup (width=1400, height=700, startx=0, starty=0)

        """
        Draws a randomly colored shape using the turtle library

        :param turt: a turtle object to draw with
        :return: None
        """
        if self.col == str("random"):
            wn.colormode(255)
            self.col = ((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))    # gives the turtle a random color
            turt.pencolor((self.col))
        else:
            turt.pencolor(self.col)

        while True:

            for num in range(10):
                if prim == "random":
                    p = random.randint(3,10)
                else:
                    p = int(prim)
                if secon == "random":
                    s = random.randint(3,10)
                else:
                    s = int(secon)
                turt.penup()
            # Move the turtle to a random place on the screen
                turt.goto(random.randint(-650, 650), random.randint(-300, 300))
                turt.pendown()
                for num in range(p):
                    turt.forward(50)
                    turt.left(360/p)           # the angle ensures a perfect hexagon

                    for num in range (s//2):
                        turt.forward(25)
                        turt.left(360//p)
        wn.exitonclick()


def main():

    prim = (input("Pick a number between 3 and 10, or type 'random'. "))
    secon = (input("Pick a second number between 3 and 10, or type 'random'. "))
    col = str(input("Pick a color, or type 'random'. "))
    Shape = Shapes(prim, secon, col)

    Shape.draw_random(prim, secon, col)

if __name__ == "__main__":
    main()
