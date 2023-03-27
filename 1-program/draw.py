import math

def draw_line(x1, y1, x2, y2, color, canvas):
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        sx = 1
    else:
        sx = -1
    if y1 < y2:
        sy = 1
    else:
        sy = -1
    err = dx - dy
    while True:
        canvas.set_pixel(x1, y1, color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy


def draw_circle(center_x, center_y, radius, color, canvas):
    """
    Draws a circle on the canvas with the given center point, radius, and color.

    Args:
        center_x (int): The x-coordinate of the center of the circle.
        center_y (int): The y-coordinate of the center of the circle.
        radius (int): The radius of the circle.
        color (tuple): A tuple of three integers (r, g, b) representing the color of the circle.
        canvas (Canvas): The canvas object to draw the circle on.
    """
    x = radius
    y = 0
    err = 0

    while x >= y:
        canvas.set_pixel(center_x + x, center_y + y, color)
        canvas.set_pixel(center_x + y, center_y + x, color)
        canvas.set_pixel(center_x - y, center_y + x, color)
        canvas.set_pixel(center_x - x, center_y + y, color)
        canvas.set_pixel(center_x - x, center_y - y, color)
        canvas.set_pixel(center_x - y, center_y - x, color)
        canvas.set_pixel(center_x + y, center_y - x, color)
        canvas.set_pixel(center_x + x, center_y - y, color)

        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x

def bezier_curve(x0, y0, x1, y1, x2, y2, x3, y3, color, canvas, num_points=100):
    for i in range(num_points):
        t = i / num_points
        x = (1-t)**3 * x0 + 3*(1-t)**2 * t * x1 + 3*(1-t) * t**2 * x2 + t**3 * x3
        y = (1-t)**3 * y0 + 3*(1-t)**2 * t * y1 + 3*(1-t) * t**2 * y2 + t**3 * y3
        canvas.set_pixel(int(x), int(y), color)

def hermite_curve(x0, y0, x1, y1, rx0, ry0, rx1, ry1, color, canvas, num_points=100):
    for i in range(num_points):
        t = i / num_points
        h00 = 2*t**3 - 3*t**2 + 1
        h10 = t**3 - 2*t**2 + t
        h01 = -2*t**3 + 3*t**2
        h11 = t**3 - t**2
        x = h00*x0 + h10*rx0 + h01*x1 + h11*rx1
        y = h00*y0 + h10*ry0 + h01*y1 + h11*ry1
        canvas.set_pixel(int(x), int(y), color)



def draw_ellipse(xc, yc, a, b, color, canvas):
    # Step 1: Compute the values of cos and sin for each degree
    cos_values = [math.cos(math.radians(angle)) for angle in range(360)]
    sin_values = [math.sin(math.radians(angle)) for angle in range(360)]

    # Step 2: Compute the x and y coordinates of the ellipse points
    points = []
    for i in range(360):
        x = xc + int(a * cos_values[i])
        y = yc + int(b * sin_values[i])
        points.append((x, y))

    # Step 3: Draw lines between the points
    for i in range(len(points) - 1):
        draw_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], color, canvas)
    draw_line(points[-1][0], points[-1][1], points[0][0], points[0][1], color, canvas)