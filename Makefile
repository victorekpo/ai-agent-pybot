run:
	/usr/bin/python3 main.py

test:
	python3 -m unittest discover

install:
	/usr/bin/python3 -m pip install -r requirements.txt