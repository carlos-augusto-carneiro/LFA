import itertools
from State import State
class PDA: #PDA = (Q, Σ, δ, q0, F)
    def __init__(self, q: State):
        self.start_state = q
        self._q = q
        self._pilha = []
        self.log = True
        self._pilha.append('$')

    def makeLog(self):
        self.log = True
    
    def merge(self, transitions1, transitions2):
        return transitions1.union(transitions2)

    def run(self, q, w, k, pilha):
        transitions = set()
        if k == len(w) and q.is_final:
            #if self.log:
             #   print(f"{q.getName()}[{k}]: {self.getPilha(pilha)}")

            #self.draw(w, k, transitions)
            return True

        if k < len(w):
            #print(f"Processando: w[{k}] = {w[k] if k < len(w) else 'N/A'}, pilha[-1] = {pilha[-1] if pilha else 'N/A'}")
            transitions = self.merge(transitions, q.transitions(w[k], pilha[-1] if pilha else None))
            transitions = self.merge(transitions, q.transitions(w[k], None))
            transitions = self.merge(transitions, q.transitions(None, pilha[-1] if pilha else None))
            transitions = self.merge(transitions, q.transitions(None, None))
            #if self.log:
             #   print(f"{q.getName()}[{k}]: {self.getPilha(pilha)}")

            self.draw(w, k, transitions)

        if k == len(w):
            
            transitions = self.merge(transitions, q.transitions(None, None))
            transitions = self.merge(transitions, q.transitions(None, pilha[-1] if pilha else None))

            #if self.log:
                #print(f"{q.getName()}[{k}]: {self.getPilha(pilha)}")

            self.draw(w, k, transitions)
        
        if len(transitions) == 0:
            #if self.log:
            #    print(f"{q.getName()}[{k}]: {self.getPilha(pilha)}")

            return self.finish(w, k, transitions)


        for transition in transitions:
            edge = transition.getEdge()
            stack = pilha.copy()

            if edge.getPop() is not None and stack and edge.getPop() == stack[-1]:
                stack.pop()

            if edge.getPush() is not None:
                stack.append(edge.getPush())

            pos = k
            if edge.getC() is not None:
                pos = k + 1

            result = self.run(transition.getState(), w, pos, stack.copy())
            if result:
                return True

        return False

    def draw(self, w, k, transitions):
        pass  # ou remova os comentários e indente corretamente
        #if self.log:
        #    print(f"Estado atual: {self._q.getName()}, Posição: {k}, Transições: {transitions}")

    def finish(self, w, k, transitions):
        # Implementação do método finish
        #if self.log:
         #   print(f"Finalizando: {w} na posição {k}")
        return False  # ou True, dependendo da lógica que você deseja implementar

    def getPilha(self, pilha):
        return ''.join(pilha)  # Retorna a pilha como uma string