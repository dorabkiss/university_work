Big Integers

This lab exercise involves implementing a Big Integer data structure, and some arithmetic 
operations involving Big Integers.
A Big Integer behaves more like a mathematical integer than the fixed-point numbers usually 
found as primitives in computers: there is no hard upper limit for Big Integers; instead, 
if larger numbers are computed then space is made for them. Mathematical operations on them 
behave like pen-and-paper integers, without any kind of overflow or wraparound behaviour.
In this implementation we will use base 10 for our digits, just as with standard arithmetical 
notation, and restrict ourselves to unsigned integers.

Basic Data Structure
Implement the basic storage for a Big Integer as an array named data (to store the digits 
of the integer) of type char. You will need a constructor, whose argument should be the size 
of the array of digits, and that size also needs to be stored in the ndigits member variable.
Implement the get(i) accessor, which should return the ith digit from the digit array, 
counting from the units position upwards – or 0 if the position requested is off the end of 
the Big Integer. 

Addition
Implement addition of two big integers. You will need to loop over each digit position in 
turn, performing the sum of the two digits along with a possible carry from the previous 
position, storing the relevant digit in the right position in the result, and storing the 
carry for the next part of the addition. The following pseudocode will give you some idea.
function Add(a,b)
n ← 1 + max(ndigits(a), ndigits(b))
r ← new BigInt(n)
c ← 0
for 0 ≤ i < n do
(c,s) ← digitsof(get(a,i)+get(a,i)+c)
set(r,i,s)
end for
return r
end function

Subtraction
Subtraction is similar to addition, with borrowing instead of carrying. 
Implement subtraction 𝐵𝑎 − 𝐵𝑏 as Ba.Sub(Bb). 
You may assume that the subtrahend 𝐵𝑏 is smaller than or equal to the minuend 𝐵𝑎. 

Multiplication
This part of the lab walks you through implementing schoolchild multiplication.

Implement Shift(), which returns a new big integer with the digits of the given Big Integer 
shifted by the specified number of places, effectively multiplying the original number by 
a power of 10. 

Multiplication by a single digit: implement MulByDigit(), which takes a digit between 0 and 9 
and produces the Big Integer which is the product of the digit and this Big Integer. 

Schoolchild multiplication: combine the shift, multiply-by-digit and addition operations to 
implement schoolchild multiplication: choose one of the two Big Integers, loop over its digits, 
multiply each digit by the other Big Integer, shift the answer appropriately and add it to the 
result so far. 

Division and Remainder
Implement operations to compute the quotient Div() and the remainder Rem() of division of 
two Big Integers. You may assume that the divisor is smaller than or equal to the dividend. 