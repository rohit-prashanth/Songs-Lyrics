song_list = ["anyone-JUSTIN_BIEBER","be_sweet-MICHELLE_ZAUNER","control-MANNEQUIN_PUSSY",
             "good_days-SZA","leave_the_door_open-BRUNO_MARS","oversharers_anonymous-WILD_PINK",
             "pick_up_your_feelings-JAZMINE_SULLIVAN","rainforest-NONAME","shelter_song-ICEAGE",
             "skin-SABRINA_CARPENTER","up-CARDI_B","wilder_days-MORGAN_WADE"]

def song_List():
    print("-----Here's the List of songs-----\n")
    for i in range(len(song_list)):
        print(f"{i+1} - {song_list[i]}")
    while True:
        option = int(input("Enter your choice: "))
        if option > 12 or option < 1:
            print("You have Entered Wrong, Please enter correct choice!.")
            continue
        else:
            return option-1
     
VALIDITY = True
while VALIDITY:
    print("Welcome to 'Songs-&-Lyrics'\n")
    option = song_List()
    path = f"C:\\Users\\rohit\\OneDrive\\Desktop\\songs_lyrics\\{song_list[option]}.txt"
    lyrics = open(path,"r")
    print(f"Your lyrics for song '{song_list[option]}' is right below. Enjoy!!\n")
    print(lyrics.read())
    print("\n")
    while VALIDITY:
        choice = input("\nDo you want to Enjoy More?? Enter-'*' or else Enter-'quit' :- ")
        if choice == '*':
            break
        elif choice == 'quit':
            print("\nAdiós amigo!, Powering Off.")
            VALIDITY = False
        else:
            print("\nPlease, Enter correct choice!!")
            continue
        
