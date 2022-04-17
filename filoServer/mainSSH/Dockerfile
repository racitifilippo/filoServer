FROM debian

RUN apt update && apt install -y openssh-server vim iproute2 iputils-ping

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin Yes/' /etc/ssh/sshd_config



