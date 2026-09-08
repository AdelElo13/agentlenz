#!/usr/bin/env python3
"""Snelle preview-renders (PNG) van de onderdelen en de assemblage, zonder OpenGL."""
import os, numpy as np, trimesh
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import heti_box as H

OUT = H.OUT
LIGHT = np.array([0.4, -0.6, 0.7]); LIGHT /= np.linalg.norm(LIGHT)

def tm(m):
    mesh = m.to_mesh(); v = np.asarray(mesh.vert_properties)[:, :3]; f = np.asarray(mesh.tri_verts)
    return trimesh.Trimesh(v, f, process=False)

def fig3(items, title, fname, elev=28, azim=-55):
    """Alle meshes in één collectie zodat matplotlib per vlak op diepte sorteert."""
    fig = plt.figure(figsize=(9, 7)); ax = fig.add_subplot(111, projection="3d")
    tris, cols = [], []
    for m, c, a in items:
        n = m.face_normals; shade = 0.55 + 0.45 * np.clip(n @ LIGHT, 0, 1)
        rgb = np.array(matplotlib.colors.to_rgb(c))
        tris.append(m.vertices[m.faces]); cols.append(np.clip(rgb[None, :] * shade[:, None], 0, 1))
    tris = np.vstack(tris); cols = np.vstack(cols)
    ax.add_collection3d(Poly3DCollection(tris, facecolors=cols, edgecolors="none"))
    allv = tris.reshape(-1, 3)
    c = (allv.min(0) + allv.max(0)) / 2; r = (allv.max(0) - allv.min(0)).max() / 2 * 1.05
    ax.set_xlim(c[0]-r, c[0]+r); ax.set_ylim(c[1]-r, c[1]+r); ax.set_zlim(c[2]-r, c[2]+r)
    ax.set_box_aspect([1, 1, 1]); ax.view_init(elev, azim); ax.set_axis_off(); ax.set_title(title)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, fname), dpi=110); plt.close(fig)
    print("  ", fname)

box, lid, gasket, foot, tray = H.box_part(), H.lid_part(), H.gasket_part(), H.foot_part(), H.load_tray_in_box()
meter = H.meter_dummy_box()
inlay = H.logo_inlay_part().translate([0, H.LOGO_Y, H.BOX_H + H.LID_TOP - H.LOGO_DEPTH])
lid_on = lid.translate([0, 0, H.BOX_H]); h_up = H.handle_part(0).translate([0, 0, H.BOX_H]); h_flat = H.handle_part(90).translate([0, 0, H.BOX_H])
jars = H.jars_in_box()
feet = None
for (x, y) in H.FOOT_POS:
    f = foot.translate([x, y, -(H.FOOT_H - H.FOOT_RECESS_H)]); feet = f if feet is None else feet + f

print("Previews:")
fig3([(tm(box), "#2e8b3d", 1), (tm(tray), "#d9d9d9", 1), (tm(jars), "#b8d8f0", 0.9), (tm(meter), "#222222", 1), (tm(feet), "#e03030", 1)],
     "Box open: tray met 4 potjes, ronde meter in de boss op de voorkant", "preview_open.png", elev=35, azim=-40)
fig3([(tm(box), "#2e8b3d", 1), (tm(lid_on), "#e0b020", 1), (tm(h_up), "#e03030", 1), (tm(meter), "#222222", 1), (tm(inlay), "#ffffff", 1), (tm(feet), "#e03030", 1)],
     "Dicht, handvat omhoog: ronde meter voor, logo in het deksel", "preview_closed_handle_up.png", elev=30, azim=-35)
fig3([(tm(box), "#2e8b3d", 1), (tm(lid_on), "#e0b020", 1), (tm(h_flat), "#e03030", 1), (tm(meter), "#222222", 1), (tm(inlay), "#ffffff", 1), (tm(feet), "#e03030", 1)],
     "Dicht, handvat plat", "preview_closed_handle_flat.png", elev=50, azim=-60)
half = H.Manifold.cube([200, 200, 200], True).translate([100, 0, 50])
cut = lambda m: tm(m - half)
fig3([(cut(box), "#2e8b3d", 1), (cut(tray), "#d9d9d9", 1), (cut(jars), "#b8d8f0", 1), (cut(lid_on), "#e0b020", 1), (cut(meter), "#222222", 1),
      (cut(gasket.translate([0, 0, H.BOX_H - (H.GASKET_H - H.GROOVE_DEPTH)])), "#111111", 1)],
     "Doorsnede: richel, potjes, gasket, meter in de boss", "preview_section.png", elev=18, azim=-35)
fig3([(tm(lid.rotate([180, 0, 0])), "#e0b020", 1)], "Deksel in printstand (bovenkant op het bed)", "preview_lid_print.png", elev=30, azim=-50)
