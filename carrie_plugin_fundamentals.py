"""
Carrie Plugin Fundementals
"""

class Plugin:
    """
    A plugin for CarrieAIAssistant
    """

    def __init__(self):
        self.commands = []

    def add_command(self, command):
        """
        Add a command to a CarrieAIAssistant plugin module
        """
        self.commands.append(command)

class Command:
    """
    A command for a CarrieAIAssistant plugin module
    """

    def __init__(self, wake_functions, call_function):
        self.wake_functions = wake_functions
        self.call_function = call_function

    def check_wake(self, command_string):
        """
        Check all a command's wake functions for its highest probabilty
        """
        return max(map(lambda x: x(command_string), self.wake_functions))
        