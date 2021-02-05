"""
Greetings plugin for Carrie
"""

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

greetings = plugins.Plugin()

#Hello World Command

helloWF = [lambda x: wf.multi_key_word(x, ["hello","hi","hiya","gooday"]),
lambda x: wf.multi_key_word(x, ["good",["morning","day","afternoon","evening"]])]

helloFunc = lambda: greetings.out("Hello")
helloCommand = plugins.Command(helloWF,helloFunc)

greetings.add_command(helloCommand)


#Test
if __name__ == '__main__':
    while True:
        IN = input("[>> ")
        if greetings.find_highest_probablity(IN):
            greetings.most_likely_command(IN).call_function()
