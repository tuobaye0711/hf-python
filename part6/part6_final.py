def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


class Athlete:
    def __init__(self, player_name, player_dob, player_times):
        self.name = player_name
        self.dob = player_dob
        self.times = player_times

    def add_time(self, new_time):
        self.times.append(new_time)
        return self.times

    def add_times(self, time_list):
        self.times.extend(time_list)
        return self.times


class AthleteList(list):
    def __init__(self, player_name, player_dob=None, player_times=[]):
        list.__init__([])
        self.name = player_name
        self.dob = player_dob
        self.extend(player_times)

    def top3(self):
        return sorted(set([sanitize(l) for l in self]))[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        data_list = data.strip().split(',')
        data_class = Athlete(data_list.pop(0), data_list.pop(0), sorted(set([sanitize(l) for l in data_list]))[0:3])
        return data_class
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


julie = get_coach_data('julie2.txt')
print(julie.name + "'s fastest times are " + str(julie.times))
james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are " + str(james.times))
mikey = get_coach_data('mikey2.txt')
print(mikey.name + "'s fastest times are " + str(mikey.times))
sarah = get_coach_data('sarah2.txt')
sarah.add_times(['3:52', '1:22', '2:13'])
print(sarah.name + "'s fastest times are " + str(sarah.times))

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.11', '1.55', '3.02'])
print(vera.top3())
print(vera)
print(vera.name)
print(vera.dob)