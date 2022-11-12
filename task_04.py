# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random as rnd

rand_songs = rnd.choices(my_favorite_songs, k = 3)

f_name = rand_songs[0][0]
s_name = rand_songs[1][0]
t_name = rand_songs[2][0]

f_timestamp = rand_songs[0][1]
s_timestamp = rand_songs[1][1]
t_timestamp = rand_songs[2][1]

time_sum = round((f_timestamp + s_timestamp + t_timestamp))

print('Длина "{}" - {}'.format(f_name, f_timestamp))
print('Длина "{}" - {}'.format(s_name, s_timestamp))
print('Длина "{}" - {}'.format(t_name, t_timestamp))
print('Три песни звучат',("%.2f"%(time_sum)),'минут')

# Отлично! Можно ещё так
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
