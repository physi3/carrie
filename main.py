"Main"
import vlc

import greetings_plugin
import edulink
import yt_music_plugin

class Carrie:
    "Carrie Object"
    def __init__(self):
        self.plugins = []
        self.vlc_player = vlc.Instance().media_player_new() #VLC

    def load_plugin(self, plugin):
        "Loads a plugin into carrie"
        plugin.add_carrie(self)
        self.plugins.append(plugin)

    def inp(self):
        "Gets input (via SR eventually)"
        return input("[>> ")

    def out(self, string):
        "Outputs string (via TTS eventually)"
        print("CarrieOut")
        print(string)

    def run_most_likely_command(self, command_string):
        """
        Returns the plugin with the highest probablility of waking
        """
        working_plugins = self.plugins.copy()
        working_plugins.sort(key = lambda x: x.find_highest_probablity(command_string))
        working_plugins[-1].most_likely_command(command_string).call_function()

carrie = Carrie()

carrie.load_plugin(greetings_plugin.greetings)
carrie.load_plugin(edulink.edulink)
carrie.load_plugin(yt_music_plugin.youtube_music_plugin)


while True:
    carrie.run_most_likely_command(carrie.inp())
