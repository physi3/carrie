"""
Carrie Plugin Fundementals
"""

class Plugin:
    """
    A plugin for CarrieAIAssistant
    """

    def __init__(self):
        self.commands = []
        self.carrie = None

    def add_command(self, command):
        """
        Add a command to a CarrieAIAssistant plugin module
        """
        self.commands.append(command)

    def find_highest_probablity(self, command_string):
        """
        Check all commands for highest probabilty
        """
        return max(map(lambda x: x.check_wake(command_string), self.commands))

    def mosts_likely_command(self, command_string):
        """
        Returns the command with the highest probablility of waking
        """
        working_funcs = self.commands.copy()
        working_funcs.sort(key = lambda x: x.check_wake(command_string))
        return working_funcs[-1]

    def out(self, string):
        """
        Carrie output (TAS)
        """
        if self.carrie is None:
            print(string)
        else:
            self.carrie.out(string)

    def wait_for_in(self):
        """
        Get's input from Carrie
        """
        return input("[>>")

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
