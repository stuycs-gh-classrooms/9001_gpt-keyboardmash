from PIL import Image

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        # Set the color of the pixel at (x, y) to the given color
        self.pixels[y][x] = color

    def get_pixel(self, x, y):
        # Get the color of the pixel at (x, y)
        return self.pixels[y][x]

    def save_image(self, filename):
        # Save the canvas as an image file
        img = Image.new('RGB', (self.width, self.height), 'white')
        pixels = img.load()
        for y in range(self.height):
            for x in range(self.width):
                pixels[x, y] = self.pixels[y][x]
        img.save(filename)

    def display_image(self):
        # Display the canvas as an image
        img = Image.new('RGB', (self.width, self.height), 'white')
        pixels = img.load()
        for y in range(self.height):
            for x in range(self.width):
                pixels[x, y] = self.pixels[y][x]
        img.show()
