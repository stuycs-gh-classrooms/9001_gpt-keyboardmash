from canvas import Canvas
from draw import *

# create canvas
canvas = Canvas(800, 800)

# draw head
draw_ellipse(400, 400, 200, 250, (100, 100, 100), canvas)

# draw eyes
draw_circle(320, 350, 30, (255, 255, 255), canvas)
draw_circle(480, 350, 30, (255, 255, 255), canvas)
draw_circle(320, 350, 15, (0, 0, 0), canvas)
draw_circle(480, 350, 15, (0, 0, 0), canvas)

# draw nose
draw_circle(400, 450, 20, (255, 0, 0), canvas)

# draw mouth
bezier_curve(320, 500, 400, 550, 400, 550, 480, 500, (200, 0, 0), canvas)

# draw ears
draw_circle(260, 270, 60, (100, 100, 100), canvas)
draw_circle(540, 270, 60, (100, 100, 100), canvas)

# draw inner ears
draw_circle(260, 270, 30, (200, 200, 200), canvas)
draw_circle(540, 270, 30, (200, 200, 200), canvas)

# draw whiskers
whisker_length = 100
whisker_angle = 30

# left whiskers
whisker_direction = (-1, -1)
draw_line(380, 450, 380 + whisker_direction[0] * whisker_length, 450 + whisker_direction[1] * whisker_length, (0, 0, 0), canvas) # middle
draw_line(380, 450, 380 + whisker_direction[0] * whisker_length * 0.8, 450 + whisker_direction[1] * whisker_length, (0, 0, 0), canvas) # top
draw_line(380, 450, 380 + whisker_direction[0] * whisker_length * 0.8, 450, (0, 0, 0), canvas) # bottom

# right whiskers
whisker_direction = (1, -1)
draw_line(420, 450, 420 + whisker_direction[0] * whisker_length, 450 + whisker_direction[1] * whisker_length, (0, 0, 0), canvas) # middle
draw_line(420, 450, 420 + whisker_direction[0] * whisker_length * 0.8, 450 + whisker_direction[1] * whisker_length, (0, 0, 0), canvas) # top
draw_line(420, 450, 420 + whisker_direction[0] * whisker_length * 0.8, 450, (0, 0, 0), canvas) # bottom

# display image
canvas.display_image()
