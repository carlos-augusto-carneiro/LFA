# .\.venv\Scripts\python.exe -m pip install readchar #import threading #import readchar
from Test import *
import time
import sys

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Tempo de execução de {func.__name__}: {end_time - start_time:.6f} segundos")
    return result

def increase_depth(s, times):
    inner = s
    for _ in range(times):
        inner = f'eqt(a){{{inner}}}'
    return inner

if __name__ == "__main__": 

    sys.setrecursionlimit(100000)

    print("\n"+"\033[43m" + "=" * 40 + "\033[0m")  
    print("\033[36m" + "Número Binário Múltiplos de 3" + "\033[0m")  
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  
    measure_time(Test.teste_y_x, '00001111')
    measure_time(Test.teste_y_x, '00001110')

    print("\n" + "\033[43m" + "=" * 40 + "\033[0m")  
    print("\033[36m" + "Reverso" + "\033[0m")  
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  
    measure_time(Test.reverso, '1001001001')
    measure_time(Test.reverso, '10101010101')

    print("\n"+"\033[43m" + "=" * 40 + "\033[0m")  
    print("\033[36m" + "While" + "\033[0m")  
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  
    measure_time(Test.while_grammar, 'eqt(a){eqt(a){}}')
    deep_string = increase_depth('eqt(a){}', 6000)
    measure_time(Test.while_grammar, deep_string)
    measure_time(Test.while_grammar, 'eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){}}}}}}}}}}}}}}}}')
    measure_time(Test.while_grammar, 'eqt(a){eqt(a){')
    print("\n")



