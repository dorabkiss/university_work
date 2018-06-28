Basic implementation
Implement a SLList linked-list class, whose basic methods are: first(), rest(), setFirst(), and setRest(). 
The “rest” must be a reference or pointer to another SLList, including the special SLList object NIL.
You should also provide a two-argument constructor, which initializes the instance with the first argument
as the first, and the second argument as the rest, of the resulting SLList.

Derived methods
Extend your implementation of linked lists to support these additional methods:
nth() return the nth item stored in the list, counting from 0 (so nth(0) should return the first item)
nthRest() return the nth rest of the list, counting from 0 (so nthRest(0) should return the given list
itself)
length() return the length of the list
sum() find the sum of the elements in a list

Remove
Implement remove, which returns a new list whose contents are the same as the original list, 
but with all instances of the given object removed. 

Reverse
Implement reverse, which returns a new list whose contents are the same as the original list 
but in reverse order. 