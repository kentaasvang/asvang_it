#!/usr/bin/python3

def main():
    HEIGHT, WIDTH = 200, 200 
    color = "#fff"

    br = HEIGHT / 3
    sr = br / 2.5
    bcx, bcy = WIDTH/2, (HEIGHT/2) + (sr)

    scx, scy = (bcx + br - sr), (bcy - br + sr - (sr*2))

    start = f"""<svg xmlns="http://www.w3.org/2000/svg" height="{HEIGHT}" width="{WIDTH}">"""

    sc = f"""<circle cx="{scx}" cy="{scy}" r="{sr}" fill="{color}" />"""
    bc = f"""<circle cx="{bcx}" cy="{bcy}" r="{br}" fill="{color}" />"""

    middle = sc + bc

    end = "</svg>"

    with open("static/logo/logo.svg", "w") as f:
        f.write(f"{start}\n{middle}\n{end}")

if __name__ == "__main__":
    main()