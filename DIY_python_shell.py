#!/usr/bin/python3
import subprocess as sp
import os
hist=[]
def get_command(in_command_string): #function takes input string from user, returns the command and the options passed to it.
    out_command_string=in_command_string.split()
    command=out_command_string[0]
    options=out_command_string[1:]
    return command, options 
command_library={
    "run": lambda args:sp.run(args,capture_output=True,text=True).stdout, #command for running non-python code. command must be executable file.
    #so if you want to run x.py using this command, you would enter 'run python x.py'. 
    #shell commands that modify the current process will not work for this. I.E., you can't enter 'run cd ..'. This will throw an error.
    "exit": lambda args:sys.exit(),
    "chdir": lambda args:os.chdir(*args),
    "cwd": lambda args:print(os.getcwd()),
    "hist": lambda args:print(hist)
}
while True: #loop containing the meat of the shell
    wd=os.getcwd() #gets the current working directory
    usr_in=str(input(">>>")) #halts and waits for input from the user 
    hist.append(usr_in) #appends the input to the shell history
    if len(usr_in)==0:
        continue #if you just hit enter, a new line is made
    else: 
        command,options=get_command(usr_in)
        if command in command_library: #if the command you entered is in the command library, then call the function it maps to on the array of options
            try:
                print(command_library[command](options))
            except FileNotFoundError:
                print("Your command was not executable.")
        else: #if not, assume it is python code and try executing directly
            try:
                exec(usr_in)
            except NameError: #if exec does not recognize the command entered, it assumes it is erroneous and prints this message:
                print("Error: Command not found. Please enter python functions to the command line.")

