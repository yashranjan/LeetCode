1. Find the pair of integers ai and a(i+1) from right side such as ai<a(i+1). If no such pair is found, then the array is already in decreasing order and no next permutation is there.
2. From i+1 to n, find the index of the element just larger than ai, let's call is aj.
3. Swap ai with aj, and reverse ai+1 to an, as the elements from i+1 to n are already in decreasing order and can't form greater permutation.
4. T.C=O(N) S.C=O(1)