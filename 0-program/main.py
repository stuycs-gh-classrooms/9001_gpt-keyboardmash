from canvas import Canvas
from draw import draw_line

# Create a canvas with a width of 200 and a height of 100
canvas = Canvas(200, 100)

# Draw a line from (10, 10) to (100, 50) in red color
draw_line(10, 10, 100, 50, (255, 0, 0), canvas)

# Display the canvas as an image
canvas.display_image()
