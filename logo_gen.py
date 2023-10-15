#!./venv/bin/python
import os
import cairosvg
from PIL import Image

def main():
    HEIGHT, WIDTH = 200, 200 

    colors = {
    "white": "#fff", 
    "black": "#000"
    }

    for colorname, colorhex in colors.items():

        br = HEIGHT / 3
        sr = br / 2.5
        bcx, bcy = WIDTH/2, (HEIGHT/2) + (sr)

        scx, scy = (bcx + br - sr), (bcy - br + sr - (sr*2))

        start = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{HEIGHT}" width="{WIDTH}">"""

        sc = f"""<circle cx="{scx}" cy="{scy}" r="{sr}" fill="{colorhex}" />"""
        bc = f"""<circle cx="{bcx}" cy="{bcy}" r="{br}" fill="{colorhex}" />"""

        middle = sc + bc

        end = "</svg>"

        svg_logo_basename = f"logo-{colorname}.svg"
        logo_folder = "static/logo"
        svg_logo_path = os.path.join(logo_folder, svg_logo_basename)
        with open(svg_logo_path, "w") as f:
            f.write(f"{start}\n{middle}\n{end}")
    
    # Output PNG file path
    png_logo_basename = "logo.png"
    png_logo_path = os.path.join(logo_folder, png_logo_basename)
    # Convert SVG to PNG
    cairosvg.svg2png(url=svg_logo_path, write_to=png_logo_path)

    # save to ico
    ico_basename = "favicon.ico"
    ico_path = os.path.join(logo_folder, ico_basename)
    png_image = Image.open(png_logo_path)
    png_image.save(ico_path, sizes=[(16, 16)])

if __name__ == "__main__":
    main()