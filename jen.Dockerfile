FROM jenkins/jenkins:lts
USER root

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://get.docker.com/ | sh
RUN usermod -aG docker jenkins

#RUN mkdir -p /etc/systemd/system/docker.service.d
USER jenkins