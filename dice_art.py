import PIL
from PIL import Image

#img = Image.open("C:/Users/stimo/Desktop/personalProjects/simon_dice_copy.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/harry.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/Lionel_Messi.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/nathan.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/uva_logo.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/rashford.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/isabelle.jpg")
#img = Image.open("C:/Users/stimo/Desktop/personalProjects/james-copy.jpg")

filepath = input("What is the file path for the image you would like to use? ")
filepath_is_valid = False

while not filepath_is_valid:
    try:
        img = Image.open(filepath)
        filepath_is_valid = True
    except FileNotFoundError:
        filepath = input("File not found. Enter filepath again: ")
    except OSError:
        filepath = input("Make sure your filepath is formatted correctly. Enter again: ")
    except:
        filepath = input("Please make sure the filepath is valid. Enter again: ")


die_w = 25
die_h = 25

die1 = Image.open("die1.jpg").resize((die_w, die_h))
die2 = Image.open("die2.jpg").resize((die_w, die_h))
die3 = Image.open("die3.jpg").resize((die_w, die_h))
die4 = Image.open("die4.jpg").resize((die_w, die_h))
die5 = Image.open("die5.jpg").resize((die_w, die_h))
die6 = Image.open("die6.jpg").resize((die_w, die_h))

image_width = img.width
image_height = img.height
image_ratio = image_width/image_height
#print("Image ratio: " + str(image_ratio))


d_width = int(input("How many dice wide would you like your image to be? "))
d_height = int(input("How many dice tall would you like your image to be? "))
input_ratio = d_width/d_height;
#print(input_ratio/image_ratio)

like_to_continue = False;
while not like_to_continue:
    while not (0.75 <= (input_ratio/image_ratio) <= 1/0.75):
        warning_input = input("Your dimensions may distort the image. Enter 'y' to continue or 'n' to enter new dimensions. ")
        while not (warning_input == 'y' or warning_input == 'n'):
            warning_input = input("Please enter 'y' or 'n' to answer the previous question.")
        if warning_input == 'y':
            like_to_continue = True
            input_ratio = 1
            image_ratio = 1
        elif warning_input == 'n':
            d_width = int(input("How many dice wide would you like your image to be? "))
            d_height = int(input("How many dice tall would you like your image to be? "))
            input_ratio = d_width/d_height
    else:
        like_to_continue = True


def map_to_die(x):
    if 0 <= x <= 255/6:
        return die1
    elif 255/6 < x <= 255/3:
        return die2
    elif 255/3 < x <= 255/2:
        return die3
    elif 255/2 < x <= 2*255/3:
        return die4
    elif 2*255/3 < x <= 5*255/6:
        return die5
    else:
        return die6

print("Generating image...")
img = img.resize((d_width, d_height))
brightnesses = []
for rows in range(d_height):
    brightnesses.append([])
pixels = img.load()

for i in range(d_height):
    for j in range (d_width):
        avg = (pixels[j, i][0] + pixels[j, i][1] + pixels[j, i][2])/3
        die_num = map_to_die(avg)
        brightnesses[i].append(die_num)


canvas = Image.new('RGB', (d_width*die_w, d_height*die_h))

for i in range(d_height):
    for j in range (d_width):
        canvas.paste(brightnesses[i][j], (j*die_w, i*die_h))

canvas = PIL.ImageOps.invert(canvas)
canvas.show()
