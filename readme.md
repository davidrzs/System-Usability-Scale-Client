# System Usability Scale Client software - Making Usability Research a tiny bit better.

This software enables you to create very simple system usability scale surveys. It has been designed to be run on a lab computer and have participants answer a set of predefined questions and then record the asnwers in a CSV file, ready to be exported to Excel for further data analysis.

It has been written for a usability study conducted at [ETH Zürich](https://ethz.ch/) and the [University of Zürich](https://www.uzh.ch/en.html).

- [Why have we written this software?](#why-have-we-written-this-software)
- [Getting Started](#getting-started)
- [How to install it](#installing)
- [License and Sources](#license-and-sources)

## Getting Started

TODO

## Why have we written this software?

TODO

## Installing

There are three options to install ...

- [download executable](#how-to-use)
- [build the executable yourself](#build-yourself)
- [run the python script](#run-the-python-script)

## How to use ...

will follow soon

## Download Executable

Will follow soon

## Run the Python script

This is very straightforward. Just follow the following steps. It is important that you have Python 3 installed:

1. Clone or download this repository
2. Run `python install.py`. This very simple script will install all needed dependencies.
3. Run `python3 main.py` and the server should start.

## Build yourself

A tiny bit more complex than just running the Python script but still doable. Just follow the following steps. It is important that you have Python 3 installed:

1. Clone or download this repository
2. Run `python install.py`. This very simple script will install all needed dependencies.
3. If you have the make buildsystem installed run `make`. If you do not have make you can run `	pyinstaller main.py --add-data 'templates:templates' --onefile` on the command line. It will have the same effect
4. Within the folder `./dist` you can find the executable `main`, this is your binary.

## License and Sources

As of right now all rights are reserved by Robin Peter and David Zollikofer

TODO