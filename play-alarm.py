import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("alarm.wav")
play_obj = wave_obj.play()
