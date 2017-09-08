#Eventex
Sistema de eventos enomendado pela morena

[![Build Status](https://travis-ci.org/anacnogueira/eventex-anaclaudianogueira.svg?branch=master)](https://travis-ci.org/anacnogueira/eventex-anaclaudianogueira)
[![Code Health](https://landscape.io/github/anacnogueira/eventex-anaclaudianogueira/master/landscape.svg?style=flat)](https://landscape.io/github/anacnogueira/eventex-anaclaudianogueira/master)

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências
5. COnfigure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:anacnogueira/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envio o codigo para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEGUB=False
#configuro - e-mail
git push heroku master -force
```