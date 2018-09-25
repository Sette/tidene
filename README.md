# Guia prático para uso do github

Certifique-se de ter o git instalado em sua máquina baseada em ubuntu

$ sudo apt install git

# Defina sua identidade

A primeira coisa que você deve fazer quando instalar o Git é definir o seu nome de usuário e endereço de e-mail. Isso é importante porque todos os commits no Git utilizam essas informações, e está imutavelmente anexado nos commits que você realiza:

$ git config --global user.name "John Doe"

$ git config --global user.email johndoe@example.com

# Defina seu ambiente

Escolha um local para iniciar seus repositórios git. Sugestão :

$ cd ~

$ mkdir git

$ cd git

# Clone um repositório

$ git clone https://github.com/Sette/tidene.git

$ cd tidene

# Faça um commit e um push

Logo depois de serem feitas as alterações, rode os seguintes comandos para enviar a novar versão para o repositório:

$ git add *

Este comando adiciona novos arquivos ao repositório local

$ git commit -m "Commit inicial"

Esta operação registra todas as alterações realizadas em arquivos do diretório

$ git push origin master 

Esta operação atualiza o repositório pricipal com as alterações realizadas

# Atualizando meu repositório

Caso haja alguma alteração no reposotório master, podemos atualizar o repositório local com o comando:

$ git pull
