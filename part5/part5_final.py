def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + ':' + secs


with open('julie.txt') as julie:
    julie = julie.read()
    julie_data = julie.strip().split(',')
with open('james.txt') as james:
    james = james.read()
    james_data = james.strip().split(',')
with open('mikey.txt') as mikey:
    mikey = mikey.read()
    mikey_data = mikey.strip().split(',')
with open('sarah.txt') as sarah:
    sarah = sarah.read()
    sarah_data = sarah.strip().split(',')
julie_list = [sanitize(each_data) for each_data in julie_data]
print(sorted(set(julie_list))[0:3])
james_list = [sanitize(each_data) for each_data in james_data]
print(sorted(set(james_list))[0:3])
mikey_list = [sanitize(each_data) for each_data in mikey_data]
print(sorted(set(mikey_list))[0:3])
sarah_list = [sanitize(each_data) for each_data in sarah_data]
print(sorted(set(sarah_list))[0:3])
