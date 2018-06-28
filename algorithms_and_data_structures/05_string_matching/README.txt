String matching

1.1 Naïve string matching
First, implement naïve matching.

1.2 Rabin-Karp string matching
Implement Rabin-Karp matching using the rolling hash function

				𝑖+𝑚−1
ℎ(𝑠𝑖..𝑖+𝑚−1) =	∑		𝑠𝑖 mod 256
				𝑘=𝑖

1.3 Knuth-Morris-Pratt string matching
Implement Knuth-Morris-Pratt matching 