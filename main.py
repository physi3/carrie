"Main"
import os

import vlc
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from porcupine import Porcupine

import greetings_plugin
import edulink
import yt_music_plugin
import open_weather_plugin
import media_control_plugin

class Carrie:
    "Carrie Object"
    def __init__(self):
        self.mic = sr.Microphone()
        self.speech_recogniser = sr.Recognizer()

        self.plugins = []

        self.vlc_player = vlc.Instance().media_player_new()

    def load_plugin(self, plugin):
        "Loads a plugin into carrie"
        plugin.add_carrie(self)
        self.plugins.append(plugin)

    def inp(self):
        "Gets input"
        temp_media_volume = self.vlc_player.audio_get_volume()
        print("Listening..\n")
        self.vlc_player.audio_set_volume(int(temp_media_volume*0.55))
        with self.mic as source:
            audio = self.speech_recogniser.listen(source)
            recognized_string = self.speech_recogniser.recognize_google(audio)
            print("I heard "+recognized_string)
            self.vlc_player.audio_set_volume(temp_media_volume)
            return recognized_string

    def out(self, string):
        "Outputs string (via TTS eventually)"
        temp_media_volume = self.vlc_player.audio_get_volume()
        self.vlc_player.audio_set_volume(int(temp_media_volume*0.55))
        print("\nCarrieOut")
        print(string)

        tts = gTTS(string, lang='en')
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
        self.vlc_player.audio_set_volume(temp_media_volume)

    def run_most_likely_command(self, command_string):
        """
        Runs command with highest likelyhood of waking from all plugins
        """
        working_plugins = self.plugins.copy()
        working_plugins.sort(key = lambda x: x.find_highest_probablity(command_string))
        working_plugins[-1].most_likely_command(command_string).call_function()

carrie = Carrie()

carrie.load_plugin(greetings_plugin.greetings)
carrie.load_plugin(edulink.edulink)
carrie.load_plugin(yt_music_plugin.youtube_music_plugin)
carrie.load_plugin(open_weather_plugin.weather_plugin)
carrie.load_plugin(media_control_plugin.media_control)

carrie_porcupine = Porcupine("blueberry", 0.5, lambda: carrie.run_most_likely_command(carrie.inp()))
carrie_porcupine.run()
