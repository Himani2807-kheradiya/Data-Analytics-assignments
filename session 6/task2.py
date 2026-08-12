playlist_prices = {
    "Workout Mix": 99,
    "Chill Vibes": 79,
    "Party Hits": 129,
    "Bollywood Beats": 149,
    "Morning Motivation": 89
}
    

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price


update_playlist_price("Party Hits", 159)

print("Updated Playlist Prices:", playlist_prices)