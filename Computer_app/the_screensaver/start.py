import sys
sys.path.append('.')
from turtle import *
from Computer_app.about_computer.size_of_screen import know_the_size_of_screen
import time

name = know_the_size_of_screen()['name']
width = know_the_size_of_screen()['width']
height = know_the_size_of_screen()['height']

width_of_app = width - 1440
height_of_app = height - 600

class StartOfApp:

    def hide_turtle():
        hideturtle()

        
    def create_window() -> None:
        Screen().setup(width_of_app, height_of_app)


    def earth() -> None:
        pass


    def sun() -> None:
        pass


    def moon() -> None:
        pass


    def horizonte(height) -> None:
        penup()
        backward(width // 2)
        # setheading(0)
        pendown()
        forward(width)


    def sky(self) -> None:
        pass


    def tree(self) -> None:
        pass

    def stop() -> None:
        time.sleep(3)
        # exitonclick()
        # bye()

paint = StartOfApp
paint.horizonte((height_of_app) // 2)
paint.stop()