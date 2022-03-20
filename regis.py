
while True:
    zapros = input('введите желаемое действие:\n''\n'
                   'просмотреть архив - 1\n'
                   'добавить данные - 2\n: ')

    if zapros == '1':
        day = input('введите дату:')
        with open('data.txt', 'r') as w:
            line = w.readline()
            while line:

                pogoda = line.split(' ')

                sdg = {int(pogoda[0]): (pogoda[1:])}

                if int(day) == int(pogoda[0]):
                    print('в искомый день была погода:'
                          '\n температура воздуха:' + pogoda[1] + ' градусов по цельсию'
                          '\n относительная влажность воздуха:' + pogoda[2] + ' процентов'
                          '\n световой поток' + pogoda[3] + ' люменов')
                    break
                line = w.readline()
            if (int(day) != int(pogoda[0])):
                print('за искомый день данных нет')


    elif zapros == '2':

        with open('data.txt', 'a') as w:

            w.write(str(input('введите дату:')) + ' ' +
                    str(input('введите температуру:')) + ' ' +
                    str(input('введите влажность:')) + ' ' +
                    str(input('введите солнечность:')) + '\n')
    else:
        print('некоррекный запроос')
