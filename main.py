# .\.venv\Scripts\python.exe -m pip install readchar #import threading #import readchar
from Test import *


if __name__ == "__main__": 

    print("\n"+"\033[43m" + "=" * 40 + "\033[0m")  
    print("\033[36m" + "Teste de Expressão Aritmética" + "\033[0m")  
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  
    Test.calc('a+a')
    Test.calc('a*a+(a+a)')
    Test.calc('a+(')

    print("\n"+"\033[43m" + "=" * 40 + "\033[0m")  # Sinais de igual em amarelo
    print("\033[36m" + "Número Binário Múltiplos de 3" + "\033[0m")  # Texto em ciano
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  # Sinais de igual em amarelo
    Test.teste_y_x('00001111')
    Test.teste_y_x('00001110')

    print("\n" + "\033[43m" + "=" * 40 + "\033[0m")  # Sinais de igual em amarelo
    print("\033[36m" + "Reverso" + "\033[0m")  # Texto "Reverso" em ciano
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  # Sinais de igual em amarelo
    Test.reverso('1001001001')
    Test.reverso('10101010101')

    print("\n"+"\033[43m" + "=" * 40 + "\033[0m")  # Caixa amarela
    print("\033[36m" + "While" + "\033[0m")  # Texto "While" em ciano
    print("\033[43m" + "=" * 40 + "\033[0m"+"\n")  # Caixa amarela
    Test.while_grammar('eqt(a){eqt(a){}}')
    Test.while_grammar('eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){}}}}}}}}}}}}}}}}')
    Test.while_grammar('eqt(a){eqt(a){}')
    print("\n")



