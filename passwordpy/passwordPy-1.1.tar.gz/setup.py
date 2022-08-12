#!/usr/bin/python

from setuptools import setup, Extension

Version = '1.1'

longDesk = '''
ENG:

create() - the function itself

length -> length

counts -> number of passwords

chars -> sets whether the password contains letters

nums -> whether the password contains numbers

symbols -> whether the password contains symbols

lowerSimbol -> sets whether the character "_" in the text with expanded space

lowerSymbolDistance -> sets the spacing of the "_" character in the text

upperLetters -> sets whether the password will contain uppercase letters

lowerLetters -> sets whether the password will contain lowercase letters

returnList -> will return the passwords as a list

If you don't enter any arguments, the function will return 1 password, 8 characters long.

Example:

    password = create(chars=false, length=16, counts=5)

    print(password)

Conclusion:
    5418074420043687

    4983825832454167

    4180923973205412

    0552142655641343

    7774606619186375


RU:

create() - сама функция

length -> длина пароля

counts -> количество паролей

chars -> задает будут ли в пароле буквы

nums -> задает будут ли в пароле цифры

symbols -> задает будут ли в пароле символы

lowerSimbol -> задает будет ли символ "_" в тексте с определенным промежутком

lowerSymbolDistance -> задает промежуток расставления символа "_" в тексте

upperLetters -> задает будут ли в пароле буквы верхнего регистра

lowerLetters -> задает будут ли в пароле буквы нижнего регистра

returnList -> вернет пароли в виде списка

Если вы не введете аргументы, то функция вернет 1 пароль длиною 8 символов.

Пример:

    password = create(chars=False, length=16, counts=5)

    print(password)

Вывод:
    5418074420043687

    4983825832454167

    4180923973205412

    0552142655641343

    7774606619186375
'''

setup(
    name='passwordPy',
    version=Version,

    author='AlmazCode',
    author_email='diamondplay43@gmail.com',

    description='Simple password generator',
    long_description=longDesk,

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['passwordPy'],

    classifiers=['License :: OSI Approved :: Apache Software License',
                'Operating System :: OS Independent',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: Developers',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Programming Language :: Python :: Implementation :: CPython'
                ]
)