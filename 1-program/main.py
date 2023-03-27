from canvas import Canvas
from draw import draw_line, draw_circle, bezier_curve, hermite_curve

# Create a new canvas with a width and height of 500 pixels
canvas = Canvas(500, 500)

# Draw a red line from (10, 10) to (100, 50)
draw_line(10, 10, 100, 50, (255, 0, 0), canvas)

# Draw a blue circle with a radius of 50 pixels centered at (250, 250)
draw_circle(250, 250, 50, (0, 0, 255), canvas)

# Draw a green Bezier curve with control points at (50, 400), (200, 50), (300, 450), and (450, 100)
bezier_curve(50, 400, 200, 50, 300, 450, 450, 100, (0, 255, 0), canvas, num_points=1000)

hermite_curve(50, 50, 400, 400, 200, 50, 300, 450, (128, 0, 128), canvas, num_points=1000)

# Display the image on the screen
canvas.display_image()

# Save the image to a file
canvas.save_image("image.png")
