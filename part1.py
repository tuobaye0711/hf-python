import nester

if 43 > 42:
    print("hello")
movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
print(movies[1])
print(movies)
print(len(movies))
movies.append("Hello World")
print(movies)
movies.pop()
print(movies)
movies.extend(["zzz1", "zzz2"])
print(movies)
movies.remove("zzz1")
print(movies)
movies.insert(0, "zzz0")
print(movies)
# movies.insert(1, 1990)
# movies.insert(3, 1995)
# movies.insert(5, 2000)
# movies.insert(7, 2005)
# movies.insert(9, 2010)
# print(movies)
# for movie in movies:
#     print(movie)
count = 0
while count < len(movies):
    print(movies[count])
    count = count+1
games = [['red alert 95', 'red alert 2', 'red alert 3'], 'super mario', 'tank battle',
         [['kof 97', 'kof 98', 'kof 99'], 'street fighter']]
nester.print_lol(games)