#!/usr/bin/env python3
"""
Dreambros HETI-style koelbox voor de Dreambros_Tray (4 dabpotjes Ø38).

Parametrisch model. Alle maten in mm. Genereert STL's in ./output en
verifieert computationeel dat de originele tray, een 48x28x15 thermo/
hygrometer, het deksel en het handvat passen.

Onderdelen:
  box.stl          PLA  - romp, meterbezel aan de voorkant, voetjes-uitsparingen
  lid.stl          PLA  - cap-deksel met skirt, snap-detent, handvat-oren
  handle.stl       PLA  - beugelhandvat, klikt op de pennen van het deksel
  gasket.stl       TPU  - afdichtring in het deksel
  foot.stl         TPU  - voetje (4x printen)
  test_meter_fit.stl   PLA - alleen de meterbezel, korte pasprint
  test_tray_fit.stl    PLA - onderste 24 mm van de box, pasprint voor de tray

Gebruik:  python3 heti_box.py            (schrijft output/*.stl en verifieert)
"""
from __future__ import annotations
import os, sys
import numpy as np
import manifold3d as m3
from manifold3d import Manifold, CrossSection, JoinType

m3.set_circular_segments(96)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
TRAY_STL = os.path.join(HERE, "reference", "Dreambros_Tray.stl")

# ------------------------------------------------------------------ tray (gemeten uit Dreambros_Tray.stl)
T_FLANGE_W, T_FLANGE_D, T_FLANGE_H = 99.0, 94.0, 3.5
T_BODY_W, T_BODY_D, T_BODY_H = 90.8, 85.8, 16.5
T_R_BODY, T_R_FLANGE = 5.0, 7.0
POCKET_D, POCKET_DEPTH = 38.6, 16.0
T_TOTAL_H = T_BODY_H + T_FLANGE_H          # 20

# ------------------------------------------------------------------ potje en meter
JAR_D = 38.0          # past in Ø38.6 pocket
JAR_H = 32.0          # AANNAME: hoogte potje met deksel. Meet na en pas aan.
JAR_PROTRUSION = JAR_H - POCKET_DEPTH       # steekt boven de tray uit
METER_BODY_W, METER_BODY_H, METER_T = 46.0, 27.0, 15.0    # inbouwmaat body
METER_BEZEL_W, METER_BEZEL_H, METER_BEZEL_T = 48.0, 28.5, 1.5

# ------------------------------------------------------------------ box
CLR = 0.3             # radiale speling per zijde
WALL = 3.2
FLOOR = 3.0
HEADSPACE = 3.0
CAV_LO_W, CAV_LO_D = T_BODY_W + 2 * 0.4, T_BODY_D + 2 * 0.4     # tray-body zit hier los in
CAV_LO_H = T_BODY_H + 0.3                                        # flens draagt op de richel, body zweeft 0.3 boven de vloer
CAV_UP_W, CAV_UP_D = T_FLANGE_W + 2 * CLR, T_FLANGE_D + 2 * CLR
CAV_UP_R = T_R_FLANGE + CLR
CAV_UP_H = T_FLANGE_H + JAR_PROTRUSION + HEADSPACE
BOX_W = CAV_UP_W + 2 * WALL           # 106.0
BOX_D = CAV_UP_D + 2 * WALL           # 101.0
BOX_R = CAV_UP_R + WALL               # 10.5
BOX_H = FLOOR + CAV_LO_H + CAV_UP_H   # 3 + 16.3 + 22.5 = 41.8
LEDGE_Z = FLOOR + CAV_LO_H

# meterbezel (voorkant, -Y)
BEZ_W, BEZ_H, BEZ_R = 58.0, 32.0, 5.0
BEZ_OUT = METER_T + 1.2 - WALL        # uitsteek zodat er 1.2 mm achterwand overblijft
BEZ_Z = 1.0 + BEZ_H / 2              # hart van de meter; bezel eindigt onder de dekselskirt
VENT_D = 2.5

# voetjes
FOOT_OD, FOOT_ID, FOOT_H = 12.0, 6.0, 3.5
FOOT_RECESS_D, FOOT_RECESS_H = FOOT_OD + 0.4, 1.6
FOOT_POS = [(sx * (BOX_W / 2 - 13), sy * (BOX_D / 2 - 13)) for sx in (-1, 1) for sy in (-1, 1)]

