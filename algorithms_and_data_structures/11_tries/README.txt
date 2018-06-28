Tries
This lab exercise involves implementing a trie data structure to store sets of strings. 
To simplify things, we will restrict our alphabet to 26 lower-case letters, and only 
implement insertion and exact querying (not prefix querying).

Standard Trie data structure
Our implementation of the standard trie data structure will represent each node as a 
27-element array of Trie objects. If the set of strings contained in the trie contains a 
string whose next character at this point is c, then the corresponding element of the array 
should be the child Trie; if it does not contain any such string, the corresponding element 
of the array should be null.

As a special case, you will need to handle the end-of-word character, which we will take as 
being { (for reasons which might become obvious if you consider ASCII offsets from a). 

You will need some kind of non-null Trie to store in the end-of-word (27th) position, but 
you should never need to look inside that Trie. 

Insert
Implement the insert method for Trie objects, which should:
• if necessary, construct a children array for the Trie;
• if necessary, construct a Trie object for the current character of the string being inserted;
• insert the substring of all but the first character into the Trie for the first characters.

Query
Once you have implemented insert, you should be able to implement the member operation (query). 
This should return true if the query string is exactly present in the Trie, and false otherwise.