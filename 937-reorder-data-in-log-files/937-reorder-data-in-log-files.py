class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def use_for_sorting(log):
            _id, logs = log.split(' ', maxsplit=1)

            if logs[0].isdigit():
                return (True, None, None)
            return (False, logs, _id)

        logs.sort(key = use_for_sorting)

        return logs
        