## Django Tutorial

Arquivo criado com intuíto de facilitar a instalação e o funcionamento do framework Django juntamente do software Docker para o desenvolvimento de websites.
 
-----------------------------------------------------------------------------------------------------------

### Tecnologia:
 
* Django version  3.0.3
* Docker version 2.4.0.0
 
-----------------------------------------------------------------------------------------------------------
 
### Instalação Docker:

```
link: https://www.docker.com/products/docker-desktop
```

* Selecione a versão instavel do Docker, exemplo: Download for Windows (stable), desta forma será feito o download da versão mais instável do docker.

* Execute-o e o instale, não há necessidade de fazer nenhuma configuração na instalação.
 
-----------------------------------------------------------------------------------------------------------

### Iniciando Docker:
* Caso ocorra algum erro ao inicia-lo relacionado a virtualização, procure na internet sobre como o ativar a virtualização, pois, a diferentes maneiras de ativa-lo tanto na INTEL quanto AMD. 

* Caso ocorra algum erro sobre WSL 2, você poderá desativa-lo em configurações do Docker em General>Use the WSL 2 based engine, desta maneira ele funciona-rá normalmente, caso deseja ativa-lo, pesquise sobre na documentação do Django.

* Caso ocorra algum erro sobre Quantidade de memória ram indisponivel, vá em Configurações>Resources e diminua a quantidade de memória ram utilizada.

-----------------------------------------------------------------------------------------------------------

### Configuração Docker: 
* Para configurar o Docker, inicie-o, redirecione-se para Configurações>Resources, configure-o de acordo com a força imposto em seu hardware.

* Minha Máquina Utilizada Ex: 
```
Processador: Pentium G 4400 2/2

Memoria RAM: 4GB
```

* Minhas Configurações Docker Ex: 

```
CPU'S: 1

Memory: 1.00GB

Swap: 1GB

Disk image size: 64gb
```

### Configurando o Projeto

na pasta raiz do projeto, vá em brinquedoteca, crie uma cópia do settings_local.py.example, cole na mesma pasta e renomeie a cópia para settings_local.py 

como ainda não temos banco de dados, não há necessidade de fazer nenhuma configuração :-)

-----------------------------------------------------------------------------------------------------------

### Rodando Docker & Django:

Inicie a aplicação do Docker.

Com ela iniciada, é necessário se posicionar com o terminal aberto na pasta raiz do projeto.

Ao rodar o comando, aparecerá uma mensagem do docker querendo compartilhar a aplicação, aceite-a. "Share It"

Para rodar a aplicação pela primeira vez, é necessário rodar esses quatro comandos.

constrói uma imagem da aplicação
```
docker-compose up --build
```

cria as tabelas da aplicação
```
docker-compose exec web python manage.py makemigrations
```

migra as informações para o banco de dados
```
docker-compose exec web python manage.py migrate
```

cria um super usuário para utiliza-lo no Django Admin
```
docker-compose exec web python manage.py createsuperuser
```

-----------------------------------------------------------------------------------------------------------

### Comandos Docker & Django:

para ativar a aplicação
```
docker-compose up
```

para desativar a aplicação
```
docker-compose down
```

para reiniciar a aplicação
```
docker-compose restart
```

para ver as aplicações ativas
```
docker ps
```

-----------------------------------------------------------------------------------------------------------

### Visualizar WebSite:

copie e cole o link no navegador.

127.0.0.1:8000

ou

localhost:8000

-----------------------------------------------------------------------------------------------------------

### Adicionando Atividades ao WebSite:

Com o docker ativo, django funcionando.

copie e cole o link no navegador.

127.0.0.1:8000/admin

ou 

localhost:8000/admin

Utilize o super usuário e senha que você criou para se conectar.

Clique em atividades e as adicione.
