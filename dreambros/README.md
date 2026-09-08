# Dreambros HETI-box

Koelbox-stijl opbergbox voor de bestaande **Dreambros_Tray** (4 dabpotjes Ø38), met ingebouwde
thermo/hygrometer aan de voorkant, TPU-afdichtring in het deksel, TPU-voetjes en een klapbaar beugelhandvat.
Bedoeld als bundelproduct: klant koopt meerdere potjes, krijgt/koopt de box erbij.

De tray is leidend. Alle maten zijn uit `reference/Dreambros_Tray.stl` gemeten, niet geschat.

## Gemeten tray-maten

| Feature | Maat |
|---|---|
| Totaal | 99 × 94 × 20 mm |
| Body (onder de flens) | 90,8 × 85,8 × 16,5 mm, hoek R5 |
| Flens | 99 × 94 × 3,5 mm, hoek R7 |
| Pockets | 4 × Ø38,6 mm, 16 mm diep, bodem 4 mm |
| Steek | 47 mm (X) × 42 mm (Y) |
| Uitdrukgaten | Ø20 onder elke pocket, Ø16 centraal |

## Ontwerp v1

| Onderdeel | Materiaal | Maat | Opmerking |
|---|---|---|---|
| `box.stl` | PLA | 106 × 101 × 42,3 mm (+13 mm bezel voor) | tray rust met de flens op een richel op 19,8 mm, body zweeft 0,3 mm boven de vloer |
| `lid.stl` | PLA | 110,6 × 105,6 mm, cap over de box | skirt 8 mm, snaptongen 16 mm aan de zijkanten, gasketgroef, handvat-oren met pennen |
| `handle.stl` | PLA | beugel, armen 40 mm | klikt over de pennen (Ø6, lip Ø7,2), ligt plat op het deksel of staat rechtop |
| `gasket.stl` | TPU | ring 2,2 × 2,0 mm | zit 1,2 mm in de groef, 0,8 mm wordt ingedrukt op de boxrand |
| `foot.stl` (4×) | TPU | Ø12 × 3,5 mm | in Ø12,4 uitsparingen, 1,9 mm zichtbaar |
| `test_tray_fit.stl` | PLA | onderste 24 mm van de box | pasprint voor de tray, eerst printen |
| `test_meter_fit.stl` | PLA | alleen de bezel | pasprint voor de meter, eerst printen |

Meter: standaard mini thermo/hygrometer, body 46 × 27 × 15 mm, front-bezel 48 × 28,5 mm (Veanic/Goabroa/Twinschip-type,
LR44). Gaat van voren in de bezel, 5 ventilatiegaten Ø2,5 naar de binnenruimte zodat hij de lucht bij de potjes meet.

**Aanname die je moet nameten:** hoogte van het Dreambros-potje met deksel = 32 mm (`JAR_H` in `heti_box.py`).
Bij een ander getal: aanpassen, script draaien, klaar. De boxhoogte volgt automatisch (3 mm headspace).

## Genereren en verifiëren

```
pip install manifold3d trimesh numpy matplotlib
python3 heti_box.py          # schrijft output/*.stl en draait de passingscontrole
python3 render_preview.py    # PNG-previews in output/
```

De passingscontrole berekent booleaanse overlap tussen de originele tray-STL, een metermodel, deksel, gasket,
handvat (3 standen) en voetjes met de box. Alles moet 0 mm³ zijn en de snapnok moet juist wél de boxwand grijpen.
Exit-code 1 als iets niet past.

## Printvolgorde

1. `test_tray_fit.stl` en `test_meter_fit.stl` (samen < 1 uur). Tray moet op de richel rusten, meter met lichte wrijving klikken.
2. Past het niet: `CLR` (speling tray) of de meterpocket-maten aanpassen in `heti_box.py`, opnieuw draaien.
3. `box.stl` rechtop, 3 perimeters, geen support nodig (bezel is 13 mm uitkraging met R5, print zonder support bij 0,2 mm lagen; anders support alleen onder de bezel).
4. `lid.stl` staat al in printstand (bovenkant op het bed). Support alleen onder de twee horizontale pennen.
5. `handle.stl` plat, `gasket.stl` en `foot.stl` in TPU (95A), gasket 100% infill.
6. Kleurbanden zoals de referentie: filamentwissel op laaghoogte in de slicer, geen extra geometrie nodig.

## Nog niet in v1

- Branding/logo-reliëf op het deksel (SVG uit de Drambros-website-sessie kan als extrude erop).
- Vriesblok-insert: alleen zinvol als er rosin in de potjes zit. De onderste holte is 91,6 × 86,4 × 16,8 mm; daar past
  een PETG-waterblok onder de tray als de tray 12 mm hoger komt te zitten.
- Sluiting is een detent (snapnok 0,6 mm), geen slot. Test de kracht met de eerste print; zwakker: `SNAP_BUMP` 0,4.
