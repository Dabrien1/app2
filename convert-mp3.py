import pydub

sound = pydub.AudioSegment.from_mp3("service-bell_daniel_simion.mp3")
sound.export("alarm.wav", format="wav")
