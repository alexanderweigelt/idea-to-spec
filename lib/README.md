# AI Prompt Library – Anwendung

Die Library führt vom Projektkontext zu einer prüfbaren Spezifikation und zum
lokalen Entwicklungsstart. Der Agent übernimmt erreichbare Vorarbeit und
delegierte Entscheidungen. Du beantwortest notwendige Fragen per Auswahl.

## Ausführungsreihenfolge

Dateinummern und Ausführungsreihenfolge stimmen überein. Die Schritte folgen
zeitlich aufeinander und können in einer gemeinsamen oder in getrennten Sessions
mit Zugriff auf dasselbe Zielrepository laufen.

| Schritt | Prompt | Ergebnis |
| --- | --- | --- |
| P01 | [Projektaufnahme und Anforderungen](01-projektaufnahme.md) | REQUIREMENTS.md, erste Anforderungsdatensätze und ein kurzes Entscheidungsjournal. |
| P02 | [Anforderungsvorlage](02-anforderungsvorlage.md) | docs/requirements/TEMPLATE.md und vereinheitlichte Datensätze. |
| P03 | [Designgrundlage](03-designgrundlage.md) | DESIGN.md mit Tokens, Komponentenregeln und prüfbaren Gestaltungskriterien. |
| P04 | [Architektur, Diagramme und Entscheidungen](04-architektur-und-diagramme.md) | ARCHITECTURE.md, notwendige ADRs und konsistente Architekturdiagramme. |
| P05 | [Projektbezogene Sicherheit](05-sicherheit.md) | SECURITY.md mit Projektzielen, Kontrollen, Prüfplan und einem Bedrohungsmodell. |
| P06 | [Konsolidierung und Modellreview](06-konsolidierung-und-threat-modeling.md) | Abgeglichene Fachdateien und kurze, nachvollziehbare Reviewbefunde. |
| P07 | [Entscheidungen und Spezifikationsbaseline](07-entscheidungen-und-baseline.md) | Aktualisierte Fachdateien, manuelle Spezifikationsprüfung und kurzer Baselinebericht; automatische Prüfung folgt in P10. |
| P08 | [Projekt-README](08-readme.md) | README.md mit funktionierender Navigation und nachvollziehbaren Startinformationen. |
| P09 | [Agent-Anweisungen und Prüfvertrag](09-agent-anweisungen.md) | AGENTS.md mit Kommando- und Gate-Vertrag sowie bei Bedarf ein geprüfter Adapter. |
| P10 | [Aufgabenplanung und Projektstart](10-aufgabenplanung-und-projektstart.md) | Arbeitspakete, eingerichtete lokale Prüfungen und CI-Konfiguration; autorisierte Issues bei entsprechender Freigabe. |

## Start und Fortsetzung

1. Öffne das Zielprojekt mit Dateizugriff und der Projektidee oder vorhandenen
   Projektdateien. Der Ablauf setzt keine vorherige Chat-Historie voraus.
2. Kopiere den gesamten Textblock von P01 in den Coding-Agenten. Die technische
   Grundlage ist bereits enthalten; kein zusätzliches Profil ist nötig.
3. Folge den Schritten P02 bis P10. Zu Beginn liest der Agent
   docs/clarifications.md und die Eingabedateien des jeweiligen Schritts. Fehlende
   Voraussetzungen verhindern den abhängigen Schritt; sie werden nicht erfunden.
4. Antworten, Delegation und ausdrücklich erteilte Befugnisse mit ihrem Umfang
   werden im Journal festgehalten. Der Agent fragt einzeln mit Vorschlägen, Folgen
   und Empfehlung; dokumentierte Befugnisse ersetzen keine menschliche Erteilung.
5. Nach jedem Schritt sichert der Agent Ergebnisse, tatsächliche Prüfungen,
   Reviewstand und nächsten Schritt im Journal. Mit vorhandener Git-Befugnis
   endet der Schritt mit einem passenden Commit oder PR-Vorschlag.
6. Gespeicherte Dateien bleiben auch ohne Commit im selben Arbeitsverzeichnis
   erhalten. Ein anderer Checkout benötigt eine ausdrückliche Übergabe noch
   uncommitteter Arbeit. Vorhandene Antworten werden bei Fortsetzung wiederverwendet.

