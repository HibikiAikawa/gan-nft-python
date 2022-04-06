import svgwrite
import numpy as np


def createSvg(pixels, output_file, width=16, height=16):
    w = width
    h = height
    pixels = pixels
    pixels_len = len(pixels)

    pixel_size = 16
    dwg = svgwrite.Drawing(output_file, size=(w * pixel_size, h * pixel_size))

    for y in range(h):
        start = y * w
        row = pixels[start:start+w]
        for x,p in enumerate(row):
            fill = f'rgb({p[0]},{p[1]},{p[2]})'
            dwg.add(dwg.rect(insert=(x * pixel_size, y * pixel_size), size=(pixel_size, pixel_size), fill=fill))
    
    center = pixel_size * w // 2
    dwg.add(dwg.text('Unchain', insert=(center, center)))
    dwg.save()


if __name__ == '__main__':
    createSvg()
