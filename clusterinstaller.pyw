from typing import Literal


print('FontLoader initalisiert...')
if sys.platform == 'linux' or platform == 'linux2':
    print('Linux erkannt.')
else:
    if sys.platform == 'darwin':
        betriebssystem = 'Mac OS'
    if sys.platform == 'win32':
        betriebssystem = 'Windows'
    print('Dieser installer funktioniert nur auf Ubuntu. Auf ' + betriebssystem + 'Funktioniert dieses Programm nicht. Exiting...')
    sys.exit(0)
# Standart Benutzer
benutzer = 'administrator'
# Gebe den Pfad wohin die Schriften kopiert werden sollen
Schriften_pfad = '/usr/share/fonts/truetype/'
try:
    d = open('/home/administrator/config.txt', 'r')	
except:
    print('Failed to read config.txt')
    sys.exit(0)
    zeilen = d.readlines()
for x in range(len(zeilen)):
    zeilen = zeilen[:-1]

            
Instructions = []
for x in range(len(zeilen)):
    subinstructions = []
    a, b = zeilen[x].split(';')
    subinstructions.append(a)
    subinstructions.append(b)
    Instructions.append(subinstructions)
print(Instructions)