Ein einzelner späterer Prompt ist mit seinen Eingabedateien nutzbar; er benötigt
die Library-Dateien nicht zur Laufzeit. Fehlende Eingaben werden als Lücke
behandelt. Ohne Zugriff auf das Zielrepository ist dieser Ablauf nicht ausführbar.

## Qualität und Änderungen

Gemeinsame Qualitätsziele gelten für alle Webprojekte. Konkrete Sicherheitsziele
folgen den tatsächlichen Risiken; es gibt kein pauschales Sicherheitslevel oder
eine Pflicht zu einer Vollmatrix. Auch statische Websites benötigen sichere
Browserausgabe, Transport- und Lieferkettenprüfung. Zugänglichkeit bleibt ein
verbindliches Ziel mit automatischen und manuellen Nachweisen.

Fachliches Verhalten liegt in FR-Datensätzen, Gestaltung im Design, technische
Entscheidungen und Diagramme in der Architektur, Kontrollen und das einzige
Bedrohungsmodell in der Sicherheit. Bei Codeänderungen wird geprüft, ob
Anforderungen, Tests und Fachdateien angepasst werden müssen. Das Ergebnis steht
in einer Reviewnotiz oder PR-Checkbox; korrekte Dateien müssen nicht künstlich
geändert werden. Struktur- und Referenzfehler bleiben blockierend.

P07 prüft den Spezifikationsstand manuell; dessen Baseline ist ein echter Git-Bezug
mit kurzem Bericht. Die automatische Spezifikationsprüfung bleibt bis P10 offen.
P09 schreibt konkrete Kommandos in AGENTS.md. P10 richtet zuerst die Laufzeit,
dann den Spec-Check und die übrigen Prüfungen ein und berichtet tatsächliche
Ausführung. Neue Blocker werden vor der Produktimplementierung behoben. Ein
Dokument oder lokaler Test allein belegt keine Produktionsreife oder Konformität.

## Arbeitspakete und Veröffentlichung

P10 erstellt zuerst lokale Arbeitspakete und die Werkzeuggrundlage. Externe Issues
werden nur im ausdrücklich freigegebenen Repository und Umfang nach konkreter
Vorschau angelegt. Ein Abgleich gespeicherter und entfernter Paketmarker verhindert
Duplikate auch nach Teilfehlern. PRs enthalten echte, prüfbare Änderungen.

Weitere Funktionen folgen in kleinen Implementierungsaufträgen. Die zehn Prompts
sind kein einzelner Auftrag, ungeprüft das ganze Produkt zu veröffentlichen.

## Prüfprotokoll für den Funktionsdurchlauf

Die Funktionsprüfung führt der Nutzer in ScannerPWA durch. Die Library bleibt
auf andere Webprojekte anwendbar. Der folgende Maßstab wird vor Beginn verwendet;
er enthält noch keine Ergebnisse. Das Durchlaufprotokoll gehört zum Zielprojekt,
beispielsweise als kurzer Abschnitt in docs/clarifications.md.

Je Prüfung festhalten: erfüllt / nicht erfüllt / nicht geprüft, Beleg mit Datei
oder Git-Bezug, ausgeführte Aktion und verbleibende Lücke. Fragen, Texteingaben,
Unterbrechungen und Dauer ebenfalls zählen; keine ungemessenen Erfolgsangaben.

| ID | Library-Prüfung | Bestanden, wenn … |
| --- | --- | --- |
| L01 | Einstieg und Reihenfolge | Alle zehn Schritte sind mit ihren angegebenen Inputs ausführbar; fehlende Inputs werden erkannt, kein späterer Toolschritt wird vorausgesetzt. |
| L02 | Geringer Eingabeaufwand | Jede Entscheidungsfrage bietet zwei bis drei Optionen, Folgen und Empfehlung; jede Freitextfrage besitzt einen belegten Grund und vorhandene Antworten werden nicht erneut abgefragt. |
| L03 | Frische Session und Fortsetzung | Mindestens ein späterer Schritt startet ohne Chat-Historie aus gespeicherten Dateien; aktive Frage, Antwort, Befugnisse und nächster Schritt bleiben bei einer Pause erhalten. |
| L04 | Gleicher gemeinsamer Vertrag | Vor dem Test und nach Änderungen sind alle Abschnitte COMMON CONTRACT bis END COMMON CONTRACT wortgleich; Abweichungen werden vor weiterer Anwendung korrigiert. |
| L05 | Konsistenz der Ergebnisse | Alle unten genannten Schrittergebnisse sind nachweisbar; Fachdateien besitzen eindeutige Zuständigkeit und keine unbehandelten widersprüchlichen Regeln. |
| L06 | Wirksame Prüfgrundlage | P10 führt die vereinbarten Kommandos tatsächlich aus und zeigt an einem absichtlichen Fehler eine zurückweisende Prüfung; manuelle und Produktionsnachweise bleiben bei fehlender Ausführung offen. |
| L07 | Ehrlicher und befugter Abschluss | Jeder Schritt dokumentiert Status und Review; Commit-/PR-Vorschläge und externe Aktionen respektieren dokumentierte Befugnisse, unbelegte Erfüllung wird nicht behauptet. |

