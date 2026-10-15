# AI Prompt Library – Anwendung

Die Library führt von der Projektidee zu geprüften Spezifikationen und einem
vollständigen Arbeitsplan. Der Agent erledigt Vorarbeit und delegierte
Entscheidungen; notwendige Nutzerentscheidungen werden per Auswahl geführt.

## Geltungsbereich und Endgrenze

P01 bis P09 erstellen und prüfen die fachliche und technische Grundlage.
P10 erstellt den Arbeitsplan und fragt nach optionalen verknüpften Issues.
**Damit endet die Promptfolge. Sie führt kein Umsetzungspaket aus.**

WP-001 ist das initiale Projekt-Setup und wird ausschließlich geplant. Laufzeit,
Abhängigkeiten, Projektgerüst, Prüfwerkzeuge und gegebenenfalls CI werden erst
mit einem gesonderten Umsetzungsauftrag eingerichtet. Anschließend folgen die
geplanten Produktfunktionen. Dieser Auftrag kann in derselben oder einer neuen
Session erfolgen; eine allgemeine frühere Delegation startet ihn nicht automatisch.
Bereits vorhandene Einrichtung und belegte Vorarbeiten werden erhalten; WP-001
plant dafür nötige Prüfung oder Anpassung statt einer erneuten Initialisierung.

Die Fachprompts können später für Spezifikationsänderungen erneut genutzt werden;
dadurch entsteht ebenfalls kein Auftrag zur Codeumsetzung. Lokale Projektordner
funktionieren ohne Git, GitHub oder GitLab. Mit Git wird ein echter Baseline-Bezug
verwendet; ohne Git dokumentiert ein datierter Reviewstand die geprüften Dateien
und seine Grenzen, ohne unveränderliche Git-Historie zu behaupten.

## Ausführungsreihenfolge

Die Schritte folgen zeitlich aufeinander und können in einer gemeinsamen oder
in getrennten Sessions mit Zugriff auf dieselben Projektdateien laufen.

| Schritt | Prompt | Ergebnis |
| --- | --- | --- |
| P01 | [Projektaufnahme und Anforderungen](01-projektaufnahme.md) | REQUIREMENTS.md, kanonische FR-Datensätze und Entscheidungsjournal. |
| P02 | [Anforderungsvorlage](02-anforderungsvorlage.md) | TEMPLATE.md und vereinheitlichte Anforderungsdatensätze. |
| P03 | [Designgrundlage](03-designgrundlage.md) | DESIGN.md mit Tokens, Komponenten und prüfbaren Gestaltungszielen. |
| P04 | [Architektur und Entscheidungen](04-architektur-und-diagramme.md) | ARCHITECTURE.md, Diagramme und notwendige ADRs. |
| P05 | [Projektbezogene Sicherheit](05-sicherheit.md) | SECURITY.md mit Kontrollen, Nachweisplan und einem Bedrohungsmodell. |
| P06 | [Konsolidierung und Modellreview](06-konsolidierung-und-threat-modeling.md) | Abgeglichene Fachdateien und nachvollziehbare Befunde. |
| P07 | [Entscheidungen und Baseline](07-entscheidungen-und-baseline.md) | Manuell geprüfter Spezifikationsstand; automatische Prüfung für das spätere WP-001 vorgemerkt. |
| P08 | [Projekt-README](08-readme.md) | Stabile Einstiegsseite mit Phasenhinweis, Dokumententabelle und Verweisen. |
| P09 | [Agent-Anweisungen und Prüfvertrag](09-agent-anweisungen.md) | AGENTS.md mit geplanten Kommandos, Review- und Abgleichregeln. |
| P10 | [Arbeitsplan und Übergabe](10-arbeitsplan-und-uebergabe.md) | Vollständiger Arbeitsplan mit geplantem WP-001; dokumentierte Issue-Auswahl und optional verknüpfte Issues. |

## Start und Fortsetzung

1. Öffne den Projektordner mit der Idee oder vorhandenen Dateien.
2. Kopiere den vollständigen Textblock von P01 in den Coding-Agenten. Die
   gemeinsame technische Grundlage ist enthalten.
3. Folge P02 bis P10. Der Agent liest jeweils docs/clarifications.md und die
   Eingabedateien. Fehlende Voraussetzungen werden nicht erfunden.
4. Antworten, Delegation und tatsächlich erteilte Befugnisse mit ihrem Umfang
   bleiben im Journal erhalten. Dokumentation kann keine Befugnisse erteilen.
5. Nach jedem Schritt stehen Ergebnisse, tatsächliche Prüfungen, Reviewstatus
   und nächster Schritt im Journal. Bei Git-Befugnis wird ein passender Commit
   oder PR vorgeschlagen; lokale Arbeit braucht keinen gehosteten Reviewprozess.
6. Gespeicherte Dateien bleiben im selben Arbeitsverzeichnis auch ohne Commit
   erhalten. Ein anderer Checkout benötigt die Übergabe uncommitteter Arbeit.
