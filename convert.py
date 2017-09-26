# Dependencies
import argparse
import molarmass

parser = argparse.ArgumentParser(
    description='Converts the mass/molecular weight of the provided compound and its quantity to molecular weight/mass',
    epilog='Insert example usage'
)

parser.add_argument('compound', help='A valid chemical compound')
parser.add_argument('quantity', help='The quantity of the compound as a float')
parser.add_argument('initial_unit', help='The initial base unit as a string - "g" or "mol"')
parser.add_argument('converted_unit', help='The desired unit to be converted to as a string - "g" or "mol"')

def convert_quantity(quantity, molar_mass, initial_unit, converted_unit):

    if initial_unit == 'g':
        return quantity / molar_mass
    else:
        return quantity * molar_mass


if __name__ == '__main__':
    args = parser.parse_args()
    compound = args.compound
    quantity = float(args.quantity)
    initial_unit = args.initial_unit
    converted_unit = args.converted_unit

    print("Compound {}; Quantity {}; Initial Unit {}; Final Unit {}".format(compound, quantity, initial_unit, converted_unit))
    molar_mass = molarmass.molar_mass(compound)

    print(convert_quantity(quantity, molar_mass, initial_unit, converted_unit))
