"""
VLC media control plugin for Carrie
"""

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

media_control = plugins.Plugin()

media_control.add_command(plugins.Command([lambda x: wf.key_word(x, ["pause"])],
lambda: media_control.carrie.vlc_player.set_pause(1)))

media_control.add_command(plugins.Command([lambda x: wf.multi_key_word(x, [["unpause","resume"]])],
lambda: media_control.carrie.vlc_player.set_pause(0)))

media_control.add_command(plugins.Command([lambda x: wf.key_word(x, ["turn","down","volume"])],
lambda: media_control.carrie.vlc_player.audio_set_volume(
    int(media_control.carrie.vlc_player.audio_get_volume()-20)
)))

media_control.add_command(plugins.Command([lambda x: wf.key_word(x, ["turn","up","volume"])],
lambda: media_control.carrie.vlc_player.audio_set_volume(
    int(media_control.carrie.vlc_player.audio_get_volume()+20)
)))
