#!/usr/bin/env python3
print('r - чтение')
print('w - перезапись или создать новый')
print('a - запись в конец')
rwa = str(input('что выбераем?: '))

#Чтение
if rwa == 'r':
    filename = str(input('Укажите файл: '))
    if filename != '':
        try:
            file = open(filename, 'r')
            print( 'В этом файле ' + str(len(file.read())) + ' символов' )
            file.close()
            y_n = str(input('Хотите посмотрет?: '))
            if y_n == 'y':
                file = open(filename, 'r')
                print('Содержимое файла ' + filename)
                print(file.read())
                file.close()
            else:
                print('Файл ' + filename + ' закрыт')
        except:
            print('Не удалось прочитать файл ' + filename)
    else:
        print('Вы не указали файл')

#Перезапись
elif rwa == 'w':
    filename = str(input('Укажите файл: '))
    text_w = str(input('что пишем?: '))
    if filename != '':
        try:
            file = open(filename, 'w')
            file.write(text_w)
            file.close()
        except:
            print('Не удалось получить файл ' + filename)
    else:
        print('Вы не указали файл')

#Запись в конец
elif rwa == 'a':
    filename = str(input('Укажите файл: '))
    text_a = str(input('что пишем?: '))
    if filename != '':
        try:
            file = open(filename, 'a')
            file.write(text_a)
            file.close()
            print('Текст добавлен в файл ' + filename)
        except:
            print('Не удалось получить файл ' + filename)
    else:
        print('Вы не указали файл')
else:
    print('Вы не указали режим работы с файлом')
