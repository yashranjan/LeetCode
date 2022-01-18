Three approaches as below
1) Sort the array and return kth element from last. TC - O(nlogn) SC - O(1)
2) Make a min-heap of size k from the array, which will hold k largest elements in the array, and return the first element. TC - O(nlogk) SC - O(k)
3) Use quick select to find the (n-k)th smallest element by paritioning around a randomly choosen pivot element. TC - O(n) in worst case can be O(n2) SC - O(1)