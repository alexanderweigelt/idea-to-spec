# Requirements
Dieses Dokument legt fest, was die Beleg-App für Mitglieder und Kassenwart tun muss. Es legt nicht fest, wie Oberfläche, Technik, Sicherheit oder rechtliche Pflichten umgesetzt werden.

## Overview
- Problem: Mitglieder verauslagen Geld für den Verein und müssen es erstattet bekommen. Die Belege sollen digital beim Kassenwart ankommen. → [OQ-GOAL-01](#oq-goal-01)
- Ziel: Beleg mit dem Handy fotografieren, Betrag und Datum bestätigen lassen, Kassenwart prüft und erstattet. → [OQ-GOAL-01](#oq-goal-01)
- Nutzer: Mitglieder und ein Kassenwart, ein Verein mit einer Kasse. → [OQ-GOAL-03](#oq-goal-03)
- Dokumentsprache: Deutsch. → [OQ-GOAL-02](#oq-goal-02)
- Nicht im Umfang: Buchhaltung, Überweisung, Bankanbindung. → [OQ-SCOPE-01](#oq-scope-01)
- Rahmen: kleines Budget, ehrenamtlich, Web-App. Store-Veröffentlichung später. → [OQ-PLATFORM-02](#oq-platform-02)

## CAPTURE – Beleg erfassen
- [FR-CAPTURE-01](docs/requirements/FR-CAPTURE-01.md) – Vorschlag für Betrag und Datum aus dem Foto, Bestätigung durch das Mitglied
- [FR-CAPTURE-02](docs/requirements/FR-CAPTURE-02.md) – manuelle Eingabe, wenn die Erkennung nichts liefert

## PHOTO – Fotogröße
- [FR-PHOTO-01](docs/requirements/FR-PHOTO-01.md) – Verkleinerung vor dem Hochladen

## CONNECT – Verbindung
- [FR-CONNECT-01](docs/requirements/FR-CONNECT-01.md) – lokale Speicherung und späteres Hochladen

## QUALITY – Qualitätsziele
- [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) – Vorschlag innerhalb von 10 Sekunden

## REVIEW – Prüfung und Erstattung
- [FR-REVIEW-01](docs/requirements/FR-REVIEW-01.md) – Status für das Mitglied
- [FR-REVIEW-02](docs/requirements/FR-REVIEW-02.md) – keine Änderung nach Einreichung

## ROLES – Rollen und Sichtbarkeit
- [FR-ROLES-01](docs/requirements/FR-ROLES-01.md) – Mitglied sieht eigene Belege, Kassenwart alle

## RETENTION – Aufbewahrung
- [FR-RETENTION-01](docs/requirements/FR-RETENTION-01.md) – Löschung zum Jahresende nach Erstattung

## PLATFORM – Plattform
- [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) – installierbare Web-App
- [FR-PLATFORM-02](docs/requirements/FR-PLATFORM-02.md) – Nutzung der Gerätekamera
- [FR-PLATFORM-03](docs/requirements/FR-PLATFORM-03.md) – deutsche Oberfläche, Beträge in Euro

## Catalog
| ID | Group | Title | Status |
|---|---|---|---|
| [FR-CAPTURE-01](docs/requirements/FR-CAPTURE-01.md) | CAPTURE | Vorschlag für Betrag und Datum | confirmed |
| [FR-CAPTURE-02](docs/requirements/FR-CAPTURE-02.md) | CAPTURE | Manuelle Eingabe bei fehlender Erkennung | confirmed |
| [FR-PHOTO-01](docs/requirements/FR-PHOTO-01.md) | PHOTO | Verkleinerung vor dem Hochladen | confirmed |
| [FR-CONNECT-01](docs/requirements/FR-CONNECT-01.md) | CONNECT | Lokale Speicherung ohne Verbindung | confirmed |
| [FR-QUALITY-01](docs/requirements/FR-QUALITY-01.md) | QUALITY | Erkennung in höchstens 10 Sekunden | confirmed |
| [FR-REVIEW-01](docs/requirements/FR-REVIEW-01.md) | REVIEW | Status der Einreichung | confirmed |
| [FR-REVIEW-02](docs/requirements/FR-REVIEW-02.md) | REVIEW | Keine Änderung nach Einreichung | confirmed |
| [FR-ROLES-01](docs/requirements/FR-ROLES-01.md) | ROLES | Sichtbarkeit der Belege | confirmed |
| [FR-RETENTION-01](docs/requirements/FR-RETENTION-01.md) | RETENTION | Löschung zum Jahresende | confirmed |
| [FR-PLATFORM-01](docs/requirements/FR-PLATFORM-01.md) | PLATFORM | Installierbare Web-App | confirmed |
| [FR-PLATFORM-02](docs/requirements/FR-PLATFORM-02.md) | PLATFORM | Gerätekamera | confirmed |
| [FR-PLATFORM-03](docs/requirements/FR-PLATFORM-03.md) | PLATFORM | Deutsch und Euro | confirmed |

## Open questions
- [x] <a id="oq-assume-01"></a>**OQ-ASSUME-01** – assumption: Mitglieder nutzen ein Smartphone mit Kamera und einen modernen Browser.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-02"></a>**OQ-ASSUME-02** – assumption: Ist Betrag oder Datum nicht erkennbar, gibt das Mitglied beides von Hand ein.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-03"></a>**OQ-ASSUME-03** – assumption: Ein Verein, eine Kasse, ein Kassenwart. Keine weiteren Rollen.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-04"></a>**OQ-ASSUME-04** – assumption: Status der Einreichung ist „eingereicht“ oder „erstattet“.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-05"></a>**OQ-ASSUME-05** – assumption: Die Erstattung selbst läuft außerhalb der App.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-06"></a>**OQ-ASSUME-06** – assumption: Die App ist auf Deutsch, Beträge in Euro.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-07"></a>**OQ-ASSUME-07** – assumption: Die lokale Kopie wird nach erfolgreichem Hochladen gelöscht.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-08"></a>**OQ-ASSUME-08** – assumption: 2 MB und 1600 Pixel sind Startwerte, die im Test geprüft werden.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-assume-09"></a>**OQ-ASSUME-09** – assumption: Ein eingereichter Beleg kann vom Mitglied nicht mehr geändert werden.
  - Antwort: bestätigt. Quelle: user (Sammelbestätigung).
- [x] <a id="oq-capture-01"></a>**OQ-CAPTURE-01** – Umgang mit dem erkannten Betrag und Datum?
  - Antwort: Vorschlag anzeigen, Mitglied bestätigt oder korrigiert. Begründung: Erkennung ist fehleranfällig. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-connect-01"></a>**OQ-CONNECT-01** – Verhalten bei schlechter Verbindung?
  - Antwort: lokal speichern, hochladen sobald Verbindung besteht. Begründung: nichts geht verloren. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-goal-01"></a>**OQ-GOAL-01** – Problem und Ziel?
  - Antwort: wie im Overview beschrieben. Begründung: Zusammenfassung der Entscheidungen. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-goal-02"></a>**OQ-GOAL-02** – Dokumentsprache?
  - Antwort: Deutsch. Begründung: vom Nutzer so geschrieben. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-goal-03"></a>**OQ-GOAL-03** – Nutzer?
  - Antwort: Mitglieder und Kassenwart, ein Verein, eine Kasse. Begründung: Annahme ASSUME-03, bestätigt. Datum: (bei Speicherung eintragen). Quelle: user.
- [ ] <a id="oq-legal-01"></a>**OQ-LEGAL-01** – Ist die Übermittlung der Belegfotos an Google Cloud Vision zulässig, und welche Verträge sind nötig? Antwortet: Legal-Prompt. Empfehlung: zuerst klären, bevor die Architektur entschieden wird.
- [ ] <a id="oq-legal-02"></a>**OQ-LEGAL-02** – Muss der Verein Belege länger aufbewahren als bis zum Jahresende nach der Erstattung? Antwortet: Legal-Prompt. Empfehlung: zusammen mit OQ-LEGAL-01 klären.
- [x] <a id="oq-photo-01"></a>**OQ-PHOTO-01** – Fotogröße vor dem Hochladen?
  - Antwort: höchstens 2 MB, lange Seite mindestens 1600 Pixel. Begründung: Kompromiss, Werte werden getestet. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-platform-01"></a>**OQ-PLATFORM-01** – Plattform?
  - Antwort: Web-App (PWA), kein Store. Begründung: einfachster Weg. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-platform-02"></a>**OQ-PLATFORM-02** – Gilt die Store-Vorgabe?
  - Antwort: vorerst nur Web-App, Store-Entscheidung später separat. Begründung: passt zu OQ-PLATFORM-01. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-quality-01"></a>**OQ-QUALITY-01** – Wartezeit bis zur Erkennung?
  - Antwort: höchstens 10 Sekunden bei guter Verbindung. Begründung: realistischer Abstand zur Cloud-Erkennung. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-retention-01"></a>**OQ-RETENTION-01** – Aufbewahrung nach der Erstattung?
  - Antwort: automatische Löschung zum Jahresende der Erstattung. Begründung: datensparsam, Frist wird von Legal geprüft. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-review-01"></a>**OQ-REVIEW-01** – Prüfung und Erstattung?
  - Antwort: Kassenwart prüft und erstattet, Mitglied sieht Status. Begründung: einfacher Ablauf. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-roles-01"></a>**OQ-ROLES-01** – Sichtbarkeit der Belege?
  - Antwort: Kassenwart sieht alle, Mitglieder nur eigene. Begründung: Schutz der Mitgliederdaten. Datum: (bei Speicherung eintragen). Quelle: user.
- [x] <a id="oq-scope-01"></a>**OQ-SCOPE-01** – Was ist ausdrücklich nicht im Umfang?
  - Antwort: keine Buchhaltung, keine Überweisung, keine Bankanbindung. Begründung: kleiner Umfang, keine Finanzdaten. Datum: (bei Speicherung eintragen). Quelle: user.
