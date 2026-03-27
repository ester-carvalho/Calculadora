def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def main():
    x = int(input('x?'))
    y = int(input('y?'))
    s = soma(x, y)
    sb = subtracao(x, y)
    print(f'Soma da Alegria ={s}')
    sb = subtracao(x, y)
    print(f'subtracao ={sb}')
    m = multiplicacao(x, y)
    print(f'multiplicacao ={m}')

    
main()
