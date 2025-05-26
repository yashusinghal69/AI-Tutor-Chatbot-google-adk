# Physics constants dictionary
PHYSICS_CONSTANTS = {
    "speed_of_light": {"value": 299792458, "unit": "m/s", "symbol": "c"},
    "gravitational_constant": {"value": 6.67430e-11, "unit": "N⋅m²/kg²", "symbol": "G"},
    "planck_constant": {"value": 6.62607015e-34, "unit": "J⋅Hz⁻¹", "symbol": "h"},
    "electron_charge": {"value": 1.602176634e-19, "unit": "C", "symbol": "e"},
    "avogadro_number": {"value": 6.02214076e23, "unit": "mol⁻¹", "symbol": "Nₐ"},
    "boltzmann_constant": {"value": 1.380649e-23, "unit": "J/K", "symbol": "k"},
    "gas_constant": {"value": 8.314462618, "unit": "J/(mol⋅K)", "symbol": "R"},
}

# Unit conversion factors
UNIT_CONVERSIONS = {
    "length": {
        "m_to_ft": 3.28084,
        "ft_to_m": 0.3048,
        "m_to_in": 39.3701,
        "in_to_m": 0.0254,
        "km_to_mi": 0.621371,
        "mi_to_km": 1.60934,
    },
    "mass": {
        "kg_to_lb": 2.20462,
        "lb_to_kg": 0.453592,
        "g_to_oz": 0.035274,
        "oz_to_g": 28.3495,
    },
    "temperature": {
        "c_to_f": lambda c: (c * 9/5) + 32,
        "f_to_c": lambda f: (f - 32) * 5/9,
        "c_to_k": lambda c: c + 273.15,
        "k_to_c": lambda k: k - 273.15,
    }
}

def get_physics_constant(constant_name: str) -> str:
    """Look up physics constants"""
    constant_name = constant_name.lower().replace(" ", "_")
    
    if constant_name in PHYSICS_CONSTANTS:
        const = PHYSICS_CONSTANTS[constant_name]
        return f"{const['symbol']} = {const['value']} {const['unit']}"
    else:
        available = ", ".join(PHYSICS_CONSTANTS.keys())
        return f"Constant '{constant_name}' not found. Available constants: {available}"

def convert_units(value: float, from_unit: str, to_unit: str) -> str:
    """Convert between different units"""
    try:
        conversion_key = f"{from_unit}_to_{to_unit}"
        
        # Check length conversions
        if conversion_key in UNIT_CONVERSIONS["length"]:
            factor = UNIT_CONVERSIONS["length"][conversion_key]
            result = value * factor
            return f"{value} {from_unit} = {result} {to_unit}"
        
        # Check mass conversions
        elif conversion_key in UNIT_CONVERSIONS["mass"]:
            factor = UNIT_CONVERSIONS["mass"][conversion_key]
            result = value * factor
            return f"{value} {from_unit} = {result} {to_unit}"
        
        # Check temperature conversions
        elif conversion_key in UNIT_CONVERSIONS["temperature"]:
            func = UNIT_CONVERSIONS["temperature"][conversion_key]
            result = func(value)
            return f"{value}°{from_unit.upper()} = {result}°{to_unit.upper()}"
        
        else:
            return f"Conversion from {from_unit} to {to_unit} not supported"
    
    except Exception as e:
        return f"Error converting units: {str(e)}"

def calculate_physics(formula: str, **kwargs) -> str:
    """Calculate physics formulas with given parameters"""
    try:
        formula = formula.lower().strip()
        
        if formula in ["force", "f=ma", "newton_second_law"]:
            mass = kwargs.get('mass', kwargs.get('m'))
            acceleration = kwargs.get('acceleration', kwargs.get('a'))
            if mass is not None and acceleration is not None:
                force = mass * acceleration
                return f"Force = mass × acceleration = {mass} kg × {acceleration} m/s² = {force} N"
        
        elif formula in ["kinetic_energy", "ke", "0.5mv2"]:
            mass = kwargs.get('mass', kwargs.get('m'))
            velocity = kwargs.get('velocity', kwargs.get('v'))
            if mass is not None and velocity is not None:
                ke = 0.5 * mass * velocity**2
                return f"Kinetic Energy = ½mv² = 0.5 × {mass} kg × ({velocity} m/s)² = {ke} J"
        
        elif formula in ["potential_energy", "pe", "mgh"]:
            mass = kwargs.get('mass', kwargs.get('m'))
            gravity = kwargs.get('gravity', kwargs.get('g', 9.81))
            height = kwargs.get('height', kwargs.get('h'))
            if mass is not None and height is not None:
                pe = mass * gravity * height
                return f"Potential Energy = mgh = {mass} kg × {gravity} m/s² × {height} m = {pe} J"
        
        else:
            return f"Formula '{formula}' not recognized. Available: force, kinetic_energy, potential_energy"
    
    except Exception as e:
        return f"Error calculating physics: {str(e)}"
