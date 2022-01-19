Approaches:
1. 2 loops and search. TC - O(n2) SC - O(1)
2. Sort and find adjancent. TC - O(nlogn) SC - O(1)
3. Hashset. TC - O(n) SC - O(n)
4. Negative marking indices. TC - O(n) SC -O(1)
5. Array as hahmap, keep on putting 0th element to its correct index till the time they are same, once same, return the value at 0th index. TC - O(n) SC-O(1)
6. Bit-count, count the no. of set-bits at each position for values in range [1,n] and for values of the list. Then compare the no. of set-bits, and if there's a difference set the corresponding bit to 1 for the anwer. TC - O(nx32) SC - O(1)
7. Floyd;s cycle detection(tortoise and hare), the intuittion is that every index's value will map to a particular index, and since a value is repeated, there will be a circle whose entry point will be this repeated value. TC - O(n) SC- O(1)
NOTE: Approach 5,6,7 works only when elements are in range [1,n] and 0 is not present. If 0 was present(with same number of elements) they would fail. In this case, the best would be to use every element as an index to know wether an element is repeated or not.