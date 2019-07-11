from time import sleep
from pyfiglet import Figlet
import termcolor as tc
from replit import clear
from periodictable import *
import re

title_font = Figlet(font='big')

def get_type(value):
    try:
        # Return int if type int
        value = int(value)
        return "int"
    except ValueError:
        # return par if it is a parenthesis else, its regular str
        if value == "(" or value == ")":
            return "par(" if value == "(" else "par)"
        else:
            return "str"
        
def is_capital(input_char):
    return True if input_char == input_char.upper() else False

def type_out(input_string, interval=0.02):
    for word in input_string:
        print(word, end="", flush=True)
        sleep(interval)
    print()

def type_out_question(input_string, interval=0.02):
    for word in input_string:
        print(word, end="", flush=True)
        sleep(interval)

def print_title(input_string):
    print(tc.colored(title_font.renderText(input_string), "red"))

def render_tutorial_screen():
    print_title("Quick Mass")
    print(tc.colored("Quickly find the molar mass of compounds!\n\n", "white", None, ["bold"]))
    print("Would you like to see a tutorial?\n")
    print("[Y]es of course \n[N]o, I already know!") 
    print("\nAnswer: ", end="")

def prompt_for_tutorial():
    clear()
    print_title("Quick Mass")
    type_out(tc.colored("Quickly find the molar mass of compounds!\n\n", "white", None, ["bold"]))
    type_out("Would you like to see a tutorial?\n")
    type_out("[Y]es of course \n[N]o, I already know!")
    type_out_question("\nAnswer: ")

    tutorial_answer = ""
    tutorial_yes = ["yes", "y", "Y"]
    tutorial_no  = ["no", "n", "N"]
    while(tutorial_answer not in tutorial_yes and
        tutorial_answer not in tutorial_no):
        clear()
        render_tutorial_screen()
        tutorial_answer = input()
    if tutorial_answer in tutorial_yes:
        do_tutorial()

def do_tutorial():
    clear()
    print_title("Tutorial")
    type_out_question("Enter Compound or Element (case sensitive): ")
    sleep(1)
    type_out("<---- Here you will type the compound exactly how you write it. [Enter]")
    input()
    clear()
    print_title("Tutorial")
    print("Enter Compound or Element (case sensitive): ", end="", flush=True)
    sleep(1)
    type_out("Ca(NO3)3\n", 0.5)
    type_out("Molar Mass: 226.094 g/mol")
    type_out("\nIt's that easy! Now let's start --> [Enter]")
    input()

def main_function():
    # This basically stores all of the Elements, (), and # in order
    token_list = []
    clear()
    print_title("Quick Mass")
    type_out_question("Enter Compound or Element (case sensitive): ")

    compound = input()
    if compound == "":
        return
    if get_type(compound[0]) == "int":
        input(tc.colored("Compounds don't start with numbers. [Enter]", "red"))
        return

    i = 0
    while (i < len(compound)):
        token = ""
        token_type = get_type(compound[i])

        # Pythonic do while loop
        # do: 
        token += compound[i]
        i += 1
        # while:
        try:
            while(token_type == get_type(compound[i])):
                if (get_type(compound[i]) == "str") and (is_capital(compound[i])):
                    break
                token += compound[i]
                i += 1
        except IndexError:
            pass
        token_list.append(token)

    # Read each value from the end of the list to the beginning
    i = len(token_list) - 1
    while (i > 0):
        # If its a number, add a multiply symbol before it.
        if get_type(token_list[i]) == "int":
            token_list.insert(i, "*")
            i -= 1
        elif get_type(token_list[i]) == "str":
            if get_type(token_list[i - 1]) != "par(":
                token_list.insert(i, "+")
                i -= 1
            else:
                i -= 1
        elif get_type(token_list[i]) == "par(":
            token_list.insert(i, "+")
            i -= 1
        else:
            i -= 1
    


    string_equation = "".join(token_list)
    element_list = re.findall("[A-Z][a-z']*", string_equation)
    if len(element_list) == 0:
        input(tc.colored("Oh no! The compound doesn't have a element that is properly cased. [Enter]", "red"))
        return
    element_list.sort(key=len, reverse=True)
    try:
        for element in element_list:
            mass = str(eval(element).mass)
            string_equation = string_equation.replace(element, mass)
        type_out("\nResults:\n--------------------------", 0.01)
        type_out("Translated Math Expression: {}".format(string_equation))
        type_out("Total Molar Mass: {}".format(eval(string_equation)))
        input("\n\nPress [Enter] to continue")
    except NameError:
        input(tc.colored("Invalid Compound! Maybe check for spelling errors? [Enter]", "red"))
        

    
prompt_for_tutorial()
while True:
    main_function()
