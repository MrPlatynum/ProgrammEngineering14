#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def replace_repeated_chars(replace_char):
    def inner_function(input_string):
        result = ''
        prev_char = ''

        for char in input_string:
            if char != prev_char:
                result += char
                prev_char = char
            else:
                result += replace_char

        return result

    return inner_function


if __name__ == "__main__":
    replace_func = replace_repeated_chars(
        input('Введите символ, на который необходимо заменить повторяющиеся символы: '))
    result = replace_func(input('Введите строку: '))
    print(result)  # выводим результат работы внутренней функции
