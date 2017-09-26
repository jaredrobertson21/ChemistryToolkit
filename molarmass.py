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


def parse_compound(compound):

    element_stoich = []
    elements = []

    for index, char in enumerate(compound):

        if char.isupper():
            # A new element is found
            if index > 0:
                # Not the first element in the string
                if compound[index - 1].isalpha():
                    # If there was no digit after the previous element,
                    # add a stoichiometric coefficient of 1 to the list
                    element_stoich.append(1)
            if index < (len(compound) - 1):
                # Not the last character in the string
                if compound[index + 1].islower():
                    # The element is a two-letter element
                    elements.append(char + compound[index + 1])
                else:
                    # The element is a single-letter element
                    elements.append(char)
            else:
                # The element is a single-letter, mono-atomic element at the end of the compound string
                elements.append(char)
                element_stoich.append(1)

        elif char.isnumeric():
            # An explicit coefficient is given
            element_stoich.append(int(char))
            # TODO: Use recursion to expand beyond single digit coefficients

        elif char == "(":
            print("Bracket")
        else:
            if index == (len(compound) - 1):
                # The element is a two-letter, mono-atomic element at the end of the compound string
                element_stoich.append(1)

    return elements, element_stoich


def molar_mass(compound):
    parsed_compound = parse_compound(compound)
    elements = parsed_compound[0]
    coefficients = parsed_compound[1]
    molar_mass_sum = 0
    for element, coefficient in zip(elements, coefficients):
        molar_mass_sum += periodic_table[element]['atomic_mass'] * coefficient

    return molar_mass_sum

if __name__ == '__main__':

    args = parser.parse_args()
    compound = args.compound

    print("Molar mass of {}: {} g/mol".format(compound, molar_mass(compound)))
