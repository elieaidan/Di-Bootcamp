class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)   
        
ibelieve = Song(["I believe I can fly, I believe I can touch the sky"])

ibelieve.sing_me_a_song()

