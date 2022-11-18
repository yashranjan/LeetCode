1) 2-loop solution: TC - O(n2) SC - O(n)/O(1)
2) 2-pointer solution: TC - O(nlogn) SC -O(1)
3) binary search: binary search for the complement value, to get the maximum sum possible. TC - O(nlogn) SC - O(1)
4) counting sort: count the frequency of each element and store in a hash map. Then, keep 2 pointers and do same as above. TC - O(n+m) SC -O(1), where m is the range of numbers