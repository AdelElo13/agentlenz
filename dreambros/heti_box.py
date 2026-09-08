#!/usr/bin/env python3
"""
Dreambros HETI-box v3 voor de Dreambros_Tray (4 dabpotjes Ø38).

Parametrisch model. Alle maten in mm. Genereert STL's in ./output en
verifieert computationeel dat de originele tray, de ronde Bambu XF001
thermo/hygrometer (Ø45 x 14, rond, in een boss op de VOORKANT), het deksel en het handvat passen.

Onderdelen:
  box.stl              PLA  - romp met ronde meterboss op de voorkant, voetjes-uitsparingen, snap-groefjes
  lid.stl              PLA  - cap-deksel met verdiept logo, venster in de skirt boven de boss, snaptongen, handvat-oren
  lid_logo_inlay.stl   PLA  - losse letters die in het verdiepte logo vallen (tweede kleur)
  handle.stl           PLA  - beugelhandvat, klikt op de pennen van het deksel
  gasket.stl           TPU  - afdichtring in het deksel
  foot.stl             TPU  - voetje (4x printen)
  test_tray_fit.stl    PLA  - onderste 24 mm van de box, pasprint voor de tray
  test_meter_fit.stl   PLA  - alleen de meterboss, pasprint voor de XF001

Logo: als reference/logo.svg bestaat wordt die gebruikt, anders de tekst LOGO_TEXT.

Gebruik:  python3 heti_box.py            (schrijft output/*.stl en verifieert)
"""
from __future__ import annotations
import os, sys
import numpy as np
import manifold3d as m3
from manifold3d import Manifold, CrossSection, JoinType, FillRule

m3.set_circular_segments(96)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
TRAY_STL = os.path.join(HERE, "reference", "Dreambros_Tray.stl")
LOGO_SVG = os.path.join(HERE, "reference", "logo.svg")

# ------------------------------------------------------------------ tray (gemeten uit Dreambros_Tray.stl)
T_FLANGE_W, T_FLANGE_D, T_FLANGE_H = 99.0, 94.0, 3.5
T_BODY_W, T_BODY_D, T_BODY_H = 90.8, 85.8, 16.5
T_R_BODY, T_R_FLANGE = 5.0, 7.0
POCKET_D, POCKET_DEPTH = 38.6, 16.0
POCKET_XY = [(sx * 23.5, sy * 21.0) for sx in (-1, 1) for sy in (-1, 1)]

# ------------------------------------------------------------------ potje
JAR_D = 38.0          # past in Ø38.6 pocket
JAR_H = 32.0          # AANNAME: hoogte potje met deksel. Meet na.
JAR_PROTRUSION = JAR_H - POCKET_DEPTH

# ------------------------------------------------------------------ meter: Bambu Lab XF001 (rond, Ø45 x 14)
MET_FLANGE_D, MET_FLANGE_T = 45.5, 1.5     # zichtbare rand aan de voorkant
MET_BODY_D, MET_T = 43.0, 14.0             # body dat door het gat gaat, totale dikte
MET_HOLE_D = MET_BODY_D + 0.4              # inbouwgat in de dekselplaat
MET_RECESS_D, MET_RECESS_T = MET_FLANGE_D + 0.4, 1.2   # verzinking voor de rand, rand steekt 0.3 uit
MET_POCKET_DEPTH = MET_RECESS_T + (MET_T - MET_FLANGE_T) + 0.3   # 14.0, blind gat vanaf de voorkant
BOSS_D = 50.0                              # ronde boss op de voorkant, 2.25 mm rand om de meter
BOSS_OUT = MET_POCKET_DEPTH + 1.2 - 3.2    # steekt 12 mm uit de wand; 1.2 mm achterwand blijft over
BOSS_ZC = BOSS_D / 2 + 1.0                 # hart van de meter, 1 mm boven de onderkant
VENT_D = 2.5

