# Project: Dreambros HETI-box

## Context
- What this builds: een 3D-geprinte koelbox-stijl opbergbox voor de bestaande Dreambros_Tray (4 dabpotjes), met ingebouwde thermo/hygrometer, TPU-afdichtring en TPU-voetjes. Bundelproduct voor klanten die meerdere potjes kopen.
- Stack: Python 3 + manifold3d (CSG) + trimesh (STL-export/meting). Geen OpenSCAD nodig.
- Platform: FDM 3D-print, PLA (romp/deksel/handvat) + TPU (gasket/voetjes).
- Phase: MVP, eerste werkend exemplaar.

## Vaste maten (gemeten uit reference/Dreambros_Tray.stl, NIET wijzigen zonder nieuwe tray)
- Tray: 99 x 94 x 20 mm. Body 90,8 x 85,8 x 16,5 (hoek R5). Flens 99 x 94 x 3,5 (hoek R7).
- 4 pockets Ø38,6 mm, 16 mm diep, bodem 4 mm. Steek 47 mm (X) x 42 mm (Y).
- Uitdrukgaten Ø20 onder elke pocket, centraal gat Ø16.
- Dreambros dabpotje: Ø38 mm. Hoogte met deksel: AANNAME 32 mm (parameter JAR_H). Meet na.
- Meter: standaard mini thermo/hygrometer, body 46 x 27 x 15 mm, front-bezel 48 x 28,5 x 1,5 mm.

## Working style
- Always start in Plan Mode. No code before the plan is approved.
- When in doubt: ask, never assume. Uitzondering: JAR_H staat als expliciete aanname in heti_box.py.
- Deliver full files, not snippets or diffs unless explicitly asked.
- Verify your own work: describe how you'll check correctness before executing.

## Verification
- `python3 heti_box.py` genereert output/*.stl en draait de passingscontrole (booleaanse overlap van tray, meter, deksel, gasket, handvat en voetjes met de box moet 0 zijn). Exit-code 1 bij een fout.
- `python3 render_preview.py` maakt PNG-previews in output/.
- Fysieke verificatie vóór de volledige print: test_tray_fit.stl (tray moet op de richel rusten) en test_meter_fit.stl (meter moet met lichte wrijving in de bezel klikken).
- Ontwerpwijziging = parameter aanpassen, script draaien, verificatie moet ALLES PAST geven.

## What I do NOT want
- Geen karakters of merken van anderen (geen HETI/YETI-parodie, geen Nickelodeon-figuren).
- Geen wijziging van de tray-maten in dit model; de tray is leidend.
- Geen nieuwe dependencies zonder overleg (huidig: manifold3d, trimesh, numpy, matplotlib).

## Known pitfalls
- manifold3d: `cube(size, center=False)` begint in de oorsprong; `cylinder` staat langs Z, roteer met `rotate([0,90,0])` voor X-as.
- De meterbezel steekt 13 mm uit de voorwand; de dekselskirt (8 mm) en de snaptongen (zijkanten) moeten daar vrij van blijven.
- Handvat-oog moet groter zijn dan het pengat, anders eet het gat het oog op (gebeurd in v0).
- Horizontale pennen op het deksel: kleine overhang, eventueel support alleen onder de pennen.
