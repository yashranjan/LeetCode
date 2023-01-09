class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDam = max(damage)
        sumDam = sum(damage)
        return sumDam-min(maxDam, armor)+1