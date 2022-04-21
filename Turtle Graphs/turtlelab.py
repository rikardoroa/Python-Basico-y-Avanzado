#script by rikardoroa
#just python it!!
import turtle


class turtle_drawning:
    turtle_ = turtle

    def _init__(self, turtle_=turtle):
        self.turtle_ = turtle_


    def draw_phrase_(self):
        # turtle pencil
        self.turtle_.speed("fast")
        self.turtle_.width(16)
        self.turtle_.pensize(5)
        self.turtle_.color("red")

        # positions for letters E
        pos_ = [-325, 280]
        for item in pos_:
            self.turtle_.penup()
            self.turtle_.setpos(item, 0)
            self.turtle_.pendown()

            for i in range(1):

                self.turtle_.forward(85)
                self.turtle_.backward(85)
                self.turtle_.right(90)
                self.turtle_.forward(85)
                self.turtle_.right(-90)
                self.turtle_.forward(85)
                self.turtle_.backward(85)
                self.turtle_.right(-90)
                self.turtle_.forward(42.5)
                self.turtle_.right(90)
                self.turtle_.forward(85)

        #position for letter T
        self.turtle_.penup()
        self.turtle_.setpos(-425, 0)
        self.turtle_.pendown()
        self.turtle_.forward(85)
        self.turtle_.backward(42.4)
        self.turtle_.right(90)
        self.turtle_.forward(85)


        #position for letter O
        self.turtle_.penup()
        self.turtle_.setpos(15, -43)
        self.turtle_.pendown()
        self.turtle_.circle(45)


        # position for letter R
        self.turtle_.penup()
        self.turtle_.setpos(400, 0)
        self.turtle_.pendown()
        self.turtle_.right(0)
        self.turtle_.forward(85)
        self.turtle_.backward(85)
        self.turtle_.right(-90)
        self.turtle_.forward(85)
        self.turtle_.circle(-20, 130, 90)
        self.turtle_.right(50)
        self.turtle_.forward(100)
        self.turtle_.right(25)
        self.turtle_.backward(115)

        # position for letter C
        self.turtle_.penup()
        self.turtle_.setpos(590, 0)
        self.turtle_.pendown()
        self.turtle_.circle(48, 250)

        # position for letter M
        self.turtle_.penup()
        self.turtle_.setpos(-65, 0)
        self.turtle_.pendown()
        self.turtle_.right(135)
        self.turtle_.forward(85)
        self.turtle_.backward(85)
        self.turtle_.right(-45)
        self.turtle_.forward(35)
        self.turtle_.right(-90)
        self.turtle_.forward(35)
        self.turtle_.right(-45)
        self.turtle_.backward(85)

        #calling the function
        self.draw_coord()
        # finish draw
        self.turtle_.done()


    def draw_coord(self):

        # turtle pencil
        # self.turtle_.speed("fast")
        self.turtle_.width(16)
        self.turtle_.pensize(5)
        self.turtle_.color("red")

        #drawning letter A
        pos_ = [180, -180]
        angle_ = [180, -90]

        for index, item in enumerate(zip(pos_, angle_)):
            self.turtle_.penup()
            self.turtle_.setpos(pos_[index], -40)
            self.turtle_.pendown()
            self.turtle_.right(angle_[index])
            self.turtle_.backward(85 - 42.5)
            self.turtle_.forward(85)
            self.turtle_.backward(42.5)
            self.turtle_.right(-90)
            self.turtle_.forward(85)
            self.turtle_.right(90)
            self.turtle_.forward(85 - 42.5)
            self.turtle_.backward(85)
            self.turtle_.right(90)
            self.turtle_.forward(85)


if __name__ == "__main__":
    drawning = turtle_drawning()
    drawning.draw_phrase_()
