1 Hash tables
1.1 Data structure
Implement a hash table, using ℎ𝑎,𝑐,𝑚(𝑥) = (𝑎𝑥 + 𝑐) mod 𝑚 as the hash and reduction function. 
The client of the hash table will specify the parameters 𝑎 and 𝑐, and the capacity of the 
storage table 𝑚. You must keep the buckets member variable public and use values of the 
hash function ℎ as indexes into that array; in a real implementation buckets would be 
declared as private, but it needs to be exposed for testing purposes. 

1.2 Basic operations
Implement the insert and find operations, for strictly positive (i.e. non-zero and 
non-negative) keys. Collision resolution for this hash table implementation uses linear 
probing: if a hash bucket is occupied on insert, move on to the next one until there is 
an unoccupied one to store the key in. Also, implement the loadFactor function, 
which should return as a float the fraction of total hash buckets that are occupied.

1.3 Further work
As it stands, your implementation of a hash table is incomplete compared with a fully-functional one:
• it doesn’t support delete;
• it has a fixed capacity, rather than being able to expand beyond its initial size;
• its collision resolution strategy is not best-of-breed.
Extend your implementation to rectify these or other problems. 