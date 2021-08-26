# KBbin2txt - KENBAK bin file to txt converter

```
Author:    		Robert Gallup (bg@robertgallup.com)
Date:      		August 26, 2021
License:   		MIT Opensource License (see license.txt) 
Compatability: 	Python 3
Version:		1.0.0
```



### KBbin2txt Overview

Command line Python utility to output a table of hex values representing the size and data from a .bmp graphics file. This would typically be used to create graphics for display by a microprocessor, say an Arduino, on an OLED or LCD.

The *input* is a .bmp file. Windows format 1-bit, grayscale (8-bit), and color (16-bit) bitmaps are known to work.

The *output* is a valid C structure variable definition with meta data for image width and height. A _raw_ format is also supported with the image data defined as an array of const unsigned char. Since bitmaps can take a significant number of bytes, the PROGMEM keyword is used to place data in program memory, rather than on the stack.

Results from bmp2hex.py are directed to **standard output**. You can redirect them to a file, or use cut/paste to transfer the output to your code.

### The command line is:

``` bash
$ python bmp2hex.py [-h] [-i] [-r] [-d] [-n] [-v] [-w WIDTH] [-b BYTESIZE] infile
```

### Where:

*-h, \-\-help* : Help<br />
*-i, \-\-invert* : Invert image pixel colors<br />
*-r, \-\-raw* : Output data in *raw* table format, not as a *structure* \[*default: anonymous structure*\]<br />
*-d, \-\-double* : Uses double byte 'uint16_t' for pixels rather than the default, 'uint8_t'<br />
*-n, \-\-named* : Uses a named structure to type each bitmap<br />
*-x, \-\-xbm* : Reverses the bit order to be consistent with XBM format<br />
*-v, \-\-version* : Displays the bmp2hex version<br />
*-w WIDTH* : Width of table in bytes. \[*default: 16*\]<br />
*-b BYTESIZE* : In *raw* format only, the bytesize of bitmap dimensions. 0=auto, 1 or 2 (big endian) \[*default: 0*\]<br />
*infile* : Path to input .bmp file. May use a list or wild cards for multiple files<br />

### Example 1:

``` bash
$ python bmp2hex.py -w 8 soba.bmp
```
Process the file *soba.bmp*. Display the pixel data with *8* hex bytes on each row.

### Output:

```
PROGMEM const struct {
  unsigned int   width;
  unsigned int   height;
  unsigned int   bitDepth;
  uint8_t        pixel_data[160];
} SOBA = {
40, 32, 1, {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x01,
0x90, 0x00, 0x00, 0x00, 0x03, 0x30, 0x00, 0x00,
0x00, 0x06, 0x60, 0x00, 0x00, 0x00, 0x0c, 0xc0,
0x00, 0x00, 0x00, 0x19, 0x80, 0x00, 0x1f, 0x00,
0x33, 0x00, 0x00, 0x7b, 0xc0, 0x66, 0x00, 0x01,
0xe0, 0xf0, 0xcc, 0x00, 0x03, 0x80, 0x39, 0x98,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff,
0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xe0,
0x07, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff,
0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xe0, 0x03,
0xff, 0xff, 0xff, 0xc0, 0x03, 0xff, 0xff, 0xff,
0xc0, 0x01, 0xff, 0xff, 0xff, 0x80, 0x01, 0xff,
0xff, 0xff, 0x80, 0x00, 0xff, 0xff, 0xff, 0x00,
0x00, 0x7f, 0xff, 0xfe, 0x00, 0x00, 0x3f, 0xff,
0xfc, 0x00, 0x00, 0x1f, 0xff, 0xf8, 0x00, 0x00,
0x0f, 0xff, 0xf0, 0x00, 0x00, 0x03, 0xff, 0xc0,
0x00, 0x00, 0x01, 0xff, 0x80, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
}
};
```

### Example 2:

``` bash
$ python bmp2hex.py -n -w 12 sobaG4.bmp
```
Process the file, *soba.bmp*, using the 'named structure' format. Use a 12-hex bytes wide listing.

### Output:

