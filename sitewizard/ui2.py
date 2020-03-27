import sys
from pprint import pprint
import subprocess

# todo: check out prompt-toolkit

from util import Util


class UI:

    printing = True

    @staticmethod
    def ask(question):
        ret = input(question + " ")
        if ret == "exit":
            UI.exit()
        return ret

    @staticmethod
    def pause(msg=None):
        if msg:
            print(msg)
        UI.ask("Paused. Press enter to continue.")

    @staticmethod
    def ask_integer(question):
        ret = UI.ask(question)

        if not Util.is_int(ret):
            print("Please enter an integer.")
            ret = UI.ask_integer(question)

        return int(ret)

    @staticmethod
    def ask_date(question):
        ret = UI.ask(question)

        if Util.is_date(ret):
            ret = Util.format_date(ret)
        else:
            print("Please enter a date.")
            ret = UI.ask_date(question)

        return ret

    @staticmethod
    def ask_boolean(question):
        ret = UI.ask(question)
        ret = ret.lower()

        if ret in ["y", "yes", "1", "true"]:
            return True

        if ret in ["n", "no", "0", "false"]:
            return False

        # if user is still here - they entered an invalid value- ask again

        print('Invalid entry: Please answer with either a "y" or an "n" ')
        return UI.ask_boolean(question)

    @staticmethod
    def ask_limited_choices(question, choices):
        if type(choices) is dict:
            return UI.ask_limited_dictionary_choices(question, choices)
        else:
            return UI.ask_limited_list_choices(question, choices)

    @staticmethod
    def ask_limited_list_choices(question, choices):
        for k, v in enumerate(choices):
            print("{}: {}".format(k, v))

        ret = UI.ask(question)
        ret = ret.lower()

        if Util.is_int(ret):
            ret = int(ret)
            if ret < len(choices):
                ret = choices[int(ret)]

        if ret in (choices):
            return ret

        # if user is still here - they entered an invalid value
        print("Invalid selection")
        return UI.ask_limited_list_choices(question, choices)

    @staticmethod
    def ask_limited_dictionary_choices(question, choices):
        index_key_map = {}
        for i, (k, v) in enumerate(choices.items()):
            index_key_map[i] = k
            print("{}: {} - {}".format(i, k, v))

        ret = UI.ask(question)
        ret = ret.lower()

        if Util.is_int(ret):
            ret = int(ret)
            if ret < len(choices):
                ret = index_key_map[ret]

        if ret in choices:
            return ret

        # if user is still here - they entered an invalid value
        print("Invalid selection")
        return UI.ask_limited_dictionary_choices(question, choices)

    @staticmethod
    def exit(msg=None):
        if msg is not None:
            print(msg)
        sys.exit()

    # run a shell command and return the output
    # todo - determine if UI is the best place to put this method
    @staticmethod
    def run(cmd, cwd=None):

        UI.pr("UI.run({})".format(cmd))
        if cmd == "exit":
            UI.exit()

        try:
            output = subprocess.check_output(cmd.split(), cwd=cwd, stderr=subprocess.STDOUT)
            output = output.decode().split("\n")

        # except subprocess.CalledProcessError as e:
        except Exception as e:
            UI.pause("an error occurred")
            output = e.output.decode().split("\n")

        return output

    @staticmethod
    def disable_printing():
        UI.printing = False

    @staticmethod
    def enable_printing():
        UI.printing = True

    # essentially just a print() method - but can be toggled on and off
    # rule of thumb: use print()/pprint() for debugging and UI.pr() for intended UI output
    @staticmethod
    def pr(msg=None):
        if UI.printing:
            print(msg)

    @staticmethod
    def ppr(msg=None):
        if UI.printing:
            pprint(msg)
