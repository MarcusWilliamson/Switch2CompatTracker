import requests
from bs4 import BeautifulSoup
import json

# Fetch game compatibility information from its eshop page.
def fetch_game_status(game):
    request = requests.get(game['url'])
    soup = BeautifulSoup(request.content, 'html.parser')
    game_data = json.loads(soup.find(id="__NEXT_DATA__").text)

    status = game.copy()
    if 'product' in game_data['props']['pageProps']['analytics']:
        sku = game_data['props']['pageProps']['analytics']['product']['sku']
        compatibility = (game_data['props']['pageProps']['initialApolloState']
                     ['StoreProduct:{\"sku\":\"' + sku + '\",\"locale\":\"en_US\"}']['compatibility'])
        print(compatibility)
        if compatibility is None:
            status['status'] = 'info_missing'
        else:
            status.update(compatibility)
    else:
        status["status"] = '404'
    return status

data = []
def main():
    with open("../json/game_list.json") as file:
        data = json.load(file)
        file.close()
    open("../json/game_statuses.json", 'w').close()  # Clear file
    with open("../json/game_statuses.json", 'a') as outfile:
        for game in data:
            print("fetching " + game['title'])
            status = fetch_game_status(game)
            json.dump(status, outfile, indent=2)
        file.close()

if __name__ == "__main__":
    main()