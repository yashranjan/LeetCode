Approaches:
1. 2 loops and search. TC - O(n2) SC - O(1)
2. Sort and find adjancent. TC - O(nlogn) SC - O(1)
3. Hashset. TC - O(n) SC - O(n)
4. Negative marking indices. TC - O(n) SC -O(1)
5. Array as hahmap, keep on putting 0th element to its correct index till the time they are same, once same, return the value at 0th index. TC - O(n) SC-O(1)
6. Bit-count, count the no. of set-bits at each position for values in range [1,n] and for values of the list. Then compare the no. of set-bits, and if there's a difference set the corresponding bit to 1 for the anwer.
Obervations->
1. Use tortoise-hare algorithm for O(n) TC solution.Consider every element to be a node, pointing to nums[val] ind.
2. One can keep swapping element at index-0 to element at element at index-0. If a match is found, return element at index 0. This is basically kind of hashing.
NOTE: Above two only works when elements are in range [1,n] and 0 is not present. If 0 was present(with same number of elements) both the approaches would fail. In this case, the best would be to use every element as an index to know wether an element is repeated or not.