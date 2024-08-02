def split_message(message: str, step: int, sep: str = '\n') -> str:
    if 0 < step <= len(message):
        new_message = ''
        step2 = 0
        while step2 + step <= len(message):
            new_message += f'{message[step2 : step2 + step]}{sep}'
            step2 += step
        return new_message
    return message

if __name__ == '__main__':
    assert split_message('Привет', 2, '!') == 'Пр!ив!ет!'
    assert split_message('Привет', 3, '!') == 'При!вет!'
    assert split_message('Привет', 10, '!') == 'Привет'
    assert split_message('Привет', 6, '!') == 'Привет!'
    assert split_message('Привет', 0, '!') == 'Привет'
    assert split_message('Привет', -5, '!') == 'Привет'