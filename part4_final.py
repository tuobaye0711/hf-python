import pickle
import nester
new_man = []
other_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
    with open('other_data.txt', 'rb') as other_file:
        other_man = pickle.load(other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
nester.print_lol(new_man)
nester.print_lol(other_man)
