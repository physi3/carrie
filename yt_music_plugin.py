"""
Music plugin (via youtube) for Carrie
"""

import pafy
import vlc
from youtubesearchpython import VideosSearch

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

vlc_ins = vlc.Instance()

youtube_music_plugin = plugins.Plugin()

ytmusicWF = [lambda x: wf.key_word(x, ["play","music"], ordered = True),
lambda x: wf.key_word(x, ["play","music","youtube"])]

def play_yt_song(plugin, vlc_instance):
    "Plays media through parsed plugin"

    plugin.out("What song would you like to play?")
    search_term = plugin.wait_for_in()

    url = VideosSearch(search_term, limit = 1).result()["result"][0]['link']

    pafy_video = pafy.new(url)
    title = pafy_video.title
    play_url = pafy_video.getbest().url

    media = vlc_instance.media_new(play_url,":no-video")
    plugin.play_media(media, media_name = title)

play_music_command = plugins.Command(ytmusicWF, lambda: play_yt_song(youtube_music_plugin, vlc_ins))
youtube_music_plugin.add_command(play_music_command)

#Test
if __name__ == '__main__':
    while True:
        IN = input("[>> ")
        if youtube_music_plugin.find_highest_probablity(IN):
            youtube_music_plugin.most_likely_command(IN).call_function()
