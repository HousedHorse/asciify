#! /usr/bin/python3
from PIL import Image, ImageDraw, ImageFont
import sys
import re
from colorama import Fore, Back, Style 
import time
from pathlib import Path

class Generator:
    def removeTransparency(img):
        canvas = Image.new('RGBA',img.size,(255,255,255,255))
        img = img.convert('RGBA')
        canvas.paste(img,mask=img)
        img = canvas
        return img

    def convertToGrayscale(img):
        img = img.convert('L')
        return img

    def resize(img,outw,outh):
        img.thumbnail((round(outw/2.5),outh))
        w = round(img.width*2.5)
        h = round(img.height)
        img = img.resize((w,h))
        return img

    def toChar(value):
        if value > 255: value = 255
        if value < 0: value = 0
        # list is from light to dark but must be read dark to light
        chars = [x for x in reversed([' ',' ','.',',',':',';','*','I','L','O','Q','B','M','#','#'])]
        key = round(value * (len(chars)-1) / 255)
        return chars[key]

    def openInput(name):
        # matches f extension
        match = re.search(r"\.([^\.]*)$",name)
        try:
            extension = match.group(1)
            # if we matched a lone dot
            if match.group(1) == '':
                # remove it
                name = name[:-1]
                raise
        except:
            extension = 'png'
            name += '.png'

        # read image or print an error
        try:
            f = Image.open(name)
            name = name.rstrip(f'.{extension}')
            extension = f'{extension}'
        except: error('Could not load file.')

        return f

    def generateASCII(imgName,outw=None,outh=None):
        info('Generating ASCII text...')
        if outw is None:
            outw = 128
        if outh is None:
            outh = outw

        info('Opening sourcefile...')
        img = Generator.openInput(imgName)

        info('Converting image to grayscale...')
        img = Generator.removeTransparency(img)
        img = Generator.convertToGrayscale(img)
        # resize the image to compensate for ascii being taller than it is wide
        info('Resizing image...')
        img = Generator.resize(img,outw,outh)
        # flattened array of grayscale values for each pixel
        data = img.getdata()
        w = img.width
        h = img.height
        # iterate through it and generate ascii
        info('Assigning ASCII to pixels...')
        s = ''
        for i,p in enumerate(data):
            load(i,len(data))
            s += Generator.toChar(p)
            if (i+1) % w == 0: s += '\n'
        flush()
        return s

    def generateASCIIImage(imgName,outw=None,outh=None,font=None):
        info('Generating ASCII image...')
        if outw is None:
            outw = 400
        if outh is None:
            outh = outw

        if outw >= 5000 or outh >= 5000:
            warn('You specified a pretty large maximum width or height. The resulting PNG will be quite large. If this was a mistake, press <CTRL-C> to cancel.')

        # load the font
        if font is None:
            #font = ImageFont.load_default()
            font = ImageFont.truetype(font=f'/usr/share/fonts/inconsolata.otf')

        # get ascii for the frame
        s = Generator.generateASCII(imgName,outw,outh)
        lines = s.splitlines()

        # figure out width and height of the image
        info('Gathering meta-data...')
        width,lineheight = font.getsize(lines[0])
        height = lineheight * len(lines)

        # draw the output
        info('Drawing image...')
        output = Image.new('RGB',(width,height), color=(255,255,255))
        d = ImageDraw.Draw(output)
        texty = 0
        for line in lines:
            load(texty,height)
            d.text((0,texty), line, font=font, fill=(0,0,0))
            texty += lineheight
        flush()

        filename = time.strftime("%m-%d-%Y_%H:%M:%S")
        filename = filename + ".png"
        info(f'Saving image as {filename}')
        output.save(filename)

    def generateASCIIGIF(gifName,outw=None,outh=None,font=None):
        info('Generating ASCII GIF (this may take some time)...')
        if outw is None:
            outw = 400
        if outh is None:
            outh = outw

        # load the font
        if font is None:
            font = ImageFont.load_default()

        # get ascii for the frame
        s = Generator.generateASCII(gifName,outw,outh)
        lines = s.splitlines()

        # figure out width and height of the image
        width = 0
        height = 0
        for line in lines:
            w,h = font.getsize(line)
            if w > width: width = w
            height += h

        # draw the frame
        frame = Image.new('RGB',(width,height), color=(255,255,255))
        d = ImageDraw.Draw(frame)
        texty = 0
        for line in lines:
            w,h = font.getsize(line)
            d.text((0,texty), line, fill=(0,0,0))
            texty += h
        frame.save('frame.png')

def displayUsage():
    print(f"{Fore.RED}Usage: asciify <COMMAND> <image_name> [max_output_width] [max_output_height]{Style.RESET_ALL}", file=sys.stderr)
    print(          f"       If you do not supply an extension for <image_name>, {Fore.RED}.png{Style.RESET_ALL} will be assumed.", file=sys.stderr)
    print()
    print(f"{Fore.RED}Commands:{Style.RESET_ALL}")
    print(f"{Fore.RED}         ascii, text, txt:{Style.RESET_ALL} convert an image to ASCII and output to stdout")
    print(f"{Fore.RED}               image, img:{Style.RESET_ALL} convert an image to ASCII and output that ASCII as a PNG")
    print(f"{Fore.RED}                      gif:{Style.RESET_ALL} convert a GIF to ASCII and output that ASCII as a GIF")
    exit(-1)

def error(msg):
    print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}", file=sys.stderr)
    exit(-1)

def info(msg):
    print(f"{Fore.GREEN}INFO:{Style.RESET_ALL} {msg}", file=sys.stderr)

def flush():
    print("", file=sys.stderr)

def load(curr,total):
    perc = round(curr/total*100)
    print(f"{Fore.GREEN}LOADING:{Style.RESET_ALL} {perc}%", file=sys.stderr, end='\r')

def warn(msg):
    print(f"{Fore.RED}WARNING:{Style.RESET_ALL} {msg}", file=sys.stderr)

def parseArgs():
    try: command = sys.argv[1].strip()
    except:
        displayUsage()
    try: imgName = sys.argv[2].strip()
    except:
        displayUsage()
    try: outw = int(sys.argv[3].strip())
    except:
        outw = None
    try: outh = int(sys.argv[4].strip())
    except:
        outh = None
    return command, imgName, outw, outh

def main():
    command,imgName,outw,outh = parseArgs()

    if command.lower() in ['image','img']:
        Generator.generateASCIIImage(imgName,outw,outh)
        info('Done.')
    elif command.lower() in ['ascii','text','txt']:
        print(Generator.generateASCII(imgName,outw,outh))
        info('Done.')
    elif command.lower() in ['gif']:
        error('Feature not yet implemented!!')
        #Generator.generateASCIIGIF(imgName,outw,outh)
        #info('Done.')
    else:
        displayUsage()

    exit(1)

main()
