from sympy import *
from sympy import plot_implicit, cos, sin, symbols, Eq, And
x, y, z = symbols('x y z')
init_printing(use_unicode=True)#O que significa essa linha?

'''
Descrição de como o usuario deve usar
'''
print('Para que apareça todos gráficos, é nescessario que se deva ir "fechando" para que os algorimos consecutivos sejam executados') 

'''
Valor da constantes de A, que deverá ser fornecido pelo o usuario
'''

a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
d=-b
if a==0 and b==0 and c==0:
    print('ATENÇÃO!')
    print('Não nescessidade de se calcular as derivadas e plotar o graficos, pois serão todos nulos')
'''
Formulas das expresões
'''
BL0=((a+c)-((b**2)+(a-c)**2)**(1/2))
alfa=((((b**2)+(a-c)**2)**(1/2)+(a+c))/(((b**2)+(a-c)**2)**(1/2)-(a+c)))
A=(1/2)*(BL0)*((y**2)-(alfa)*(x**2))
A1=-A
E=Eq(A, 1)
E1=Eq(A1,1)

'''
Calculo das derivadas
'''
Bx=diff(A, y)
By=diff(-A, x)
soma=Bx-By
vetor=[Bx,By]#Estou tentando plotar esse vetor, não consegui ainda

print('A componente Bx será:')
print(Bx)
print('A componente By será:')
print(By)
print('O valor da alfa é:')
print(alfa)

'''
Gráfico de Bx e By respectivamente
'''
x, y = symbols('x y')
from sympy import symbols
from sympy.plotting import plot
print('Grafico de Bx será:')
x = symbols('x')
plot(Bx,title='Gráfico de Bx')
print('Grafico de By será:')
plot(By,title='Gráfico de By')

'''
Gráfico do B total
'''
print('O Grafico do B total será:')
x, y = symbols('x y')
p1 = plot_implicit(Eq(soma, 1))
if alfa<0:
    print('A equação do potencial vetor é:')
    print(E)
if alfa==-1:
    print('A equação do potencial vetor é:')
    print(E)
if alfa>0:
    print('A equação do potencial vetor em x é:')
    print(E)
    print('A equação do potencial vetor em y é:')
    print(E1)
    
'''
Examinando os pontos neutros
'''
 
if alfa<0:
    print('As linhas de campo são elípticas, e neste caso, a origem é referida como um ponto neutro tipo-O, como será apresentado no grafico em 2 dimensões')
    x, y = symbols('x y')
    p1 = plot_implicit(Eq(A, 1),title='Ponto Neutro tipo O')
if alfa==-1:
    print(' As linhas de campo são circulares, como será apresentado no grafico em 2 dimensões')
    x, y = symbols('x y')
    p1 = plot_implicit(Eq(A, 1))
if alfa>0:
    print(' As linhas de campo têm forma hiperbólica e existe um ponto neutro tipo-X ou linha-X, como será apresentado no grafico em 2 dimensões')
    p1 = plot_implicit(Eq(A, 1),title='Ponto Neutro tipo X no eixo x')
    p2 = plot_implicit(Eq(A1, 1),title='Ponto Neutro tipo X no eixo y')
#Mano estou tendo plotar os graficos das equações A e A1 em mesmo plano cartesiano, no caso aí, ele está
#plotanto um de cada vez.
