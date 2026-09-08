#!/usr/bin/env python3
"""Bundelt de STL's uit output/ in drie 3MF-printjobs, uitgelegd op een 256x256 plaat."""
import os, numpy as np, trimesh
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "output")

def load(name):
    m = trimesh.load(os.path.join(OUT, name + ".stl"))
    m.apply_translation(-m.bounds[0])          # hoek op (0,0,0), onderkant op z=0
    return m

def plate(jobname, items, gap=8):
    """items: lijst van (objectnaam, mesh, aantal). Rij-layout van links naar rechts, wrap bij 240 mm."""
    scene = trimesh.Scene()
    x = y = 0.0; row_h = 0.0
    for name, mesh, count in items:
        for i in range(count):
            m = mesh.copy(); w, d, _ = m.extents
            if x + w > 250: x = 0.0; y += row_h + gap; row_h = 0.0
            m.apply_translation([x, y, 0]); x += w + gap; row_h = max(row_h, d)
            scene.add_geometry(m, node_name=f"{name}_{i+1}" if count > 1 else name, geom_name=f"{name}_{i+1}" if count > 1 else name)
    path = os.path.join(OUT, jobname + ".3mf")
    scene.export(path)
    ext = scene.bounds[1] - scene.bounds[0]
    print(f"  {jobname + '.3mf':22s} {len(scene.geometry)} objecten, plaat {ext[0]:.0f} x {ext[1]:.0f} mm, {os.path.getsize(path)//1024} kB")

print("3MF-jobs:")
plate("01_pasprints_PLA", [("test_tray_fit", load("test_tray_fit"), 1), ("test_meter_fit", load("test_meter_fit"), 1)])
plate("02_box_PLA",       [("box", load("box"), 1), ("lid", load("lid"), 1), ("handle", load("handle"), 1), ("lid_logo_inlay", load("lid_logo_inlay"), 1)])
plate("03_gasket_voetjes_TPU", [("gasket", load("gasket"), 1), ("foot", load("foot"), 4)])
