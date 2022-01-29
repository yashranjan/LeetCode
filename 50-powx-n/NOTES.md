Obervations:
1. For calculating x^n, first calculate x^(n/2) and then square it. TC - O(logn) SC - O(logn) for recursion stack. This is also known as fast power recursive method.
2. In fast power iterative, for calculating x^n, the binary representation of n is traversed and if a bit is set 1, then add the corresponding value of x in the answer. TC - O(logn) SC - O(1).