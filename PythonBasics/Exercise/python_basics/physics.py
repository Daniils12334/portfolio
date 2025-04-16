import math
def tomsona_formula():
    user_input_L = float(input("Ievadiet induktivitati: ")) #μH
    user_input_R = float(input("Ievadiet Kondensatora kapacitati: ")) #pF
    L = user_input_L * 1e-6
    C = user_input_R * 1e-12
    f = 1 / (2 * math.pi * math.sqrt(L * C))
    print(f"f = {f/1e6:.1f} MHz")  # MHz

def tomsona_formula_kapacitate():
    user_input_1 = float(input("Ievadiet spoles induktivitāti (μH): "))  # μH
    user_input_2 = float(input("Ievadiet frekvenci (Hz): "))  # Hz
    L = user_input_1 * 1e-6
    C = 1 / ( (2 * math.pi * user_input_2) ** 2 * L )
    print(f"Kapacitāte = {C * 1e12:.2f} pF")  # pF

tomsona_formula_kapacitate()



