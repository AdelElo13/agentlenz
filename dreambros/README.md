# Dreambros HETI-box

Koelbox-stijl opbergbox voor de bestaande **Dreambros_Tray** (4 dabpotjes Ø38), met de ronde Bambu Lab XF001
thermo/hygrometer in een ronde boss op de voorkant, verdiept DREAMBROS-logo met losse inlay in een tweede kleur, TPU-afdichtring,
TPU-voetjes en een klapbaar beugelhandvat.
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

## Ontwerp v3

| Onderdeel | Materiaal | Maat | Opmerking |
|---|---|---|---|
| `box.stl` | PLA | 106 × 101 × 52 mm, boss steekt 12 mm uit de voorkant | ronde meterboss Ø50 met D-profiel, tray rust met de flens op een richel op 19,8 mm |
| `lid.stl` | PLA | 110,6 × 105,6 mm, cap over de box | verdiept logo 0,6 mm in het hart, venster van 52 mm in de voorkant van de skirt boven de boss, snaptongen 16 mm aan de zijkanten, gasketgroef, handvat-oren met pennen |
| `lid_logo_inlay.stl` | PLA, 2e kleur | 78 × 8 × 0,6 mm | losse letters, 0,1 mm speling, vallen vlak in het verdiepte logo |
| `handle.stl` | PLA | beugel, armen 40 mm | klikt over de pennen (Ø6, lip Ø7,2), ligt plat op het deksel of staat rechtop |
| `gasket.stl` | TPU | ring 2,2 × 2,0 mm | zit 1,2 mm in de groef, 0,8 mm wordt ingedrukt op de boxrand |
| `foot.stl` (4×) | TPU | Ø12 × 3,5 mm | in Ø12,4 uitsparingen, 1,9 mm zichtbaar |
| `test_tray_fit.stl` | PLA | onderste 24 mm van de box | pasprint voor de tray, eerst printen |
| `test_meter_fit.stl` | PLA | alleen de boss met stuk voorwand | pasprint voor de XF001, eerst printen |

**Meter:** Bambu Lab XF001, rond, Ø45 × 14 mm, inbouwgat Ø43. Zit in een ronde boss Ø50 op de voorkant, zoals de
referentiefoto's. Blind gat Ø43,4 × 14 mm vanaf de voorkant met verzinking Ø45,9 voor de rand; de rand steekt 0,3 mm
uit. Vijf ventilatiegaten Ø2,5 door de achterwand van het gat naar de binnenruimte, zodat hij de lucht bij de potjes
meet. Vast door wrijving van de snaptabs in het gat; zit hij los, druppel lijm.

**Boss-vorm:** rond aan de bovenkant, recht naar de vloer (D-profiel). Daardoor geen enkele overhang naar beneden en
dus geen support op een zichtvlak. De box is hierdoor 52 mm hoog (meter Ø50 + rand), en het deksel heeft een venster
in de skirt boven de boss.

**Logo:** verdiept 0,6 mm in het hart van de dekselbovenkant. Staat nu als tekst `DREAMBROS`
(DejaVu Sans Bold, 78 mm breed). Zet het echte logo als `reference/logo.svg` neer (gesloten paden, geen strokes)
en het script gebruikt die automatisch, geschaald op `LOGO_W`. De inlay wordt dan ook uit de SVG gemaakt.

**Aanname die je moet nameten:** hoogte van het Dreambros-potje met deksel = 32 mm (`JAR_H` in `heti_box.py`).
Bij een ander getal: aanpassen, script draaien, klaar. De boxhoogte volgt automatisch.

## Genereren en verifiëren

```
pip install manifold3d trimesh numpy matplotlib
python3 heti_box.py          # schrijft output/*.stl en draait de passingscontrole
python3 render_preview.py    # PNG-previews in output/
```

De passingscontrole berekent booleaanse overlap tussen de originele tray-STL, een metermodel, deksel, gasket,
handvat (3 standen) en voetjes met de box. Alles moet 0 mm³ zijn en de snapnok moet juist wél de boxwand grijpen.
Exit-code 1 als iets niet past.

## Printvolgorde en oppervlak

1. `01_pasprints_PLA.3mf`: `test_tray_fit` en `test_meter_fit` (samen < 1 uur). Tray moet op de richel rusten, XF001 moet met lichte wrijving in de boss vallen, rand 0,3 mm uitstekend.
2. Past het niet: `CLR` (tray) of `MET_HOLE_D` (meter) aanpassen in `heti_box.py`, opnieuw draaien.
3. `02_box_PLA.3mf`: box rechtop, deksel al omgekeerd (bovenkant op het bed), handvat plat, logo-inlay plat. Geen support nodig, behalve optioneel onder de twee horizontale Ø6-pennen; zonder support zakken die 0,2 mm door, dat werkt nog.
4. `03_gasket_voetjes_TPU.3mf`: TPU 95A, gasket 100% infill, 4 voetjes.

Voor een glad, krasvrij resultaat:
- **Dekselbovenkant ligt op het bed.** Textured PEI geeft een matte, uniforme bovenkant; smooth PEI geeft glans. Dat is het zichtvlak, dus kies het bed dat je mooi vindt.
- **Logo-inlay:** eerst het deksel printen, daarna de inlay in de tweede kleur los printen en in de verdieping drukken (0,1 mm speling, druppel lijm). Met AMS/MMU kun je de inlay ook als object op dezelfde plaat in kleur 2 slicen.
- **Box:** naad op "achterkant" of "uitgelijnd" zetten, 3 wanden, buitenwand eerst, 0,16 mm lagen voor de buitenkant. Elephant-foot compensatie 0,1 mm zodat de voetjes-uitsparingen en de onderkant strak blijven.
- **Geen support op zichtvlakken.** Het ontwerp heeft geen overhangen op de buitenkant. Alleen de pennen zijn horizontaal.
- **Kleurbanden** zoals de referentie: filamentwissel op laaghoogte in de slicer, geen extra geometrie nodig.

## Nog niet in v3

- Echt Dreambros-logo: alleen de SVG ontbreekt nog, de haak zit erin.
- Vriesblok-insert: alleen zinvol als er rosin in de potjes zit. De onderste holte is 91,6 × 86,4 × 16,8 mm; daar past
  een PETG-waterblok onder de tray als de tray 12 mm hoger komt te zitten.
- Sluiting is een detent (snapnok 0,6 mm), geen slot. Test de kracht met de eerste print; zwakker: `SNAP_BUMP` 0,4.
