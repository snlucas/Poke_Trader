# Poke_Trader
 Calculadora para troca de Pokémons.
 Para realizar uma troca, é levado em consideração um número máximo de Pokémons (6 por padrão).


## Status
- [x] Aplicação com verificação de troca.
- [x] Deploy no Heroku.
- [ ] Dockerfile para aplicação local.
- [ ] Sistema de cadastro/login.
- [ ] Registro de trocas.
- [ ] Página de registro de trocas.
- [ ] Diminuir requests para tornar a aplicação mais rápida e eliminar timeouts.


## Como Rodar
- [Deploy](https://flask-poke-trader.herokuapp.com/)
- <em>Usando Python:</em>
  - $ pip install -r requirements.txt
  - $ flask run
    -  Se necessário:
      - Linux (Unix): 
      - $ export FLASK_APP=app.py
      - $ export FLASK_ENV=development 
      
      - Windows:
      - $ set FLASK_APP=app.py
      - $ set FLASK_ENV=development
