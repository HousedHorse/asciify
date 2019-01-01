# ASCII Art Generator

By: William "HousedHorse" Findlay

## Dependencies

All libraries are installed with the makefile. If the makefile doesn't work,
install them manually with `pip`.

- Python3 (I use version 3.7.1 but other versions might work)
- libraries (installed via makefile)
  - Pillow
  - colorama
  
**Windows Users:** This program is meant to be run on UNIX-like operating systems.
If you're on Windows you should still be able to run it, but the process of running
it and installing dependencies will be **much different** than what is shown here.

## Installation

1. `$ git clone https://github.com/HousedHorse/asciify`
1. `$ cd asciify`
1. `$ sudo make install`

## Usage

Supply a command followed by the image name, with extension, as a command line argument.
If you supply an image name without an extension, the program will assume the
image is in `.png` format.

### ASCII Text

By default, the program prints to `stdout`. In order to capture your
output in a `.txt` file, run the program using output redirection as follows:

`$ asciify txt my_image.png > output.txt`

Optionally, you can supply a maximum width and a maximum height as follows:

`$ asciify txt my_image.png 128 128 > output.txt` produces a maximum size 128x128 character version of the ASCII art.

### ASCII Images

The program will generate ASCII text from the original image file and then save it as a PNG.

`$ asciify img my_image.png`

Optionally, you can supply a maximum width and a maximum height as follows:

`$ asciify img my_image.png 128 128` produces a maximum size 128x128 character version of the ASCII art image.

Note that the dimensions of the actual image produced will be larger.

## ASCII GIFs

Just give it a `GIF` file and supply the `gif` command.

`$ asciify gif my_gif.gif`

Optionally, you can supply a maximum width and a maximum height as follows:

`$ asciify gif my_gif.gif 128 128` produces a maximum size 128x128 character version of the ASCII art GIF.

**This command will take a very long time as it essentially performs the ASCII Image operation on EACH FRAME.**
Please be patient and it is advised not to make the size too large.
