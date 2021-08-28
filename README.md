## KBbintxt - Converts KENBAK-1 .bin files to text

```
Author:    		Robert Gallup (bg@robertgallup.com)
Date:      		August 26, 2021
License:   		MIT Opensource License (see license.txt) 
Compatability:		Python 3
Version:		1.0.0
```

### KBbintxt Overview

KBbintxt is a command line utility, written in Python, that outputs a comma-separated list of octal values representing the data from a .bin file representing the 256-byte memory contents of a KENBAK-1 program. 

The primary purpose is to convert the output from assembler-generated .bin file to a text format that can be uploaded through a serial connection to a KENBAK-1 emulator running Mark Wilson's firmware (http://funnypolynomial.com/software/arduino/kenbak.html)

Output from KBbintxt.py is directed to **standard output**. You can redirect it to a file, or use cut/paste to transfer the output to the KENBAK through a serial monitor.

### The command line is:

``` bash
$ python KBbintxt.py [-h] [-p N] [-r] [-s] [-v] infile
```

### Where:

*-h, \-\-help* : Help<br />
*-p N, \-\-pgm_start* : Sets the byte number for the start of the program<br />
*-r, \-\-raw* : Output just the octal bytes without file name header<br />
*-s, \-\-strip* : Strips trailing zeros from the listing and terminates with an "e"<br />
*-v, \-\-version* : Displays the bmp2hex version<br />
<br />
*infile* : Path to input .bmp file. May use a list or wild cards for multiple files<br />

### Example:

``` bash
$ python3 KBbintxt.py Fibonacci.bin
```
Process the file *Fibonacci.bin*. Display the binary data as octal bytes

### Output:

```

Fibonacci.bin
0000,0000,0000,0004,0023,0000,0034,0036,0023,0001,0034,0037,0233,0000,0026,0036,
0006,0037,0212,0201,0200,0000,0036,0040,0034,0200,0203,0001,0347,0016,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,0000,
```

### Example:

``` bash
$ python3 KBbintxt.py -s -r Fibonacci.bin
```

Process the file *Fibonacci.bin*. Display the binary data as octal bytes, strip zero bytes from the end, and don't print the filename.

### Output:

```
0000,0000,0000,0004,0023,0000,0034,0036,0023,0001,0034,0037,0233,0000,0026,0036,
0006,0037,0212,0201,0200,0000,0036,0040,0034,0200,0203,0001,0347,0016,e
```

