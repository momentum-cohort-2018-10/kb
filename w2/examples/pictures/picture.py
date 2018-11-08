from PIL import Image
import random


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height))

    def save(self, filename):
        self.image.save(filename)

    def draw_point(self, coords, color):
        self.image.putpixel(coords, color)

    def scramble(self):
        for x in range(self.width):
            for y in range(self.height):
                self.draw_point(
                    (x, y), (random.randint(0, 255), random.randint(0, 255),
                             random.randint(0, 255)))


def canvas_from_file(filename):
    with open(filename) as file:
        line = file.readline().strip()
        coords = line.split(" ")
        coords = [int(x) for x in coords]

    return Canvas(coords[0], coords[1])


if __name__ == "__main__":
    canvas = canvas_from_file("image.txt")
    canvas.scramble()
    canvas.save("test.png")
