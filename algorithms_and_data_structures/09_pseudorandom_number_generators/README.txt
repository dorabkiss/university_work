Linear Congruential generator

Implement a Linear congruential pseudorandom number generator, supporting the operations 
next and seed. One of the issues described in the lecture relates to the low bits of a 
pseudorandom sequence from an LCG having very little entropy (e.g. the lowest bit of the 
numbers alternating between 0 and 1). One way of mitigating this is to have a larger 
internal state, and return to the user only the higher-entropy bits. For example, Java’s 
java.util.Random and POSIX’s lrand48 both implement a 48-bit internal state, and the next 
method returns the state shifted right by 16 bits. Extend your implementation to support this; 
define a new constructor with signature 
LCG(long _a, long _c, long _m, long seed, long _shift)


Xorshift generator

Implement a xorshift random number generator; specifically, the general version (with 
arbitrary shifts a, b and c) of unsigned long xor given on page 4 of George Marsaglia’s 
“Xorshift RNGs”, published by the Journal of Statistical Software in July 2003.
Your implementation should maintain the one unsigned 32-bit word of state, and update and 
return it according to:
x ← x ⊕ leftshift(x,a)
x ← x ⊕ rightshift(x,b)
x ← x ⊕ leftshift(x,c)
return x