# ------------------------------------------------------------------ box
CLR = 0.3
WALL = 3.2
FLOOR = 3.0
LID_TOP = 3.0
HEADSPACE_MIN = 3.0
CAV_LO_W, CAV_LO_D = T_BODY_W + 2 * 0.4, T_BODY_D + 2 * 0.4
CAV_LO_H = T_BODY_H + 0.3                  # flens draagt op de richel, body zweeft 0.3 boven de vloer
CAV_UP_W, CAV_UP_D = T_FLANGE_W + 2 * CLR, T_FLANGE_D + 2 * CLR
CAV_UP_R = T_R_FLANGE + CLR
BOX_H_BOSS = BOSS_ZC + BOSS_D / 2 + 1.0    # boss moet 1 mm onder de boxrand blijven
BOX_H_JARS = FLOOR + CAV_LO_H + T_FLANGE_H + JAR_PROTRUSION + HEADSPACE_MIN
BOX_H = max(BOX_H_BOSS, BOX_H_JARS)
HEADSPACE = BOX_H - (FLOOR + CAV_LO_H + T_FLANGE_H + JAR_PROTRUSION)
CAV_UP_H = T_FLANGE_H + JAR_PROTRUSION + HEADSPACE
BOX_W = CAV_UP_W + 2 * WALL                # 106.0
BOX_D = CAV_UP_D + 2 * WALL                # 101.0
BOX_R = CAV_UP_R + WALL                    # 10.5
LEDGE_Z = FLOOR + CAV_LO_H
JAR_TOP_Z = LEDGE_Z + T_FLANGE_H - POCKET_DEPTH + JAR_H

# voetjes
FOOT_OD, FOOT_ID, FOOT_H = 12.0, 6.0, 3.5
FOOT_RECESS_D, FOOT_RECESS_H = FOOT_OD + 0.4, 1.6
FOOT_POS = [(sx * (BOX_W / 2 - 13), sy * (BOX_D / 2 - 13)) for sx in (-1, 1) for sy in (-1, 1)]

# ------------------------------------------------------------------ deksel (cap over de box)
SKIRT_T = 2.0
SKIRT_H = 8.0
SKIRT_IN_W, SKIRT_IN_D = BOX_W + 2 * CLR, BOX_D + 2 * CLR
SKIRT_IN_R = BOX_R + CLR
LID_W, LID_D, LID_R = SKIRT_IN_W + 2 * SKIRT_T, SKIRT_IN_D + 2 * SKIRT_T, SKIRT_IN_R + SKIRT_T
GROOVE_W, GROOVE_DEPTH = 2.4, 1.2
RIM_MID_W, RIM_MID_D = (CAV_UP_W + BOX_W) / 2, (CAV_UP_D + BOX_D) / 2
RIM_MID_R = (CAV_UP_R + BOX_R) / 2
GASKET_W, GASKET_H = 2.2, 2.0
SNAP_W, SNAP_BUMP, SNAP_BUMP_H = 14.0, 0.6, 2.0
TONGUE_L, TONGUE_T = 16.0, 1.6
SNAP_SLOT = 1.0
SNAP_Z_BELOW = TONGUE_L - SNAP_BUMP_H / 2 - 0.5
NOTCH_W, NOTCH_DEPTH, NOTCH_H = SNAP_W + 0.6, SNAP_BUMP + 0.15, SNAP_BUMP_H + 0.4
EAR_W, EAR_D, EAR_H = 6.0, 14.0, 10.5
PIN_D, PIN_L, PIN_LIP_D, PIN_LIP_L = 6.0, 8.8, 7.2, 0.8
PIN_Z = LID_TOP + 6.5
SKIRT_WINDOW_W = BOSS_D + 2.0              # venster in de skirt aan de voorkant, boven de boss

# logo (verdiept in de dekselplaat, aan de voorkant onder de meter)
LOGO_TEXT = "DREAMBROS"
LOGO_W = 78.0                              # doelbreedte
LOGO_DEPTH = 0.6
LOGO_Y = 0.0                               # logo in het hart van het deksel
INLAY_CLR = 0.1