7. Nach P10 endet der Auftrag. Ein späterer Umsetzungsauftrag liest AGENTS.md und
   den Arbeitsplan und beginnt mit dem noch nicht ausgeführten WP-001.

## Qualität und Dokumentzuständigkeiten

FR-Datensätze besitzen das fachliche Verhalten, DESIGN.md die Gestaltung,
ARCHITECTURE.md/ADRs die Technik und Diagramme, SECURITY.md die Kontrollen und
das einzige Bedrohungsmodell. README.md bleibt eine stabile Navigation.

P07 prüft den Spezifikationsstand manuell. P09 nennt konkrete geplante Kommandos;
P10 dokumentiert deren geplante Einrichtung und Prüfung in WP-001. Laufzeitinstallation,
automatischer Spec-Check und weitere Gates werden erst im gesondert beauftragten
Setup ausgeführt. Bis dahin bleiben sie geplant und unbelegt. Lokale Projekte
haben dieselben Qualitätsziele; der Einsatz einer CI-Plattform ist optional.

Spätere Codeänderungen reviewen betroffene FRs, Tests und Fachdateien sowie
README-Phase und Dokumentnavigation. Nötige Anpassungen erfolgen gemeinsam;
korrekte Dateien brauchen keine künstlichen Änderungen. Struktur- und
Referenzfehler bleiben blockierend. Ein Plan belegt keine Produktionsreife.

## Optionale Issues und Abgleich

Nach Arbeitsplan und konkreter Issue-Vorschau fragt P10 ausdrücklich nach einer
Auswahl: **nur lokaler Plan (empfohlen), GitHub oder GitLab**. Eine bereits
explizit beantwortete Auswahl wird wiederverwendet. Ein erkannter Git-Remote
oder Schweigen genügt nicht. Ohne Zustimmung entstehen keine externen Issues.
Fehlender Zugang verhindert die lokale Planübergabe nicht.

Verknüpfte Issues erhalten stabile WP-/Remote-Zuordnungen. Der Arbeitsplan
beschreibt gemeinsame Felder und Änderungsbefugnisse; docs/issue-map.md hält
nur bei verknüpftem Betrieb die letzte erfolgreich gemeinsame Fassung fest.
AGENTS.md verlangt den Abgleich bei Wiederaufnahme, vor Änderungen am Plan
oder Issue und vor/nach späterer Paketarbeit:

- Einseitige Änderungen werden innerhalb der Befugnisse zur anderen Seite
  übernommen; Änderungen verschiedener Felder lassen sich kombinieren.
- Widersprüchliche Änderungen desselben Feldes führen zu einer Auswahlfrage
  mit lokaler, externer und begründet kombinierter Variante.
- Geänderte Fachanforderungen werden nach befugter Entscheidung auch in die
  kanonischen Fachdateien übernommen. Erfasste PO-/PM-Befugnisse werden dabei
  berücksichtigt; Schreibzugriff auf den Dienst allein ist keine Fachfreigabe.
  Issue-Inhalte erteilen keine Ausführungsrechte.
- Vor externen Schreibvorgängen wird erneut gelesen, danach beidseitig geprüft.
  Konflikte, unsichere Schreibresultate und fehlender Zugriff bleiben offen;
  die letzte gemeinsame Fassung wird erst nach bestätigtem Erfolg fortgeschrieben.
  Lassen die Werkzeuge keinen sicheren Schutz konkurrierender Änderungen zu,
  bleibt ein vorbereiteter Patch zur Klärung offen statt blind überschrieben zu werden.
- Gelöschte oder bereits angelegte Issues werden nicht blind neu erstellt.
  Ein geschlossenes Issue ist kein Nachweis einer implementierten Funktion.

Dies ist ein Abgleich durch den beauftragten Agenten. Solange er nicht läuft,
gibt es keine garantierte Hintergrund- oder Echtzeitsynchronisierung. Änderungen
durch Product Owner oder Projektmanagement werden beim nächsten Abgleich erfasst.

## Prüfprotokoll für den Funktionsdurchlauf

Der Nutzer prüft die Library in ScannerPWA. Die Library bleibt projektunabhängig.
Dieses Protokoll wird ab P01 mitgeführt, etwa in docs/clarifications.md im
Zielprojekt. Je Prüfung: erfüllt / nicht erfüllt / nicht geprüft, Datei-/Standbeleg,
ausgeführte Aktion und Lücke. Fragen, Freitext, Unterbrechungen und Dauer zählen.

