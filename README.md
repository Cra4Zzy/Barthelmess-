# Barthelmess Maschinenhandel

Individuell gestalteter Website-Entwurf für Michael Barthelmeß, Reichenbach 7, 91555 Feuchtwangen.

## Seiten und Funktionen
- Startseite, Maschinenkatalog, Leistungen, Über uns und Kontakt.
- Sechs eigene Maschinendetailseiten sowie vorläufige Impressums- und Datenschutzhinweise.
- Suche, Kategorien, Sortierung und lokale Merkliste.
- Anfrageformular mit Maschinenübernahme, Validierung, Zusammenfassung und Textdownload.
- Sechs mit KI erstellte Bildmotive und lokal eingebundene Schriften.
- Responsive Gestaltung, Animationen, mobile Navigation und Berücksichtigung reduzierter Bewegung.

## Direkt bereitstellen
Die Website liegt im Hauptverzeichnis und benötigt keinen Build und keine npm-Abhängigkeiten. Der komplette Ordner kann auf einem statischen Webhost bereitgestellt werden. Relative Pfade unterstützen auch GitHub Pages unter einem Repository-Unterpfad.

Lokal: `python -m http.server 8000` im Repository starten und `http://localhost:8000/` öffnen. `index.html` ist der Einstieg.

## Bearbeiten
`build.py` enthält die Seitentemplates und die Beispieldaten des Katalogs. `python build.py` erzeugt die HTML-Seiten und `assets/catalog.json`. CSS und Interaktionen liegen in `assets/style.css` und `assets/app.js`. Bilder und Schriftdateien sind vollständig enthalten.

Prüfungen: `node --check assets/app.js`, `node check-functions.cjs` und `python check.py`.

## Stand des Entwurfs
Die Maschinen sind ausdrücklich Beispielangebote; Bilder sind KI-generierte Motive, keine Aufnahmen tatsächlicher Bestandsmaschinen. Der Katalog enthält weiterhin Preise auf Anfrage. Das Kontaktformular sendet keine Nachrichten, sondern bietet eine lokale Textdatei zum Download an. Onlinekauf und Zahlung sind nicht eingerichtet. Vor dem öffentlichen Kundenstart müssen echte Angebote, Preise, Bilder und Kontaktangaben eingesetzt, der Formularversand angebunden und die rechtlichen Texte vervollständigt werden.

Der Entwurf verwendet `noindex,nofollow` und eine sperrende robots.txt. Es sind keine Analytics oder extern geladenen Schriften eingebaut. Eine visuelle Browserprüfung war in der Erstellungsumgebung nicht verfügbar.

Der vorherige Repository-Stand wurde vor der Übernahme im Branch `backup/vor-barthelmess-2026-10-14` gesichert.
