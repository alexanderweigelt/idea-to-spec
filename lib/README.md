# AI Prompt Library – Anwendung

Wähle den Prompt für die aktuelle Aufgabe. Jeder Textblock ist eigenständig
nutzbar und enthält die gemeinsame Qualitätsgrundlage. Kein Prompt setzt die
Ausführung eines anderen voraus. Benötigt werden fachlich ausreichende Eingaben,
die auch aus bestehenden Dokumenten oder deinem Projektkontext stammen können.
Jeder Prompt erstellt oder aktualisiert seine eigene Ergebnisdatei. Der Agent
prüft im Dateisystem, welche anderen Artefakte bereits vorliegen, und liest daraus
die für seine Aufgabe relevanten Informationen. Fehlende Dateien allein erzwingen
keinen weiteren Prompt-Lauf.

## Promptübersicht und empfohlener Ablauf

Bei einer neuen Idee sind Anforderungen ein sinnvoller Anfang. Darauf können
Gestaltung, Architektur und Sicherheit aufbauen; Review und Klärung schaffen
eine belastbare Grundlage für den Arbeitsplan. README und Agent-Anweisungen
werden ergänzt, sobald die nötigen Informationen vorliegen.

Die Tabellenreihenfolge ist eine Orientierung. Wähle nur passende Aufgaben und
wiederhole sie bei Bedarf. Ohne Benutzeroberfläche entfällt beispielsweise das
Design; Architektur, Sicherheit und Planung arbeiten mit dem übrigen Kontext.
Ein belastbarer Arbeitsplan braucht geklärte Ziele und technische Entscheidungen.
Fehlende wesentliche Informationen werden geklärt, ohne andere Prompts zu erzwingen.

| Prompt | Ergebnisdatei | Inhalt |
| --- | --- | --- |
| [Projektaufnahme und Anforderungen](projektaufnahme.md) | REQUIREMENTS.md | Fachliche Anforderungen mit beobachtbaren Kriterien und offenen Fragen. |
| [Anforderungsvorlage](anforderungsvorlage.md) | docs/requirements/TEMPLATE.md | Einheitliche Vorlage und entsprechend aufbereitete Anforderungsdatensätze. |
| [Designgrundlage](designgrundlage.md) | DESIGN.md | Gestaltung und zugängliche Interaktion für die benötigte Benutzeroberfläche. |
| [Architektur und Entscheidungen](architektur-und-diagramme.md) | ARCHITECTURE.md | Technische Struktur, begründete Entscheidungen und passende Diagramme. |
| [Projektbezogene Sicherheit](sicherheit.md) | SECURITY.md | Sicherheitsanforderungen, Bedrohungsmodell und geplante Nachweise. |
| [Konsolidierung und Modellreview](konsolidierung-und-threat-modeling.md) | docs/specification-review.md | Abgeglichene Spezifikationen und nachvollziehbare Befunde. |
| [Entscheidungen und Baseline](entscheidungen-und-baseline.md) | docs/baseline-review.md | Geklärte Blocker und manuell geprüfter Spezifikationsstand. |
| [Projekt-README](projekt-readme.md) | README.md | Stabile Einstiegsseite mit Zweck, Phase und Dokumentnavigation. |
| [Agent-Anweisungen](agent-anweisungen.md) | AGENTS.md | Kompakte Entwicklungsregeln und projektbezogene Prüfkommandos. |
| [Arbeitsplan und Übergabe](arbeitsplan-und-uebergabe.md) | docs/work-plan.md | Umsetzungspakete, lokale Nachverfolgung und optional verknüpfte Issues. |

## Nutzung und Fortsetzung

1. Öffne den Projektordner und wähle eine passende Vorlage.
2. Kopiere ihren vollständigen Textblock in den Coding-Agenten. Er prüft die
   vorhandenen Artefakte selbst; ergänze nur Informationen, die daraus fehlen.