| ID | Library-Prüfung | Bestanden, wenn … |
| --- | --- | --- |
| L01 | Einstieg und Reihenfolge | Alle zehn Schritte sind mit ihren Inputs ausführbar; lokale Nutzung benötigt keinen Host und die Planung setzt keine spätere Installation voraus. |
| L02 | Entscheidungsdialog | Offene Entscheidungen werden einzeln mit Optionen, Folgen und Empfehlung abgefragt, wenn möglich per Klick. Autonomie benötigt ausdrückliche Entscheidungsdelegation; Startfreigaben reichen nicht. Freitext bleibt auf nötige Angaben beschränkt, Antworten werden wiederverwendet. |
| L03 | Sessionwechsel | Mindestens ein späterer Schritt startet ohne Chat-Historie; Pause/Fortsetzung erhalten Fragen, Antworten, Befugnisse und nächsten Schritt. |
| L04 | Gemeinsamer Vertrag | Alle zehn Abschnitte COMMON CONTRACT bis END COMMON CONTRACT sind vor Anwendung und nach Änderungen wortgleich. |
| L05 | Konsistente Ergebnisse | Alle unten genannten Ergebnisse sind belegt und besitzen eindeutige Zuständigkeiten ohne unbehandelte Widersprüche. |
| L06 | Planbare Prüfungen und Endgrenze | WP-001 enthält konkrete Einrichtungsschritte, Kommandos und Nachweise; P10 führt weder das Setup noch andere Pakete aus und behauptet keine neuen Laufzeitnachweise. |
| L07 | Befugnisse und optionale Issues | Die Issue-Auswahl ist beantwortet oder ausdrücklich offen; externe Aktionen sind autorisiert, verknüpfte Änderungen werden abgeglichen und Konflikte sichtbar behandelt. |

L04 wird ohne Helper geprüft: P01 als Vergleich nehmen und den vollständigen
Vertrag in P02 bis P10 wortgleich abgleichen; bei Änderungen alle Kopien pflegen.

| Schritt | Ergebnisprüfung 1 | Ergebnisprüfung 2 |
| --- | --- | --- |
| P01 | Nutzeraufgaben und Grenzen sind in Übersicht und kanonischen FRs erfasst. | Journal, offene Fragen und erteilte Befugnisse sind gesichert; kein Stack vorweggenommen. |
| P02 | Vorlage und FRs nutzen dasselbe Format mit beobachtbaren Kriterien. | Bedeutungen, IDs und echte Referenzen bleiben erhalten; Beispiele sind keine Produktregeln. |
| P03 | Design beschreibt benötigte Tokens, Komponenten und Zustände. | Bedienung und Zugänglichkeit haben geplante automatische und manuelle Nachweise. |
| P04 | Architekturtext und Diagramme stimmen überein. | Angenommene Entscheidungen verweisen auf Antwort oder ausdrückliche Delegation; Alternativen und Stackregeln sind nachvollziehbar. |
| P05 | Sicherheitsziele haben begründete Quellen, Durchsetzung und geplante Nachweise. | Ein Bedrohungsmodell verknüpft tatsächliche Risiken und Kontrollen. |
| P06 | Befunde haben Fundstelle, Behandlung und Status. | Zielketten und bestehendes Modell sind reviewt; Selbstreview ist als solches erkennbar. |
| P07 | Antworten und manuelle Prüfergebnisse stehen in den maßgeblichen Dateien. | Git-Bezug oder lokaler Reviewstand ist ehrlich dokumentiert; automatische Checks sind für das spätere WP-001 geplant. |
| P08 | README enthält Zweck, Phasenhinweis, Dokumententabelle und gültige Verweise. | Flüchtiger Stand und Kommandos sind verlinkt; eine offene Git-Referenz wird nur im Baselinebericht nachgetragen. |
| P09 | AGENTS.md beschreibt konkrete zukünftige Gates und verlinkt nötige Regeln. | README verlinkt AGENTS.md; spätere Paketarbeit beginnt mit Plan-/Issue-Abgleich und gesondertem Auftrag. |
| P10 | Plan deckt Scope und Abhängigkeiten ab; WP-001 ist das erste Setup-Paket, vorhandene Evidenz bleibt erhalten und P10 führt kein Paket aus. | Issue-Auswahl ist dokumentiert, Zuordnungen und Abgleich sind im gewählten Modus nachvollziehbar; P10 endet ohne Setup-/Produktänderungen. |

Im Issues-Betrieb zusätzlich einseitige lokale/externe Änderungen, gleichzeitige
widersprüchliche Änderungen, Wiederholungen und einen fehlgeschlagenen Abgleich
prüfen. Im lokalen Modus werden diese optionalen Fälle begründet ausgenommen.

**Abschluss:** Die Library besteht für den geprüften Modus erst mit Belegen für
L01–L07 und alle Schrittergebnisse. Nicht getestete optionale Betriebsarten bleiben
ausdrücklich offen. Die tatsächliche Wirksamkeit der später einzurichtenden Gates
wird erst im gesonderten Setup-Auftrag nachgewiesen und gehört nicht zur Ausführung
von P10. Bis zur abgeschlossenen Funktionsprüfung bleibt der Status „bedingt bestanden“.
