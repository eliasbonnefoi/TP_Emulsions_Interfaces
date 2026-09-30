import numpy as np
import matplotlib.pyplot as plt

C = np.array([5, 3, 2, 1.5, 1, 0.5, 0.25, 0.1])

N_gouttes = 50 #nombre moyen de gouttes utilisées

g = 9.81
a = 0.78e-3
delta_a = 0.03e-3
delta_M_balance = 100
rho_L = 1000

M_goutte_g = np.array([0.0132, 0.0133, 0.0148, 0.0165, 0.0188, 0.022, 0.0243, 0.0245])
delta_M_goutte = delta_M_balance / N_gouttes  # Incertitude sur une seule goutte

#Conversion SI
M_kg = M_goutte_g * 1e-3
dM_kg = delta_M_goutte * 1e-6

V = M_kg / rho_L
x = a / (V**(1/3))

# Polynome de f
f = 1.811 - 1.495*x + 0.987*(x**2) - 0.089*(x**3)

# Calcul de gamma
gamma = (M_kg * g) / (np.pi * f * a)
gamma_mN = gamma * 1000  # Conversion en mN/m

# Propagation des incertitudes
rel_M = dM_kg / M_kg
rel_a = delta_a / a
delta_gamma_mN = gamma_mN * np.sqrt(rel_M**2 + rel_a**2)

# Tracé du graphique
plt.figure(figsize=(10, 6))
plt.errorbar(C, gamma_mN, yerr=delta_gamma_mN, fmt='ro-', capsize=5,
             linewidth=1.5, markersize=6, label='Données expérimentales')

plt.xscale('log')  # Échelle logarithmique pour les concentrations
plt.grid(True, which="both", ls="-", alpha=0.5)

plt.title('Tension interfaciale $\gamma$ en fonction de la concentration (log)')
plt.xlabel('Concentration $C$ (g/L)')
plt.ylabel('Tension interfaciale $\gamma$ (mN/m)')
plt.legend()

# Affichage des résultats numériques
print(f"{'C (g/L)':<10} | {'Gamma (mN/m)':<15} | {'Incertitude (+/-)':<15}")
print("-" * 45)
for i in range(len(C)):
    print(f"{C[i]:<10} | {gamma_mN[i]:<15.2f} | {delta_gamma_mN[i]:<15.2f}")

plt.show()