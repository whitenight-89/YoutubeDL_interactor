from os import path
from subprocess import Popen, PIPE
from Exceptions import *


class YoutubeDL_interactor:
    def __init__(self, path_to_binaries):
        self.path_to_binaries = path_to_binaries
        self._check_path()

    # Checks

    def _check_path(self):
        self._check_path_validity()
        self._check_binaries_presence()

    def _check_path_validity(self):
        if not path.exists(self.path_to_binaries):
            raise PathDoesNotExistException("The given path does not exist")

    def _check_binaries_presence(self):
        binaries = ["youtube-dl.exe", "ffmpeg.exe"]

        for binary in binaries:
            self._check_binary_presence(binary)

    def _check_binary_presence(self, binary_name_with_extension):
        if not path.exists(
                path.join(self.path_to_binaries, binary_name_with_extension)):
            raise BinaryNotPresentException(f"{binary_name_with_extension} not found in given path")

    # interaction

    def interact_using_list(self, command:[str]) -> str:
        def _check_format():
            """doesn't check if the command exists, just if the format is plausible

            format required example:

            command = ["--option1 value1", "-o2 value2"]
            """
            for option in command:
                if not option.startswith("-"):
                    raise FormatNotCorrectException(f"option '{option}' does not start with a dash")

                for value in option.split()[1:]:
                    if value.startswith("-"):
                        raise FormatNotCorrectException(f"multiple options given at once: '{option}''")

        def _call_ytdl(youtubeDL_location) -> str:
            args = [youtubeDL_location] + command

            p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            o, e = p.communicate()

            output = ""
            for c in o:
                output += chr(c)

            return output

        if not isinstance(command, list):
            raise WrongTypeException("command was not given in the form of a list")

        if command[0] == "youtube-dl" and command[0] == "youtube-dl.exe":
            command = command[1:]

        _check_format()

        # TODO: catch exceptions thrown by youtube-dl
        return _call_ytdl(path.join(self.path_to_binaries, "youtube-dl"))

    def interact_using_string(self, command:str)  -> str:
        """Just passes the command on as a list

        type your command as if it would be entered in cli

        format required example:

            command = "--option1 value1 -o2 value2"
        """
        def _parse_to_list() -> [str]:
            return [command.split(" -")[0]] + [f"-{option}" for option in command.split(" -")[1:]]

        if not isinstance(command, str):
            raise WrongTypeException("command was not given in the form of a string")

        return self.interact_using_list(_parse_to_list())
