from canvas import Canvas
from draw import *

canvas = Canvas(400, 400)

# Draw head
draw_circle(200, 200, 150, (170, 120, 80), canvas)
draw_circle(150, 150, 50, (170, 120, 80), canvas)
draw_circle(250, 150, 50, (170, 120, 80), canvas)

# Draw ears
draw_circle(130, 110, 30, (170, 120, 80), canvas)
draw_circle(270, 110, 30, (170, 120, 80), canvas)

# Draw eyes
draw_circle(175, 175, 20, (255, 255, 255), canvas)
draw_circle(225, 175, 20, (255, 255, 255), canvas)
draw_circle(175, 175, 10, (0, 0, 0), canvas)
draw_circle(225, 175, 10, (0, 0, 0), canvas)

# Draw nose
draw_circle(200, 250, 20, (0, 0, 0), canvas)

# Draw mouth
bezier_curve(150, 300, 200, 320, 200, 320, 250, 300, (0, 0, 0), canvas)

canvas.display_image()
