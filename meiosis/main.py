from cromossome.main import load_hooks_from_manifesto
from cromossome.nln import parse
from time import sleep
from traceback import format_exc
if __name__ != "__main__":

    raise ImportError("This file isn't meant to be imported")

print ("You have now run Meiosis")

settings = ""
data = ""

print("Processing settings...")
with open("settings.nln") as f:

    settings = f.read()
print("Loading settings OK ")
settings = parse(settings)
print("Parsing settings OK")
print("Processing manifest...",end='')

if not ("manifest" in settings.keys()):

    raise LookupError("Settings file missing the required mannifest path, loading can't proceed")

with open(settings["manifest"]) as f:

    data = f.read()

print ("Loading manifest OK")
data = parse(data)
print ("Parsing Manifest OK")
print ("Passing Manifest to Cromossome...")
look_up_table = load_hooks_from_manifesto(data)
print ("Cromosome has provided all the hooks declared, finishing launch preparations")
# Do all the other launch prep here
command_list = list(look_up_table.keys())
command_list_str = '- '+('\n -'.join(command_list))
last_error = ''
# Do all the other launch prep here
print ("All launch preparations OK! launching in 1")
import os
os.system('cls' if os.name == 'nt' else 'clear') # SCARY! look into other ways of clearing the STDOUT
sleep (1)
print (
    """
    Meiosis V1 - The Open REPL CLI
    First made by Jecrs as part of the Replication OAIF
    To list all installed commands type '?' then enter
    """
)
while True:

    data = input(">")
    if data == "?":
        print(command_list_str)
        continue
    if data == "*":
        print(last_error+"\n Error print-out ended")
        continue
    dl = len(data)
    ef = True
    for comm in command_list:
        data = data.removeprefix(comm).removeprefix(" ")
        if len(data) != dl:
            try:
                look_up_table[comm](data.split(" "))
            except:
                last_error = format_exc()
                print("[Warning] The last command exited with an error, to print the last error type '*' then enter")
            ef = False
            break
    if ef:
        print("[Error] Invalid Command, to get a list of comand type '?' then enter")

    

            
            
