class MinhaExcecao(Exception):
    pass

def funcao (x):
    if x<0 or x>100:
        raise Exception ('Valor invalido')
    elif x%2 ==0:
        raise MinhaExcecao('par não!')


def divide (a, b):
    try:    
        c= a/b
        return c
        
    except ValueError:
        print('Erro de Valor')
    
    except Exception :
       print('Sua nota abaixou')
    
    except ZeroDivisionError:
        print('Divisão por zero não')
    finally:
        print('passei por aqui')

        
        
  




    
