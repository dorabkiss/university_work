1 Linked lists (cont’d)
1.1 Sublist 
By adding to your existing SLList class, implement a sublist method such that 
sublist(int start, int end) returns a fresh list whose contents are the elements in 
positions between start (inclusive) and end (exclusive). You may assume that start is 
less than or equal to end, and that end is less than or equal to the length of the list.
For example, if x represents the three-element list (7 9 14), x.sublist(1,2) should 
return a fresh list (9) and x.sublist(2,2) should return NIL.

1.2 Merge
By adding to your existing SLList class, implement a merge method such that 
merge(SLlist b) returns the result of merging the contents of this with b.  
You may assume that the contents of this and b are already sorted in ascending order.

1.3 Merge sort
By adding to your existing SLList class, implement a mergesort method such that 
mergesort() returns a list of the sorted contents.

2 Stacks and Queues
2.1 Stacks  
The implementation of stacks, based on the basic operations SLList class, is provided.
Implement the basic operations:
push![o] add o to the top of the stack
top return the top element of the stack
pop! remove and return the top element of the stack
empty? return true if the stack has no elements

2.2 Queues
The implementation of queues, based on the basic operations SLList class, is provided.
Implement the basic operations:
head return the element at the head of the queue
dequeue! return and remove the element at the head of the queue
enqueue![o] add o to the tail of the queue
empty? return true if the queue has no elements.