# ------------------------------------------------------------------ deksel (cap over de box)
LID_TOP = 3.0
SKIRT_T = 2.0
SKIRT_H = 8.0
SKIRT_IN_W, SKIRT_IN_D = BOX_W + 2 * CLR, BOX_D + 2 * CLR
SKIRT_IN_R = BOX_R + CLR
LID_W, LID_D, LID_R = SKIRT_IN_W + 2 * SKIRT_T, SKIRT_IN_D + 2 * SKIRT_T, SKIRT_IN_R + SKIRT_T
# gasket groef in de onderkant van de dekselplaat, boven de boxrand (rand = CAV_UP .. BOX)
GROOVE_W, GROOVE_DEPTH = 2.4, 1.2
RIM_MID_W, RIM_MID_D = (CAV_UP_W + BOX_W) / 2, (CAV_UP_D + BOX_D) / 2
RIM_MID_R = (CAV_UP_R + BOX_R) / 2
GASKET_W, GASKET_H = 2.2, 2.0         # 0.8 mm boven de groef uit -> wordt ingedrukt
# snap-detent: veertong in de skirt voor/achter, nokje 0.6 naar binnen, groefje in de boxwand
SNAP_W, SNAP_BUMP, SNAP_BUMP_H = 14.0, 0.6, 2.0
TONGUE_L, TONGUE_T = 16.0, 1.6      # veertong hangt langs de zijwand, langer dan de skirt
SNAP_SLOT = 1.0
SNAP_Z_BELOW = TONGUE_L - SNAP_BUMP_H / 2 - 0.5   # nok onderaan de tong
NOTCH_W, NOTCH_DEPTH, NOTCH_H = SNAP_W + 0.6, SNAP_BUMP + 0.15, SNAP_BUMP_H + 0.4
# handvat-oren op het deksel, pen naar buiten (X)
EAR_W, EAR_D, EAR_H = 6.0, 14.0, 10.5
PIN_D, PIN_L, PIN_LIP_D, PIN_LIP_L = 6.0, 8.8, 7.2, 0.8   # pen langer dan de arm (8) + speling, dan de borglip
PIN_Z = LID_TOP + 6.5                 # hoog genoeg dat greep (6 mm) plat op het deksel kan liggen

# ------------------------------------------------------------------ handvat
ARM_T, ARM_W = 8.0, 4.0               # langs pen-as (X) 8 breed, in draairichting 4 dik
ARM_L = 40.0                          # pen -> hart van de greep
BAR_W, BAR_H = 6.0, 6.0
HOLE_D = PIN_D + 0.4


def rrect(w, d, r, h, z=0.0):
    """Afgeronde rechthoek, gecentreerd in XY, van z tot z+h."""
    cs = CrossSection.square([w - 2 * r, d - 2 * r], True).offset(r, JoinType.Round, 2.0, 64)
    return cs.extrude(h).translate([0, 0, z])


def cyl(d, h, x=0.0, y=0.0, z=0.0):
    return Manifold.cylinder(h, d / 2).translate([x, y, z])


