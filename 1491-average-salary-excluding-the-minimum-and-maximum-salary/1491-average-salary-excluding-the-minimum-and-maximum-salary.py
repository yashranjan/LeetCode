class Solution:
    def average(self, salary: List[int]) -> float:
        totSalary = sum(salary) - max(salary) - min(salary)
        return totSalary/(len(salary)-2)