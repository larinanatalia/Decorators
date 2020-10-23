# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
from datetime import datetime

def logger(function):
    def new_function(*args, **kwargs):
        date = datetime.now().date()
        time = datetime.now().time()
        result = function(*args, **kwargs)
        argum = args
        kwar = kwargs
        with open ('log.txt','a') as f:
            f.write(f'The function "{function.__name__}" was called {date} at {time}, with arguments:{argum},{kwar}.\n'
                    f'Result is {result} \n')
        print(result)
    return new_function


@logger
def sum(a,b):
    return a + b