def box_part() -> Manifold:
    body = rrect(BOX_W, BOX_D, BOX_R, BOX_H)
    # meterbezel aan de voorkant
    bez_cs = CrossSection.square([BEZ_W - 2 * BEZ_R, BEZ_H - 2 * BEZ_R], True).offset(BEZ_R, JoinType.Round, 2.0, 32)
    bez = bez_cs.extrude(BEZ_OUT + WALL)                      # extrude langs Z, daarna kantelen naar -Y
    bez = bez.rotate([90, 0, 0])                             # nu langs -Y, vlak in XZ
    bez = bez.translate([0, -BOX_D / 2 + WALL, BEZ_Z])       # van binnenwand naar buiten
    body = body + bez
    # holtes
    body = body - rrect(CAV_LO_W, CAV_LO_D, T_R_BODY + 0.4, CAV_LO_H + 0.01, FLOOR)
    body = body - rrect(CAV_UP_W, CAV_UP_D, CAV_UP_R, CAV_UP_H + 1, LEDGE_Z)
    # meterpocket (vanaf de voorkant, 15 diep) + bezel-verzinking
    front_y = -BOX_D / 2 - BEZ_OUT
    pocket = Manifold.cube([METER_BODY_W + 0.4, METER_T + 0.2, METER_BODY_H + 0.4], True)
    pocket = pocket.translate([0, front_y + (METER_T + 0.2) / 2 - 0.01, BEZ_Z])
    recess = Manifold.cube([METER_BEZEL_W + 0.6, METER_BEZEL_T + 0.3, METER_BEZEL_H + 0.6], True)
    recess = recess.translate([0, front_y + (METER_BEZEL_T + 0.3) / 2 - 0.01, BEZ_Z])
    body = body - pocket - recess
    # ventilatiegaten van pocket naar binnenruimte (meter meet de lucht bij de potjes)
    for dx in (-15, -7.5, 0, 7.5, 15):
        v = Manifold.cylinder(WALL + BEZ_OUT + 2, VENT_D / 2).rotate([-90, 0, 0])
        body = body - v.translate([dx, -BOX_D / 2 - 1, BEZ_Z - 6])
    # snap-groefjes in voor- en achterwand
    for sx in (-1, 1):
        n = Manifold.cube([NOTCH_DEPTH * 2, NOTCH_W, NOTCH_H], True)
        body = body - n.translate([sx * BOX_W / 2, 0, BOX_H - SNAP_Z_BELOW])
    # voetjes-uitsparingen
    for (x, y) in FOOT_POS:
        body = body - cyl(FOOT_RECESS_D, FOOT_RECESS_H + 0.01, x, y, -0.01)
    return body


def lid_part() -> Manifold:
    """Deksel in eigen coördinaten: dekselplaat z in [0, LID_TOP], skirt eronder tot -SKIRT_H."""
    plate = rrect(LID_W, LID_D, LID_R, LID_TOP)
    skirt = rrect(LID_W, LID_D, LID_R, SKIRT_H, -SKIRT_H) - rrect(SKIRT_IN_W, SKIRT_IN_D, SKIRT_IN_R, SKIRT_H + 1, -SKIRT_H - 0.5)
    lid = plate + skirt
    # gasket-groef in onderkant plaat
    groove = rrect(RIM_MID_W + GROOVE_W, RIM_MID_D + GROOVE_W, RIM_MID_R + GROOVE_W / 2, GROOVE_DEPTH + 0.01, -0.01) \
        - rrect(RIM_MID_W - GROOVE_W, RIM_MID_D - GROOVE_W, RIM_MID_R - GROOVE_W / 2, GROOVE_DEPTH + 1, -0.5)
    lid = lid - groove
    # snap-tongen op de zijkanten: hangen TONGUE_L onder de plaat, los van de skirt via sleuven, nokje naar binnen
    for sx in (-1, 1):
        xc = sx * (SKIRT_IN_W / 2 + TONGUE_T / 2)
        tongue = Manifold.cube([TONGUE_T, SNAP_W, TONGUE_L], True).translate([xc, 0, -TONGUE_L / 2])
        lid = lid + tongue
        for sy in (-1, 1):
            slot = Manifold.cube([SKIRT_T * 2 + 1, SNAP_SLOT, SKIRT_H - 1.5], True)
            lid = lid - slot.translate([sx * (SKIRT_IN_W / 2 + SKIRT_T / 2), sy * (SNAP_W / 2 + SNAP_SLOT / 2), -SKIRT_H + (SKIRT_H - 1.5) / 2 - 0.01])
        bump = Manifold.cube([SNAP_BUMP, SNAP_W, SNAP_BUMP_H], True)
        lid = lid + bump.translate([sx * (SKIRT_IN_W / 2 - SNAP_BUMP / 2 + 0.001), 0, -SNAP_Z_BELOW])
    # handvat-oren + pennen
    for sx in (-1, 1):
        ear = Manifold.cube([EAR_W, EAR_D, EAR_H], True).translate([sx * (LID_W / 2 - EAR_W / 2), 0, LID_TOP + EAR_H / 2 - 0.01])
        pin = Manifold.cylinder(PIN_L, PIN_D / 2).rotate([0, sx * 90, 0]).translate([sx * LID_W / 2, 0, PIN_Z])
        lip = Manifold.cylinder(PIN_LIP_L, PIN_LIP_D / 2, PIN_D / 2 - 0.3).rotate([0, sx * 90, 0]).translate([sx * (LID_W / 2 + PIN_L), 0, PIN_Z])
        lid = lid + ear + pin + lip
    return lid


