#!/usr/bin/env python3
tel_list = {
    "Kamil": "+7963258125",
    "Ali": "+76325879",
    "Sonya": "+79365891"
}
uname = input('Чей телефон нужен?: ')
utel = tel_list.get(uname, 'Не найден')
print(utel)
