# Dependencies
import argparse
import json

# Constants
PERIODIC_TABLE_PATH = 'PeriodicTable.json'

periodic_table = json.load(open(PERIODIC_TABLE_PATH, 'r'))

parser = argparse.ArgumentParser(
    description='Calculates the molar mass of the provided chemical compount',
    epilog='Insert example usage'
)

parser.add_argument('compound', help='A valid chemical compound')

def parseCompound(compound):

    element_stoich = []
    elements = []

    for char in compound:
        if char.isupper():
            print("Upper: " + char)
            elements.append(char)
        elif char.isnumeric():
            print("Number: " + char)
            element_stoich.append(char)
        elif char == "(":
            print("Bracket")
        else:
            print("Lowercase: " + char)

    print(elements, element_stoich)

args = parser.parse_args()
compound = args.compound
# print(periodic_table[compound]['atomic_mass'])

parseCompound(compound)
        
