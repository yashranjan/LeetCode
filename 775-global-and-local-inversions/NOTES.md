Observations:
1. A local inversion is a global inversion
2. For a global inversion to occur(without a local inversion) then A[i] > A[i+2].
3. If we just need to prove that global inversion count is not equal to local inversion, finding a pair such as above is enough, which can be done in O(n) time by keeping the track of minimum element seen so far from the right and comparing it with i-2.