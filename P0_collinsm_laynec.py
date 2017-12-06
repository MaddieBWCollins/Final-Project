######################################################################
# Author: Cameron Layne and Maddie Collins
# Username: laynec and collinsm
#
# Assignment: P0
#
######################################################################
import random     #import modules
import turtle

class Shapes:


    def __init__(self, prim, secon, col):
        """
         Initialize a shape with random kaleidoscopic qualities.
        :param prim: This was originally 's' in the previous code. It is the primary number in out algorithm. It is user input.
        :param secon: Also used to be a part of 's'. It is the secondary number to make the shapes. Also user input.
        :param col: Sets the color of the shape. User can pick a color or it can be random.
        """

        self.prim = prim
        self.secon = secon
        self.col = col

    def draw_random(self, prim, secon, col):  #This function is what draws the shapes.
        turt = turtle.Turtle()
        wn = turtle.Screen()
        wn.setup (width=1400, height=700, startx=0, starty=0)
        wn.onclick(turt.goto)      #This lets the user interact live by moving the turtle to the clicked location.

        if self.col == str("random"):      #If user picks random, this allows for a random RGB color value to be selected.
            wn.colormode(255)
            self.col = ((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))    # gives the turtle a random color
            turt.pencolor((self.col))
        else:                            #Otherwise, the color is what the user selects.
            turt.pencolor(self.col)

        while True:                     #This allows the code to repeat indefinatly.

            for num in range(10):
                if prim == "random":             #If the user types random, a random integer is selected for the primary number.
                    p = random.randint(3,10)
                else:                            #Otherwise, their choice is used.
                    p = int(prim)
                if secon == "random":             #If the user types random, a random integer is selected for the secondary number.
                    s = random.randint(1,10)
                else:                            #Otherwise, their choice is used.
                    s = int(secon)
                turt.penup()
                turt.goto(random.randint(-650, 650), random.randint(-300, 300))    # Move the turtle to a random place on the screen
                turt.pendown()
                for num in range(p):
                    turt.forward(50)
                    turt.left(360/p)

                    for num in range (s//2):       #This is the magical kaleidoscope algorithim that makes the cool shapes;
                        turt.forward(25)           #honestly, we're not sure how it works. But it sure looks cool.
                        turt.left(360//p)
        wn.exitonclick()



def main():

    prim = (input("Pick a number between 3 and 10, or type 'random'. "))
    secon = (input("Pick a second number between 3 and 10, or type 'random'. "))          #Inputs to select the values.
    col = str(input("Pick a color, or type 'random'. "))
    Shape = Shapes(prim, secon, col)

    Shape.draw_random(prim, secon, col)                    #Call the function.

if __name__ == "__main__":
    main()
