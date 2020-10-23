from datetime import datetime

def new_function(path):
    def logger(function):
        def new_function(*args, **kwargs):
            date = datetime.now().date()
            time = datetime.now().time()
            result = function(*args, **kwargs)
            argum = args
            kwar = kwargs
            with open(path, 'a') as f:
                f.write(f'The function "{function.__name__}" was called {date} at {time}, with arguments:{argum},{kwar}.\n'
                        f'Result is {result} \n')
            return result
        return new_function
    return logger


@new_function('logg.txt')
def sum(a, b):
    return a + b