3. Der Agent nutzt vorhandene Antworten und klärt offene Entscheidungen per
   Auswahl. Autonome Entscheidungen benötigen eine ausdrückliche Delegation.
4. Ergebnisse, Fragen, Befugnisse, tatsächliche Prüfungen und nächste sinnvolle
   Arbeit bleiben in docs/clarifications.md oder einem vorhandenen gleichwertigen
   Journal erhalten. Eine neue Session braucht keine Chat-Historie.
5. Der Auftrag endet mit der gewählten Aufgabe. Ein weiterer Prompt oder die
   Umsetzung startet durch einen neuen Auftrag.

Dateinamen in den Prompts sind Vorgaben für neue Dokumente. Gleichwertige
Projektdateien können weiterverwendet werden. Erzeugte Dokumente nennen fachliche
Aufgaben und Projektartefakte; sie setzen keine Kenntnis dieser Library voraus.
Bei Git-Befugnis schlägt der Agent einen passenden Commit oder PR vor. Gespeicherte
Dateien bleiben im selben Arbeitsverzeichnis auch ohne Commit erhalten; ein anderer
Checkout benötigt die Übergabe uncommitteter Arbeit.

## Grenze zur Umsetzung

Alle Vorlagen erstellen oder prüfen Spezifikationen und Pläne. Sie installieren
keine Werkzeuge und führen weder Setup noch Produktentwicklung aus. Der
Arbeitsplan sieht WP-001 als initiales Setup vor; vorhandene Einrichtung wird
entsprechend ihrem tatsächlichen Stand berücksichtigt.

Ein gesonderter Umsetzungsauftrag nutzt den Arbeitsplan und vorhandene
Agent-Anweisungen. Laufzeit, Projektgerüst, Prüfbefehle und gegebenenfalls CI
werden erst dann eingerichtet und nachgewiesen. Geplante Prüfungen gelten bis
zur tatsächlichen Ausführung als offen. Ein Plan belegt keine Produktionsreife.

## Dokumentzuständigkeiten und Nachverfolgung

Anforderungen besitzen das fachliche Verhalten, Design die Gestaltung,
Architektur und ADRs die Technik samt Diagrammen, Sicherheit die Kontrollen
und das Bedrohungsmodell. Nur relevante Dokumente werden benötigt. README
navigiert, Agent-Anweisungen verlinken Entwicklungsregeln. Der Arbeitsplan
besitzt Stand und Nachverfolgung.

Lokale Projekte benötigen weder Git noch einen Hostingdienst. Ein Baseline-Review
verwendet mit Git einen tatsächlichen Commit-Bezug, andernfalls einen datierten
lokalen Reviewstand mit benannten Grenzen.

Der Arbeitsplan-Prompt fragt ausdrücklich, ob zusätzlich Issues in GitHub oder
GitLab angelegt werden sollen; eine bereits beantwortete Auswahl wird übernommen.
Ohne Zustimmung bleibt es beim lokalen Plan. Verknüpfte Issues werden nach den
Regeln im Arbeitsplan abgeglichen: einseitige Änderungen innerhalb erteilter
Befugnisse übernehmen, widersprüchliche Änderungen gemeinsam klären und nur
bestätigte Ergebnisse als synchron melden. Der Abgleich erfolgt bei Wiederaufnahme,
Plan-/Issue-Änderungen und vor/nach späterer Paketarbeit, ohne Hintergrunddienst.

## Prüfprotokoll für den Funktionsdurchlauf

Der Nutzer prüft die Library in ScannerPWA. Dokumentiere pro angewendetem Prompt
und Prüfung: erfüllt / nicht erfüllt / nicht geprüft / nicht anwendbar, mit
Datei-/Standbeleg, tatsächlicher Aktion und verbleibender Lücke. Zähle Fragen,
Freitext, Unterbrechungen und Dauer. Bewerte ausgelassene Aufgaben anhand des
Projektumfangs, nicht als fehlende Pflichtschritte.

