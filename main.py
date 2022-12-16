import argparse
import math
from decimal import * 

PRECISION = 100

parser = argparse.ArgumentParser(description ='Calculate the energy required to accelerate an object by taking into account relativity')

parser.add_argument("velocity", type=int, help="The velocity to accelerate the object to")
parser.add_argument("mass", type=int, help="The mass of the object to accelerate")
parser.add_argument("--precision", "-p", type=int, default=PRECISION, help=f"The precision of the decimal digits when doing mathematical operations (defaults to {PRECISION})")

args = parser.parse_args()

mass = args.mass
velocity = args.velocity
getcontext().prec = args.precision

SPEED_OF_LIGHT = 299_792_458
MILL_NAMES = ['',' Thousand',' Million',' Billion',' Trillion', " Quadrillion", " Quintillion", " Sextillion", " Septtillion"]

def millify(n):
	'''Function obtained from https://stackoverflow.com/a/3155023'''

	n = float(n)
	millidx = max(0,min(len(MILL_NAMES)-1,
						int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

	return '{:,.0f}{}'.format(n / 10**(3 * millidx), MILL_NAMES[millidx])

def to_decimal(string: str, istype: str) -> Decimal:
	try:
		output = Decimal(string)
		if output < 0:
			raise ValueError("{istype} should be above zero")
	except ValueError:
		raise Exception(f"Invalid literal for {istype}")
	else:
		return output

print("Velocity: {:,}\nMass: {:,}".format(velocity, mass))

print("Calculating...")

try:
	lorentz_factor = 1/(Decimal(1)-(Decimal(velocity)/Decimal(SPEED_OF_LIGHT))**2).sqrt()
	total_energy = (lorentz_factor-1)*mass*SPEED_OF_LIGHT**2
except ValueError as err:
	if velocity >= SPEED_OF_LIGHT:
		raise Exception("Velocity must be less than the speed of light ({:,})".format(SPEED_OF_LIGHT))
	else:
		raise err
except ZeroDivisionError as err:
	if velocity >= SPEED_OF_LIGHT:
		raise Exception("Velocity must be less than the speed of light ({:,})".format(SPEED_OF_LIGHT))
except Exception as err:
	raise err
else:
	print("Total energy in Joules required to accelarate an object of {:,}kg at {:,}m/s is {} Joules or {:,} Joules rounded to the first 2 decimals".format(mass, velocity, millify(total_energy), round(total_energy, 2)))