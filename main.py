# .\.venv\Scripts\python.exe -m pip install readchar #import threading #import readchar
from Test import *
from colorama import Fore, Style, init


if __name__ == "__main__": 
    init(autoreset=True)

    print(Fore.YELLOW + "=" * 40)
    print(Fore.CYAN + "Teste de Expressão Aritmética")
    print(Fore.YELLOW + "=" * 40)
    Test.calc(Fore.GREEN + 'a+a')
    Test.calc(Fore.GREEN + 'a*a+(a+a)')
    Test.calc(Fore.RED + 'a+(')

    print("\n" + Fore.YELLOW + "=" * 40)
    print(Fore.CYAN + "Número Binário Múltiplos de 3")
    print(Fore.YELLOW + "=" * 40)
    Test.teste_y_x(Fore.GREEN + '00001111')
    Test.teste_y_x(Fore.RED + '00001110')

    print("\n" + Fore.YELLOW + "=" * 40)
    print(Fore.CYAN + "Reverso")
    print(Fore.YELLOW + "=" * 40)
    Test.reverso(Fore.GREEN + '1001001001')
    Test.reverso(Fore.RED + '10101010101')

    print(Fore.YELLOW + "=" * 40)  # Caixa amarela
    print(Fore.CYAN + "While")  # Texto "While" em ciano
    print(Fore.YELLOW + "=" * 40)  # Caixa amarela
    Test.while_grammar(Fore.GREEN + 'eqt(a){eqt(a){}}')
    Test.while_grammar(Fore.GREEN + 'eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){eqt(a){}}}}}}}}}}}}}}}}')
    Test.while_grammar(Fore.RED + 'eqt(a){eqt(a){}')