# ------------------------------------------------------------------ handvat
ARM_T, ARM_W = 8.0, 4.0
ARM_L = 40.0
BAR_W, BAR_H = 6.0, 6.0
HOLE_D = PIN_D + 0.4
EYE_R = HOLE_D / 2 + 2.5


def rrect(w, d, r, h, z=0.0):
    cs = CrossSection.square([w - 2 * r, d - 2 * r], True).offset(r, JoinType.Round, 2.0, 64)
    return cs.extrude(h).translate([0, 0, z])


def cyl(d, h, x=0.0, y=0.0, z=0.0):
    return Manifold.cylinder(h, d / 2).translate([x, y, z])


def logo_cross_section() -> CrossSection:
    """Logo als 2D-doorsnede, gecentreerd, LOGO_W breed. SVG als die er is, anders tekst."""
    if os.path.exists(LOGO_SVG):
        import trimesh
        path = trimesh.load_path(LOGO_SVG)
        polys = []
        for poly in path.polygons_full:
            polys.append([tuple(p) for p in np.array(poly.exterior.coords)[:-1]])
            for hole in poly.interiors:
                polys.append([tuple(p) for p in np.array(hole.coords)[:-1]])
        cs = CrossSection(polys, FillRule.EvenOdd)
        cs = cs.mirror([0, 1]) if False else cs
    else:
        from matplotlib.textpath import TextPath
        from matplotlib.font_manager import FontProperties
        tp = TextPath((0, 0), LOGO_TEXT, size=10, prop=FontProperties(family="DejaVu Sans", weight="bold"))
        cs = CrossSection([[tuple(p) for p in np.array(c)] for c in tp.to_polygons()], FillRule.EvenOdd)
    b = cs.bounds()
    w, d = b[2] - b[0], b[3] - b[1]
    s = LOGO_W / w
    cs = cs.translate([-(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2]).scale([s, s])
    return cs


def box_part(notches: bool = True) -> Manifold:
    body = rrect(BOX_W, BOX_D, BOX_R, BOX_H)
    body = body - rrect(CAV_LO_W, CAV_LO_D, T_R_BODY + 0.4, CAV_LO_H + 0.01, FLOOR)
    # ronde meterboss op de voorkant: cilinder langs Y + vulling naar de vloer (D-profiel, geen overhang naar beneden)
    y_in = -BOX_D / 2 + WALL
    depth = BOSS_OUT + WALL
    boss = Manifold.cylinder(depth, BOSS_D / 2).rotate([90, 0, 0]).translate([0, y_in, BOSS_ZC])
    fill = Manifold.cube([BOSS_D, depth, BOSS_ZC], False).translate([-BOSS_D / 2, y_in - depth, 0])
    body = body + boss + fill
    body = body - rrect(CAV_UP_W, CAV_UP_D, CAV_UP_R, CAV_UP_H + 1, LEDGE_Z)
    # blind gat voor de meter vanaf de voorkant + verzinking voor de rand
    y_front = -BOX_D / 2 - BOSS_OUT
    body = body - Manifold.cylinder(MET_POCKET_DEPTH + 1, MET_HOLE_D / 2).rotate([-90, 0, 0]).translate([0, y_front - 1, BOSS_ZC])
    body = body - Manifold.cylinder(MET_RECESS_T + 1, MET_RECESS_D / 2).rotate([-90, 0, 0]).translate([0, y_front - 1, BOSS_ZC])
    # ventilatiegaten van het gat naar de binnenruimte (meter meet de lucht bij de potjes)
    for dx in (-12, -6, 0, 6, 12):
        body = body - Manifold.cylinder(depth + 2, VENT_D / 2).rotate([-90, 0, 0]).translate([dx, y_front - 1, BOSS_ZC + 14])
    for sx in ((-1, 1) if notches else ()):
        n = Manifold.cube([NOTCH_DEPTH * 2, NOTCH_W, NOTCH_H], True)
        body = body - n.translate([sx * BOX_W / 2, 0, BOX_H - SNAP_Z_BELOW])
    for (x, y) in FOOT_POS:
        body = body - cyl(FOOT_RECESS_D, FOOT_RECESS_H + 0.01, x, y, -0.01)
    return body


def lid_part(with_logo: bool = True) -> Manifold:
    """Deksel in eigen coördinaten: plaat z in [0, LID_TOP], skirt eronder."""
    plate = rrect(LID_W, LID_D, LID_R, LID_TOP)
    skirt = rrect(LID_W, LID_D, LID_R, SKIRT_H, -SKIRT_H) - rrect(SKIRT_IN_W, SKIRT_IN_D, SKIRT_IN_R, SKIRT_H + 1, -SKIRT_H - 0.5)
    lid = plate + skirt
    groove = rrect(RIM_MID_W + GROOVE_W, RIM_MID_D + GROOVE_W, RIM_MID_R + GROOVE_W / 2, GROOVE_DEPTH + 0.01, -0.01) \
        - rrect(RIM_MID_W - GROOVE_W, RIM_MID_D - GROOVE_W, RIM_MID_R - GROOVE_W / 2, GROOVE_DEPTH + 1, -0.5)
    lid = lid - groove
    # venster in de voorkant van de skirt, zodat het deksel over de meterboss valt
    win = Manifold.cube([SKIRT_WINDOW_W, SKIRT_T * 2 + 2, SKIRT_H + 1], True)
    lid = lid - win.translate([0, -LID_D / 2 + SKIRT_T / 2, -SKIRT_H / 2 - 0.5 - 0.01])
    # logo verdiept in de bovenkant
    if with_logo:
        lid = lid - logo_cross_section().extrude(LOGO_DEPTH + 0.01).translate([0, LOGO_Y, LID_TOP - LOGO_DEPTH])
    # snaptongen op de zijkanten
    for sx in (-1, 1):
        xc = sx * (SKIRT_IN_W / 2 + TONGUE_T / 2)
        lid = lid + Manifold.cube([TONGUE_T, SNAP_W, TONGUE_L], True).translate([xc, 0, -TONGUE_L / 2])
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


def logo_inlay_part() -> Manifold:
    """Losse letters, 0.1 mm kleiner, vallen in het verdiepte logo (tweede kleur, vlak met de bovenkant)."""
    cs = logo_cross_section().offset(-INLAY_CLR, JoinType.Round, 2.0, 16)
    return cs.extrude(LOGO_DEPTH)


def gasket_part() -> Manifold:
    return rrect(RIM_MID_W + GASKET_W, RIM_MID_D + GASKET_W, RIM_MID_R + GASKET_W / 2, GASKET_H) \
        - rrect(RIM_MID_W - GASKET_W, RIM_MID_D - GASKET_W, RIM_MID_R - GASKET_W / 2, GASKET_H + 1, -0.5)


def foot_part() -> Manifold:
    return cyl(FOOT_OD, FOOT_H) - cyl(FOOT_ID, FOOT_H + 1, 0, 0, -0.5)


def handle_part(angle_deg: float = 0.0) -> Manifold:
    """Handvat in deksel-coördinaten, scharnierend om de X-as door de pennen. 0 = rechtop, 90 = plat naar +Y."""
    x_in = LID_W / 2 + 0.3
    parts = []
    for sx in (-1, 1):
        arm = Manifold.cube([ARM_T, ARM_W, ARM_L], False).translate([0, -ARM_W / 2, 0])
        arm = arm + Manifold.cylinder(ARM_T, EYE_R).rotate([0, 90, 0])
        arm = arm - Manifold.cylinder(ARM_T + 2, HOLE_D / 2).rotate([0, 90, 0]).translate([-1, 0, 0])
        arm = arm.translate([x_in if sx > 0 else -x_in - ARM_T, 0, 0])
        parts.append(arm)
    bar = Manifold.cube([2 * (x_in + ARM_T), BAR_W, BAR_H], True).translate([0, 0, ARM_L])
    h = parts[0] + parts[1] + bar
    return h.rotate([angle_deg, 0, 0]).translate([0, 0, PIN_Z])


def meter_dummy_box() -> Manifold:
    """XF001 in boxcoördinaten, in de boss: rand Ø45.5 x 1.5 in de verzinking (0.3 uitstekend), body Ø43 erachter."""
    y_front = -BOX_D / 2 - BOSS_OUT
    y0 = y_front - (MET_FLANGE_T - MET_RECESS_T)                     # voorkant van de rand
    flange = Manifold.cylinder(MET_FLANGE_T, MET_FLANGE_D / 2).rotate([-90, 0, 0]).translate([0, y0, BOSS_ZC])
    body = Manifold.cylinder(MET_T - MET_FLANGE_T, MET_BODY_D / 2).rotate([-90, 0, 0]).translate([0, y0 + MET_FLANGE_T, BOSS_ZC])
    return flange + body


def meter_coupon(box: Manifold) -> Manifold:
    """Pasprint: alleen de boss met een stuk voorwand, zelfde printstand als de box."""
    return box ^ Manifold.cube([BOSS_D + 8, BOSS_OUT + WALL + 4, BOX_H + 2], True).translate([0, -BOX_D / 2 - BOSS_OUT / 2 + 0.5, BOX_H / 2])


def load_tray_in_box() -> Manifold:
    import trimesh
    t = trimesh.load(TRAY_STL)
    v = np.asarray(t.vertices, dtype=np.float64); f = np.asarray(t.faces, dtype=np.uint32)
    v = v - [T_FLANGE_W / 2, T_FLANGE_D / 2, 0] + [0, 0, LEDGE_Z - T_BODY_H]
    return Manifold(m3.Mesh(vert_properties=v.astype(np.float32), tri_verts=f))


def jars_in_box() -> Manifold:
    j = None
    for (x, y) in POCKET_XY:
        c = cyl(JAR_D, JAR_H, x, y, LEDGE_Z + T_FLANGE_H - POCKET_DEPTH)
        j = c if j is None else j + c
    return j


def export(m: Manifold, name: str):
    import trimesh
    mesh = m.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]; f = np.asarray(mesh.tri_verts)
    tm = trimesh.Trimesh(v, f, process=True)
    tm.export(os.path.join(OUT, name))
    print(f"  {name:22s} {tm.extents.round(1)}  watertight={tm.is_watertight}  vol={tm.volume/1000:.1f} cm3")
    return tm


