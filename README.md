<h1 align="center">Blog</h1>

<!-- <h6 align="center"> 
	Se você quiser visualizar as imagens do aplicativo, clique <a href="github/images/README.md">aqui</a>.
</h6> -->

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o Django como framework back-end e o Bootstrap como framework front-end. 

A ideia é:

_"Criar um Blog onde o mesmo tenha um design simples e belo, com intuito de promover o aprendizado e gerar um projeto completo utilizando o Django framework."_

--------------------------------------------------------------------------------------

<h3 id="tabela-de-conteudo">:ab: Tabela de Conteúdo</h3>

* [Sobre](#sobre)
* [Tabela de Conteudo](#tabela-de-conteudo)
* [Status do Projeto](#status)
* [Por Que](#por-que)
* [Tecnologias](#tecnologias)
* [Funcionalidades](#funcionalidades)
* [Instalação do Projeto](#instalando)
    * [Clonando Repositório](#clonando)
    * [Windows](#rodando-windows)
    * [Linux](#rodando-linux)
* [Comandos](#comandos)
* [Autor](#autor)
* [Licença](#license)

--------------------------------------------------------------------------------------

<h3 id="status">:heavy_exclamation_mark: Status do Projeto</h3>

<h4 align="center"> 
	🚧: Sistema Web em construção... 🚧:
</h4>

--------------------------------------------------------------------------------------

<h3 id="por-que">:question: Por Que</h3>

Este projeto faz parte do meu portfólio pessoal, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade&melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

<h3 id="tecnologias">:rocket: Tecnologias</h3>

As seguintes ferramentas foram usadas na construção do projeto:

- [Django Framework](https://www.djangoproject.com/)
- [Boostrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

--------------------------------------------------------------------------------------

<h3 id="funcionalidades">:sparkles: Funcionalidades</h3>

- [X] Possibilita a criação de pastas.
- [X] Possibilita a criação de varias sub pastas.

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

<h4 id="clonando">Clonando o Repositório</h4>

```
git clone git@github.com:LucasSantus/django-blog.git

cd django-blog
```

<h4 id="rodando">Rodando o Projeto</h4>

> Antes de rodar o projeto, é necessário configurar o settings_local.py

<h4 id="rodando-windows">
	<strong>Windows</strong>
</h4>

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

```
python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations blog

python manage.py makemigrations usuarios

python manage.py migrate

python manage.py collectstatic

python manage.py runserver
```

<h4 id="rodando-linux">
	<strong>Linux</strong>
</h4>

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Preparando Ambiente Virtual**

Com o terminal aberto, digite no terminal:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations blog

python manage.py makemigrations usuarios

python manage.py migrate

python manage.py collectstatic

python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```
**Acessando o Projeto**

para visualizar o projeto: http://127.0.0.1:8000/

**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="comandos">:paperclip: Comandos</h3>

> **Observação:** Caso tenha surgido dúvidas sobre os códigos no processo de instalação, o link abaixo contém explicações dos comandos e scripts para "automátição" do projeto.

Para melhor entendimento sobre os comandos mostrados acima, clique [aqui](COMMANDS.md).

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autor(es)</h3>

<table>
	<tr>
		<td>
			<div> 
				<a href="https://github.com/LucasSantus">
					<img style="border-radius: 50%;" src="https://github.com/LucasSantus.png" width="100px;" alt=""/>
					<br />
					Lucas Santus
				</a>
			</div>
		</td>
	</tr>
</table>
<br />
Feito com ❤️ por Lucas Santus!<br />
Obrigado por visitar e boa codificação!<br />

--------------------------------------------------------------------------------------

<h3 id="license">:memo: License</h3>

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/django-blog/blob/master/LICENSE) para melhores detalhes.

