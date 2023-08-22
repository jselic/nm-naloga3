import numpy as np
from src.MissionControl import MissionControl

def RK4(system,initial_conditions,h, t_values):
    """
    Numerično rešuje sistem diferencialnih enačb z uporabo metode Runge-Kutta četrtega reda.

    Arguments:
        sistem (function): Funkcija, ki predstavlja sistem diferencialnih enačb. Sprejema argumente sistem(spremenljivke, t),
                          kjer je spremenljivke seznam začetnih vrednosti spremenljivk in t časovni parameter.
        zacetni_pogoji (list): Seznam začetnih pogojev za spremenljivke sistema.
        h (float): Velikost koraka integracije.
        vrednosti_t (array-like): Seznam časovnih točk, pri katerih želimo izračunati rešitev.

    Returns:
        array-like: Matrika rešitev sistema diferencialnih enačb pri vsaki časovni točki v vrednosti_t.
    """
    solution = np.zeros((len(t_values), len(initial_conditions)))
    solution[0] = initial_conditions
    
    for i in range(1,len(t_values)):
        t = t_values[i-1]
        variables = solution[i-1]
        
        k1 = h * np.array(system(MissionControl,variables, t))
        k2 = h * np.array(system(MissionControl,variables + 0.5 * k1, t + 0.5 * h))
        k3 = h * np.array(system(MissionControl,variables + 0.5 * k2, t + 0.5 * h))
        k4 = h * np.array(system(MissionControl,variables + k3, t + h))
    
        solution[i] = variables + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
    return solution