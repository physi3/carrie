"""
Edulink plugin for Carrie
"""

import requests
import ics
import arrow

import carrie_plugin_fundamentals as plugins
import wake_functions as wf
import human_readablilty_methods as hr

def humanize_event(event):
    "Rewrites an ics.Event into a string that is more human readable."
    return "{0.name} in {0.location} {1}".format(event,event.begin.humanize())

def get_timeline():
    "Get's edulink timeline from .edulinkurl."
    with open(".edulinkurl") as url_text:
        return ics.Calendar(requests.get(url_text.read()).text).timeline

edulink = plugins.Plugin()

#Next Lesson Command
wake_func = [lambda x: wf.multi_key_word(x, [["what","what's"],"next","lesson"])]

def get_next_lesson_string():
    "Return the next lesson as a human readable string."
    humanized_next_lesson = humanize_event(list(get_timeline().start_after(arrow.now()))[0])
    return "Your next lesson is {}".format(humanized_next_lesson)

edulink.add_command(plugins.Command(wake_func, lambda: plugins.out(get_next_lesson_string())))

#Today Lessons Command
wake_func = [lambda x: wf.multi_key_word(x, [["what","what's"],"lessons",["today","today's"]])]
def todays_lessons_string():
    "Returns today's lessons as a human readable string."
    lessons = hr.list_foramtting(list(map(lambda x: x.name,list(get_timeline().today()))))
    return "Your lessons today are: "+lessons+"."

edulink.add_command(plugins.Command(wake_func, lambda: plugins.out(todays_lessons_string())))

while True:
    IN = input("[>> ")
    if edulink.find_highest_probablity(IN):
        print(edulink.find_highest_probablity(IN)+100)
        edulink.mosts_likely_command(IN).call_function()
