import itertools
from State import State
class PDA: #PDA = (Q, Σ, δ, q0, F)
    def __init__(self, q: State):
        self.start_state = q
        self._q = q
        self._pilha = []
        self.log = False
        self._pilha.append('#')
    
    def run(self, input_string):
        stack = ['$']  # Inicializa a pilha com o símbolo de início
        #for char in input_string:
        #    if char in ['e', 'q', 't', '(', 'a', ')', '{', '}']:  # Verifica se o caractere é um dos desejados
        #        stack.append(char)

        current_state = self.start_state

        for char in input_string:
            print(f'Processando: {char}, Estado atual: {current_state.getName()}, Pilha: {stack}')
            transition_found = False
            top_symbol = stack[-1] if stack else None  # Verifica o topo da pilha

            # Procura por transições com o símbolo atual e o topo da pilha
            for transition in current_state.transitions(char, top_symbol):
                if transition.getEdge().getPop() is None or (top_symbol and top_symbol == transition.getEdge().getPop()):
                    print(f'Transição encontrada: {transition}')
                    if transition.getEdge().getPop():
                        stack.pop()  # Desempilha o símbolo
                    if transition.getEdge().getPush():
                        stack.append(transition.getEdge().getPush())  # Empilha o novo símbolo
                    current_state = transition.getState()  # Muda para o próximo estado
                    transition_found = True
                    break

            if not transition_found:
                print(f'Transição não encontrada para {char}')
                return False  # Retorna falso se não encontrar transição

        # Processa transições epsilon após consumir toda a entrada
        while True:
            transition_found = False
            top_symbol = stack[-1] if stack else None  # Verifica o topo da pilha

            for transition in current_state.transitions(None, top_symbol):
                if transition.getEdge().getC() is None and (not transition.getEdge().getPop() or (top_symbol and top_symbol == transition.getEdge().getPop())):
                    print(f'Transição epsilon encontrada: {transition}')
                    if transition.getEdge().getPop():
                        stack.pop()  # Desempilha o símbolo
                    if transition.getEdge().getPush():
                        stack.append(transition.getEdge().getPush())  # Empilha o novo símbolo
                    current_state = transition.getState()  # Muda para o próximo estado
                    transition_found = True
                    break

            if not transition_found:
                break  # Sai do loop se não houver mais transições

        # Verifica se o estado final é aceito e se a pilha está vazia ou contém apenas o símbolo de início
        result = current_state.isFinal() and (not stack or stack == ['$'])
        if result:
            print(f'Reconheceu: {input_string}')
        else:
            print(f'Rejeitou: {input_string}')
        return result