| ID | Library-Prüfung | Bestanden, wenn … |
| --- | --- | --- |
| L01 | Eigenständige Nutzung | Jeder angewendete Prompt erzeugt seine Ergebnisdatei und nutzt relevante vorhandene Artefakte ohne vorgeschriebene Library-Läufe. Ein Projekt ohne UI benötigt kein Design-Dokument; lokale Nutzung braucht keinen Host. |
| L02 | Entscheidungsdialog | Offene Entscheidungen werden mit Optionen, Folgen und Empfehlung abgefragt. Autonomie benötigt ausdrückliche Entscheidungsdelegation; Antworten werden wiederverwendet. |
| L03 | Sessionwechsel | Ein Prompt startet ohne Chat-Historie; Fortsetzung erhält Fragen, Antworten, Befugnisse und nächste Arbeit aus Projektdateien. |
| L04 | Gemeinsamer Vertrag | Alle Abschnitte COMMON CONTRACT bis END COMMON CONTRACT sind wortgleich. |
| L05 | Konsistente Ergebnisse | Die angewendeten Prompts liefern ihre unten genannten Ergebnisse; Projektdateien enthalten verständliche fachliche Bezüge ohne Library-Kennungen. |
| L06 | Endgrenze | Keine Vorlage führt Setup oder Umsetzungspakete aus. Geplante Prüfungen gelten nicht als bestanden. |
| L07 | Befugnisse und optionale Issues | Externe Aktionen sind autorisiert; die Issue-Auswahl und der Abgleich verknüpfter Änderungen bleiben nachvollziehbar. |

L04 wird ohne Helper geprüft: einen vollständigen gemeinsamen Vertrag als
Vergleich nehmen und alle Kopien abgleichen; Änderungen in allen Kopien pflegen.

| Prompt | Ergebnisprüfung |
| --- | --- |
| Projektaufnahme | Nutzeraufgaben und Grenzen sind nachvollziehbar erfasst; Fragen und Befugnisse sind gesichert, kein Stack wird neu festgelegt. |
| Anforderungsvorlage | Anforderungen nutzen beobachtbare Kriterien; Bedeutungen, IDs und Referenzen bleiben erhalten. |
| Designgrundlage | Benötigte Gestaltung und Zustände sind konsistent; Zugänglichkeit hat passende geplante Nachweise. |
| Architektur | Text und Diagramme stimmen überein; Entscheidungen haben eine Antwort oder ausdrückliche Delegation als Grundlage. |
| Sicherheit | Tatsächliche Risiken sind mit Anforderungen, Durchsetzung und geplanten Nachweisen verknüpft. |
| Konsolidierung | Die eigene Reviewdatei nennt Befunde mit Fundstelle, Behandlung und Status; Selbstreview ist erkennbar. |
| Baseline | Der geprüfte Umfang und tatsächliche Ergebnisse sind dokumentiert; Git-Bezug oder lokaler Reviewstand sind ehrlich benannt. |
| Projekt-README | Zweck, Phase und gültige Dokumentverweise bleiben stabil; flüchtiger Stand ist nur verlinkt. |
| Agent-Anweisungen | Regeln und anwendbare Prüfkommandos sind nachvollziehbar; vorhandener Arbeitsplan und dessen Nachverfolgung sind verlinkt. |
| Arbeitsplan | Pakete decken den Umfang und ihre Abhängigkeiten ab, bleiben unausgeführt und haben eine dokumentierte Issue-Auswahl. |

Im Issues-Betrieb zusätzlich einseitige Änderungen, Konflikte, Wiederholungen und
fehlgeschlagenen Abgleich prüfen. Nicht getestete Betriebsarten bleiben offen.
Die praktische Prüfung der entkoppelten Vorlagen steht noch aus; die Wirksamkeit
später einzurichtender Prüfwerkzeuge wird erst während der beauftragten Umsetzung
nachgewiesen.
