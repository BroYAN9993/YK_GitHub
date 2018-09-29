#!usr/bin/python
# -*- coding: utf-8 -*-
filename = 'guest_book.txt'
prompt = 'Enter your name, or enter "exit" to exit: '
with open(filename, 'a') as file_object:
    while True:
        guestname = raw_input(prompt)
        if guestname != 'exit':
            file_object.write(guestname + '\n')
        else:
            break