def gasket_part() -> Manifold:
    return rrect(RIM_MID_W + GASKET_W, RIM_MID_D + GASKET_W, RIM_MID_R + GASKET_W / 2, GASKET_H) \
        - rrect(RIM_MID_W - GASKET_W, RIM_MID_D - GASKET_W, RIM_MID_R - GASKET_W / 2, GASKET_H + 1, -0.5)


def foot_part() -> Manifold:
    return cyl(FOOT_OD, FOOT_H) - cyl(FOOT_ID, FOOT_H + 1, 0, 0, -0.5)


def handle_part(angle_deg: float = 0.0) -> Manifold:
    """Handvat in deksel-coördinaten, scharnierend om de X-as door de pennen (z=PIN_Z).
    angle 0 = rechtop, 90 = plat naar +Y op het deksel."""
    x_in = LID_W / 2 + 0.3                      # binnenkant arm net buiten het oor
    parts = []
    for sx in (-1, 1):
        arm = Manifold.cube([ARM_T, ARM_W, ARM_L], False).translate([0, -ARM_W / 2, 0])
        arm = arm + Manifold.cylinder(ARM_T, HOLE_D / 2 + 2.5).rotate([0, 90, 0])     # rond oog om de pen, 2.5 mm wand
        arm = arm - Manifold.cylinder(ARM_T + 2, HOLE_D / 2).rotate([0, 90, 0]).translate([-1, 0, 0])
        arm = arm.translate([x_in if sx > 0 else -x_in - ARM_T, 0, 0])
        parts.append(arm)
    bar = Manifold.cube([2 * (x_in + ARM_T), BAR_W, BAR_H], True).translate([0, 0, ARM_L])
    h = parts[0] + parts[1] + bar
    return h.rotate([angle_deg, 0, 0]).translate([0, 0, PIN_Z])


def meter_dummy() -> Manifold:
    """Meterlichaam 46x27x15 + bezel 48x28.5x1.5, in boxcoördinaten op zijn plek."""
    front_y = -BOX_D / 2 - BEZ_OUT
    body = Manifold.cube([METER_BODY_W, METER_T, METER_BODY_H], True).translate([0, front_y + METER_T / 2 + 0.1, BEZ_Z])
    bez = Manifold.cube([METER_BEZEL_W, METER_BEZEL_T, METER_BEZEL_H], True).translate([0, front_y + METER_BEZEL_T / 2 + 0.1, BEZ_Z])
    return body + bez


def load_tray_in_box() -> Manifold:
    import trimesh
    t = trimesh.load(TRAY_STL)
    v = np.asarray(t.vertices, dtype=np.float64); f = np.asarray(t.faces, dtype=np.uint32)
    v = v - [T_FLANGE_W / 2, T_FLANGE_D / 2, 0]                      # centreren (tray-STL loopt 0..99, 0..94)
    v = v + [0, 0, LEDGE_Z - T_BODY_H]                                 # flens rust op de richel
    mesh = m3.Mesh(vert_properties=v.astype(np.float32), tri_verts=f)
    return Manifold(mesh)


def export(m: Manifold, name: str):
    import trimesh
    mesh = m.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]; f = np.asarray(mesh.tri_verts)
    tm = trimesh.Trimesh(v, f, process=True)
    path = os.path.join(OUT, name)
    tm.export(path)
    print(f"  {name:22s} {tm.extents.round(1)}  watertight={tm.is_watertight}  vol={tm.volume/1000:.1f} cm3")
    return tm


