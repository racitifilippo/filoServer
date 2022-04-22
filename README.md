# filoServer

Questa cartella contiene due servizi: <br>SSH, Web Server</br>. 

Per avviare i servizi che vuoi esegui il file <br>start.py</br> e segui la procedura guidata.

Per stoppare i containers eseguire il file <br>stop.py</br>.


<br>Web Server</br>:
 - porta 80 dell'host e 80 del container
 - nella cartella html inserire i file della tua webapp
 - il webServer utilizzato è apache2. bisogna entrare nel container per modificare i file di apache

<br>SSH Server</br>:
 - porta 22 dell'host e 22 del container
 - il servizio ssh utilizzato è openssh-server
