
import numpy as np
import pandas as pd

def compute_udr_data(n_max=20, delta=1.0, rs=1.0):
    n = np.arange(2, n_max+1)
    radii = rs * n**2
    energies = delta / n**2
    curv_density = energies / (4 * np.pi * radii**2)
    df_radii = pd.DataFrame({'n': n, 'radius_rs_units': radii})
    df_energies = pd.DataFrame({'n': n, 'energy_normalized': energies})
    df_curvature = pd.DataFrame({'n': n, 'curvature_density_normalized': curv_density})
    return df_radii, df_energies, df_curvature

if __name__ == "__main__":
    radii, energies, curvature = compute_udr_data()
    radii.to_csv("radii.csv", index=False)
    energies.to_csv("energies.csv", index=False)
    curvature.to_csv("curvature.csv", index=False)
