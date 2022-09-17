import sys
import math

sys.argv.pop(0)
args_len = len(sys.argv)

speed_of_light = 299_792_458

def to_int(string: str, istype: str):
	try:
		output = int(string)
	except ValueError:
		raise Exception(f"Invalid literal for {istype}")
	else:
		return output

if args_len >= 1:
	velocity = sys.argv[0]
else:
	velocity = to_int(input("Please enter object's velocity in meters per second: "), "velocity")
if args_len >= 2:
	mass = sys.argv[1]
else:
	mass = to_int(input("Please enter object's mass in kilograms: "), "mass")

print(f"Velocity: {velocity}\nMass: {mass}")

print("Calculating...")

try:
	total_energy = mass*velocity/math.sqrt(1-(velocity**2/speed_of_light**2))
except ValueError as err:
	if velocity >= speed_of_light:
		raise Exception(f"Velocity must be less than the speed of light ({speed_of_light})")
	else:
		raise err
except Exception as err:
	raise err
else:
	print(f"Total energy in Joules required to accelarate an object of {mass}kg at {velocity}m/s is {total_energy} Joules")