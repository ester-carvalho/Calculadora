def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def main():
    x = int(input('x?'))
    y = int(input('y?'))
    s = soma(x, y)
    sb = subtracao(x, y)
    print(f'soma ={s}')
    sb = subtracao(x, y)
    print(f'subtracao ={sb}')
    
main()
