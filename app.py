import pokebase
import flask


app = flask.Flask(__name__, static_url_path='', static_folder='frontend/build')
app.config.from_object('config.DevConfig')


@app.route('/', methods=['GET', 'POST'])
def index():
    """HomePage"""
    if flask.request.method == 'POST':
        # Check if trade is valid
        # Show Flash message
        from player import Player
        from pokemon import Pokemon
        from trade_calculator import TradeCalculator


        # Receive data from form
        player_dict = {'player_1': [], 'player_2': []}
        pokemons = []
        # Iterate through form players
        for p in range(1, 3):
            # Iterate through form players select
            for i in range(1, 7):
                pokemons.append(flask.request.form[f"player{p}Select{i}"])
            # Set pokemons for each player, without empty str
            player_dict[f'player_{p}'] = list(filter(None, pokemons))
            pokemons = []  # reset list

        # Create lists of Pokemon Objects
        player_1_pokemons = []
        player_2_pokemons = []
        for pokemon_name in player_dict['player_1']:
            player_1_pokemons.append(Pokemon(pokemon_name, pokebase.pokemon(pokemon_name).base_experience))
        for pokemon_name in player_dict['player_2']:
            player_2_pokemons.append(Pokemon(pokemon_name, pokebase.pokemon(pokemon_name).base_experience))

        # Check if any pokemon was choosed, otherwise an exception is raised
        if not player_1_pokemons and not player_2_pokemons:
            flask.flash('A troca não pode ser realizada.\nNão foram selecionados pokémons para a troca!', 'danger')
        else:
            player_1 = Player(player_1_pokemons)
            player_2 = Player(player_2_pokemons)
            
            tc = TradeCalculator(player_1, player_2)

            # Check Trade
            if tc.is_trade_valid():
                flask.flash('Troca Efetuada!', 'success')
            else:
                flask.flash('A troca não pode ser realizada.\nA experiência dos pokémons difere em mais de 2 pontos!', 'danger')

        return flask.redirect(flask.url_for('index'))

    # Define list of Pokemon names
    pokebase_resource_list = pokebase.APIResourceList('pokemon')
    pokemon_list = pokebase_resource_list.__dict__['_APIResourceList__results']
    pokemon_list = [pokemon['name'] for pokemon in pokemon_list]

    return flask.render_template('index.html', pokemon_list=pokemon_list)
