from argparse import ArgumentParser
import hashlib
import string
import random
import time
import os
import re

BLOCKSIZE = 65536

generate_string = lambda: ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=12))
dll_location = "\\Release\\csgo-hops.dll"

# All variables used in the bunny hop cheat
variables = {
    "DLL_NAME":generate_string(),
    "dwForceJump":generate_string(),
    "dwLocalPlayer":generate_string(),
    "m_fFlags":generate_string(),
    "gameAddress":generate_string(),
    "LocalPlayer":generate_string(),
    "localPlayerAddress":generate_string(),
    "bhop":generate_string(),
    "moveType":generate_string(),
    "move":generate_string(),
    "jump":generate_string(),
    "getClientDLLAddress":generate_string(),
    "updateLocalPlayerAddress":generate_string(),
    "isValid":generate_string(),
    "getAddresses":generate_string(),
}


def get_file_hash(filename: str) -> str:
    """ Gets the SHA1 hash of a file
    :param filename: Filename to get the hash of
    :return: a hash as a str
    """
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)
    return hasher.hexdigest()

def get_file_content(filename: str) -> list:
    """ Fetches a files content
    :param filename: Filename to read
    :return: A list of lines
    """
    try:
        with open(filename, "r") as f:
            content: str = f.read()
        return content
    except  EnvironmentError:
        return None


def save_content_to_file(content: str, filename: str) -> bool:
    """ Writes content to a file
    :param content: Content to write
    :param filename: Filename to write the content too
    """
    try:
        with open(filename, "w") as f:
            f.seek(0)
            f.write(content)
        return True
    except EnvironmentError:
        return False

class CheatCompiler:
    def __init__(self, project_directory: str, variables: list, export_location: str, files: dict) -> None:
        """
        :param project_directory: Project location for the project
        :param variables: Cheat source variables to randomize (format {old_name:new_name})
        :param export_location: DLL/EXE export location to look for the file
        :param files: a dict containing the files the pull the source from and the file to create the randomized source under
        :param arch: PC architecture to export the DLL/exe to
        """
        self.project_directory = project_directory
        self.variables = variables
        self.export_location = self.project_directory + export_location
        self.files = files
        os.chdir(self.project_directory)

    def compile(self) -> None:
        """
        Compiles the cheat into a DLL
        """
        os.system(f"MSBuild.exe {self.project_directory} /t:build /p:Configuration=Release;Platform=x86")
    
    def randomize(self) -> bool:
        """ Randomizes the variables accross all files in the cheat source
        :return: True if alll files were randomized
        """
        for old_file, new_file in self.files.items():
            content = get_file_content(old_file)
            content = self.modify_variables(content)
            if not save_content_to_file(content, new_file):
                return False
        return True

    def modify_variables(self, cheat_source: str)  -> str:
        """ Modifies a cheat source to randomize the variable names
        :param cheat_source: The source code
        :param variables: A dict in the following format {old_name:new_name}
        :return: The modified source
        """
        for attr, new_name in self.variables.items():
            cheat_source = re.sub(attr, new_name, cheat_source)
        return cheat_source

    def show_export_data(self):
        """ Prints the SHA1 hash and compile time
        """
        print(f"[*] SHA1: {get_file_hash(self.export_location)} | {self.export_location}")
        print(f"[*] Was compiled @ {time.ctime(os.path.getctime(self.export_location))}")

    def work(self) -> bool:
        """ Randomizes & Compiles a cheat source
        1. Randomize the cheat source
        2. Compile the dll/exe
        3. Show the export 

        :return: True if the dll/exe was created
        """
        if not self.randomize():
            print(f"[-] Failed to randomize the cheat source. Is the project directory correct: {self.project_directory}")
            return False
        self.compile()
        self.show_export_data()
        return True

if __name__ == "__main__":
    parser = ArgumentParser(description='Tool used to compile and randomize CSGO cheats')
    parser.add_argument('--dir', '-D', required=True, help="csgo-hops directory")
    args = parser.parse_args()
    files = {
            f"{args.dir}\\csgo-hops\\_cheat.cpp":  f"{args.dir}\\csgo-hops\\cheat.cpp",
            f"{args.dir}\\csgo-hops\\_cheat.h":  f"{args.dir}\\csgo-hops\\cheat.h",
            f"{args.dir}\\csgo-hops\\_dllmain.cpp":  f"{args.dir}\\csgo-hops\\dllmain.cpp"
        }
    c = CheatCompiler(args.dir, variables, dll_location, files)
    c.work()
