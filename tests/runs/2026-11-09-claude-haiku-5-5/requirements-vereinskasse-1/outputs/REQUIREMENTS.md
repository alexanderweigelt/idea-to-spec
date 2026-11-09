# Requirements
Dieses Dokument beschreibt, was die Vereins-App für Auslagenbelege tut. Gestaltung (DESIGN.md), Sicherheit (SECURITY.md) und rechtliche Fragen (LEGAL.md) gehören nicht hierher.

## Overview
- Problem: [OQ-OVERVIEW-01](#oq-overview-01)
- Ziel: [OQ-OVERVIEW-02](#oq-overview-02)
- Nutzer: [OQ-OVERVIEW-03](#oq-overview-03)
- Dokumentsprache und Oberflächensprache: [OQ-OVERVIEW-04](#oq-overview-04)

## ROLES
- [FR-ROLE-01](docs/requirements/FR-ROLE-01.md) – Mitglied sieht nur eigene Einreichungen
- [FR-ROLE-02](docs/requirements/FR-ROLE-02.md) – Kassenwart sieht alle Einreichungen und setzt den Status

## STATUS
- [FR-STATUS-01](docs/requirements/FR-STATUS-01.md) – Drei Stufen einer Einreichung
- [FR-STATUS-02](docs/requirements/FR-STATUS-02.md) – Mitglied sieht den aktuellen Status

## RECOGNITION
- [FR-RECOGNITION-01](docs/requirements/FR-RECOGNITION-01.md) – Vorschlag für Betrag und Datum aus dem Foto
- [FR-RECOGNITION-02](docs/requirements/FR-RECOGNITION-02.md) – Bestätigung oder Korrektur vor dem Absenden

## PLATFORM
- [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) – Installation als PWA auf dem Startbildschirm

## OFFLINE
- [FR-OFFLINE-01](docs/requirements/FR-OFFLINE-01.md) – Zwischenspeichern und automatisches Senden ohne Doppelanlage

## QUALITY
- [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) – Erkennungsvorschlag innerhalb von 5 Sekunden
- [FR-QUALITY-02](docs/requirements/FR-QUALITY-02.md) – Absenden in höchstens 60 Sekunden
- [FR-QUALITY-03](docs/requirements/FR-QUALITY-03.md) – Lauffähig in aktuellen Android Chrome und iOS Safari

## EXCLUSION
- [OQ-EXCLUSION-01](#oq-exclusion-01) – Keine Zahlung und keine Bankanbindung in der App
- [OQ-EXCLUSION-02](#oq-exclusion-02) – Kein Store-Auftritt (App Store, Google Play)

## Catalog
| ID | Group | Title | Status |
|---|---|---|---|
| [FR-ROLE-01](docs/requirements/FR-ROLE-01.md) | ROLES | Mitglied sieht nur eigene Einreichungen | confirmed |
| [FR-ROLE-02](docs/requirements/FR-ROLE-02.md) | ROLES | Kassenwart sieht alle und setzt den Status | confirmed |
| [FR-STATUS-01](docs/requirements/FR-STATUS-01.md) | STATUS | Drei Stufen einer Einreichung | confirmed |
| [FR-STATUS-02](docs/requirements/FR-STATUS-02.md) | STATUS | Mitglied sieht den aktuellen Status | confirmed |
| [FR-RECOGNITION-01](docs/requirements/FR-RECOGNITION-01.md) | RECOGNITION | Vorschlag für Betrag und Datum | confirmed |
| [FR-RECOGNITION-02](docs/requirements/FR-RECOGNITION-02.md) | RECOGNITION | Bestätigung oder Korrektur vor dem Absenden | confirmed |
| [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) | PLATFORM | Installation als PWA | confirmed |
| [FR-OFFLINE-01](docs/requirements/FR-OFFLINE-01.md) | OFFLINE | Zwischenspeichern ohne Doppelanlage | confirmed |
| [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) | QUALITY | Erkennungsvorschlag in 5 Sekunden | confirmed |
| [FR-QUALITY-02](docs/requirements/FR-QUALITY-02.md) | QUALITY | Absenden in 60 Sekunden | confirmed |
| [FR-QUALITY-03](docs/requirements/FR-QUALITY-03.md) | QUALITY | Lauffähig in aktuellen Browsern | confirmed |

## Open questions
- [x] <a id="oq-overview-01"></a>**OQ-OVERVIEW-01** – Welches Problem wird gelöst?
  - Antwort: Auslagenbelege werden heute auf Papier eingereicht. Der Kassenwart sammelt und prüft sie von Hand.
  - Begründung: Annahme A1, bestätigt.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user (Annahme, bestätigt)
- [x] <a id="oq-overview-02"></a>**OQ-OVERVIEW-02** – Was ist das Ziel?
  - Antwort: Mitglieder reichen Belege digital ein und sehen den Status. Der Kassenwart hat alle Einreichungen an einer Stelle.
  - Begründung: Annahme A2, bestätigt.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user (Annahme, bestätigt)
- [x] <a id="oq-overview-03"></a>**OQ-OVERVIEW-03** – Wer nutzt die App?
  - Antwort: Vereinsmitglieder, die Auslagen einreichen, und der Kassenwart, der prüft und den Status setzt. Keine externen Nutzer.
  - Begründung: Annahme A3, bestätigt.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user (Annahme, bestätigt)
- [x] <a id="oq-overview-04"></a>**OQ-OVERVIEW-04** – In welcher Sprache?
  - Antwort: Dokumente und Oberfläche nur auf Deutsch.
  - Begründung: Annahme A4, bestätigt. Die Sprache der Vorlage ist Deutsch.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user (Annahme, bestätigt)
- [x] <a id="oq-exclusion-01"></a>**OQ-EXCLUSION-01** – Wie wird ausgezahlt?
  - Antwort: Die Auszahlung erfolgt außerhalb der App. Die App dokumentiert nur den Status, es gibt keine Bankanbindung und keine Zahlungsdatei.
  - Begründung: Geringster Aufwand, keine Zahlungsrisiken.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user
- [x] <a id="oq-exclusion-02"></a>**OQ-EXCLUSION-02** – Gibt es einen Store-Auftritt?
  - Antwort: Nein. Die App läuft nur als PWA. App Store und Google Play entfallen.
  - Begründung: Keine Gebühren, passt zum Budget. Widerspruch zur ursprünglichen Idee wurde bewusst entschieden.
  - Datum: [bei Speicherung eintragen]
  - Quelle: user
- [ ] <a id="oq-role-01"></a>**OQ-ROLE-01** – Wie wird verhindert, dass ein Mitglied fremde Einreichungen über eine direkte Adresse aufruft?
  - Empfehlung: Zugriffsschutz serverseitig prüfen, nicht nur in der Oberfläche ausblenden.
  - Antwortet: SECURITY-Prompt
- [ ] <a id="oq-role-02"></a>**OQ-ROLE-02** – Wer vergibt Konten und die Kassenwart-Rolle, und wie wird sie an einen Nachfolger übergeben?
  - Empfehlung: Der Vorstand legt fest, wer die Rolle hat. Nur er kann sie ändern.
  - Antwortet: SECURITY-Prompt
- [ ] <a id="oq-status-01"></a>**OQ-STATUS-01** – Darf der Kassenwart einen falsch gesetzten Status korrigieren?
  - Empfehlung: Ja, mit Hinweis auf die vorherige Stufe. Das Mitglied sieht die Änderung.
  - Antwortet: DESIGN-Prompt
- [ ] <a id="oq-recognition-01"></a>**OQ-RECOGNITION-01** – Wie genau und wie schnell erkennt Google Cloud Vision Betrag und Datum auf echten Belegen?
  - Empfehlung: Mit etwa 20 echten Belegen von Mitgliedern testen, bevor die Oberfläche gebaut wird.
  - probe: yes
  - Antwortet: ARCHITECTURE-Prompt (erstes Arbeitspaket)
- [ ] <a id="oq-offline-01"></a>**OQ-OFFLINE-01** – Was passiert bei vollem lokalen Speicher oder sehr großen Fotos?
  - Empfehlung: Foto vor dem Speichern verkleinern. Bei vollem Speicher einen klaren Hinweis zeigen, statt still zu scheitern.
  - Antwortet: ARCHITECTURE-Prompt
- [ ] <a id="oq-platform-01"></a>**OQ-PLATFORM-01** – Welche Mindestversionen der Browser werden unterstützt?
  - Empfehlung: Die jeweils aktuelle und die vorherige Hauptversion.
  - Antwortet: ARCHITECTURE-Prompt
- [ ] <a id="oq-data-01"></a>**OQ-DATA-01** – Wie werden Datenschutz und Aufbewahrung der Belege geregelt (Auftragsverarbeitung mit Google, Übermittlung außerhalb der EU, Löschfristen)?
  - Empfehlung: Vor jeder weiteren Entscheidung rechtlich klären, weil Belege personenbezogene Daten enthalten.
  - Antwortet: LEGAL-Prompt
