def make_album(name, title):
    music_album = {'Artist Name': name.title(), "Album's Title": title.title()}
    return music_album


while True:
    print('Enter your favourite artist names and their titles')
    print('(feel free to press "q" anytime you want to leave this page!)')
    A_name = input('Artist name: ')
    if A_name == 'q':
        break

    A_title = input("Album's Title: ")
    if A_title == 'q':
        break

    formatted_music_album = make_album(A_name, A_title)
    print(formatted_music_album)
