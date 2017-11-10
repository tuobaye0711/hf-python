class AthleteList(list):
    def __init__(self, player_name, player_dob=None, player_times=[]):
        list.__init__([])
        self.name = player_name
        self.dob = player_dob
        self.extend(player_times)

    def top3(self):
        return sorted(set([sanitize(l) for l in self]))[0:3]