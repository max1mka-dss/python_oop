class MediaPlayer:
    color = 'red'
    circle =2
    def open(self,file):
        #self.file = file
        setattr(self,'filename',file)
    def play(self):
        print(f"Воспроизведение {self.filename}")

media1 = MediaPlayer()
media1.open('filemedia1')
#filemedia = 'filemedia'

media2 = MediaPlayer()
media2.open('filemedia2')

media1.play()
media2.play()
