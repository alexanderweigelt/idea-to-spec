# Requirements

Dieses Dokument legt fest, was die Beleg-App des Sportvereins prüfbar leisten muss. Es regelt nicht Gestaltung, Technikwahl, Sicherheit oder Rechtsfragen; diese verantworten DESIGN.md, die Architektur, SECURITY.md und LEGAL.md.

## Overview

- Problem: [OQ-OVERVIEW-02](#oq-overview-02)
- Ziel: [OQ-OVERVIEW-03](#oq-overview-03)
- Nutzer: [OQ-OVERVIEW-04](#oq-overview-04)
- Dokumentsprache: [OQ-OVERVIEW-01](#oq-overview-01)
- Vorgaben: Anforderungen in EARS, Abnahmekriterien in Gherkin; keine Abweichung.

## PLATFORM – Plattform und Verteilung

- [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) – Nutzung als installierbare Web-App

## OCR – Automatisches Auslesen

- [FR-OCR-01](docs/requirements/FR-OCR-01.md) – Vorschlag von Betrag und Datum
- [FR-OCR-02](docs/requirements/FR-OCR-02.md) – Manuelle Eingabe ohne Vorschlag
- [FR-OCR-03](docs/requirements/FR-OCR-03.md) – Bestätigung vor dem Absenden

## ACCESS – Nutzer, Rollen und Zugang

- [FR-ACCESS-01](docs/requirements/FR-ACCESS-01.md) – Einladung per E-Mail
- [FR-ACCESS-02](docs/requirements/FR-ACCESS-02.md) – Mitglied sieht nur eigene Belege
- [FR-ACCESS-03](docs/requirements/FR-ACCESS-03.md) – Kassenwart sieht alle Belege
- [FR-ACCESS-04](docs/requirements/FR-ACCESS-04.md) – Keine Änderung fremder Angaben durch den Kassenwart

## FLOW – Kernablauf

- [FR-FLOW-01](docs/requirements/FR-FLOW-01.md) – Beleg als erstattet markieren
- [FR-FLOW-02](docs/requirements/FR-FLOW-02.md) – Rückfrage mit Begründung
- [FR-FLOW-03](docs/requirements/FR-FLOW-03.md) – Ablehnung mit Begründung
- [FR-FLOW-04](docs/requirements/FR-FLOW-04.md) – Korrektur nach Rückfrage
- [FR-FLOW-05](docs/requirements/FR-FLOW-05.md) – Endstatus sind unveränderlich
- [FR-FLOW-06](docs/requirements/FR-FLOW-06.md) – Status und Begründung für das Mitglied sichtbar
- [FR-FLOW-07](docs/requirements/FR-FLOW-07.md) – Beleg zurückziehen
- [FR-FLOW-08](docs/requirements/FR-FLOW-08.md) – Statusprotokoll
- [FR-FLOW-09](docs/requirements/FR-FLOW-09.md) – Pflichtangaben einer Einreichung
- [FR-FLOW-10](docs/requirements/FR-FLOW-10.md) – IBAN im Profil
- [FR-FLOW-11](docs/requirements/FR-FLOW-11.md) – E-Mail an den Kassenwart
- [FR-FLOW-12](docs/requirements/FR-FLOW-12.md) – E-Mail an das Mitglied
- [FR-FLOW-13](docs/requirements/FR-FLOW-13.md) – Liste offener Belege
- [FR-FLOW-14](docs/requirements/FR-FLOW-14.md) – CSV-Export erstatteter Belege

## QUALITY – Qualitätsziele

- [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) – Einreichen in höchstens 2 Minuten
- [FR-QUALITY-02](docs/requirements/FR-QUALITY-02.md) – Mengengerüst
- [FR-QUALITY-03](docs/requirements/FR-QUALITY-03.md) – Entwurf ohne Verbindung
- [FR-QUALITY-04](docs/requirements/FR-QUALITY-04.md) – Entwurf später absenden
- [FR-QUALITY-05](docs/requirements/FR-QUALITY-05.md) – Fotos höchstens 2 MB

## RETENTION – Aufbewahrung

- [FR-RETENTION-01](docs/requirements/FR-RETENTION-01.md) – Automatische Löschung abgeschlossener Belege
- [FR-RETENTION-02](docs/requirements/FR-RETENTION-02.md) – Beginn des Geschäftsjahres einstellbar

## SCOPE – Abgrenzung

- [OQ-SCOPE-01](#oq-scope-01) – Was die App nicht leistet

## Catalog

| ID | Group | Title | Status |
|---|---|---|---|
| [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) | PLATFORM | Nutzung als installierbare Web-App | confirmed |
| [FR-OCR-01](docs/requirements/FR-OCR-01.md) | OCR | Vorschlag von Betrag und Datum | confirmed |
| [FR-OCR-02](docs/requirements/FR-OCR-02.md) | OCR | Manuelle Eingabe ohne Vorschlag | confirmed |
| [FR-OCR-03](docs/requirements/FR-OCR-03.md) | OCR | Bestätigung vor dem Absenden | confirmed |
| [FR-ACCESS-01](docs/requirements/FR-ACCESS-01.md) | ACCESS | Einladung per E-Mail | confirmed |
| [FR-ACCESS-02](docs/requirements/FR-ACCESS-02.md) | ACCESS | Mitglied sieht nur eigene Belege | confirmed |
| [FR-ACCESS-03](docs/requirements/FR-ACCESS-03.md) | ACCESS | Kassenwart sieht alle Belege | confirmed |
| [FR-ACCESS-04](docs/requirements/FR-ACCESS-04.md) | ACCESS | Keine Änderung fremder Angaben durch den Kassenwart | confirmed |
| [FR-FLOW-01](docs/requirements/FR-FLOW-01.md) | FLOW | Beleg als erstattet markieren | confirmed |
| [FR-FLOW-02](docs/requirements/FR-FLOW-02.md) | FLOW | Rückfrage mit Begründung | confirmed |
| [FR-FLOW-03](docs/requirements/FR-FLOW-03.md) | FLOW | Ablehnung mit Begründung | confirmed |
| [FR-FLOW-04](docs/requirements/FR-FLOW-04.md) | FLOW | Korrektur nach Rückfrage | confirmed |
| [FR-FLOW-05](docs/requirements/FR-FLOW-05.md) | FLOW | Endstatus sind unveränderlich | confirmed |
| [FR-FLOW-06](docs/requirements/FR-FLOW-06.md) | FLOW | Status und Begründung für das Mitglied sichtbar | confirmed |
| [FR-FLOW-07](docs/requirements/FR-FLOW-07.md) | FLOW | Beleg zurückziehen | confirmed |
| [FR-FLOW-08](docs/requirements/FR-FLOW-08.md) | FLOW | Statusprotokoll | confirmed |
| [FR-FLOW-09](docs/requirements/FR-FLOW-09.md) | FLOW | Pflichtangaben einer Einreichung | confirmed |
| [FR-FLOW-10](docs/requirements/FR-FLOW-10.md) | FLOW | IBAN im Profil | confirmed |
| [FR-FLOW-11](docs/requirements/FR-FLOW-11.md) | FLOW | E-Mail an den Kassenwart | confirmed |
| [FR-FLOW-12](docs/requirements/FR-FLOW-12.md) | FLOW | E-Mail an das Mitglied | confirmed |
| [FR-FLOW-13](docs/requirements/FR-FLOW-13.md) | FLOW | Liste offener Belege | confirmed |
| [FR-FLOW-14](docs/requirements/FR-FLOW-14.md) | FLOW | CSV-Export erstatteter Belege | confirmed |
| [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) | QUALITY | Einreichen in höchstens 2 Minuten | confirmed |
| [FR-QUALITY-02](docs/requirements/FR-QUALITY-02.md) | QUALITY | Mengengerüst | confirmed |
| [FR-QUALITY-03](docs/requirements/FR-QUALITY-03.md) | QUALITY | Entwurf ohne Verbindung | confirmed |
| [FR-QUALITY-04](docs/requirements/FR-QUALITY-04.md) | QUALITY | Entwurf später absenden | confirmed |
| [FR-QUALITY-05](docs/requirements/FR-QUALITY-05.md) | QUALITY | Fotos höchstens 2 MB | confirmed |
| [FR-RETENTION-01](docs/requirements/FR-RETENTION-01.md) | RETENTION | Automatische Löschung abgeschlossener Belege | confirmed |
| [FR-RETENTION-02](docs/requirements/FR-RETENTION-02.md) | RETENTION | Beginn des Geschäftsjahres einstellbar | confirmed |

## Open questions

### OVERVIEW

- [x] <a id="oq-overview-01"></a>**OQ-OVERVIEW-01** – In welcher Sprache wird die Spezifikation geführt?
  - Antwort: Deutsch
  - Begründung: Alle Angaben des Auftraggebers sind deutsch.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-overview-02"></a>**OQ-OVERVIEW-02** – Welches Problem löst die App?
  - Antwort: Belege kommen verspätet oder gar nicht beim Kassenwart an, und offene Erstattungen sind schwer zu überblicken.
  - Begründung: Hauptschmerz des Kassenwarts
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-overview-03"></a>**OQ-OVERVIEW-03** – Woran wird der Erfolg gemessen?
  - Antwort: Ein Mitglied braucht vom Foto bis zur Einreichung höchstens 2 Minuten, und der Kassenwart sieht alle offenen Belege in einer Liste.
  - Begründung: direkt prüfbar, verplant keine Arbeitszeit des Kassenwarts
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-overview-04"></a>**OQ-OVERVIEW-04** – Wer nutzt die App?
  - Antwort: bis zu 50 einreichende Vereinsmitglieder und der Kassenwart (ggf. mit Vertretung)
  - Begründung: Mengengerüst des Vereins
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer

### PLATFORM

- [x] <a id="oq-platform-01"></a>**OQ-PLATFORM-01** – Wie kommt die App zu den Mitgliedern?
  - Antwort: nur als PWA über den Browser, installierbar auf dem Startbildschirm; App Store und Google Play eventuell später
  - Begründung: keine Store-Gebühren, keine Store-Prüfung, kein Ablehnungsrisiko nach Apple-Regel 4.2; der Entwickler kennt nur Webtechnik
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-platform-02"></a>**OQ-PLATFORM-02** – Welches Budget steht für den Betrieb zur Verfügung?
  - Antwort: höchstens wenige Euro pro Monat; Entwicklung ehrenamtlich
  - Begründung: Vereinsbudget
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-platform-03"></a>**OQ-PLATFORM-03** – Annahme: Unterstützt werden die jeweils letzten zwei Hauptversionen von Safari (iOS) und Chrome (Android).
  - Antwort: bestätigt
  - Begründung: deckt die Geräte der Mitglieder ab, ohne Altlasten zu testen
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer

### OCR

- [x] <a id="oq-ocr-01"></a>**OQ-OCR-01** – Welche Rolle spielt die automatische Erkennung mit Google Cloud Vision?
  - Antwort: Sie schlägt Betrag und Datum vor; das Mitglied prüft und korrigiert vor dem Einreichen.
  - Begründung: Vision liefert nur Rohtext, Belege enthalten mehrere Beträge, Fehler müssen abgefangen werden.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [ ] <a id="oq-ocr-02"></a>**OQ-OCR-02** – Wie gut erkennt die Lösung Betrag und Datum auf 20–30 echten Vereinsbelegen?
  - Empfehlung: Die Probe ist bestanden, wenn mindestens 80 % der Beträge und mindestens 80 % der Daten korrekt vorgeschlagen werden. Sonst entfällt die automatische Erkennung, und es gilt die manuelle Eingabe ([FR-OCR-02](docs/requirements/FR-OCR-02.md)).
  - probe: yes
  - Beantwortet von: Planungs-Prompt (erstes Arbeitspaket)
- [ ] <a id="oq-ocr-03"></a>**OQ-OCR-03** – Ist die Übermittlung der Belegfotos an Google zulässig, und was ist dafür nötig (Auftragsverarbeitungsvertrag, Information der Mitglieder)?
  - Empfehlung: vor der Probe mit echten Belegen klären
  - Beantwortet von: Legal-Prompt
- [x] <a id="oq-ocr-04"></a>**OQ-OCR-04** – Annahme: Ohne Verbindung gibt es keinen automatischen Vorschlag; das Mitglied trägt Betrag und Datum selbst ein.
  - Antwort: bestätigt
  - Begründung: Die Erkennung läuft über das Netz.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-ocr-05"></a>**OQ-OCR-05** – Annahme: Der Vorschlag erscheint spätestens 10 Sekunden nach der Aufnahme; danach erscheinen leere Felder.
  - Antwort: bestätigt
  - Begründung: hält das 2-Minuten-Ziel ein
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer

### ACCESS

- [x] <a id="oq-access-01"></a>**OQ-ACCESS-01** – Wie erhalten Mitglieder Zugang?
  - Antwort: Der Kassenwart lädt per E-Mail ein; es gibt die Rollen „Mitglied“ (eigene Belege) und „Kassenwart“ (alle Belege).
  - Begründung: kein Fremdzugang, einfach zu verwalten
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-access-02"></a>**OQ-ACCESS-02** – Annahme: Mitglieder ohne E-Mail-Adresse reichen wie bisher auf Papier ein.
  - Antwort: bestätigt
  - Begründung: Die Einladung setzt eine E-Mail-Adresse voraus.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-access-03"></a>**OQ-ACCESS-03** – Annahme: Es kann mehrere Kassenwart-Konten geben, z. B. für eine Vertretung.
  - Antwort: bestätigt
  - Begründung: Urlaub und Ausfall des Kassenwarts
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-access-04"></a>**OQ-ACCESS-04** – Annahme: Ein Einladungslink ist 7 Tage gültig und lässt sich erneut senden.
  - Antwort: bestätigt
  - Begründung: Ein alter Link ist kein dauerhafter Zugang.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer

### FLOW

- [x] <a id="oq-flow-01"></a>**OQ-FLOW-01** – Wie wird ausgezahlt?
  - Antwort: Der Kassenwart überweist außerhalb der App; die App markiert den Beleg nur als „Erstattet“.
  - Begründung: keine Bankanbindung nötig
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-02"></a>**OQ-FLOW-02** – Welche Status durchläuft ein Beleg?
  - Antwort: Eingereicht → Rückfrage, Abgelehnt oder Erstattet; Begründung Pflicht bei Rückfrage und Ablehnung; nach einer Rückfrage korrigiert das Mitglied, und der Beleg ist wieder „Eingereicht“.
  - Begründung: klärt unleserliche oder falsche Belege ohne Papierweg
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-03"></a>**OQ-FLOW-03** – Wie erfahren Beteiligte von Änderungen?
  - Antwort: per E-Mail; der Kassenwart bei neuer oder korrigierter Einreichung, das Mitglied bei jeder Statusänderung
  - Begründung: funktioniert auf jedem Gerät, auch ohne installierte App
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-04"></a>**OQ-FLOW-04** – Welche Angaben gehören zu einer Einreichung?
  - Antwort: Foto, Betrag, Datum, Verwendungszweck; die IBAN hinterlegt das Mitglied einmal im Profil.
  - Begründung: alles für die Überweisung beisammen
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-05"></a>**OQ-FLOW-05** – Darf ein Mitglied einen eingereichten Beleg ändern oder zurückziehen?
  - Antwort: Zurückziehen ja, solange der Kassenwart nicht entschieden hat; ändern nein.
  - Begründung: Der Beleg ändert sich nie während der Prüfung.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-06"></a>**OQ-FLOW-06** – Annahme: Der Kassenwart ändert Angaben eines Mitglieds nicht selbst, sondern stellt eine Rückfrage.
  - Antwort: bestätigt
  - Begründung: Nachvollziehbar bleibt, wer welchen Betrag angegeben hat.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-07"></a>**OQ-FLOW-07** – Annahme: Bei der Korrektur nach einer Rückfrage darf das Mitglied Foto, Betrag, Datum und Verwendungszweck ändern und eine Antwort schreiben.
  - Antwort: bestätigt
  - Begründung: Jede Rückfrage lässt sich in der App beantworten.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-08"></a>**OQ-FLOW-08** – Annahme: Jede Statusänderung wird mit Datum, Uhrzeit und Person protokolliert und ist für Mitglied und Kassenwart sichtbar.
  - Antwort: bestätigt
  - Begründung: Nachvollziehbarkeit für Mitglied, Kassenwart und Kassenprüfung
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-09"></a>**OQ-FLOW-09** – Annahme: Belegfotos können auch aus der Fotogalerie hochgeladen werden.
  - Antwort: bestätigt
  - Begründung: Belege werden oft schon vorher fotografiert.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-10"></a>**OQ-FLOW-10** – Annahme: Ein Beleg hat 1 bis 3 Fotos.
  - Antwort: bestätigt
  - Begründung: lange Kassenbons
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-11"></a>**OQ-FLOW-11** – Annahme: Die IBAN wird beim Speichern anhand der Prüfziffer geprüft; ungültige IBANs werden abgewiesen.
  - Antwort: bestätigt
  - Begründung: vermeidet Fehlüberweisungen durch Tippfehler
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-12"></a>**OQ-FLOW-12** – Annahme: Mit jedem Beleg wird die IBAN gespeichert, die bei der Einreichung gilt; spätere Profiländerungen gelten nur für neue Belege.
  - Antwort: bestätigt
  - Begründung: Der Kassenwart überweist auf die beim Einreichen angegebene Verbindung.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-13"></a>**OQ-FLOW-13** – Annahme: Der Verwendungszweck ist Pflicht und hat 3–200 Zeichen.
  - Antwort: bestätigt
  - Begründung: Der Kassenwart muss die Auslage zuordnen können.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-14"></a>**OQ-FLOW-14** – Annahme: Der Kassenwart erhält auch eine E-Mail, wenn ein Beleg zurückgezogen wird.
  - Antwort: bestätigt
  - Begründung: Er prüft keinen erledigten Beleg mehr.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-15"></a>**OQ-FLOW-15** – Annahme: Scheitert der E-Mail-Versand, wird die Statusänderung trotzdem gespeichert.
  - Antwort: bestätigt
  - Begründung: Der Status ist in der App immer sichtbar.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-16"></a>**OQ-FLOW-16** – Annahme: Die CSV-Datei enthält Belegdatum, Betrag, Verwendungszweck, Mitgliedsname, IBAN und Erstattungsdatum, formatiert für deutsches Excel (Semikolon, Dezimalkomma, Umlaute korrekt).
  - Antwort: bestätigt
  - Begründung: direkt in Excel lesbar
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-17"></a>**OQ-FLOW-17** – Annahme: Der Zeitraum des Exports bezieht sich auf das Erstattungsdatum.
  - Antwort: bestätigt
  - Begründung: passt zum Kassenbuch
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-flow-18"></a>**OQ-FLOW-18** – Braucht der Kassenwart eine Übergabe ins Kassenbuch?
  - Antwort: ja, als CSV-Export der erstatteten Belege eines frei wählbaren Zeitraums
  - Begründung: wenig Aufwand, kein Abtippen
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer

### QUALITY

- [x] <a id="oq-quality-01"></a>**OQ-QUALITY-01** – Mit welchen Mengen ist zu rechnen?
  - Antwort: bis 50 einreichende Mitglieder und bis 100 Belege pro Monat (erwartet: ca. 30)
  - Begründung: deutlich innerhalb kostenloser Kontingente
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-quality-02"></a>**OQ-QUALITY-02** – Was passiert ohne Verbindung beim Einreichen?
  - Antwort: Foto und Angaben werden als Entwurf auf dem Gerät gespeichert; das Mitglied sendet ihn später mit einem Fingertipp ab.
  - Begründung: Schlechter Empfang in Halle und auf dem Platz; automatisches Nachsenden geht auf dem iPhone nicht.
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-quality-03"></a>**OQ-QUALITY-03** – Annahme: Fotos werden vor dem Hochladen auf höchstens 2 MB verkleinert und bleiben lesbar.
  - Antwort: bestätigt
  - Begründung: schnelles Hochladen bei schwacher Verbindung, geringer Speicherbedarf
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-quality-04"></a>**OQ-QUALITY-04** – Annahme: Das 2-Minuten-Ziel gilt als erfüllt, wenn mindestens 4 von 5 Testpersonen aus dem Verein es bei normaler Mobilverbindung schaffen.
  - Antwort: bestätigt
  - Begründung: macht das Ziel prüfbar
  - Datum: JJJJ-MM-TT
  - Quelle: Nutzer
- [x] <a id="oq-quality-05"></a>**OQ-QUALITY-05** – Annahme: Beim Speichern eines Entwurfs auf einem iPhone ohne installierte App erscheint ein Hinweis, dass der Entwurf nach 7
