Approaches:
1. Brute - TC O(n2)
2. Sorting - middle element will be major TC - O(nlogn) SC - O(n)
3. Divide and conquer - get the majority for the left and right sub-array, if they agree that's the majority, otherwise count the occurences of them in the whole sub-array and return appropriately.
3. Hashmap - TC - O(n) SC - O(n)
4. Boyer-Moore voting algo - It works on the fact that if we discard an equal number of majority and minority elements from an array, the remaining suffix will still have the same majority element. TC - O(n) SC - O(1)
5. Bit-manip - For every bit, count if its occuring more than majority, if yes, it's gonna be set  in the majority element as well. TC - O(n) SC - O(1). NOTE: In python, if you're going to set the 32nd bit(LSB being 1st bit) then do ans = -((1<<31)-ans).