class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def funcForSorting(log):
            _id, logs = log.split(' ', maxsplit=1)
            if logs[0].isdigit():
                return (1, None, None)
            return (0, logs, _id)
        
        logs.sort(key=funcForSorting)
        
        return logs