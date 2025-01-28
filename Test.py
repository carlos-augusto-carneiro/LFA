from State import State
from Util import Util
from PDA import PDA
class Test:
    @staticmethod
    def calc(w):
        #  E -> T+E
        #  E -> T
        #  T -> F*E
        #  T -> F
        #  F -> a
        #  F -> (E)
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')

        qa = State('qa')
        qb = State('qb')
        qi = State('qi')
        qj = State('qj')
        qm = State('qm')
        qn = State('qn')
        
        qf.setFinal()

        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, 'E')
        
        # E -> T+E
        q2.addTransition(qa, None, 'E', 'E')
        qa.addTransition(qb, None, None, '+')
        qb.addTransition(q2, None, None, 'T')


        # E -> T
        q2.addTransition(q2, None, 'E', 'T')

        # T -> F*E
        q2.addTransition(qi, None, 'T', 'E')
        qi.addTransition(qj, None, None, '*')
        qj.addTransition(q2, None, None, 'F')

        # T -> F
        q2.addTransition(q2, None, 'T', 'F')

        # F -> a
        q2.addTransition(q2, None, 'F', 'a')

        # F -> (E)
        q2.addTransition(qm, None, 'F', ')')
        qm.addTransition(qn, None, None, 'E')
        qn.addTransition(q2, None, None, '(')

        q2.addTransition(q2, 'a', 'a', None)
        q2.addTransition(q2, '+', '+', None)
        q2.addTransition(q2, '*', '*', None)
        q2.addTransition(q2, '(', '(', None)
        q2.addTransition(q2, ')', ')', None)


        q2.addTransition(qf, None, '$', None)

        pda = PDA(q0)
        pda.makeLog()
        b = pda.run(q0, w, 0, ['$'])  

        Util.checkout(b, w)

    @staticmethod
    def teste_y_x(w):
        #print("{ w in Σ^* | w é um número binario multiplo de 3}")
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        q0.setFinal()

        q0.addTransition(q0, '0', None, None)
        q0.addTransition(q1, '1', None, None)
        q1.addTransition(q0, '1', None, None)
        q1.addTransition(q2, '0', None, None)
        q2.addTransition(q2, '1', None, None)
        q2.addTransition(q1, '0', None, None)

        pda = PDA(q0)
        b = pda.run(q0, w, 0, ['$'])  
        Util.checkout(b, w)

    @staticmethod
    def reverso(w): #L = { ww^R | w in Σ^*={0,1}}
        q1 = State('q1')
        q2 = State('q2')
        q3 = State('q3')
        q4 = State('q4')
        q4.setFinal()
        
        q1.addTransition(q2, None, None, '$')	
        q2.addTransition(q2, '0', None, '0')
        q2.addTransition(q2, '1', None, '1')
        q2.addTransition(q3, None, None, None)
        q3.addTransition(q3, '0', '0', None)
        q3.addTransition(q3, '1', '1', None)
        q3.addTransition(q4, None, '$', None)

        pda = PDA(q1)
        b = pda.run(q1, w, 0, ['$'])  
        Util.checkout(b,w)

    @staticmethod
    def while_grammar(w):
        q0 = State('q0')  
        q1 = State('q1')  
        q2 = State('q2')  

        q2.setFinal()  

        
        # Transições para reconhecer "eqt"
        q0.addTransition(q1, 'e', None, None) 
        q1.addTransition(q1, 'q', None, None)  
        q1.addTransition(q1, 't', None, None)  

        q1.addTransition(q1, '(', None, '(')  
        q1.addTransition(q1, 'a', None, None)  
        q1.addTransition(q1, ')', '(', None) 

        q1.addTransition(q1, '{', None, '{')  
        q1.addTransition(q1, 'e', None, None) 
        q1.addTransition(q1, 'q', None, None)  
        q1.addTransition(q1, 't', None, None)  
        q1.addTransition(q1, '(', None, '(')  
        q1.addTransition(q1, 'a', None, None)  
        q1.addTransition(q1, ')', '(', None)  
        q1.addTransition(q1, '{', None, '{') 
        q1.addTransition(q1, '}', '{', None)  

        # Transição para aceitar a entrada ao final
        q1.addTransition(q2, None, '$', None) 


        pda = PDA(q0)
        b = pda.run(q0, w, 0, ['$'])  
        Util.checkout(b, w)