def make_album(name, title):
    music_album = {'Artist Name': name.title(), "Album's Title": title.title()}
    return music_album


message1 = make_album('radiohead', 'in rainbows')
print(message1)
message2 = make_album('tame impala', 'currents')
print(message2)
message3 = make_album('portishead', 'dummy')
print(message3)
