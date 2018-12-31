# ASCII Art Generator

By: William "HousedHorse" Findlay

## Important

This program produces large amounts of text in order to keep the resolution nice.

That means **if you want to view your picture you need to use a very small font**.
In a terminal, I recommend zooming way out if your terminal supports doing so.
In a word processor, use a **monospaced font** and set the **font size to around 2-6**.

In the future, I may add the option to change output sizes.

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
