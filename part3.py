import os
if os.path.exists('sketch.txt'):
# the_file = open('sketch.txt')
# for each_line in the_file:
#     if not each_line.find(':') == -1:
#         (talker, words) = each_line.split(':', 1)
#         print(talker + ' said:', end='')
#         print(words)
# the_file.close()
    the_file = open('sketch.txt')
    for each_line in the_file:
        try:
            (talker, words) = each_line.split(':', 1)
            print(talker + ' said:', end='')
            print(words)
        except ValueError:
            pass
    the_file.close()
else:
    print('The data file is missing!')