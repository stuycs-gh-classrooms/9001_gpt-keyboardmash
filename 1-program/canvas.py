from PIL import Image

class Canvas:
    def __init__(self, width, height, background_color=(200, 200, 200)):
        self.width = width
        self.height = height
        self.pixels = [[background_color for _ in range(height)] for _ in range(width)]

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
