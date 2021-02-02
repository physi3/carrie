"""
Greetings plugin for Carrie
"""

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

greetings = plugins.Plugin()


#Hello World Command
helloWF = lambda x: wf.key_word(x, ["hello"])
helloFunc = lambda: plugins.out("Hello")
helloCommand = plugins.Command([helloWF],helloFunc)

greetings.add_command(helloCommand)


#Test
IN = "good morning"
if helloCommand.check_wake(IN):
    helloCommand.call_function()
