# Requirements

Dieses Dokument ist zuständig für die Anforderungen an die Prompt-Library „Idea to Spec“ (lib/) und ist ihr einziger Maßstab; es legt nicht den Wortlaut der Prompts selbst fest.

## Overview

| Thema | ID |
|---|---|
| Problem und Ziel | [OQ-SCOPE-01](#oq-scope-01) |
| Nutzer | [OQ-SCOPE-02](#oq-scope-02) |
| Dokumentsprache | [OQ-SCOPE-03](#oq-scope-03) |
| Abgrenzung | [OQ-SCOPE-04](#oq-scope-04), [OQ-SCOPE-05](#oq-scope-05), [OQ-SCOPE-06](#oq-scope-06) |
| Fertig, wenn | [OQ-SCOPE-07](#oq-scope-07) |

## SCOPE – Zweck und Abgrenzung

| ID | Titel |
|---|---|
| [OQ-SCOPE-01](#oq-scope-01) | Was ist der Zweck (Problem und Ziel)? |
| [OQ-SCOPE-02](#oq-scope-02) | Für wen ist die Library? |
| [OQ-SCOPE-03](#oq-scope-03) | In welcher Sprache sind die Spezifikationsdokumente dieses Projekts? |
| [OQ-SCOPE-04](#oq-scope-04) | Gehören Umsetzung und Code dazu? |
| [OQ-SCOPE-05](#oq-scope-05) | Gehören Projekte außerhalb des Webs dazu? |
| [OQ-SCOPE-06](#oq-scope-06) | Garantiert die Library die Machbarkeit? |
| [OQ-SCOPE-07](#oq-scope-07) | Wann ist das Projekt fertig? |
| [OQ-SCOPE-08](#oq-scope-08) | Unterscheidet die Library Projekttypen? |
| [OQ-SCOPE-09](#oq-scope-09) | Wie wird das Ziel beschrieben? |
| [OQ-SCOPE-10](#oq-scope-10) | Was ist eine Solution Vision? |
| [OQ-SCOPE-11](#oq-scope-11) | Was gilt als Webprojekt? |
| [OQ-SCOPE-12](#oq-scope-12) | Was wurde aus der alten Fassung bewusst weggelassen? |

## FLOW – Ablauf und Aufbau

| ID | Titel |
|---|---|
| [FR-FLOW-01](docs/requirements/FR-FLOW-01.md) | Empfohlene Abfolge, Anforderungen zuerst |
| [FR-FLOW-02](docs/requirements/FR-FLOW-02.md) | Einheitliche Vorlage je Prompt |
| [FR-FLOW-03](docs/requirements/FR-FLOW-03.md) | Dokumentbezüge je Prompt |
| [FR-FLOW-04](docs/requirements/FR-FLOW-04.md) | Ein Kopierblock, vorbelegt, anpassbare Stellen markiert |
| [FR-FLOW-05](docs/requirements/FR-FLOW-05.md) | Höchstens 8 Prompts im Kernablauf |
| [OQ-FLOW-01](#oq-flow-01) | Wie sind anpassbare Stellen markiert? |
| [OQ-FLOW-02](#oq-flow-02) | Welcher Standard gilt für das Design-Dokument? |
| [OQ-FLOW-03](#oq-flow-03) | Welche Prompts bilden den Kernablauf? |
| [OQ-FLOW-04](#oq-flow-04) | Wie ist ein Prompt aufgebaut? |
| [OQ-FLOW-05](#oq-flow-05) | Wie werden Ergebnisdokumente benannt und gegliedert? |
| [OQ-FLOW-06](#oq-flow-06) | Welche Sprache gilt wo? |
| [OQ-FLOW-07](#oq-flow-07) | Was enthält der Leitfaden? |
| [OQ-FLOW-08](#oq-flow-08) | Mit welchen Standards sind die Prompts vorbelegt? |

## DIALOG – Gesprächsführung und Prüftiefe

| ID | Titel |
|---|---|
| [FR-DIALOG-01](docs/requirements/FR-DIALOG-01.md) | Gesprächsführung ohne Erfinden, Start mit einem Satz |
| [FR-DIALOG-02](docs/requirements/FR-DIALOG-02.md) | Nur Wichtiges fragen, Rest als Annahme |
| [FR-DIALOG-03](docs/requirements/FR-DIALOG-03.md) | Form der Fragen |
| [FR-DIALOG-04](docs/requirements/FR-DIALOG-04.md) | Delegation „entscheide selbst“ |
| [FR-DIALOG-05](docs/requirements/FR-DIALOG-05.md) | Fachprüfung vor dem Festschreiben |
| [FR-DIALOG-06](docs/requirements/FR-DIALOG-06.md) | Alarme sofort, Machbarkeitsprobe zuerst |
| [FR-DIALOG-07](docs/requirements/FR-DIALOG-07.md) | Themenliste je Fragerunde |
| [FR-DIALOG-08](docs/requirements/FR-DIALOG-08.md) | Kompakter Stand ohne Dateizugriff |
| [FR-DIALOG-09](docs/requirements/FR-DIALOG-09.md) | Fachbegriffe erklären |
| [OQ-DIALOG-01](#oq-dialog-01) | Was war die Hauptursache der Schwächen der alten Fassung? |
| [OQ-DIALOG-02](#oq-dialog-02) | Darf der Mensch Entscheidungen delegieren? |
| [OQ-DIALOG-03](#oq-dialog-03) | Prüft jeder Prompt Sicherheitsfolgen? |
| [OQ-DIALOG-04](#oq-dialog-04) | Wie behält man den Überblick über alles Offene und macht in einem neuen Chat weiter, ohne eigene Datei? |
| [OQ-DIALOG-05](#oq-dialog-05) | Womit beginnt der Anforderungs-Prompt? |
| [OQ-DIALOG-06](#oq-dialog-06) | Wann werden Antworten gespeichert? |
| [OQ-DIALOG-07](#oq-dialog-07) | Wer erfasst Rollen und Rechte? |

## REQ – Anforderungen

| ID | Titel |
|---|---|
| [FR-REQ-01](docs/requirements/FR-REQ-01.md) | ID und Ja/Nein-Prüfbarkeit |
| [FR-REQ-02](docs/requirements/FR-REQ-02.md) | Erlaubte ID-Arten, sprechend und stabil |
| [OQ-REQ-01](#oq-req-01) | Welches ID-Format gilt, und wo stehen AC? |
| [OQ-REQ-02](#oq-req-02) | Wer vergibt rechtliche Anforderungen? |
| [OQ-REQ-03](#oq-req-03) | Welche Themengruppen hat dieses Projekt? |
| [OQ-REQ-04](#oq-req-04) | Wie wurde die Solution Vision übernommen, und was ist der Maßstab? |
| [OQ-REQ-05](#oq-req-05) | Wo liegt die Anforderungsvorlage? |
| [OQ-REQ-06](#oq-req-06) | Wie werden Abnahmekriterien geschrieben? |
| [OQ-REQ-07](#oq-req-07) | Wofür gibt es ADRs, und wie werden andere Entscheidungen und Annahmen festgehalten? |

## SPEC – Spezifikation und Prüfung

| ID | Titel |
|---|---|
| [FR-SPEC-01](docs/requirements/FR-SPEC-01.md) | Prüf-Prompt listet Widersprüche und Lücken |
| [FR-SPEC-02](docs/requirements/FR-SPEC-02.md) | Wann die Spezifikation fertig ist |
| [FR-SPEC-03](docs/requirements/FR-SPEC-03.md) | Änderungen einarbeiten ohne Neuaufbau |
| [FR-SPEC-04](docs/requirements/FR-SPEC-04.md) | Einheitliches Dokumentgerüst |
| [FR-SPEC-05](docs/requirements/FR-SPEC-05.md) | Jede Aussage hat eine ID |
| [FR-SPEC-06](docs/requirements/FR-SPEC-06.md) | Eine Datei je Anforderung, höchstens ca. 40 Zeilen |
| [OQ-SPEC-01](#oq-spec-01) | Wie werden fehlende Kriterien eingearbeitet? |
| [OQ-SPEC-02](#oq-spec-02) | Wo stehen Prüfbefunde und die Freigabe? |
| [OQ-SPEC-03](#oq-spec-03) | Wo stehen Architekturentscheidungen, und was passiert mit ersetzten? |
| [OQ-SPEC-04](#oq-spec-04) | Was passiert mit einer gestrichenen Anforderung? |
| [OQ-SPEC-05](#oq-spec-05) | Wie sieht ein Verweis aus? |
| [OQ-SPEC-06](#oq-spec-06) | Wie werden offene Fragen dargestellt? |
| [OQ-SPEC-07](#oq-spec-07) | Wie werden IDs für Menschen verständlich? |
| [OQ-SPEC-08](#oq-spec-08) | Welches Vorbild gilt für den Aufbau der Spezifikation? |
| [OQ-SPEC-09](#oq-spec-09) | Wie zeigt das README den Stand der Spezifikation? |
| [OQ-SPEC-10](#oq-spec-10) | Wie laufen Änderungen? |
| [OQ-SPEC-11](#oq-spec-11) | Welche Regeln gelten für die Prüfung? |

## WP – Arbeitspakete

| ID | Titel |
|---|---|
| [FR-WP-01](docs/requirements/FR-WP-01.md) | Verweise und Abdeckung |
| [FR-WP-02](docs/requirements/FR-WP-02.md) | Abnahmekriterien und Aufwand |
| [FR-WP-03](docs/requirements/FR-WP-03.md) | Teilungsregeln |
| [OQ-WP-01](#oq-wp-01) | Muss jedes Arbeitspaket auf die Gates verweisen? |
| [OQ-WP-02](#oq-wp-02) | Wie werden Arbeitspakete abgelegt? |
| [OQ-WP-03](#oq-wp-03) | Was enthält ein Arbeitspaket? |
| [OQ-WP-04](#oq-wp-04) | Was enthält die AGENTS.md eines Zielprojekts? |

## USE – Nutzung

| ID | Titel |
|---|---|
| [FR-USE-01](docs/requirements/FR-USE-01.md) | Übersprungener Schritt wird erkannt |
| [FR-USE-02](docs/requirements/FR-USE-02.md) | Funktioniert in jedem KI-Chat |
| [OQ-USE-01](#oq-use-01) | Vertragen sich FR-SPEC-06 (eigene Datei je Anforderung) und FR-USE-02 (jeder KI-Chat)? |
| [OQ-USE-02](#oq-use-02) | Wie wird weitergearbeitet? |

## Catalog

| ID | Group | Title | Status |
|---|---|---|---|
| [FR-FLOW-01](docs/requirements/FR-FLOW-01.md) | FLOW | Empfohlene Abfolge, Anforderungen zuerst | confirmed |
| [FR-FLOW-02](docs/requirements/FR-FLOW-02.md) | FLOW | Einheitliche Vorlage je Prompt | confirmed |
| [FR-FLOW-03](docs/requirements/FR-FLOW-03.md) | FLOW | Dokumentbezüge je Prompt | confirmed |
| [FR-FLOW-04](docs/requirements/FR-FLOW-04.md) | FLOW | Ein Kopierblock, vorbelegt, anpassbare Stellen markiert | confirmed |
| [FR-FLOW-05](docs/requirements/FR-FLOW-05.md) | FLOW | Höchstens 8 Prompts im Kernablauf | confirmed |
| [FR-DIALOG-01](docs/requirements/FR-DIALOG-01.md) | DIALOG | Gesprächsführung ohne Erfinden, Start mit einem Satz | confirmed |
| [FR-DIALOG-02](docs/requirements/FR-DIALOG-02.md) | DIALOG | Nur Wichtiges fragen, Rest als Annahme | confirmed |
| [FR-DIALOG-03](docs/requirements/FR-DIALOG-03.md) | DIALOG | Form der Fragen | confirmed |
| [FR-DIALOG-04](docs/requirements/FR-DIALOG-04.md) | DIALOG | Delegation „entscheide selbst“ | confirmed |
| [FR-DIALOG-05](docs/requirements/FR-DIALOG-05.md) | DIALOG | Fachprüfung vor dem Festschreiben | confirmed |
| [FR-DIALOG-06](docs/requirements/FR-DIALOG-06.md) | DIALOG | Alarme sofort, Machbarkeitsprobe zuerst | confirmed |
| [FR-DIALOG-07](docs/requirements/FR-DIALOG-07.md) | DIALOG | Themenliste je Fragerunde | confirmed |
| [FR-DIALOG-08](docs/requirements/FR-DIALOG-08.md) | DIALOG | Kompakter Stand ohne Dateizugriff | confirmed |
| [FR-DIALOG-09](docs/requirements/FR-DIALOG-09.md) | DIALOG | Fachbegriffe erklären | confirmed |
| [FR-REQ-01](docs/requirements/FR-REQ-01.md) | REQ | ID und Ja/Nein-Prüfbarkeit | confirmed |
| [FR-REQ-02](docs/requirements/FR-REQ-02.md) | REQ | Erlaubte ID-Arten, sprechend und stabil | confirmed |
| [FR-SPEC-01](docs/requirements/FR-SPEC-01.md) | SPEC | Prüf-Prompt listet Widersprüche und Lücken | confirmed |
| [FR-SPEC-02](docs/requirements/FR-SPEC-02.md) | SPEC | Wann die Spezifikation fertig ist | confirmed |
| [FR-SPEC-03](docs/requirements/FR-SPEC-03.md) | SPEC | Änderungen einarbeiten ohne Neuaufbau | confirmed |
| [FR-SPEC-04](docs/requirements/FR-SPEC-04.md) | SPEC | Einheitliches Dokumentgerüst | confirmed |
| [FR-SPEC-05](docs/requirements/FR-SPEC-05.md) | SPEC | Jede Aussage hat eine ID | confirmed |
| [FR-SPEC-06](docs/requirements/FR-SPEC-06.md) | SPEC | Eine Datei je Anforderung, höchstens ca. 40 Zeilen | confirmed |
| [FR-WP-01](docs/requirements/FR-WP-01.md) | WP | Verweise und Abdeckung | confirmed |
| [FR-WP-02](docs/requirements/FR-WP-02.md) | WP | Abnahmekriterien und Aufwand | confirmed |
| [FR-WP-03](docs/requirements/FR-WP-03.md) | WP | Teilungsregeln | confirmed |
| [FR-USE-01](docs/requirements/FR-USE-01.md) | USE | Übersprungener Schritt wird erkannt | confirmed |
| [FR-USE-02](docs/requirements/FR-USE-02.md) | USE | Funktioniert in jedem KI-Chat | confirmed |

## Open questions

### SCOPE

- [x] <a id="oq-scope-01"></a>**OQ-SCOPE-01** – Was ist der Zweck (Problem und Ziel)?
  - answer: Eine Reihe kopierbarer, rollenbasierter Prompts, die ein Webprojekt Schritt für Schritt von einer unvollständigen Idee zu einer abgestimmten, widerspruchsfreien Spezifikation führt. Daraus entstehen prüfbare Arbeitspakete als Grundlage für Spec-Driven Development.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-02"></a>**OQ-SCOPE-02** – Für wen ist die Library?
  - answer: Entwickler und Produktverantwortliche, die ein Webprojekt mit einem KI-Chat planen.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-03"></a>**OQ-SCOPE-03** – In welcher Sprache sind die Spezifikationsdokumente dieses Projekts?
  - answer: Deutsch; Überschriften, Feldnamen und Gherkin-Schlüsselwörter wie in docs/REQUIREMENT_TEMPLATE.md (englisch).
  - reason: Library-Standard „Sprache des Nutzers“; die Vorlage bleibt wörtlich
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-04"></a>**OQ-SCOPE-04** – Gehören Umsetzung und Code dazu?
  - answer: Nein. Regeln und Prüfbefehle für die Umsetzung (AGENTS.md) sind erlaubt.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-05"></a>**OQ-SCOPE-05** – Gehören Projekte außerhalb des Webs dazu?
  - answer: Nein.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-06"></a>**OQ-SCOPE-06** – Garantiert die Library die Machbarkeit?
  - answer: Nein. Die Spezifikation macht Risiken sichtbar und schickt sie früh in eine Machbarkeitsprobe.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-07"></a>**OQ-SCOPE-07** – Wann ist das Projekt fertig?
  - answer: Wenn jemand mit nur einer groben Idee die Prompts in der empfohlenen Reihenfolge nutzt und am Ende eine Spezifikation ohne Widersprüche plus Arbeitspakete hat, die ein Entwickler oder KI-Agent ohne Rückfragen umsetzen und prüfen kann.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-08"></a>**OQ-SCOPE-08** – Unterscheidet die Library Projekttypen?
  - answer: Nein; Web ist nur der Rahmen.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-09"></a>**OQ-SCOPE-09** – Wie wird das Ziel beschrieben?
  - answer: Ja/Nein-Prüfkriterien ersetzen „Muss enthalten“.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-scope-10"></a>**OQ-SCOPE-10** – Was ist eine Solution Vision?
  - answer: Gemeinsames Zielbild einer konkreten Softwarelösung einschließlich ihrer wesentlichen Fähigkeiten. Die Solution Vision dieses Projekts ist in REQUIREMENTS.md aufgegangen und wird nicht getrennt geführt.
  - reason: anerkannter Fachbegriff
  - date: 2026-11-08 · source: user
- [x] <a id="oq-scope-11"></a>**OQ-SCOPE-11** – Was gilt als Webprojekt?
  - answer: Software, die über einen Browser oder Webprotokolle wie HTTP bereitgestellt oder genutzt wird – ein Satz, keine Typenliste, kein Nachweis.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-scope-12"></a>**OQ-SCOPE-12** – Was wurde aus der alten Fassung bewusst weggelassen?
  - answer: Projekttypenliste, Baseline als eigener Schritt (geht in die Prüfung auf), eigener Abschnitt „kurzer Weg“, Bereitschaftsliste, Versionsregel, feste Rollensatz-Formulierung, Regel „spezifiziert/umgesetzt/geprüft“.
  - reason: –
  - date: 2026-11-08 · source: user

### FLOW

- [x] <a id="oq-flow-01"></a>**OQ-FLOW-01** – Wie sind anpassbare Stellen markiert?
  - answer: Anpassbar sind INPUT und DEFAULTS; kein eigenes Markierungszeichen.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-flow-02"></a>**OQ-FLOW-02** – Welcher Standard gilt für das Design-Dokument?
  - answer: design.md-Format (google-labs-code), „version: alpha“ (im Original geprüft; 0.3.0 war die CLI-Version); weggelassene Abschnitte im Feld „omitted“.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-flow-03"></a>**OQ-FLOW-03** – Welche Prompts bilden den Kernablauf?
  - answer: 7 Prompts: Anforderungen → Design (inkl. Barrierefreiheit) → Architektur → Sicherheit → Prüfung → Arbeitspakete → AGENTS.md. Recht ist ein optionaler Zusatz außerhalb des Kerns, empfohlen vor Design und Architektur. 1 Platz Reserve.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-flow-04"></a>**OQ-FLOW-04** – Wie ist ein Prompt aufgebaut?
  - answer: Eine Markdown-Datei je Prompt in lib/ (englisch, kleingeschrieben, Bindestrich, ohne Nummern). Oben ein kurzer deutscher Kopf (Rolle, braucht zwingend, nutzt falls vorhanden, erzeugt, fertig wenn), darunter genau ein englischer Kopierblock: Rollensatz (Auftrag und Grenze), Eingabeblock mit benannten, freiwilligen Feldern, vorbelegtes Defaults-Feld. Kein gemeinsamer Grundtext für alle Prompts.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-flow-05"></a>**OQ-FLOW-05** – Wie werden Ergebnisdokumente benannt und gegliedert?
  - answer: Übliche Namen (REQUIREMENTS.md, DESIGN.md, ARCHITECTURE.md, SECURITY.md, AGENTS.md, ggf. LEGAL.md); das Gerüst gibt der Prompt als knappe Überschriftenliste oder als Name des Standards vor.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-flow-06"></a>**OQ-FLOW-06** – Welche Sprache gilt wo?
  - answer: Kopf und Leitfaden deutsch; Prompts und AGENTS.md englisch; Gespräch in der Sprache des Nutzers; Sprache der Projektdokumente wird einmal festgelegt (Standard: Sprache des Nutzers); IDs, Dateinamen und Code englisch.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-flow-07"></a>**OQ-FLOW-07** – Was enthält der Leitfaden?
  - answer: lib/README.md, deutsch, eine Übersichtsseite: kurze Erklärung von Spec-Driven Development (Spezifikation so konkret, dass ihre Erfüllung prüfbar ist; Grundlage für Planung, Umsetzung, Test, Review und Abnahme), Reihenfolge, je Prompt eine Zeile, Umgang mit offenen Fragen, ein Satz zu kleinen Vorhaben (Rollen weglassen), ein Satz zu großen Projekten, ein Satz zu Änderungen, „Empfohlen: ein neuer Chat je Prompt; ein gemeinsamer Chat funktioniert ebenfalls.“, Übergang zur Umsetzung über AGENTS.md. Details nur im Prompt-Kopf.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-flow-08"></a>**OQ-FLOW-08** – Mit welchen Standards sind die Prompts vorbelegt?
  - answer: Anforderungen: EARS, Abnahmekriterien Gherkin. Arbeitspakete: Abnahmekriterien Gherkin. Design: siehe [OQ-FLOW-02](#oq-flow-02). Architektur: arc42 schlank, MADR 4.0.0, Mermaid nur bei Bedarf. Sicherheit: OWASP ASVS 5.0 Stufe 2, STRIDE. Barrierefreiheit: WCAG 2.2 AA, nur mit Benutzeroberfläche. Recht: DSGVO bei EU-Personenbezug, Lizenzprüfung, keine Rechtsberatung. Abweichung wird in der Fachdatei begründet; ein nicht zutreffender Standard entfällt mit Begründung. Qualitätsziele sind normale Anforderungen; Gates stehen in AGENTS.md.
  - reason: –
  - date: 2026-11-08 · source: user

### DIALOG

- [x] <a id="oq-dialog-01"></a>**OQ-DIALOG-01** – Was war die Hauptursache der Schwächen der alten Fassung?
  - answer: Die Prompts waren Fragebogen mit Formvorschriften statt Analyse. Lösung allgemein über [FR-DIALOG-05](docs/requirements/FR-DIALOG-05.md), nicht auf ein Testprojekt zugeschnitten.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-dialog-02"></a>**OQ-DIALOG-02** – Darf der Mensch Entscheidungen delegieren?
  - answer: Ja; Machbarkeits- und Umfangsalarme werden nie delegiert.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-dialog-03"></a>**OQ-DIALOG-03** – Prüft jeder Prompt Sicherheitsfolgen?
  - answer: Nein. Allein zuständig ist der Sicherheits-Prompt; er prüft alle vorhandenen Beiträge.
  - reason: eine zuständige Stelle
  - date: 2026-11-07 · source: user
- [ ] <a id="oq-dialog-04"></a>**OQ-DIALOG-04** – Wie behält man den Überblick über alles Offene und macht in einem neuen Chat weiter, ohne eigene Datei?
  - context: Idee: die Themenliste des Interviews als Datei speichern (Status je Thema, aktive Frage, Verweise ins Fachdokument, per Skript geprüft) – nicht die Prüfbefundliste. Die Library hält die Themenliste nur im Chat.
  - recommendation: – (noch nicht besprochen)
- [x] <a id="oq-dialog-05"></a>**OQ-DIALOG-05** – Womit beginnt der Anforderungs-Prompt?
  - answer: Kernfragen: Problem, Ziel, Nutzer, Kernfunktionen, typische Abläufe, Rollen und Rechte (wer darf welche Daten sehen oder ändern), Rahmenbedingungen, Ausschlüsse. Optional ein Vorgabendokument (Lastenheft, Pflichtenheft, Unternehmensstandards). Reihenfolge: Vorgabe > Standard > Frage. Große Projekte: Vorgabendokument und Teilbereiche nacheinander.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-dialog-06"></a>**OQ-DIALOG-06** – Wann werden Antworten gespeichert?
  - answer: Sofort in alle betroffenen Dateien.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-dialog-07"></a>**OQ-DIALOG-07** – Wer erfasst Rollen und Rechte?
  - answer: Der Anforderungs-Prompt, als Produktverhalten.
  - reason: –
  - date: 2026-11-08 · source: user

### REQ

- [x] <a id="oq-req-01"></a>**OQ-REQ-01** – Welches ID-Format gilt, und wo stehen AC?
  - answer: KIND-GROUP-NN; AC ebenso, in der Datei ihrer Anforderung.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-req-02"></a>**OQ-REQ-02** – Wer vergibt rechtliche Anforderungen?
  - answer: Der Rechts-Prompt vergibt FR-LEGAL-NN (eigener Katalog in LEGAL.md).
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-req-03"></a>**OQ-REQ-03** – Welche Themengruppen hat dieses Projekt?
  - answer: FLOW, DIALOG, REQ, SPEC, WP, USE (wie die Abschnitte der Solution Vision) und SCOPE für Zweck, Abgrenzung und Fertig-Bedingung.
  - reason: nichts erfunden
  - date: 2026-11-07 · source: user
- [x] <a id="oq-req-04"></a>**OQ-REQ-04** – Wie wurde die Solution Vision übernommen, und was ist der Maßstab?
  - answer: Je Prüfkriterium ein FR, geteilt nur, wo ein EARS-Satz oder ca. 40 Zeilen nicht reichen. Abgrenzung, Fertig-Bedingung und alle Entscheidungen sind geschlossene OQ. REQUIREMENTS.md ist der einzige Maßstab.
  - reason: Das Projekt hält sich an die eigene Library (ein Maßstab, IDs, Katalog, Datei je Anforderung)
  - date: 2026-11-07 · source: user
- [x] <a id="oq-req-05"></a>**OQ-REQ-05** – Wo liegt die Anforderungsvorlage?
  - answer: docs/REQUIREMENT_TEMPLATE.md.
  - reason: Hauptverzeichnis bleibt aufgeräumt; alles zur Spezifikation liegt in docs/
  - date: 2026-11-08 · source: user
- [x] <a id="oq-req-06"></a>**OQ-REQ-06** – Wie werden Abnahmekriterien geschrieben?
  - answer: Gherkin in einem Codeblock „gherkin“, jeder Schritt (Given/When/Then) auf einer eigenen Zeile.
  - reason: für Menschen lesbar, Gherkin-Standard
  - date: 2026-11-08 · source: user
- [x] <a id="oq-req-07"></a>**OQ-REQ-07** – Wofür gibt es ADRs, und wie werden andere Entscheidungen und Annahmen festgehalten?
  - answer: ADR nur für Architektur (arc42 Kap. 9, MADR). Andere Entscheidungen sind geschlossene OQ mit Antwort, Begründung, Datum und Quelle; Annahmen sind OQ mit Empfehlung. Die ID-Art T entfällt.
  - reason: –
  - date: 2026-11-08 · source: user

### SPEC

- [x] <a id="oq-spec-01"></a>**OQ-SPEC-01** – Wie werden fehlende Kriterien eingearbeitet?
  - answer: Sammeln und in einem Durchgang einarbeiten.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-spec-02"></a>**OQ-SPEC-02** – Wo stehen Prüfbefunde und die Freigabe?
  - answer: Prüfbefunde sind OQ „from: review“ im zuständigen Fachdokument (Ergebnis resolved oder accepted); die Freigabe ist eine Zeile unter der Tabelle im README-Abschnitt „Specification“. Keine REVIEW.md.
  - reason: eine eigene Prüfdatei war nicht verlangt
  - date: 2026-11-07 · source: user
- [x] <a id="oq-spec-03"></a>**OQ-SPEC-03** – Wo stehen Architekturentscheidungen, und was passiert mit ersetzten?
  - answer: ADRs in docs/decisions/; eine ersetzte ADR bleibt („superseded by“).
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-spec-04"></a>**OQ-SPEC-04** – Was passiert mit einer gestrichenen Anforderung?
  - answer: Die Katalogzeile bleibt, Titel „withdrawn – see OQ-…“.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-spec-05"></a>**OQ-SPEC-05** – Wie sieht ein Verweis aus?
  - answer: Ein Markdown-Link, dessen sichtbarer Text nur die ID ist; Ziel ist die Datei der Anforderung, der ADR oder des Arbeitspakets, der Anker der OQ (HTML-Anker im OQ-Eintrag) oder die Überschrift des AC in der Datei seiner Anforderung.
  - reason: erfüllt [FR-SPEC-04](docs/requirements/FR-SPEC-04.md) und macht Verweise anklickbar
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-06"></a>**OQ-SPEC-06** – Wie werden offene Fragen dargestellt?
  - answer: Als Checkbox-Liste, ein Block je OQ mit Feldern untereinander: [ ] offen (recommendation, ggf. probe), [ ] mit „assumption:“ vor der Frage für Annahmen, [x] geschlossen (answer, reason, date, source). Die Checkbox ersetzt das Feld status. Alle OQ stehen nach Themengruppe und Nummer geordnet; die leere Checkbox kennzeichnet offene Punkte.
  - reason: für Menschen leichter lesbar; Box und Feld zugleich könnten sich widersprechen
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-07"></a>**OQ-SPEC-07** – Wie werden IDs für Menschen verständlich?
  - answer: Der Wegweiser im README.md enthält den Abschnitt „IDs lesen“ (Überschrift in der Dokumentsprache) mit den 7 ID-Arten und jeder im Projekt genutzten Themengruppe; der Anforderungs-Prompt legt ihn auch in Zielprojekten an. Dateinamen bleiben die reine ID.
  - reason: Dateinamen aus der ID ändern sich nie, Links bleiben stabil
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-08"></a>**OQ-SPEC-08** – Welches Vorbild gilt für den Aufbau der Spezifikation?
  - answer: withdrawn – covered by [FR-REQ-02](docs/requirements/FR-REQ-02.md), [FR-SPEC-04](docs/requirements/FR-SPEC-04.md), [FR-SPEC-06](docs/requirements/FR-SPEC-06.md), [OQ-SPEC-09](#oq-spec-09)
  - reason: keine Verweise auf externe, temporäre Quellen; der Inhalt steht bereits in den genannten IDs
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-09"></a>**OQ-SPEC-09** – Wie zeigt das README den Stand der Spezifikation?
  - answer: Der Anforderungs-Prompt legt im README.md des Zielprojekts den Abschnitt „Specification“ an (Tabelle Document | Responsibility | Status) und überschreibt nichts Vorhandenes; jeder spätere Prompt ergänzt seine Zeile. Kein eigener Prompt dafür.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-10"></a>**OQ-SPEC-10** – Wie laufen Änderungen?
  - answer: Über den zuständigen Prompt: nur Betroffenes ändern, IDs bleiben, danach den Prüf-Prompt erneut ausführen. Betrifft eine Änderung einen fremden Beitrag, entsteht dort eine OQ. Kein eigener Änderungs-Prompt.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-spec-11"></a>**OQ-SPEC-11** – Welche Regeln gelten für die Prüfung?
  - answer: Je Vorgabe genau eine zuständige Stelle; eine fremde Entscheidung wird nie überschrieben, sondern wird OQ. Messwerte (z. B. Antwortzeiten) sind ein akzeptierter Punkt mit Startwert plus ein Arbeitspaket „messen, dann festlegen“. Freigabe durch einen Menschen.
  - reason: –
  - date: 2026-11-08 · source: user

### WP

- [x] <a id="oq-wp-01"></a>**OQ-WP-01** – Muss jedes Arbeitspaket auf die Gates verweisen?
  - answer: Nein; Gates gelten für alle Pakete, kein Verweis je Paket.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-wp-02"></a>**OQ-WP-02** – Wie werden Arbeitspakete abgelegt?
  - answer: Je Paket eine Datei docs/work-packages/WP-…md plus WORK_PACKAGES.md (Reihenfolge, Abdeckungstabelle, Katalog) als Ergebnisdatei; Teilungswerte 5/1 im INPUT.
  - reason: –
  - date: 2026-11-07 · source: user
- [x] <a id="oq-wp-03"></a>**OQ-WP-03** – Was enthält ein Arbeitspaket?
  - answer: Anforderungs-IDs, Vorgänger, Aufwand klein/mittel/groß mit Begründung, Teilungsfragen, Abnahme als Gherkin; keine heimlichen neuen Entscheidungen. Die Abdeckungstabelle hat keine leeren Zeilen. Eine Machbarkeitsprobe kommt zuerst, wo [FR-DIALOG-06](docs/requirements/FR-DIALOG-06.md) sie verlangt.
  - reason: –
  - date: 2026-11-08 · source: user
- [x] <a id="oq-wp-04"></a>**OQ-WP-04** – Was enthält die AGENTS.md eines Zielprojekts?
  - answer: Agentenneutral; je Aufgabenart ein Verweis auf die zu lesende Datei; kurze imperative Sicherheitsregeln je Stack, jede mit Quelle (z. B. OWASP Cheat Sheet Series, Framework-Doku), ohne Quelle keine Regel; Gates als konkrete Prüfbefehle; die Regel „Ein Arbeitspaket ist erst fertig, wenn seine Abnahmekriterien erfüllt sind und alle Gates bestehen.“
  - reason: –
  - date: 2026-11-08 · source: user

### USE

- [x] <a id="oq-use-01"></a>**OQ-USE-01** – Vertragen sich [FR-SPEC-06](docs/requirements/FR-SPEC-06.md) (eigene Datei je Anforderung) und [FR-USE-02](docs/requirements/FR-USE-02.md) (jeder KI-Chat)?
  - answer: Ja. Ohne Dateizugriff entstehen viele kleine Textblöcke (mehr Kopierarbeit und Token); das ist bewusst akzeptiert.
  - reason: Teil der Solution Vision
  - date: 2026-11-07 · source: user
- [x] <a id="oq-use-02"></a>**OQ-USE-02** – Wie wird weitergearbeitet?
  - answer: Der Stand wird aus den Dateien erkannt, Einstieg ist der README-Abschnitt „Specification“. Ohne Dateizugriff gibt die KI den kompletten Markdown-Text aus und sagt, dass nichts gespeichert wurde.
  - reason: –
  - date: 2026-11-08 · source: user
