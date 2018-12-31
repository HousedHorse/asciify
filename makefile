install:
	pip3 install Pillow colorama; chmod +x ascii.py; cp ascii.py /usr/bin/asciify; mkdir /usr/share/fonts; cp ./inconsolata.otf\
		/usr/share/fonts