def main():
    os.makedirs(OUT, exist_ok=True)
    box, lid, gasket, foot, handle = box_part(), lid_part(), gasket_part(), foot_part(), handle_part(90)
    print("Onderdelen:")
    export(box, "box.stl")
    export(lid.rotate([180, 0, 0]), "lid.stl")                         # printen met de bovenkant op het bed
    export(handle_part(0).translate([0, 0, -PIN_Z]).rotate([90, 0, 0]).translate([0, 0, HOLE_D / 2 + 2.5]), "handle.stl")
    export(gasket, "gasket.stl")
    export(foot, "foot.stl")
    export(box ^ rrect(BOX_W + 40, BOX_D + 40, 1, 24.0), "test_tray_fit.stl")
    export(box ^ Manifold.cube([BEZ_W + 8, 40, BEZ_H + 8], True).translate([0, -BOX_D / 2 - 6, BEZ_Z]), "test_meter_fit.stl")

    print("\nVerificatie:")
    ok = True
    tray = load_tray_in_box()
    inter = (tray ^ box).volume()
    print(f"  tray x box overlap           : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    tb = tray.bounding_box()
    print(f"  tray z-bereik in box         : {tb[2]:.2f} .. {tb[5]:.2f}  (richel {LEDGE_Z:.2f}, vloer {FLOOR})")
    ok &= abs(tb[2] - (LEDGE_Z - T_BODY_H)) < 1e-6 and tb[2] >= FLOOR
    jar_top = LEDGE_Z + T_FLANGE_H - POCKET_DEPTH + JAR_H
    print(f"  bovenkant potje              : {jar_top:.2f}  boxrand {BOX_H:.2f}  ruimte {BOX_H - jar_top:.2f}"); ok &= BOX_H - jar_top >= HEADSPACE - 1e-6
    md = meter_dummy()
    inter = (md ^ box).volume()
    print(f"  meter x box overlap          : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    # meter mag niet in de holte steken
    cav = rrect(CAV_UP_W, CAV_UP_D, CAV_UP_R, BOX_H, FLOOR)
    inter = (md ^ cav).volume()
    print(f"  meter x binnenruimte overlap : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    lid_on = lid.translate([0, 0, BOX_H])
    inter = (lid_on ^ box).volume()
    print(f"  deksel x box overlap         : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT (snapnok raakt zonder groef?)"); ok &= inter < 1e-6
    inter = (lid_on ^ tray).volume() + (lid_on ^ md).volume()
    print(f"  deksel x tray/meter overlap  : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    g_on = gasket.translate([0, 0, BOX_H - (GASKET_H - GROOVE_DEPTH)])   # gasket in de groef, 0.8 onder de plaat
    inter = (g_on ^ lid_on).volume()
    print(f"  gasket x deksel overlap      : {inter:.3f} mm3  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    for ang, naam in ((0, "rechtop"), (90, "plat"), (45, "half")):
        h_on = handle_part(ang).translate([0, 0, BOX_H])
        inter = (h_on ^ lid_on).volume() + (h_on ^ box).volume()
        hb = h_on.bounding_box()
        print(f"  handvat {naam:8s} overlap     : {inter:.3f} mm3  z {hb[2]:.1f}..{hb[5]:.1f}  ->", "OK" if inter < 1e-6 else "FOUT"); ok &= inter < 1e-6
    # detent: nok in de skirt moet in de groef van de box vallen (dus overlap met box zónder groef > 0)
    box_no_notch = rrect(BOX_W, BOX_D, BOX_R, BOX_H)
    inter = (lid_on ^ box_no_notch).volume()
    print(f"  snapnok grijpt in boxwand    : {inter:.2f} mm3 (moet > 0) ->", "OK" if inter > 1 else "FOUT"); ok &= inter > 1
    fo = 0.0
    for (x, y) in FOOT_POS:
        f_on = foot.translate([x, y, -(FOOT_H - FOOT_RECESS_H + 0.1)])
        fo += (f_on ^ box).volume()
    print(f"  voetjes x box overlap        : {fo:.3f} mm3  ->", "OK" if fo < 1e-6 else "FOUT"); ok &= fo < 1e-6
    # bezel moet onder de skirt en de tongen blijven
    bez_top = BEZ_Z + BEZ_H / 2
    print(f"  bezel top {bez_top:.1f} < skirt onderkant {BOX_H - SKIRT_H:.1f} ->", "OK" if bez_top < BOX_H - SKIRT_H - 0.3 else "FOUT"); ok &= bez_top < BOX_H - SKIRT_H - 0.3
    print(f"\nBuitenmaat box {BOX_W} x {BOX_D} x {BOX_H} mm, met deksel {LID_W} x {LID_D} x {BOX_H + LID_TOP + EAR_H:.1f} mm, bezel steekt {BEZ_OUT:.1f} mm uit.")
    print("RESULTAAT:", "ALLES PAST" if ok else "ER IS EEN PROBLEEM")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
