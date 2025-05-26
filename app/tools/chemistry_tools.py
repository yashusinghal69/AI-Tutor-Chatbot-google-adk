# Chemistry data and constants
PERIODIC_TABLE = {
    "h": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": 1.008, "symbol": "H"},
    "he": {"name": "Helium", "atomic_number": 2, "atomic_mass": 4.003, "symbol": "He"},
    "li": {"name": "Lithium", "atomic_number": 3, "atomic_mass": 6.941, "symbol": "Li"},
    "c": {"name": "Carbon", "atomic_number": 6, "atomic_mass": 12.011, "symbol": "C"},
    "n": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": 14.007, "symbol": "N"},
    "o": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": 15.999, "symbol": "O"},
    "na": {"name": "Sodium", "atomic_number": 11, "atomic_mass": 22.990, "symbol": "Na"},
    "mg": {"name": "Magnesium", "atomic_number": 12, "atomic_mass": 24.305, "symbol": "Mg"},
    "al": {"name": "Aluminum", "atomic_number": 13, "atomic_mass": 26.982, "symbol": "Al"},
    "cl": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": 35.453, "symbol": "Cl"},
    "ca": {"name": "Calcium", "atomic_number": 20, "atomic_mass": 40.078, "symbol": "Ca"},
    "fe": {"name": "Iron", "atomic_number": 26, "atomic_mass": 55.845, "symbol": "Fe"},
    "cu": {"name": "Copper", "atomic_number": 29, "atomic_mass": 63.546, "symbol": "Cu"},
    "ag": {"name": "Silver", "atomic_number": 47, "atomic_mass": 107.868, "symbol": "Ag"},
    "au": {"name": "Gold", "atomic_number": 79, "atomic_mass": 196.967, "symbol": "Au"}
}

CHEMISTRY_CONSTANTS = {
    "avogadro_number": {"value": 6.02214076e23, "unit": "mol⁻¹", "symbol": "Nₐ"},
    "gas_constant": {"value": 8.314, "unit": "J/(mol⋅K)", "symbol": "R"},
    "planck_constant": {"value": 6.62607015e-34, "unit": "J⋅s", "symbol": "h"},
    "speed_of_light": {"value": 2.998e8, "unit": "m/s", "symbol": "c"},
    "electron_charge": {"value": 1.602176634e-19, "unit": "C", "symbol": "e"},
    "atomic_mass_unit": {"value": 1.66054e-27, "unit": "kg", "symbol": "u"}
}

from typing import Optional


def get_element_info(element: str) -> str:
    """Get information about a chemical element"""
    element = element.lower().strip()
    
    if element in PERIODIC_TABLE:
        elem = PERIODIC_TABLE[element]
        return (f"{elem['name']} ({elem['symbol']})\n"
               f"Atomic Number: {elem['atomic_number']}\n"
               f"Atomic Mass: {elem['atomic_mass']} u")
    else:
        available = ", ".join([v['symbol'] for v in PERIODIC_TABLE.values()])
        return f"Element '{element}' not found. Available elements: {available}"

def calculate_molar_mass(formula: str) -> str:
    """Calculate molar mass of a chemical formula"""
    try:
        import re
        
        # Simple parser for basic formulas like H2O, NaCl, CaCO3
        formula = formula.replace(" ", "")
        
        # Find all element-number pairs
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, formula)
        
        total_mass = 0
        composition = []
        
        for element, count in matches:
            count = int(count) if count else 1
            element_lower = element.lower()
            
            if element_lower in PERIODIC_TABLE:
                mass = PERIODIC_TABLE[element_lower]['atomic_mass']
                element_mass = mass * count
                total_mass += element_mass
                composition.append(f"{element}: {count} × {mass:.3f} = {element_mass:.3f}")
            else:
                return f"Unknown element: {element}"
        
        result = f"Molar mass of {formula}:\n"
        result += "\n".join(composition)
        result += f"\nTotal: {total_mass:.3f} g/mol"
        
        return result
    
    except Exception as e:
        return f"Error calculating molar mass: {str(e)}"

def balance_equation(equation: str) -> str:
    """Simple equation balancer for basic reactions"""
    try:
        # This is a simplified balancer for demonstration
        # For complex equations, a more sophisticated algorithm would be needed
        
        if "=" in equation or "→" in equation or "->" in equation:
            separator = "=" if "=" in equation else ("→" if "→" in equation else "->")
            reactants, products = equation.split(separator)
            
            return (f"Equation: {equation.strip()}\n"
                   f"Note: This is a simplified balancer. For complex equations, "
                   f"manual balancing or specialized software is recommended.\n"
                   f"Basic approach: Count atoms on both sides and adjust coefficients.")
        else:
            return "Please provide equation with reactants and products separated by =, →, or ->"
    
    except Exception as e:
        return f"Error balancing equation: {str(e)}"

def calculate_molarity(solute_moles: Optional[float] = None, volume_liters: Optional[float] = None, molarity: Optional[float] = None) -> str:
    """Calculate molarity using M = n/V"""
    try:
        # Calculate missing variable using M = n/V
        if molarity is not None and volume_liters is not None and solute_moles is None:
            solute_moles = molarity * volume_liters
            return f"Moles of solute = Molarity × Volume = {molarity} M × {volume_liters} L = {solute_moles:.3f} mol"
        
        elif solute_moles is not None and volume_liters is not None and molarity is None:
            molarity = solute_moles / volume_liters
            return f"Molarity = Moles / Volume = {solute_moles} mol / {volume_liters} L = {molarity:.3f} M"
        
        elif solute_moles is not None and molarity is not None and volume_liters is None:
            volume_liters = solute_moles / molarity
            return f"Volume = Moles / Molarity = {solute_moles} mol / {molarity} M = {volume_liters:.3f} L"
        
        else:
            return "Error: Provide exactly two of the three values (solute_moles, volume_liters, molarity)"
    
    except Exception as e:
        return f"Error calculating molarity: {str(e)}"


def get_chemistry_constant(constant_name: str) -> str:
    """Get chemistry constants"""
    constant_name = constant_name.lower().replace(" ", "_")
    
    if constant_name in CHEMISTRY_CONSTANTS:
        const = CHEMISTRY_CONSTANTS[constant_name]
        return f"{const['symbol']} = {const['value']} {const['unit']}"
    else:
        available = ", ".join(CHEMISTRY_CONSTANTS.keys())
        return f"Constant '{constant_name}' not found. Available constants: {available}"

def calculate_ph(concentration: float, is_acid: bool = True) -> str:
    """Calculate pH from H+ or OH- concentration"""
    try:
        import math
        
        if is_acid:
            # pH = -log[H+]
            ph = -math.log10(concentration)
            poh = 14 - ph
            return (f"Given [H+] = {concentration} M\n"
                   f"pH = -log[H+] = -log({concentration}) = {ph:.2f}\n"
                   f"pOH = 14 - pH = {poh:.2f}\n"
                   f"Solution is {'acidic' if ph < 7 else 'basic' if ph > 7 else 'neutral'}")
        else:
            # pOH = -log[OH-], pH = 14 - pOH
            poh = -math.log10(concentration)
            ph = 14 - poh
            return (f"Given [OH-] = {concentration} M\n"
                   f"pOH = -log[OH-] = -log({concentration}) = {poh:.2f}\n"
                   f"pH = 14 - pOH = {ph:.2f}\n"
                   f"Solution is {'acidic' if ph < 7 else 'basic' if ph > 7 else 'neutral'}")
    
    except Exception as e:
        return f"Error calculating pH: {str(e)}"
