# ASCII Art Generator

By: William "HousedHorse" Findlay

## Dependencies

All libraries are installed with the makefile. If the makefile doesn't work,
install them manually with `pip`.

- Python3 (I use version 3.7.1 but other versions might work)
- libraries (installed via makefile)
  - Pillow
  - colorama

## Installation

1. `$ git clone https://github.com/HousedHorse/asciify`
1. `$ cd asciify`
1. `$ sudo make install`

## Usage

Supply the image name, with extension, as a command line argument.
If you supply an image name without an extension, it will assume the
image is in `.png` format.

By default, the program prints to `stdout`. In order to capture your
output in a `.txt` file, run the program using output redirection as follows:

`$ asciify my_image.png > output.txt`

Optionally, you can supply a maximum width and a maximum height as follows:

`$ asciify my_image.png 128 128 > output.txt` produces a 128x128 version of the ASCII art.
