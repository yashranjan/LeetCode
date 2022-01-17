class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = {}
        for i in cpdomains:
            freq, domain = i.split(' ')
            freq = int(freq)
            curr = ''
            for subDomain in domain.split('.')[::-1]:
                if curr == '':
                    curr = subDomain
                else:
                    curr = subDomain + '.' + curr
                if curr in domainCount:
                    domainCount[curr] += freq
                else:
                    domainCount[curr] = freq
        ans = []
        for key, value in domainCount.items():
            ans.append('{} {}'.format(value, key))
        return ans
        