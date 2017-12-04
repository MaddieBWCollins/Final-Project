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


    def __init__(self, prim, secon, col, coord):
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
        self.coord = coord

    def draw_random(self, prim, secon, col):
        turt = turtle.Turtle()
        wn = turtle.Screen()
        """
        Draws a randomly colored shape using the turtle library

        :param turt: a turtle object to draw with
        :return: None
        """

        turt.color = col

        for num in range(prim):
            turt.forward(50)
            turt.left(360/prim)           # the angle ensures a perfect hexagon

            for num in range (secon//2):
                turt.forward(25)
                turt.left(360//prim)
        wn.exitonclick()


def main():
    Shapes.prim = int(input("Pick a number between 3 and 10. "))
    Shapes.secon = int(input("Pick a second number between 3 and 10. "))
    Shapes.col = str(input("Pick a color, or type 'random'. "))
    if Shapes.col == str("random"):
        Shapes.col = ((random.random(), random.random(), random.random()))     # gives the turtle a random color
    else:
        pass
    Shapes.draw_random(Shapes.prim, Shapes.secon, Shapes.col)

if __name__ == "__main__":
    main()