```
struct GFXMeta {
  unsigned   int width;
  unsigned   int height;
  unsigned   int bitDepth;
             int baseline;
  uint8_t   *pixel_data;
};

PROGMEM uint8_t const SOBAG4_PIXELS[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f,
0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x0f, 0xf0, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00,
0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xf0, 0x0f, 0xf0, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x44, 0x44, 0x00, 0x00, 0x00, 0x00,
0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x04, 0x44, 0x40, 0x44, 0x44, 0x00, 0x00, 0x00, 0x0f, 0xf0, 0x0f, 0xf0,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x44, 0x40, 0x00, 0x00,
0x44, 0x44, 0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x44, 0x40, 0x00, 0x00, 0x00, 0x00, 0x44, 0x40, 0x0f,
0xf0, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00,
0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00,
0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07,
0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00
};
GFXMeta const SOBAG4 = {40, 32, 4, 0, (uint8_t *)SOBAG4_PIXELS};
```

### Example 3:

``` bash
$ python bmp2hex.py -n *.bmp >Graphics.h
```
Process all of the *bmp* files in the current directory using the 'named structure' format.

### Output:

Output results to the file, *Graphics.h*

```
struct GFXMeta {
  unsigned   int width;
  unsigned   int height;
  unsigned   int bitDepth;
             int baseline;
  uint8_t   *pixel_data;
};

PROGMEM uint8_t const SOBA_PIXELS[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0x01, 0x90, 0x00, 0x00, 0x00, 0x03, 0x30, 0x00, 0x00,
0x00, 0x06, 0x60, 0x00, 0x00, 0x00, 0x0c, 0xc0, 0x00, 0x00, 0x00, 0x19, 0x80, 0x00, 0x1f, 0x00,
0x33, 0x00, 0x00, 0x7b, 0xc0, 0x66, 0x00, 0x01, 0xe0, 0xf0, 0xcc, 0x00, 0x03, 0x80, 0x39, 0x98,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xe0,
0x07, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xe0, 0x07, 0xff, 0xff, 0xff, 0xe0, 0x03,
0xff, 0xff, 0xff, 0xc0, 0x03, 0xff, 0xff, 0xff, 0xc0, 0x01, 0xff, 0xff, 0xff, 0x80, 0x01, 0xff,
0xff, 0xff, 0x80, 0x00, 0xff, 0xff, 0xff, 0x00, 0x00, 0x7f, 0xff, 0xfe, 0x00, 0x00, 0x3f, 0xff,
0xfc, 0x00, 0x00, 0x1f, 0xff, 0xf8, 0x00, 0x00, 0x0f, 0xff, 0xf0, 0x00, 0x00, 0x03, 0xff, 0xc0,
0x00, 0x00, 0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
GFXMeta const SOBA = {40, 32, 1, 0, (uint8_t *)SOBA_PIXELS};


PROGMEM uint8_t const SOBAG4_PIXELS[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf0, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f,
0xf0, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xf0, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xf0, 0x0f,
0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x44, 0x44, 0x00, 0x00, 0x00, 0x00,
0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x44, 0x40, 0x44,
0x44, 0x00, 0x00, 0x00, 0x0f, 0xf0, 0x0f, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04,
0x44, 0x40, 0x00, 0x00, 0x44, 0x44, 0x00, 0x00, 0xff, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x44, 0x40, 0x00, 0x00, 0x00, 0x00, 0x44, 0x40, 0x0f, 0xf0, 0x0f, 0xf0, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00,
0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77,
0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77,
0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x77, 0x77, 0x77, 0x77,
0x70, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
GFXMeta const SOBAG4 = {40, 32, 4, 0, (uint8_t *)SOBAG4_PIXELS};


PROGMEM uint8_t const SOBAG8_PIXELS[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff,
0xff, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00,
0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff,
0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x42, 0x41, 0x43, 0x43, 0x42, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42, 0x42, 0x43, 0x42, 0x00, 0x43, 0x42,
0x42, 0x42, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x43,
0x41, 0x43, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42, 0x42, 0x42, 0x43, 0x00, 0x00, 0x00, 0x00,
0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42, 0x42, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x42, 0x42, 0x42, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0xff, 0xff, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x74, 0x74, 0x75, 0x75, 0x74, 0x75, 0x74, 0x75, 0x74, 0x75, 0x73,
0x74, 0x75, 0x74, 0x74, 0x75, 0x73, 0x75, 0x75, 0x75, 0x75, 0x74, 0x75, 0x75, 0x75, 0x75, 0x75,
0x74, 0x75, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x75, 0x74,
0x75, 0x75, 0x75, 0x74, 0x74, 0x75, 0x73, 0x74, 0x75, 0x74, 0x73, 0x73, 0x75, 0x75, 0x73, 0x74,
0x75, 0x75, 0x75, 0x75, 0x75, 0x75, 0x75, 0x75, 0x73, 0x74, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x73, 0x73, 0x74, 0x73, 0x74, 0x75, 0x74, 0x75, 0x75, 0x75,
0x75, 0x75, 0x75, 0x75, 0x74, 0x74, 0x74, 0x73, 0x74, 0x75, 0x73, 0x74, 0x75, 0x74, 0x75, 0x74,
0x74, 0x75, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x75, 0x74,
0x74, 0x75, 0x73, 0x75, 0x75, 0x74, 0x75, 0x74, 0x74, 0x75, 0x75, 0x74, 0x74, 0x74, 0x75, 0x74,
0x75, 0x74, 0x73, 0x74, 0x75, 0x74, 0x74, 0x74, 0x75, 0x75, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x74, 0x75, 0x75, 0x75, 0x75, 0x73, 0x74, 0x75, 0x74, 0x74,
0x74, 0x74, 0x75, 0x74, 0x75, 0x75, 0x75, 0x75, 0x74, 0x75, 0x75, 0x74, 0x75, 0x74, 0x75, 0x73,
0x74, 0x74, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x75,
0x74, 0x74, 0x75, 0x74, 0x74, 0x75, 0x75, 0x75, 0x73, 0x75, 0x75, 0x75, 0x74, 0x75, 0x75, 0x74,
0x75, 0x75, 0x74, 0x74, 0x74, 0x74, 0x75, 0x74, 0x75, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x75, 0x75, 0x74, 0x75, 0x75, 0x75, 0x75, 0x74, 0x75,
0x74, 0x75, 0x75, 0x73, 0x74, 0x75, 0x75, 0x74, 0x74, 0x75, 0x75, 0x73, 0x74, 0x74, 0x75, 0x74,
0x74, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75,
0x75, 0x75, 0x75, 0x75, 0x74, 0x75, 0x73, 0x74, 0x73, 0x75, 0x73, 0x74, 0x75, 0x75, 0x74, 0x75,
0x75, 0x74, 0x73, 0x75, 0x73, 0x75, 0x75, 0x74, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x75, 0x74, 0x75, 0x75, 0x74, 0x75, 0x75, 0x75,
0x75, 0x74, 0x73, 0x75, 0x75, 0x74, 0x74, 0x75, 0x75, 0x75, 0x73, 0x73, 0x74, 0x75, 0x75, 0x74,
0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x75, 0x73, 0x73, 0x73, 0x75, 0x75, 0x74, 0x75, 0x74, 0x75, 0x75, 0x73, 0x75, 0x75, 0x75, 0x75,
0x75, 0x75, 0x74, 0x75, 0x74, 0x74, 0x75, 0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x75, 0x74, 0x75, 0x75, 0x74, 0x75,
0x75, 0x73, 0x74, 0x73, 0x73, 0x75, 0x74, 0x73, 0x74, 0x74, 0x74, 0x75, 0x75, 0x73, 0x75, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x75, 0x74, 0x75, 0x74, 0x75, 0x75, 0x73, 0x75, 0x75, 0x73, 0x73, 0x73, 0x73, 0x74,
0x74, 0x75, 0x75, 0x75, 0x75, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x75, 0x73, 0x75, 0x75,
0x74, 0x75, 0x75, 0x75, 0x74, 0x74, 0x75, 0x75, 0x74, 0x75, 0x75, 0x74, 0x74, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x74, 0x74, 0x75, 0x75, 0x75, 0x75, 0x73, 0x74, 0x75, 0x75, 0x74, 0x75,
0x73, 0x75, 0x75, 0x75, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x74,
0x75, 0x74, 0x75, 0x74, 0x74, 0x74, 0x75, 0x74, 0x75, 0x74, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x75, 0x75, 0x75, 0x73, 0x74, 0x75, 0x74, 0x75, 0x73,
0x73, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
GFXMeta const SOBAG8 = {40, 32, 8, 0, (uint8_t *)SOBAG8_PIXELS};


PROGMEM uint8_t const SOBARGB_PIXELS[] = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8,
0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8,
0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00,
0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00,
0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8,
0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0x00, 0x00, 0xe0, 0xef, 0xe0, 0xef,
0xe0, 0xef, 0xe0, 0xef, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0xef,
0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0xef, 0xe0, 0xef,
0xe0, 0xef, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0xe0, 0xef, 0xe0, 0xef, 0xe0, 0xef, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8,
0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x2b,
0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b, 0x5a, 0x2b,
0x5a, 0x2b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
GFXMeta const SOBARGB = {40, 32, 16, 0, (uint8_t *)SOBARGB_PIXELS};
```