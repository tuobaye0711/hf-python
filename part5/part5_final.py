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
print(sorted(julie_list))
james_list = [sanitize(each_data) for each_data in james_data]
print(sorted(james_list))
mikey_list = [sanitize(each_data) for each_data in mikey_data]
print(sorted(mikey_list))
sarah_list = [sanitize(each_data) for each_data in sarah_data]
print(sorted(sarah_list))