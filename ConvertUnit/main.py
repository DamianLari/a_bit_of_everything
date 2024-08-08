import argparse

def convert_distance(value, from_unit, to_unit):
    conversions = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'g': 1,
        'kg': 1000,
        'mg': 0.001,
        'lb': 453.592,
        'oz': 28.3495,
        'stone': 6350.29
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'l': 1,
        'ml': 0.001,
        'm3': 1000,
        'cm3': 0.001,
        'in3': 0.0163871,
        'ft3': 28.3168,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return (value * 9/5) + 32
        elif to_unit == 'K':
            return value + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (value - 32) * 5/9
        elif to_unit == 'K':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return value - 273.15
        elif to_unit == 'F':
            return (value - 273.15) * 9/5 + 32
    return value


parser = argparse.ArgumentParser(description='Convert units of distance, weight, volume, or temperature.')
parser.add_argument('type', choices=['distance', 'weight', 'volume', 'temperature'], help='Type of conversion: distance, weight, volume, or temperature')
parser.add_argument('value', type=float, help='The value to convert')
parser.add_argument('from_unit', help='The unit to convert from')
parser.add_argument('to_unit', help='The unit to convert to')

args = parser.parse_args()

if args.type == 'distance':
    result = convert_distance(args.value, args.from_unit, args.to_unit)
elif args.type == 'weight':
    result = convert_weight(args.value, args.from_unit, args.to_unit)
elif args.type == 'volume':
    result = convert_volume(args.value, args.from_unit, args.to_unit)
elif args.type == 'temperature':
    result = convert_temperature(args.value, args.from_unit, args.to_unit)

print(f"{args.value} {args.from_unit} = {result} {args.to_unit}")
