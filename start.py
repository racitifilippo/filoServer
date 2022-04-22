import os


sel = input('Quali server vuoi avviare? (Scrivere il numero seguito dagli spazi)\n   -1) SSH Server\n   -2) Web Server\n')

# Metto insieme tutti i pezzi per il docker-compose file
comp = 'version: "3.9"\n\nservices:\n'
if '1' in sel:
    comp += open("SSHServer/dock-comp.txt").read()
    comp += "\n\n"
if '2' in sel:
    comp += open("webServer/dock-comp.txt").read()
    comp += "\n\n"
comp += open("network.txt", "r").read()
try:
    dockerCompose = open("docker-compose.yaml", "w")
    dockerCompose.write(comp)
    dockerCompose.flush()
    dockerCompose.close()
    #print('----Docker compose CREATO')
except:
    print('----Docker compose NON CREATO')
    exit() 


# Chiusura vecchi containers se gia in esecuzione ed eliminazione vecchie immagini
os.system('docker-compose -f docker-compose-old.yaml down')
image = os.popen('docker image ls').read().split('\n')
image = image[:len(image)-1]
for i in range (len(image)):
    arr = image[i].split(' ')
    l = len(arr)
    for ii in range(len(arr)):
        if arr[l-1-ii] == '':
            arr.pop(l-ii-1)
    #print(arr)

    if (arr[0] == 'debian_web-server') or (arr[0] == 'debian_ssh'):
        os.system('docker image rm ' + arr[2])
    

# Creazione delle immagini e dei containers con il docker compose up
try:
    print('---- Creazione delle immagini e dei container')
    os.system('docker-compose up -d --build')
    print('---- Creazione avvenuta')
    old = open('docker-compose-old.yaml', 'w')
    old.write(comp)
    old.flush()
    old.close()
except:
    print('---- Creazione NON avvenuta')
    exit()


# Avvio di tutti i servizi
processi = os.popen('docker ps').read().split('\n')
processi = processi[:len(processi)-1]
for i in range (len(processi)):
    arr = processi[i].split('   ')
    if arr[1] == 'debian_web-server':
        os.system('docker exec -it ' + arr[0] + ' service apache2 start')
        print('---- Web Server in ESECUZIONE')
    if arr[1] == 'debian_ssh':
        os.system('docker exec -it ' + arr[0] + ' bash')
        os.system('passwd')
        os.system('ciao')
        os.system('ciao')
        os.system('service ssh start')
        print('---- SSH Server in ESECUZIONE')

