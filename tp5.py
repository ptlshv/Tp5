"""
shivank patel
407
tp5 dessiner image
 """

import arcade
import arcade.draw.circle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "PAYSAGE"


def sol():

    arcade.draw.draw_lrbt_rectangle_filled(
        0,
        SCREEN_WIDTH,
        0,
        SCREEN_HEIGHT / 3.5,
        arcade.csscolor.DARK_GREEN)


y = SCREEN_HEIGHT / 2 + 40


def soleil():
    arcade.draw.draw_arc_filled(400, 150, 900, 800, arcade.color.BURNT_ORANGE, 0, 180,)


def chaine_carcatere():
    affichage = arcade.Text("shivank > picasso", 20, SCREEN_HEIGHT - 40, arcade.color.BLACK)
    affichage.draw()


def montagne():
    arcade.draw.draw_triangle_filled(-100, y - 190, -50, y + 100, 60, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(-10, y - 190, 100, y + 60, 200, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(100, y - 190, 250, y + 90, 400, y - 190, arcade.color.DAVY_GREY)

    arcade.draw.draw_triangle_filled(300, y - 190, 500, y + 20, 700, y - 190, arcade.color.DAVY_GREY)

    points = [(640, y - 190), (775, y + 60), (950, y - 190)]
    arcade.draw.draw_polygon_filled(points, arcade.color.DAVY_GREY)


def riviere():
    arcade.draw.circle.draw_ellipse_filled(430, y - 205, 250, 130, arcade.color.SEA_BLUE)

    arcade.draw.circle.draw_ellipse_filled(370, y - 270, 300, 130, arcade.color.SEA_BLUE)

    arcade.draw.circle.draw_ellipse_filled(300, y - 315, 270, 130, arcade.color.SEA_BLUE)


def arbre():
    arcade.draw.draw_lrbt_rectangle_filled(70, 120, 120, 200, arcade.color.DARK_BROWN)

    arcade.draw_circle_filled(95, 240, 60, arcade.color.FOREST_GREEN)

    arcade.draw.draw_lrbt_rectangle_filled(680, 730, 120, 200, arcade.color.DARK_BROWN)

    arcade.draw_circle_filled(705, 240, 60, arcade.color.FOREST_GREEN)

    arcade.draw_line(75, 120, 75, 180, arcade.color.GOLDEN_BROWN, 1.3)

    arcade.draw_line(115, 120, 115, 180, arcade.color.GOLDEN_BROWN, 1.3)

    arcade.draw_line(95, 120, 95, 180, arcade.color.GOLDEN_BROWN, 1.3)

    arcade.draw_line(685, 120, 685, 180, arcade.color.GOLDEN_BROWN, 1.3)

    arcade.draw_line(725, 120, 725, 180, arcade.color.GOLDEN_BROWN, 1.3)

    arcade.draw_line(705, 120, 705, 180, arcade.color.GOLDEN_BROWN, 1.3)


def pomme():

    arcade.draw.draw_point(81, 290, arcade.color.MEDIUM_CANDY_APPLE_RED, 10)
    arcade.draw.draw_point(115, 262, arcade.color.MEDIUM_CANDY_APPLE_RED, 5)
    arcade.draw.draw_point(50, 253, arcade.color.MEDIUM_CANDY_APPLE_RED, 8)
    arcade.draw.draw_point(120, 210, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(70, 200, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(80, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(130, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(680, 200, arcade.color.MEDIUM_CANDY_APPLE_RED, 8)
    arcade.draw.draw_point(725, 290, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(686, 268, arcade.color.MEDIUM_CANDY_APPLE_RED, 10)
    arcade.draw.draw_point(730, 195, arcade.color.MEDIUM_CANDY_APPLE_RED, 6)
    arcade.draw.draw_point(750, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 9)
    arcade.draw.draw_point(690, 235, arcade.color.MEDIUM_CANDY_APPLE_RED, 7)
    arcade.draw.draw_point(660, 240, arcade.color.MEDIUM_CANDY_APPLE_RED, 6)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.OU_CRIMSON_RED)


arcade.start_render()

soleil()
sol()
riviere()
montagne()
arbre()
pomme()
chaine_carcatere()


arcade.finish_render()


arcade.run()
