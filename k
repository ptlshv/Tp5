"""
shivank patel
407
tp5 dessiner image
 """

import arcade
import arcade.draw.circle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.OU_CRIMSON_RED)


arcade.start_render()

def sol(self):

    arcade.draw.draw_lrbt_rectangle_filled(
        0,
        SCREEN_WIDTH,
        0,
        SCREEN_HEIGHT / 3.5,
        arcade.csscolor.DARK_GREEN)
y = SCREEN_HEIGHT / 2 + 40



def soleil(self):
    arcade.draw.draw_arc_filled(400, 150, 900, 800, arcade.color.BURNT_ORANGE, 0, 180,)

def montagne(self):
    arcade.draw.draw_triangle_filled(-100, y - 190,-50, y + 100, 60, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(-10, y - 190,100, y + 60, 200, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(100, y - 190, 250, y + 90, 400, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(300, y - 190, 500, y + 20, 700, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(640, y - 190, 775, y + 60, 950, y - 190, arcade.color.DAVY_GREY)

def riviere(self):
    arcade.draw.circle.draw_ellipse_filled(430, y - 205, 250, 130, arcade.color.SEA_BLUE )

    arcade.draw.circle.draw_ellipse_filled(370, y - 270, 300, 130, arcade.color.SEA_BLUE )

    arcade.draw.circle.draw_ellipse_filled(300, y - 315, 270, 130, arcade.color.SEA_BLUE )


def arbre(self):
    arcade.draw.draw_lrbt_rectangle_filled(70, 120, 120, 200, arcade.color.DARK_BROWN)

    arcade.draw_circle_filled(95, 240, 60, arcade.color.FOREST_GREEN)

    arcade.draw.draw_lrbt_rectangle_filled(680, 730, 120, 200, arcade.color.DARK_BROWN)

    arcade.draw_circle_filled(705, 240, 60, arcade.color.FOREST_GREEN)

def pomme(self):

    arcade.draw.draw_point(81, 290, arcade.color.MEDIUM_CANDY_APPLE_RED, 10)

    arcade.draw.draw_point(115, 262, arcade.color.MEDIUM_CANDY_APPLE_RED, 5)

    arcade.draw.draw_point(50, 253, arcade.color.MEDIUM_CANDY_APPLE_RED, 8)

    arcade.draw.draw_point(120, 210, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)

    arcade.draw.draw_point(70, 200, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)

    arcade.draw.draw_point(80, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)

    arcade.draw.draw_point(130, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)


arcade.finish_render()



arcade.run()