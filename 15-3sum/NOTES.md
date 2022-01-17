1) For removing the duplicates(in case of sorted approach), note these facts:
i. If the first element is equal to its previous, skip it
ii. If the two-element's sum matches, then skip all the left side elements which matches
TC - O(n2) SC - O(1)
2) Sort and then use a hashset to find the remaining sum. Above facts still applies. TC - O(n2) SC-O(n)
3) No-sort approach, extra hash-set needs to be created for removing the duplicates. Complexities same as above.