#!/usr/bin/env python3
"""Main simulation script for periodic wave absorber."""
import meep as mp
import numpy as np

def main():
    # Simulation parameters
    resolution = 30  # pixels/um
    cell_size = mp.Vector3(10, 10, 0)  # 2D simulation
    
    # Material geometry
    geometry = []
    
    # Sources
    sources = [
        mp.Source(
            mp.ContinuousSource(frequency=0.15),
            component=mp.Ez,
            center=mp.Vector3(-4, 0, 0),
            size=mp.Vector3(0, 2, 0)
        )
    ]
    
    # PML layers - optimized for grazing angles
    # Use higher-order polynomial grading (m=4) for smoother transition
    # Increase PML thickness to 2.0 for better absorption at oblique incidence
    # Reduced asymptotic reflection R_asymptotic to 1e-9 for improved accuracy
    pml_layers = [mp.PML(thickness=2.0, direction=mp.X, R_asymptotic=1e-9, pml_profile=lambda u: u**4),
                  mp.PML(thickness=2.0, direction=mp.Y, R_asymptotic=1e-9, pml_profile=lambda u: u**4)]
    
    # Setup simulation
    sim = mp.Simulation(
        cell_size=cell_size,
        geometry=geometry,
        sources=sources,
        resolution=resolution,
        boundary_layers=pml_layers,
        symmetries=[mp.Mirror(mp.Y, phase=-1)]
    )
    
    # Run simulation
    sim.run(until=200)
    
    # Collect data
    # ...

if __name__ == "__main__":
    main()
