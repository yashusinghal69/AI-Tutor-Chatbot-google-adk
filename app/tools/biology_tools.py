from typing import Optional

# Biology data and constants
BIOLOGY_DATA = {
    "cell_types": {
        "prokaryotic": {"description": "Cells without membrane-bound nucleus", "examples": ["bacteria", "archaea"]},
        "eukaryotic": {"description": "Cells with membrane-bound nucleus", "examples": ["plant cells", "animal cells", "fungal cells"]}
    },
    "organelles": {
        "nucleus": {"function": "Controls cell activities and contains DNA", "found_in": "eukaryotic cells"},
        "mitochondria": {"function": "Produces ATP through cellular respiration", "found_in": "eukaryotic cells"},
        "chloroplasts": {"function": "Conducts photosynthesis", "found_in": "plant cells"},
        "ribosomes": {"function": "Protein synthesis", "found_in": "all cells"},
        "endoplasmic_reticulum": {"function": "Protein and lipid synthesis", "found_in": "eukaryotic cells"},
        "golgi_apparatus": {"function": "Modifies and packages proteins", "found_in": "eukaryotic cells"}
    },
    "body_systems": {
        "circulatory": {"function": "Transports blood, nutrients, and oxygen", "organs": ["heart", "blood vessels", "blood"]},
        "respiratory": {"function": "Gas exchange (oxygen and carbon dioxide)", "organs": ["lungs", "trachea", "bronchi"]},
        "digestive": {"function": "Breaks down food and absorbs nutrients", "organs": ["stomach", "intestines", "liver"]},
        "nervous": {"function": "Controls body functions and processes information", "organs": ["brain", "spinal cord", "nerves"]},
        "skeletal": {"function": "Provides structure and protects organs", "organs": ["bones", "cartilage", "ligaments"]}
    },
    "genetics": {
        "dna_bases": ["adenine", "thymine", "guanine", "cytosine"],
        "rna_bases": ["adenine", "uracil", "guanine", "cytosine"],
        "base_pairs": {"adenine": "thymine", "thymine": "adenine", "guanine": "cytosine", "cytosine": "guanine"}
    }
}

def get_biology_info(topic: str, subtopic: str = None) -> str:
    """Get information about biological topics"""
    topic = topic.lower().replace(" ", "_")
    
    if topic in BIOLOGY_DATA:
        data = BIOLOGY_DATA[topic]
        
        if subtopic:
            subtopic = subtopic.lower().replace(" ", "_")
            if subtopic in data:
                info = data[subtopic]
                if isinstance(info, dict):
                    result = f"{subtopic.replace('_', ' ').title()}:\n"
                    for key, value in info.items():
                        result += f"- {key.replace('_', ' ').title()}: {value}\n"
                    return result.strip()
                else:
                    return f"{subtopic.replace('_', ' ').title()}: {info}"
            else:
                available = ", ".join(data.keys())
                return f"Subtopic '{subtopic}' not found. Available: {available}"
        else:
            result = f"{topic.replace('_', ' ').title()}:\n"
            for key, value in data.items():
                if isinstance(value, dict):
                    result += f"- {key.replace('_', ' ').title()}: {value.get('description', 'N/A')}\n"
                else:
                    result += f"- {key.replace('_', ' ').title()}: {value}\n"
            return result.strip()
    else:
        available = ", ".join(BIOLOGY_DATA.keys())
        return f"Topic '{topic}' not found. Available topics: {available}"

