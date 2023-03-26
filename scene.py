# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from tracemalloc import start
from draw2d import \
    start_drawing, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, 0, scene_height)
    draw_cloud(canvas, 150, 400)
    draw_cloud(canvas, 500, 375)
    draw_ground(canvas, scene_width, scene_height)

    # Draw birds
    draw_bird(canvas, 20, 300)
    draw_bird(canvas, 100, 330)
    draw_bird(canvas, 200, 350)
    draw_bird(canvas, 300, 300)
    draw_bird(canvas, 400, 350)
    draw_bird(canvas, 500, 300)
    draw_bird(canvas, 600, 350)
    draw_bird(canvas, 650, 250)
    draw_bird(canvas, 700, 325)
    draw_bird(canvas, 450, 200)

    # Draw trees
    draw_pine_tree(canvas, 200, 300)
    draw_pine_tree(canvas, 100, 250)
    draw_pine_tree(canvas, 300, 275)

    # Draw the lake
    draw_lake(canvas, scene_width, scene_height)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky."""
    draw_rectangle(canvas, 0, scene_height / 4,
        scene_width, scene_height, width=0, fill="sky blue")


def draw_sun(canvas, startX, startY):
    """Draw the sun at location startX and startY."""
    draw_oval(canvas, startX, startY, startX + 100, startY - 100, width=7, outline="yellow2", fill="yellow1")


def draw_cloud(canvas, startX, startY):
    """Draw one cloud at location startX and startY."""
    draw_oval(canvas, startX, startY + 75, startX + 150, startY, width=8, outline="white", fill="snow1")
    draw_oval(canvas, startX + 100, startY + 75, startX + 250, startY, width=8, outline="white", fill="snow1")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground."""
    draw_rectangle(canvas, 0, 0,
    scene_width, scene_height / 4, width=0, fill="burlywood4")

def draw_bird(canvas, startX, startY):
    """Draw a bird at location startX and startY."""

    # Draw two arcs to create a bird.
    draw_arc(canvas, startX, startY, startX + 20, startY + 10, start=0)
    draw_arc(canvas, startX + 20, startY, startX + 40, startY + 10, start=90)


def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)"""

    # Compute the coordinates of the skirt and trunk.
    skirt_left = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210
    trunk_left = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
                   trunk_right, skirt_bottom, fill="brown")

    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
                 skirt_right, skirt_bottom, fill="forestGreen")

    
def draw_lake(canvas, x, y):
    """Draw the lake at location x and y."""
    
    # Compute the coordinates of the start point and end point of the lake.
    start_lake_x = x / 3 * 2
    start_lake_y = 0
    end_lake_x = x
    end_lake_y = y / 4
    draw_oval(canvas, start_lake_x, start_lake_y, end_lake_x, end_lake_y, width=8, outline="dodgerBlue2", fill="dodgerBlue1")

# Call the main function so that
# this program will start executing.

main()
