def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        data_list = data.strip().split(',')
        data_dict = dict()
        data_dict['Name'] = data_list.pop(0)
        data_dict['DOB'] = data_list.pop(0)
        data_dict['Times'] = str(sorted(set([sanitize(l) for l in data_list]))[0:3])
        return data_dict
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


julie = get_coach_data('julie2.txt')
print(julie['Name'] + "'s fastest times are " + julie['Times'])
james = get_coach_data('james2.txt')
print(james['Name'] + "'s fastest times are " + james['Times'])
mikey = get_coach_data('mikey2.txt')
print(mikey['Name'] + "'s fastest times are " + mikey['Times'])
sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are " + sarah['Times'])