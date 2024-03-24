import os

root = "music"

for path, dir, files in os.walk(root, topdown=True):
    if files:
        first_split = os.path.split(path)
        second_split = os.path.split(first_split[0])
        for f in files:
            song_details = f[:-5].split(' - ')
            print(song_details)
