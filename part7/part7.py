import pickle
from athletelist import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        data_list = data.strip().split(',')
        return (AthleteList(data_list.pop(0), data_list.pop(0), data_list))
    except IOError as ioerr:
        print('File error (get_coach_data): ' + str(ioerr))
        return (None)


def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as ath_file:
            pickle.dump(all_athletes, ath_file)
    except IOError as ioerr:
        print('File error(put and store): ' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as ath_file:
            all_athletes = pickle.load(ath_file)
    except IOError as ioerr:
        print('File error(get_from_store): ' + str(ioerr))
    return all_athletes

