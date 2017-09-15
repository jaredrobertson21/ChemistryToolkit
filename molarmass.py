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

args = parser.parse_args()
compound = args.compound
print(periodic_table[compound]['atomic_mass'])