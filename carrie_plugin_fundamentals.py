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
    def __init__(self, wake_function):
        self.wake_function = wake_function
