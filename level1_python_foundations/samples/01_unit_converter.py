# 01_unit_converter.py
# Level 1 — Topic 1: Variables, types, f-strings

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length between common units via meters."""
    to_meters = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    }

    if from_unit not in to_meters or to_unit not in to_meters:
        raise ValueError(f"Unsupported unit. Supported: {list(to_meters.keys())}")

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result


if __name__ == "__main__":
    value = 5.0
    from_u = "km"
    to_u = "mile"
    converted = convert_length(value, from_u, to_u)

    print(f"{value} {from_u} = {converted:.4f} {to_u}")
    # Expected: 5.0 km = 3.1069 mile
