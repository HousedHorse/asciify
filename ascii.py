#! /usr/bin/python3
from PIL import Image
import sys
import re
from colorama import Fore, Back, Style 

class Generator:
    def __init__(self,imgName):
        # matches file extension
        match = re.search(r"\.([^\.]*)$",imgName)
        try:
            extension = match.group(1)
            # if we matched a lone dot
            if match.group(1) == '':
                # remove it
                imgName = imgName[:-1]
                raise
        except:
            extension = 'png'
            imgName += '.png'

        # read image or print an error
        try:
            self.img = Image.open(imgName)
            self.imgName = imgName.rstrip(f'.{extension}')
            self.extension = f'{extension}'
        except: error('Could not load image.')

        self.removeTransparency()
        self.convertToGrayscale()
        # resize the image to compensate for ascii being taller than it is wide
        self.resize()

    def removeTransparency(self):
        canvas = Image.new('RGBA',self.img.size,(255,255,255,255))
        self.img = self.img.convert('RGBA')
        canvas.paste(self.img,mask=self.img)
        self.img = canvas

    def convertToGrayscale(self):
        self.img = self.img.convert('L')

    def resize(self):
        self.img.thumbnail((128,128))
        w = round(self.img.width*2)
        h = round(self.img.height)
        self.img = self.img.resize((w,h))

    # static member function to convert a value to an ascii character
    def toChar(value):
        if value > 255: value = 255
        if value < 0: value = 0
        # list is from light to dark but must be read dark to light
        chars = [x for x in reversed([' ','.',',',':',';','O','Q','M','#'])]
        key = round(value * (len(chars)-1) / 255)
        return chars[key]

    def generate(self):
        # flattened array of grayscale values for each pixel
        data = self.img.getdata()
        w = self.img.width
        h = self.img.height
        # iterate through it and generate ascii
        s = ''
        for i,p in enumerate(data):
            s += Generator.toChar(p)
            if (i+1) % w == 0: s += '\n\r'
        return s

def displayUsage():
    print(f"{Fore.RED}Usage: asciify <image_name>{Style.RESET_ALL}", file=sys.stderr)
    print(          f"       If you do not supply an extension, {Fore.RED}.png{Style.RESET_ALL} will be assumed.", file=sys.stderr)
    exit(-1)

def error(msg):
    print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}", file=sys.stderr)
    exit(-1)

def parseArgs():
    try: imgName = sys.argv[1].strip()
    except:
        displayUsage()
    return imgName

def main():
    imgName = parseArgs()

    g = Generator(imgName)
    print(g.generate())

    exit(1)

main()
