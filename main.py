from PIL import Image
import math

CHARS = {0: ' ', 1: '.', 2: '*', 3: ':', 4: ';', 5:'+',6: '$', 7: '#'}

img = Image.open("./images/cane_cucciolo.jpg")
image_rgb = img.convert("RGB")


class ImageElaborator:
  def __init__(self, img, image_rgb, size):
    self.img = img
    self.image_rgb = image_rgb
    self.imgX, self.imgY = size
    self.macropixel_amountX = 128

  def get_macro_pixels(self):
    self.side = math.floor(self.imgX / self.macropixel_amountX)
    self.macropixel_amountY = math.floor(self.imgY / self.side)
    list_chars = []
    for iy in range(self.macropixel_amountY):
      preY = iy * self.side
      list_charsX = []
      for ix in range(self.macropixel_amountX):
        preX = ix * self.side
        sum_macropixel = 0
        for y in range(self.side):
          for x in range(self.side):
            r, g, b = image_rgb.getpixel((x+ preX, y+preY))
            sum_macropixel += (r + g + b) / 3
        media_macropixel = sum_macropixel / (self.side * self.side)
        char = CHARS[round(media_macropixel * 7 / 255)]
        list_charsX.append(char)
      list_chars.append(list_charsX)
    return self.getPrintedImage(list_chars)


  @staticmethod
  def getPrintedImage(image: list[list[str]]):
    string = ''
    for y in image:
      for x in y:
        string += x
      string += '\n'
    return string

  @staticmethod
  def printTextImage(text):
    with open('./textImage.txt', 'w') as f:
      f.write(text)
      f.close()


  def start(self):
    self.finalImage = self.get_macro_pixels()
    print(self.finalImage)
    self.printTextImage(self.finalImage)


if __name__ == '__main__':
  img_elaborator = ImageElaborator(img, image_rgb, img.size)
  img_elaborator.start()