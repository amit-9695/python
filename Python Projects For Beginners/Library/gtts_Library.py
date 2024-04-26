import gtts
import playsound
txt = input("Enter your Message:- \n")
sound = gtts.gTTS(txt, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")