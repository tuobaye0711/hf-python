def str_to_list(old_str, new_list):
    old_str = old_str.strip()
    if old_str.find(',') > -1:
        (new_data, new_str) = old_str.split(',', 1)
        new_list.append(new_data)
        str_to_list(new_str, new_list)
    else:
        new_list.append(old_str)
        return new_list


def read_data(data_in):
    new_list = []
    str_to_list(data_in, new_list)
    time_list = []
    for each_data in new_list:
        if each_data.find('.') > -1:
            (min, sec) = each_data.split('.');
            time = min + ':' + sec
            time_list.append(time)
        elif each_data.find('-') > -1:
            (min, sec) = each_data.split('-');
            time = min + ':' + sec
            time_list.append(time)
        else:
            time_list.append(each_data)
    return time_list


julie = open('julie.txt').read()
julie_data = read_data(julie)
print(julie_data)
james = open('james.txt').read()
james_data = read_data(james)
print(james_data)
sarah = open('sarah.txt').read()
sarah_data = read_data(sarah)
print(sarah_data)
mikey = open('mikey.txt').read()
mikey_data = read_data(mikey)
print(mikey_data)