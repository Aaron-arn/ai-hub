"""Unit converter: length, weight, temperature and volume conversions."""

import sys

LENGTH_TO_M = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

WEIGHT_TO_KG = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,
    "oz": 0.028349523125,
    "t": 1000.0,
    "st": 6.35029318,
}

VOLUME_TO_L = {
    "l": 1.0,
    "ml": 0.001,
    "m3": 1000.0,
    "gal": 3.785411784,
    "qt": 0.946352946,
    "pt": 0.473176473,
    "cup": 0.2365882365,
    "floz": 0.0295735295625,
}

TEMPERATURE = {"c", "f", "k"}
CATEGORIES = [LENGTH_TO_M, WEIGHT_TO_KG, VOLUME_TO_L]


def convert_temperature(value, source, target):
    if source == "c":
        kelvin = value + 273.15
    elif source == "f":
        kelvin = (value - 32) * 5 / 9 + 273.15
    else:
        kelvin = value
    if target == "c":
        return kelvin - 273.15
    if target == "f":
        return (kelvin - 273.15) * 9 / 5 + 32
    return kelvin


def convert(value, source, target):
    for table in CATEGORIES:
        if source in table and target in table:
            return value * table[source] / table[target]
    if source in TEMPERATURE and target in TEMPERATURE:
        return convert_temperature(value, source, target)
    raise ValueError(f"no known conversion from '{source}' to '{target}'")


def usage():
    print("Usage: python main.py <value> <from_unit> <to_unit>")
    print("Length: m km cm mm in ft yd mi")
    print("Weight: kg g mg lb oz t st")
    print("Volume: l ml m3 gal qt pt cup floz")
    print("Temperature: c f k")


def main():
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)
    try:
        value = float(sys.argv[1])
        result = convert(value, sys.argv[2].lower(), sys.argv[3].lower())
        print(f"{result:g}")
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
