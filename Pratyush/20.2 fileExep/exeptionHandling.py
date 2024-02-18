def divide():
    import dalBhat
    a=int(input("pls give number 1 "))
    b=int(input("pls give number 2 "))
    print(a/b)
    
    f1=open('sillyfile.txt','r')
    print(c)

def list():
    a=[None]*5
    print(a[6])


try:
    list()
except Exception as e:
    print('skill issue')
    print (e)

'''except FileNotFoundError:
    print('the file wasn not found')
except ModuleNotFoundError:
    print('silly module not found')
except IndexError:
    print('value outside index')
except:
    print('different issue')1'''