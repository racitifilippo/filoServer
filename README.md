# filoServer

Questa cartella contiene due servizi: <b>SSH, Web Server</b>. 

Per avviare i servizi che vuoi esegui il file <b>start.py</b> e segui la procedura guidata.

Per stoppare i containers eseguire il file <b>stop.py</b>.


<b>Web Server</b>:
 - porta 80 dell'host e 80 del container
 - nella cartella html inserire i file della tua webapp
 - il webServer utilizzato è apache2. bisogna entrare nel container per modificare i file di apache

<b>SSH Server</b>:
 - porta 22 dell'host e 22 del container
 - il servizio ssh utilizzato è openssh-server
