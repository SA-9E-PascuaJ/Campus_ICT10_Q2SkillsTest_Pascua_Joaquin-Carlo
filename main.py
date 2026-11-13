from pyscript import document

# ts is the dictionary with all the non-metals
elements = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"name": "Helium", "number": 2, "mass": 4.0026},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "I": {"name": "Iodine", "number": 53, "mass": 126.90},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.29},
    "Rn": {"name": "Radon", "number": 86, "mass": 222},
}


# ts runs when you click the button
def search(event):
    symbol = document.getElementById("symbol").value.strip().capitalize()
    result = document.getElementById("result")

    # ts checks if the symbol is in the dictionary
    if symbol in elements:
        e = elements[symbol]
        result.innerHTML = f"""
            <p>Element Symbol: {symbol}</p>
            <p>Element Name: {e["name"]}</p>
            <p>Atomic Number: {e["number"]}</p>
            <p>Atomic Mass: {e["mass"]}</p>
        """
    else:
        result.innerHTML = f"<p>The element '{symbol}' does not exist in the non-metals list.</p>"