def classify_organism(characteristics: str) -> str:
    """Classify organisms based on characteristics"""
    characteristics = characteristics.lower()
    
    classification = []
    
    # Kingdom classification
    if any(word in characteristics for word in ["plant", "photosynthesis", "chlorophyll", "cell wall"]):
        classification.append("Kingdom: Plantae")
    elif any(word in characteristics for word in ["animal", "multicellular", "heterotrophic", "mobile"]):
        classification.append("Kingdom: Animalia")
    elif any(word in characteristics for word in ["fungus", "fungi", "decomposer", "spores"]):
        classification.append("Kingdom: Fungi")
    elif any(word in characteristics for word in ["bacteria", "prokaryotic", "single cell"]):
        classification.append("Kingdom: Bacteria")
    
    # Cell type
    if any(word in characteristics for word in ["nucleus", "organelles", "membrane bound"]):
        classification.append("Cell Type: Eukaryotic")
    elif any(word in characteristics for word in ["no nucleus", "prokaryotic"]):
        classification.append("Cell Type: Prokaryotic")
    
    # Nutrition
    if any(word in characteristics for word in ["photosynthesis", "autotrophic", "makes own food"]):
        classification.append("Nutrition: Autotrophic")
    elif any(word in characteristics for word in ["heterotrophic", "consumes", "eats"]):
        classification.append("Nutrition: Heterotrophic")
    
    if classification:
        return "Classification based on characteristics:\n" + "\n".join(classification)
    else:
        return "Unable to classify based on given characteristics. Please provide more specific traits."

def calculate_genetics(calculation_type: str, **kwargs) -> str:
    """Perform genetics calculations"""
    try:
        calc_type = calculation_type.lower().strip()
        
        if calc_type in ["allele_frequency", "hardy_weinberg"]:
            p = kwargs.get('p', kwargs.get('dominant_frequency'))
            q = kwargs.get('q', kwargs.get('recessive_frequency'))
            
            if p is not None and q is None:
                q = 1 - p
            elif q is not None and p is None:
                p = 1 - q
            elif p is not None and q is not None:
                if abs(p + q - 1) > 0.001:
                    return "Error: p + q must equal 1"
            else:
                return "Error: Provide either p (dominant frequency) or q (recessive frequency)"
            
            # Calculate genotype frequencies
            AA = p**2
            Aa = 2*p*q
            aa = q**2
            
            return (f"Hardy-Weinberg Equilibrium:\n"
                   f"Allele frequencies: p = {p:.3f}, q = {q:.3f}\n"
                   f"Genotype frequencies:\n"
                   f"- AA (homozygous dominant): {AA:.3f} ({AA*100:.1f}%)\n"
                   f"- Aa (heterozygous): {Aa:.3f} ({Aa*100:.1f}%)\n"
                   f"- aa (homozygous recessive): {aa:.3f} ({aa*100:.1f}%)")
        
        elif calc_type in ["punnett_square", "cross"]:
            parent1 = kwargs.get('parent1', kwargs.get('p1', ''))
            parent2 = kwargs.get('parent2', kwargs.get('p2', ''))
            
            if not parent1 or not parent2:
                return "Error: Provide genotypes for both parents (e.g., parent1='Aa', parent2='Bb')"
            
            # Simple monohybrid cross
            if len(parent1) == 2 and len(parent2) == 2:
                offspring = []
                for allele1 in parent1:
                    for allele2 in parent2:
                        offspring.append(f"{allele1}{allele2}")
                
                # Count genotypes
                from collections import Counter
                counts = Counter(offspring)
                total = len(offspring)
                
                result = f"Punnett Square Results ({parent1} × {parent2}):\n"
                for genotype, count in counts.items():
                    percentage = (count/total) * 100
                    result += f"- {genotype}: {count}/{total} ({percentage:.1f}%)\n"
                
                return result.strip()
            else:
                return "Error: Currently supports only simple monohybrid crosses (e.g., 'Aa' × 'Bb')"
        
        else:
            return f"Calculation type '{calculation_type}' not supported. Available: allele_frequency, punnett_square"
    
    except Exception as e:
        return f"Error in genetics calculation: {str(e)}"

def get_dna_complement(dna_sequence: str) -> str:
    """Get the complementary DNA strand"""
    try:
        dna_sequence = dna_sequence.upper().replace(" ", "")
        complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        
        complement = ""
        for base in dna_sequence:
            if base in complement_map:
                complement += complement_map[base]
            else:
                return f"Error: Invalid DNA base '{base}'. Use A, T, G, C only."
        
        return f"Original:    5'-{dna_sequence}-3'\nComplement:  3'-{complement}-5'"
    
    except Exception as e:
        return f"Error finding DNA complement: {str(e)}"