def main():
    os.makedirs(OUT, exist_ok=True)
    box, lid, gasket, foot = box_part(), lid_part(), gasket_part(), foot_part()
    inlay = logo_inlay_part()
    print("Onderdelen:")
    export(box, "box.stl")
    export(lid.rotate([180, 0, 0]), "lid.stl")                                   # bovenkant op het bed
    export(inlay.rotate([180, 0, 0]).translate([0, 0, LOGO_DEPTH]), "lid_logo_inlay.stl")   # zichtkant op het bed
    export(handle_part(0).translate([0, 0, -PIN_Z]).rotate([90, 0, 0]).translate([0, 0, EYE_R]), "handle.stl")
    export(gasket, "gasket.stl")
    export(foot, "foot.stl")
    export(box ^ rrect(BOX_W + 40, BOX_D + 40, 1, 24.0), "test_tray_fit.stl")
    export(meter_coupon(box), "test_meter_fit.stl")

    print("\nVerificatie:")
    ok = True
    def chk(label, val, cond, unit="mm3"):
        nonlocal ok
        print(f"  {label:34s}: {val:8.3f} {unit}  ->", "OK" if cond else "FOUT"); ok &= cond
    tray, jars = load_tray_in_box(), jars_in_box()
    chk("tray x box overlap", (tray ^ box).volume(), (tray ^ box).volume() < 1e-6)
    tb = tray.bounding_box()
    chk("tray onderkant boven de vloer", tb[2] - FLOOR, tb[2] >= FLOOR - 1e-6, "mm")
    chk("ruimte boven potjes tot boxrand", BOX_H - JAR_TOP_Z, BOX_H - JAR_TOP_Z >= HEADSPACE - 1e-6, "mm")
    lid_on = lid.translate([0, 0, BOX_H]); met_on = meter_dummy_box()
    chk("meter x box overlap", (met_on ^ box).volume(), (met_on ^ box).volume() < 1e-6)
    cav = rrect(CAV_UP_W, CAV_UP_D, CAV_UP_R, BOX_H, FLOOR)
    chk("meter x binnenruimte overlap", (met_on ^ cav).volume(), (met_on ^ cav).volume() < 1e-6)
    chk("meter x deksel overlap", (met_on ^ lid_on).volume(), (met_on ^ lid_on).volume() < 1e-6)
    mb = met_on.bounding_box()
    chk("meter rand voor de boss (uitsteek)", (-BOX_D / 2 - BOSS_OUT) - mb[1], True, "mm")
    chk("boss top onder de boxrand", BOX_H - (BOSS_ZC + BOSS_D / 2), BOX_H - (BOSS_ZC + BOSS_D / 2) >= 1.0 - 1e-6, "mm")
    chk("deksel x box overlap", (lid_on ^ box).volume(), (lid_on ^ box).volume() < 1e-6)
    chk("deksel x tray/potjes overlap", (lid_on ^ tray).volume() + (lid_on ^ jars).volume(), (lid_on ^ tray).volume() + (lid_on ^ jars).volume() < 1e-6)
    g_on = gasket.translate([0, 0, BOX_H - (GASKET_H - GROOVE_DEPTH)])
    chk("gasket x deksel overlap", (g_on ^ lid_on).volume(), (g_on ^ lid_on).volume() < 1e-6)
    inl_on = inlay.translate([0, LOGO_Y, BOX_H + LID_TOP - LOGO_DEPTH])
    chk("logo-inlay x deksel overlap", (inl_on ^ lid_on).volume(), (inl_on ^ lid_on).volume() < 1e-6)
    for ang, naam in ((0, "rechtop"), (90, "plat"), (45, "half")):
        h_on = handle_part(ang).translate([0, 0, BOX_H])
        v = (h_on ^ lid_on).volume() + (h_on ^ box).volume() + (h_on ^ met_on).volume()
        chk(f"handvat {naam} overlap", v, v < 1e-6)
    box_no_notch = box_part(notches=False)
    chk("snapnok grijpt in boxwand (>0)", (lid_on ^ box_no_notch).volume(), (lid_on ^ box_no_notch).volume() > 1)
    fo = sum((foot.translate([x, y, -(FOOT_H - FOOT_RECESS_H + 0.1)]) ^ box).volume() for (x, y) in FOOT_POS)
    chk("voetjes x box overlap", fo, fo < 1e-6)
    print(f"\nBox {BOX_W} x {BOX_D} x {BOX_H:.1f} mm, met deksel {LID_W} x {LID_D} x {BOX_H + LID_TOP + EAR_H:.1f} mm.")
    print(f"Meter Ø{MET_FLANGE_D} zit in een boss Ø{BOSS_D} op de voorkant, {BOSS_OUT:.1f} mm uitstekend, gat Ø{MET_HOLE_D}, {MET_POCKET_DEPTH:.1f} mm diep. Logo: {'SVG' if os.path.exists(LOGO_SVG) else 'tekst ' + LOGO_TEXT}.")
    print("RESULTAAT:", "ALLES PAST" if ok else "ER IS EEN PROBLEEM")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
