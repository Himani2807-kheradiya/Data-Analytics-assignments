def sum_playlist_durations(durations):
    if len(durations) == 0:
        return 0
    return durations[0] + sum_playlist_durations(durations[1:])


durations = [180, 240, 200, 300]
print("Total duration:", sum_playlist_durations(durations), "seconds")