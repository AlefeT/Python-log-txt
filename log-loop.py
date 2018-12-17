# -*- coding: utf-8 -*-
#!/usr/bin/python3


#Importa bibliotecas
print('\n\n\nImportando bibliotecas...')

import time
import sys

print('Bibliotecas importadas!')



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# [ Funcao de escrever Log ]
def log_write(str):
    try:
        # Abre o arquivo de Log
        log = open("log.txt", "a")
        # Escreve str no Log
        log.write(str)
        # Fecha o arquivo Log
        log.close()

    except Exception as E:
        print(E)
        time.sleep(3600)
        sys.exit()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# [ Inicia o Log ".txt" ]
log_write('\n\n\n\n- - - - - - - - - - Log iniciado! - - - - - - - - - -\n')
print('\n\n\n- - - Log iniciado! - - -')


# [ Loop exemplo para salvar log a cada loop ]
for i in range(11):
        log_write('\n\nIniciando o loop ' + str(i) + '\n')
        print('\nIniciando o loop ' + str(i) + '...')
        time.sleep(1)

        if i >= 10:
            log_write('\n\n\n- - - - - - - - - - Finalizando Log. - - - - - - - - - -')
            print('\n\n- - - Finalizando Log. - - -')
            time.sleep(10)
            sys.exit()



