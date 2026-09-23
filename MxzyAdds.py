import os
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Enter():
    print()
    input('Premi Enter per continuare--}')