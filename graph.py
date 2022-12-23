import json
from PIL import Image, ImageDraw
import math
from math import sin

def main():
    json_file = open("graph.json")
    params = json.load(json_file)
    
    arr_y = []
    for x in range(params["x0"], params["xk"], params["xdelta"]):
        #y = math.sin(x / 3) * 100
        #y = x
        y = params["a1"] * sin(params["b1"] * x) +\
            params["a2"] * sin(params["b2"] * x) + \
            params["a3"] * sin(params["b3"] * x)
        arr_y.append((x * -1,y))

      
    #draw.line(shape, fill=0)
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for i in range(0,len(arr_y)):
        curr_x, curr_y = arr_y[i]
        # Determine x min and max
        if x_min > curr_x:
            x_min = curr_x
        if x_max < curr_x:
            x_max = curr_x
        # Determine y min and max
        if y_min > curr_y:
            y_min = curr_y
        if y_max < curr_y:
            y_max = curr_y

    x_sz = math.floor(math.fabs(x_min) + math.fabs(x_max))
    y_sz = math.floor(math.fabs(y_min) + math.fabs(y_max))

    img = Image.new("L",(x_sz,y_sz),"WHITE")
    draw = ImageDraw.Draw(img)

    for i in range(0,len(arr_y) - 1):
        i_next = i + 1
        x_1,y_1 = arr_y[i]
        x_1 = x_1 - x_min
        y_1 = y_1 - y_min
        x_2,y_2 = arr_y[i_next]
        x_2 = x_2 - x_min
        y_2 = y_2 - y_min
        draw.line([x_1,y_1,x_2,y_2],fill=0)

    img.show()    

    # for x in range(img.width // 2 * -1,img.width // 2):
    #     for y in range(img.height // 2 * -1,img.height // 2):
    #         xImg = x + (img.width // 2)
    #         xImg = xImg * -1
    #         yImg = y + (img.height // 2)
    #         yImg = yImg * -1

    #         if (x == 0):
    #              img.putpixel((xImg,yImg),0)
    #         if (y == 0):
    #             img.putpixel((xImg,yImg),0)


if __name__ == "__main__":
    main()