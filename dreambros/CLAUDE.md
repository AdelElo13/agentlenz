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
- Meter: Bambu Lab XF001, rond, rand Ø45,5 x 1,5, body Ø43, totaal 14 mm dik. Inbouwgat Ø43,4. Zit in een ronde boss Ø50 op de VOORKANT (eis van de eigenaar).
- Logo: verdiept 0,6 mm in het deksel. reference/logo.svg wordt automatisch gebruikt als die bestaat, anders tekst DREAMBROS.

## Working style
- Always start in Plan Mode. No code before the plan is approved.
- When in doubt: ask, never assume. Uitzondering: JAR_H staat als expliciete aanname in heti_box.py.
- Plaatsing, vorm en functie van onderdelen (waar zit de meter, hoe sluit het deksel, wat zit waar) beslis ik NIET zelf. Eerst vragen, dan bouwen. Fout gemaakt in v2: meter zonder overleg naar het deksel verplaatst. De eigenaar wil de ronde meter op de VOORKANT.
- Deliver full files, not snippets or diffs unless explicitly asked.
- Verify your own work: describe how you'll check correctness before executing.

## Verification
- `python3 heti_box.py` genereert output/*.stl en draait de passingscontrole (booleaanse overlap van tray, meter, deksel, gasket, handvat en voetjes met de box moet 0 zijn). Exit-code 1 bij een fout.
- `python3 render_preview.py` maakt PNG-previews in output/.
- Fysieke verificatie vóór de volledige print: test_tray_fit.stl (tray moet op de richel rusten) en test_meter_fit.stl (XF001 moet met lichte wrijving in de boss vallen, rand 0,3 mm uitstekend).
- Ontwerpwijziging = parameter aanpassen, script draaien, verificatie moet ALLES PAST geven.

## What I do NOT want
- Geen karakters of merken van anderen (geen HETI/YETI-parodie, geen Nickelodeon-figuren).
- Geen wijziging van de tray-maten in dit model; de tray is leidend.
- Geen nieuwe dependencies zonder overleg (huidig: manifold3d, trimesh, numpy, matplotlib, lxml voor 3MF).
- Geen supports op zichtvlakken; oppervlak moet glad en krasvrij zijn.

## Known pitfalls
- manifold3d: `cube(size, center=False)` begint in de oorsprong; `cylinder` staat langs Z, roteer met `rotate([0,90,0])` voor X-as.
- Een Ø45-meter op de voorwand vraagt een box van 52 mm hoog en een venster in de dekselskirt boven de boss. Zo gebouwd in v3.
- De boss heeft een D-profiel (rond boven, recht naar de vloer) zodat er geen overhang naar beneden is: printbaar zonder support, glad.
- Deksel wordt met de bovenkant op het bed geprint: alles op de bovenkant moet verdiept zijn, nooit verhoogd.
- Handvat-oog moet groter zijn dan het pengat, anders eet het gat het oog op (gebeurd in v0).
- Horizontale pennen op het deksel: kleine overhang, eventueel support alleen onder de pennen.
