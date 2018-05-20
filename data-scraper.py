import datetime
import requests

general_data_url = 'https://fantasy.premierleague.com/drf/elements/'
xtd_player_data_url = 'https://fantasy.premierleague.com/drf/element-summary/'
out_dir = 'scraped_data/'

# Retrieves the general data
gen_data = requests.get(general_data_url).json()

# For each player in the general data, receives their player data and appends it to the general data for the player
full_data = {}
for gen_player_data in gen_data:
    player_id = gen_player_data['id']
    xtd_player_data = requests.get(xtd_player_data_url + str(player_id)).json()

    full_player_data = gen_player_data
    full_player_data.update(xtd_player_data)
    full_data[player_id] = full_player_data

# Writes the data to a file
with open(out_dir + str(datetime.datetime.now()), "w") as text_file:
    print(full_data, file=text_file)
