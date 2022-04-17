# filoServer

Questa cartella contiene tre servizi: SSH, Web Server e una bossa di un server DNS (ancora in via di sviluppo). 

Per creare i vari containers creare una finestra di terminale nella cartella e digitare --> docker-compose up -d --build

Dopo aver creato i vari containers, dobbiamo startarli manualmente entrando in ogni containers e digitanto nella sua riga di comando:
  - Per quanto riguarda il container <b>SSH</b> bisogna scrivere --> service ssh start
  - Per il servizio <b>Web Server</b> dobbiamo scrivere --> service apache2 start

Nella prossima versione ci sara un modo per inserire automaticamente i file del Web Server da una cartella che ci sara nei file del progetto alla sua cartella apposita nel container. 
