class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        matches_dict = defaultdict(list)
        
        players_set = set()
        
        for winner, loser in matches:
            matches_dict[loser].append(winner)
            players_set.add(winner)
            players_set.add(loser)
        
        res = [[], []]
        
        for player in sorted(players_set):
            if player not in matches_dict:
                res[0].append(player)
            elif len(matches_dict[player])==1:
                res[1].append(player)
        
        return res