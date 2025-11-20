import requests
from bs4 import BeautifulSoup
import json

# Fetch game compatibility information from its eshop page.
def fetch_game_status(game):
    request = requests.get(game['url'])
    soup = BeautifulSoup(request.content, 'html.parser')
    game_data = json.loads(soup.find(id="__NEXT_DATA__").text)
            

# For debugging: output site's json to file for reading         
    # with open("utils/assets/test.json", 'w') as json_file:
    #     json.dump(game_data, json_file, indent=2)
    # json_file.close()

    status = game.copy()
    if 'product' in game_data['props']['pageProps']['analytics']:
        sku = game_data['props']['pageProps']['analytics']['product']['sku']
        compatibility = (game_data['props']['pageProps']['initialApolloState']
                     #['StoreProduct:{\"sku\":\"' + sku + '\",\"locale\":\"en_US\"}']['compatibility'])   --- old site format
                     ['Product:{\"sku\":\"' + sku + '\"}']['compatibility'])
        if compatibility is None:
            status['status'] = 'info_missing'
        else:
            status.update(compatibility)
    else:
        status["status"] = '404'
    return status

data = []  # Data to read from
out_data = []  # Data to write to
def main():
    with open("src/json/game_list.json") as file:
        data = json.load(file)
        file.close()
    open("src/json/game_statuses.json", 'w').close()  # Clear file
    with open("src/json/game_statuses.json", 'a') as outfile:
        count = 0
        for game in data:
            # if count > 10:  # Debugging
                # break
            print("fetching " + game['title'])
            out_data.append(fetch_game_status(game))
            # count += 1  # Debugging
        json.dump(out_data, outfile, indent=2)
        file.close()

if __name__ == "__main__":
    main()