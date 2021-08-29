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

The primary purpose is to convert the output from assembler-generated .bin files to a text format that can be uploaded through serial connection to a KENBAK-1 emulator running Mark Wilson's firmware (http://funnypolynomial.com/software/arduino/kenbak.html)

Output from KBbintxt.py is directed to standard output. You can redirect it to a file, or use cut/paste from the terminal window to transfer the output to the KENBAK through a serial monitor.

### The command line is:

``` bash
$ python KBbintxt.py [-h] [-p N] [-r] [-s] [-x] [-v] infile
```

### Where:

*-h, \-\-help* : Help<br />
*-p N, \-\-pgm_start* : Sets the byte number for the start of the program<br />
*-r, \-\-raw* : Outputs just numeric bytes without file name header<br />
*-s, \-\-strip* : Strips trailing zeros from the listing and terminates with an "e"<br />*-x, \-\-hex_format* : Outputs numbers in hexadecimal rather than octal<br />*-v, \-\-version* : Outputs version information<br />
<br />
*infile* : Path to input file. May use a list or wild cards for multiple files<br />

### Example:

``` bash
$ python3 KBbintxt.py blink.bin
```
Process the file *blink.bin*. Display all 256 bytes in octal format.

### Output:

```

blink.bin
0000,0000,0000,0004,0023,0252,0034,0200,0334,0000,0013,0001,0223,0277,0367,0022,
0043,0006,0000,0213,0001,0243,0023,0357,0022,0000,0000,0000,0000,0000,0000,0000,
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
$ python3 KBbintxt.py -s -r blink.bin
```

Process the file *blink.bin*. Display bytes in octal format, strip zero bytes from the end, and print only raw data (not the file name).

### Output:

```
0000,0000,0000,0004,0023,0252,0034,0200,0334,0000,0013,0001,0223,0277,0367,0022,
0043,0006,0000,0213,0001,0243,0023,0357,0022,e
```



### Example:

``` bash
$ python3 KBbintxt.py -s -r -x blink.bin
```

Process the file *blink.bin*. Display bytes in hexadecimal format, strip zero bytes from the end, and print only raw data (not the file name).

### Output:

```
0x000,0x000,0x000,0x004,0x013,0x0AA,0x01C,0x080,0x0DC,0x000,0x00B,0x001,0x093,0x0BF,0x0F7,0x012,
0x023,0x006,0x000,0x08B,0x001,0x0A3,0x013,0x0EF,0x012,e
```

