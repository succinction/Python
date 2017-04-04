'''
   1  // The base-10 number  1: (1 x 1) is 1
  10  // The base-10 number  2: (1 x 2) + (0 x 1) is 2
  11  // The base-10 number  3: (1 x 2) + (1 x 1) is 3
 100  // The base-10 number  4: (1 x 4) + (0 x 2) + (0 x 1) is 4
1000  // The base-10 number  8: (1 x 8) + (0 x 4) + (0 x 2) + (0 x 1) is 8
1001  // The base-10 number  9: (1 x 8) + (0 x 4) + (0 x 2) + (1 x 1) is 9

var options;
options = 1   // 1 is 0001; bit 0 is on: air-conditioning only
options = 2   // 2 is 0010; bit 1 is on: CD player only
options = 4   // 4 is 0100; bit 2 is on: sunroof only
options = 8   // 8 is 1000; bit 3 is on: leather seats only

// Here's the cool part: combining options
options = 5   // 5  is 0101: air-conditioning (1) and a sunroof (4)
options = 10  // 10 is 1010: CD player (2) and leather (8)
options = 15  // 15 is 1111: fully loaded baby!

Whenever we want to add or remove options, we just add or subtract the value of the appropriate bit:

var options = 0;  // No options to start
options += 4;     // Add sunroof (options is 4, or 0100)
options += 1;     // Add air-conditioning (options is 5, or 0101)
options += 2;     // Add CD player (options is 7, or 0111)
options -= 4;     // Remove the sunroof (options is 3, or 0011)
options += 8;     // Add leather seats (options is 11, or 1011)


AND

  1111
& 0100
------
  0100

In this example, bits 0 and 3 are 1 in both operands and are therefore set to 1 in the result. Bits 1 and 2 are set to 0 in the result:

  1101
& 1011
------
  1001


15 & 4   // Result is 4
13 & 11  // Result is 9

In practice, the bitwise AND operator is used to check whether a particular flag or set of flags (i.e., bits) is true or false.

The following example checks whether bit 2 (which has the value 4) is set to true:

if (x & 4) {
  // Do something
}
Or, we can check whether either bit 2 or bit 3 (which has the value 8) is set to true:

if (x & (4|8)) {
  // Do something
}
Note that the preceding example checks whether bit 2 or bit 3 is set using the | operator discussed next. To check whether both bits 2 and 3 are set, we can use:

if (x & (4|8) == (4|8)) {
  // Do something
}
The bitwise AND operator is also used to set individual bits in a number to false; see "Bitwise NOT" later in this article.

Bitwise OR
The Bitwise OR operator (|) combines the bits of two numbers by performing a logical OR operation on each bit of the numbers. Like bitwise AND, bitwise OR returns the result of the combination as a number. A bitwise OR expression takes the form:

operand1 | operand2
The operands can be any numbers, but they are converted to 32-bit binary integers before the operation occurs. The fractional portion of an operand, if any, is discarded.

Note that the bitwise OR uses the single-character operator, |, and operates on individual bits within a number, whereas the logical OR operator discussed in Chapter 5, "Operators" of ActionScript, The Definitive Guide uses the two-character operator, ||, and treats each operand as a whole.

Each bit in the result is determined by taking the logical OR of the bits of the two operands. Therefore, if a bit is set to 1 in either (or both) operand1 or operand2, that bit will be set to 1 in the result. Compare the following pseudoexamples to those shown earlier for the bitwise AND operator.

In this example, only bit 1 is set to 0 in the result because bit 1 is 0 in both operands. The other bits are set to 1:

  1101
| 0100
------
  1101
In this example, all bits are set to 1 in the result because each bit contains a 1 in at least one of the two operands:

  1101
| 1011
------
  1111
In actual code, where decimal numbers are used, this reads:

13 | 4    // Result is 13
13 | 11   // Result is 15
In practice, we often use bitwise OR to combine multiple numbers that represent individual options into a single numeric value that represents all the options of a system. For example, the following code combines bit 2 (value 4) and bit 3 (value 8):

options = 4 | 8;
The bitwise OR operator is also used to set an option to true in an existing value. The following example sets the option represented by bit 3 (value 8) to true. If the value in bit 3 is already true, it is untouched:

options = options | 8;
Multiple bits can also be set at once:

options = options | 4 | 8;

############################################## XOR

  1011
^ 1101
------
  0110
In this example, all the bits match in both operands, so the result is all zeros:

  0010
^ 0010
------
  0000
In this example, bits 0, 2, and 3 differ in the two operands, so those bits are set to 1 in the result. Bit 1 is the same in both operands, so it is set to 0 in the result:

  0110
^ 1011
------
  1101
Translated to decimal numbers, the preceding examples become:

11 ^ 13    // Result is 6
2 ^ 2      // Result is 0
6 ^ 11     // Result is 13
The bitwise XOR operator is typically used to toggle options between 1 and 0 (true and false). To toggle the option indicated by bit 2 (whose value is 4), we could use:

options = options ^ 4;

##########################################################

The bitwise NOT operator is typically used with the
bitwise AND operator to clear specific bits (i.e., set them to 0).
For example, to clear bit 2, we could use:

options = options & ~4;
The expression ~4 returns a 32-bit integer containing all 1s,
except for a 0 in bit 2. By bitwise ANDing that number with the
options variable, options' bit 2 is cleared and other bits are
left unchanged. The preceding can be written more succinctly as:

options &= ~4;
The same technique can be used to clear multiple bits at once; the following example clears bits 2 and 3:

options &= ~(4 | 8);

##########################################################

Shifting a number left by 4 bits is equivalent to multiplying it by 24 (i.e., 16). In decimal, this reads:

9 << 4  // Result is 9 * 16, i.e., 144
Notice that in prior examples, we "manually" specified the value associated with a particular bit: 1 for bit 0, 2 for bit 1, 4 for bit 2, 8 for bit 3, and so on. The left shift operator is very handy for calculating a bit position's equivalent value:

(1 << 0)    // Bit 0 equals 1
(1 << 1)    // Bit 1 equals 2
(1 << 2)    // Bit 2 equals 4
(1 << 3)    // Bit 3 equals 8
(1 << 15)   // Much easier than remembering bit 15 equates to 32768!
The left shift operator is also handy for dynamically selecting bits by numeric index rather than bit value. This example counts up all the bits set to one in a number.

// Using Left Shift to Count Bits That Are Set

myNumber = 27583;  // The number whose ones we'll count
count = 0;
for (var i=0; i < 32; i++) {
  if (myNumber & (1 << i)) {
    count++;
  }
}
The next example is a variation on the previous example using the right shift operator. We can repeatedly right-shift the value and check its rightmost bit (bit 0), instead of using the left shift operator to calculate the bit value associated with each bit.

// Counting Bits Using Right Shift

myNumber = 27583;
count = 0;
temp = myNumber;    // Make a copy for temporary use
for (var i = 0; i < 32; i++) {
  if (temp & 1) {
    count++;
  }
  temp = temp >> 1;
}
The variable myNumber is copied into the temporary variable temp because the right shift is destructive; the variable temp ends up with a final value of 0.

###############################

Bitwise Operations Applied
We began our look at bitwise operators using the example of a Flash site that sells cars. Now that we've seen how bitwise operators work, let's use them to determine the cost of a car, as shown the next example. You can download the .fla file for this example here.

// Real-Life Bitwise Operations

// First, set the options (usually by adding and subtracting numbers
// based on the selections of a fill-in form, but we hardcode them here)
var hasAirCon   = (1<<0)    // Bit 0: 0 means no, 1 means yes
var hasCDplayer = (0<<1)    // Bit 1: 0 means no, 2 means yes
var hasSunRoof  = (1<<2)    // Bit 2: 0 means no, 4 means yes
var hasLeather  = (1<<3)    // Bit 3: 0 means no, 8 means yes

// Now combine the options into a single number using bitwise OR
var carOptions = hasAirCon | hasCDplayer | hasSunRoof | hasLeather;

// Here's a function that calculates the price
function totalPrice(carOptions) {
  var price = 0;
  if (carOptions & 1) {  // If the first bit is set
    price += 1000;       // add $1000
  }
  if (carOptions & 2) {  // If the second bit is set
    price += 500;        // add $500
  }
  if (carOptions & 4) {  // If the third bit is set
    price += 1200;       // add $1200
  }
  if (carOptions & 8) {  // If the fourth bit is set
    price += 800;        // add $800
  }

  return price;
}

// Everything's set to go: let's call the function and see if it works!
trace(totalPrice(carOptions));  // Returns 3000. Cool...
To avoid hardcoded bit values throughout your code, it's good practice to store the bit values corresponding to specific options in variables, such as:

var airConFLAG   = 1 << 0;  // Bit 0, whose value is 1
var cdPlayerFLAG = 1 << 1;  // Bit 1, whose value is 2
var sunroofFLAG  = 1 << 2;  // Bit 2, whose value is 4
var leatherFLAG  = 1 << 3;  // Bit 3, whose value is 8



'''
'''
SET BITS WITH OR | 11|4 = 15; 15|4 = 15
CHECK BITS WITH AND & 11&4 = 0; 15&4 = 4
TOGGLE BITS WITH XOR ^ 11^4 = 15; 15^4 = 11
clear BITS WITH NOT ~ AND AND & 15 & ~4 = 11 ; 11&~4 = 11;

'''



print("    ##### BITWISE CALCULATOR ##### \n")


while True:
    bits = input('Enter a set of bits as a string of 1 and 0: \n>>>')
# print('>>>21')
# print('>>>52631')
# print('>>>684268421')
    print('>>> ' + str(int(bits, 2)))

    itgr = input ('Enter Interger: \n>>>')
    print(bin(int(itgr)))
    if input("quit? y "):
        quit()
