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

    for index, char in enumerate(compound):

        if char.isupper():
            # A new element is found
            if index > 0:
                # Check if there was no digit after the previous elements
                # Add a stoichiometric coefficient of 1 to the list
                if compound[index - 1].isalpha():
                    element_stoich.append(1)
            if index < (len(compound) - 1):
                if compound[index + 1].islower():
                    # The element is a two-letter element
                    elements.append(char + compound[index + 1])
                    print(elements)
            else:
                # The element is a one-letter element
                elements.append(char)

        elif char.isnumeric():
            # An explicit coefficient is given
            print("Number: " + char)
            element_stoich.append(int(char))
        elif char == "(":
            print("Bracket")
        else:
            print("Lowercase: " + char)

    print(elements, element_stoich)

args = parser.parse_args()
compound = args.compound
# print(periodic_table[compound]['atomic_mass'])

parseCompound('NaMoO4H2O')