Die Vertragsprüfung L04 erfolgt als Checkliste, ohne Helper: P01 als Vergleich
nehmen und den vollständigen Abschnitt in P02 bis P10 wortgleich abgleichen.
Bei Änderungen alle zehn Kopien aktualisieren; ein bloßes Lesen einer Kopie
prüft deren Übereinstimmung nicht.

| Schritt | Ergebnisprüfung 1 | Ergebnisprüfung 2 |
| --- | --- | --- |
| P01 | Bekannte Nutzeraufgaben und Grenzen sind in REQUIREMENTS.md und kanonischen FRs nachvollziehbar erfasst. | Offene Fragen besitzen Fundstellen; Journal, Delegation und erteilte Befugnisse sind gespeichert, kein unbegründeter Stack gewählt. |
| P02 | TEMPLATE.md und FRs nutzen dasselbe Format mit beobachtbaren Kriterien und gültigen Referenzen. | Bedeutungen und IDs bleiben erhalten; Platzhalter zählen nicht als Produktanforderungen. |
| P03 | DESIGN.md beschreibt tatsächlich benötigte Tokens, Komponenten und Zustände ohne zusätzliche Funktionen. | Bedienungs- und Zugänglichkeitsziele besitzen geplante automatische und manuelle Nachweise. |
| P04 | Architekturtext und Diagramme stimmen bei Komponenten, Flüssen und Grenzen überein. | Wesentliche Entscheidungen haben nachvollziehbaren Status, Alternativen und konkrete Stackregeln. |
| P05 | Projektbezogene Sicherheitsziele haben begründete Quellenzuordnung, Durchsetzung und Nachweise. | Ein Bedrohungsmodell verknüpft tatsächliche Risiken und Kontrollen; keine zweite Diagramm- oder Modellkopie entsteht. |
| P06 | Widersprüche und Befunde sind mit Fundstelle, Behandlung und Status abgeglichen. | Zielketten und das vorhandene Bedrohungsmodell wurden tatsächlich reviewt; Selbstreview und unabhängige Prüfung sind unterscheidbar. |
| P07 | Antworten sind in maßgebliche Dateien übernommen; Produktblocker und manuelle Prüfergebnisse stehen im Baselinebericht. | Git-Bezug oder ausstehender Bezug ist korrekt dokumentiert; automatische Checks sind ausdrücklich für P10 vorgemerkt. |
| P08 | README beschreibt tatsächlichen Zweck und Stand mit gültigen Verweisen. | Verfügbare und geplante Kommandos sind korrekt unterschieden, ohne zweite Spezifikation. |
| P09 | AGENTS.md nennt konkrete Kommandos, Sperrbedingungen und verantwortete manuelle Gates. | Ladeverhalten und noch ausstehende Einrichtung sind ehrlich benannt; FR-/Testauswirkungen sind als Reviewpunkt geregelt. |
| P10 | Pakete decken den bestätigten Scope ab; Laufzeit und Spec-Check sind vor dessen Ausführung vorhanden, Ergebnisse und Fehlerprobe dokumentiert. | Weitere Gates und Befugnisse sind geprüft; autorisierte externe Issues bleiben bei Wiederholung eindeutig zugeordnet, sonst ist Nichtausführung vermerkt. |

**Abschluss:** Endgültig bestanden ist die Library erst, wenn L01 bis L07 und
alle Schrittergebnisse im Funktionsdurchlauf belegt sind. Nicht ausgeführte
Prüfungen bleiben offen. Unanwendbare Teilfälle, etwa nicht beauftragte externe
Issues, benötigen eine begründete Scope-Angabe und ersetzen keinen anderen
Nachweis. Bis dahin lautet der Prüfstatus „bedingt bestanden“.
