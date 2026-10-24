# Idea to Spec – Leitfaden (Version 1.0.0-beta.1)

Idea to Spec führt ein Webprojekt von der Projektidee zu einer abgestimmten, prüfbaren Spezifikation und daraus abgeleiteten Arbeitspaketen. Jeder Schritt ist ein kopierbarer Prompt. Die Prompts arbeiten gemeinsam mit Ihnen, halten Ergebnisse in Projektdateien fest und sind unabhängig voneinander nutzbar.

Für Websites, Webanwendungen, PWAs und Web-APIs ist die Library gedacht. Angrenzende Projekte (Hybrid-Apps, Browsererweiterungen) können sie nutzen; das ist ungeprüft.

## So arbeiten Sie

1. Kopieren Sie den englischen Prompt-Block aus der Datei und füllen Sie den Eingabeblock aus. Leere Felder sind erlaubt. Prüfen Sie dabei das Feld **Defaults**: Dort stehen die Standards, die die KI ohne Rückfrage anwendet. Ersetzen Sie, was für Ihr Projekt nicht passt. Fügen Sie den Prompt dann in Ihre KI-Session ein.
2. Übergeben Sie im Chat, was Sie schon haben: Projektunterlagen und optional ein Vorgabendokument, etwa Unternehmensstandards oder vertraglich vereinbarte Details. Das Vorgabendokument hat Vorrang vor den Defaults.
3. Was weder Prompt noch Unterlagen beantworten, fragt die KI im Gespräch.
4. Die KI führt im Gespräch und schreibt das Ergebnis in die Ergebnisdatei im Zielprojekt. Ohne Dateizugriff liefert sie einen vollständigen Markdown-Entwurf und sagt ausdrücklich, dass nichts gespeichert wurde. Übernehmen Sie ihn dann selbst.
5. Eine eigene Session je Rolle wird empfohlen; eine gemeinsame Session funktioniert ebenso. Neue Sessions setzen anhand der Projektdateien fort, nicht anhand früherer Chats.

Die Reihenfolge unten ist eine Empfehlung. Nutzen Sie nur, was Ihr Projekt braucht: Ein kleines Projekt braucht oft nur Anforderungen, Architektur und Arbeitspakete.

## Prompt-Übersicht (empfohlene Reihenfolge)

| Schritt | Prompt | Ergebnisdatei |
| --- | --- | --- |
| 1 | [Anforderungen](requirements.md) | `REQUIREMENTS.md` |
| 2 (optional) | [Anforderungsvorlage](requirements-template.md) | `docs/requirements/TEMPLATE.md` |
| 3 | [Recht](legal.md), empfohlen vor Design und Architektur | `LEGAL.md` |
| 4 | [Design](design.md) (inkl. Barrierefreiheit) | `DESIGN.md` |
| 5 | [Architektur](architecture.md) | `ARCHITECTURE.md` |
| 6 | [Sicherheit](security.md) | `SECURITY.md` |
| 7 | [Konsolidierung](consolidation.md) | `docs/consolidation.md` |
| 8 | [Entscheidungen und Baseline](decisions-and-baseline.md) | `docs/baseline-review.md` |
| 9 | [Agent-Anweisungen](agent-instructions.md) | `AGENTS.md` |
| 10 | [Arbeitspakete](work-packages.md) | `docs/work-packages.md` |
| jederzeit | [Projekt-README](project-readme.md) | `README.md` |

Rollen und Dateinamen sind Beispiele. Ergänzen Sie Fachgebiete oder bündeln Sie zusammengehörige Beiträge, wenn das zum Projekt passt.

## Die Schritte im Einzelnen

Zu jedem Schritt gilt: Voraussetzungen und Eingaben stehen im Kopf der Prompt-Datei. Die Prüfkriterien unten prüfen Sie, bevor Sie weitergehen.

### Anforderungen
- **Wann:** am Anfang, auch mit einer unvollständigen Idee.
- **Entscheidungen:** Ziel, Nutzer, Umfang, Ausschlüsse sowie welche Daten verarbeitet werden und wer sie sehen oder ändern darf; die KI fragt das Wichtigste zuerst.
- **Ergebnis:** Anforderungen (FR) mit Abnahmekriterien (AC); unklare Punkte als Entwurf mit offener Frage (OQ).
- **Prüfen:** Jede Anforderung hat ein beobachtbares Abnahmekriterium; Fehler-, Grenz- und Berechtigungsfälle sind beschrieben oder offen benannt.

### Anforderungsvorlage (optional)
- **Wann:** wenn Anforderungen uneinheitlich vorliegen oder Sie ein festes Format wollen.
- **Ergebnis:** Vorlage, vorhandene Anforderungen im selben Format.
- **Prüfen:** Bedeutung und Kennungen sind unverändert.

### Recht
- **Wann:** vor Design und Architektur, damit Entscheidungen zu Schriften, Bibliotheken und Drittanbietern im rechtlichen Rahmen fallen.
- **Entscheidungen:** Zielmarkt, personenbezogene Daten, Drittanbieter, Projektlizenz.
- **Ergebnis:** rechtlicher Rahmen, Anforderungen, Lizenzregeln. Keine Rechtsberatung: die Prüfung bleibt bei einem Menschen.
- **Prüfen:** Offene Rechtsfragen sind als solche markiert, nichts ist als geprüft ausgegeben, was nicht geprüft wurde.

### Design
- **Wann:** nach den Anforderungen, wenn das Projekt eine Oberfläche hat.
- **Ergebnis:** Abläufe, Komponenten, Zustände und Barrierefreiheit (WCAG 2.2 AA) mit Prüfkette.
- **Prüfen:** Jeder Ablauf verweist auf Anforderungen; Barrierefreiheit hat ein Kriterium, einen Nachweis und ein Gate.

### Architektur
- **Wann:** nach den Anforderungen, bei Bedarf nach Recht und Design.
- **Entscheidungen:** Technologien und Betriebsrahmen; jede Wahl wird als Entscheidung (ADR) festgehalten.
- **Prüfen:** Schnittstellen, Datenhaltung und Entscheidungen sind beschrieben; benötigte reale Betriebsangaben sind benannt. Werte, die erst eine Messung am realen System liefert, haben einen Startwert mit Grundlage (als Annahme) oder bleiben offen; beides wird als „messen, dann festlegen“ geplant.

### Sicherheit
- **Wann:** empfohlen direkt nach der Architektur. Sicherheit wird früh einbezogen: Die Anforderungen beschreiben Daten und Zugriffsrechte, und jeder Beitrag prüft seine Änderungen auf Sicherheitsfolgen.
- **Entscheidungen:** Bedrohungen und Schutzanforderungen, im Gespräch mit Ihnen.
- **Ergebnis:** Bedrohungen (STRIDE), Schutzanforderungen (SEC) nach ASVS 5.0 Stufe 2, je mit Durchsetzungspunkt, Test (T) und Gate; kurze Sicherheitsregeln für Agenten zum gewählten Technologiestack, jede mit Quelle.
- **Prüfen:** Jede Schutzanforderung hat einen Durchsetzungspunkt und einen geplanten Nachweis. „Dokumentiert“ heißt nicht „durchgesetzt“. Keine Agentenregel ohne Quelle. Bedrohungsanalyse und Schutzanforderungen sind vor der Umsetzung von einem Menschen geprüft.

#### Threat Modeling: Bedrohungen systematisch untersuchen

Beim Threat Modeling (Bedrohungsmodellierung) betrachten Sie, wie das System missbraucht werden könnte und welcher Schutz nötig ist. Der Sicherheitsbeitrag entsteht dabei so:

1. **System beschreiben:** Stellen Sie Bausteine, Datenflüsse, externe Dienste und schützenswerte Daten aus der Architektur zusammen. Benennen Sie Vertrauensgrenzen: Übergänge zwischen Bereichen mit unterschiedlichen Zugriffsrechten oder unterschiedlichem Vertrauen.
2. **Offene Fragen klären:** Klären Sie fehlende Angaben zu Rollen, Anmeldung, Berechtigungen und Betrieb gemeinsam mit der KI, eine Frage nach der anderen.
3. **Bedrohungen untersuchen:** Gehen Sie die relevanten Datenflüsse und Vertrauensgrenzen mit STRIDE durch, zum Beispiel auf unberechtigten Zugriff oder Datenmanipulation.
4. **Schutz und Prüfung planen:** Leiten Sie daraus Schutzanforderungen (SEC) ab. Halten Sie für jede fest, wo sie durchgesetzt wird und welcher Test (T) mit welchem Gate ihre Erfüllung prüfen soll.
5. **Ergebnis festhalten:** Dokumentieren Sie Bedrohungen, Schutzanforderungen und offene Fragen in `SECURITY.md`. Ein einfaches Datenflussdiagramm kann helfen, wenn es Zusammenhänge klarer macht.

In eigenen Worten angelehnt an [Manicodes „Integration: Threat Modeling Workflow“](https://docs.manicode.ai/docs/integrations/threat-modeling-workflow/), angepasst an die Ergebnisdateien von Idea to Spec.

### Konsolidierung
- **Wann:** wenn mindestens zwei Beiträge vorliegen, und erneut nach größeren Änderungen.
- **Ergebnis:** Prüfbericht mit Widersprüchen, Lücken und Zuständigkeiten; Urteil „bereit“, „bereit mit Lücken“ oder „nicht bereit“.
- **Prüfen:** Jede verbindliche Vorgabe hat genau eine zuständige Datei; andere verweisen darauf.

### Entscheidungen und Baseline
- **Wann:** nach der Konsolidierung, vor den Arbeitspaketen.
- **Entscheidungen:** die blockierenden offenen Fragen, nacheinander.
- **Ergebnis:** festgehaltener, referenzierbarer Spezifikationsstand.
- **Prüfen:** Keine blockierende Frage ist offen; verbleibende Lücken und ihr Umfang sind sichtbar.

### Agent-Anweisungen
- **Wann:** vor der Umsetzung, nachdem die Fachdateien ihre Gates festgelegt haben.
- **Ergebnis:** `AGENTS.md` mit Regeln, Verweisen je Aufgabenart auf die Sicherheitsregeln in `SECURITY.md` und konkreten Prüfkommandos je Gate; fehlende Kommandos sind als „geplant“ markiert.
- **Prüfen:** Kein Kommando ist erfunden; jedes Gate ist einer Fachdatei zugeordnet.

### Arbeitspakete
- **Wann:** wenn der Umfang ausreichend spezifiziert ist (Konsolidierung „bereit“ oder „bereit mit Lücken“).
- **Ergebnis:** Pakete (WP) mit Ziel, Umfang, Spezifikationsbezug, Vorgängern, grober Komplexität, Abnahmekriterien (Gherkin) und geplanten Prüfungen.
- **Prüfen:** Jede Anforderung im Umfang ist abgedeckt; kein Paket ist „groß“; kein Paket verlangt eine stille neue Entscheidung. Jeder noch zu messende Wert hat ein Paket „messen, dann festlegen“, dessen Ergebnis über den zuständigen Fachprompt in die Spezifikation geht.

## Kennungen und Kennzeichnung

FR Anforderung · AC Abnahmekriterium · OQ offene Frage · ADR Architekturentscheidung · SEC Sicherheitsanforderung · T Test · WP Arbeitspaket. Eine Kennung wird nie neu vergeben; Verweise laufen über sie. Inhalte sind gekennzeichnet als bestätigt, Default (bestätigter Standard), Annahme, KI-Vorschlag, offen oder delegiert. Klärungen stehen mit Begründung und Datum bei der offenen Frage oder der Entscheidung.

## Offene Fragen und Widersprüche

- Was die Defaults im Prompt, Ihr Vorgabendokument oder die Projektunterlagen beantworten, übernimmt die KI ohne Rückfrage und nennt die Quelle.
- Nur was keine dieser Stellen beantwortet, legt sie Ihnen vor: eine Entscheidung pro Nachricht, die blockierende zuerst, mit begründeter Empfehlung. Sie bestätigen oder wählen etwas anderes.
- Die KI verwendet bereits beantwortete Fragen wieder.
- Eine Entscheidung trifft die KI nur, wenn Sie sie ausdrücklich delegiert haben.
- Lehnt ein Prompt eine bestätigte Entscheidung eines anderen Beitrags ab, überschreibt er sie nicht. Er legt eine offene Frage (OQ) mit Bezug an, und Sie entscheiden.

## Rücksprünge

Erkenntnisse aus Design, Architektur oder Sicherheit können Anforderungen verändern. Gehen Sie dann zum zuständigen Prompt zurück, ändern Sie dort und führen Sie die Konsolidierung erneut aus. Eine Entscheidung, die Sie bestätigen, trägt der jeweilige Prompt in derselben Runde in alle betroffenen Dateien ein, auch in die anderer Beiträge; dafür ist keine weitere Freigabe nötig. Neue Änderungen nach Konsolidierung oder Arbeitsplanung laufen über den zuständigen Fachprompt; betroffene Beiträge und Arbeitspakete werden aktualisiert oder konkret benannt. Setzen Sie erst fort, wenn die Prüfkriterien des betroffenen Schritts wieder erfüllt sind.

## Kleine Änderungen und Fehlerbehebungen (kurzer Weg)

1. Ändern Sie mit dem Anforderungs-Prompt nur die betroffene Anforderung und ihr Abnahmekriterium.
2. Lassen Sie weg, was für den kleinen Umfang keinen Nutzen hat (zum Beispiel Recht, Design, Konsolidierung).
3. Prüfen Sie, ob Architektur oder Sicherheit betroffen sind, und aktualisieren Sie betroffene Beiträge.
4. Aktualisieren oder ergänzen Sie die betroffenen Arbeitspakete. Das bleibt auch hier Pflicht.

## Übergang in die Umsetzung

Idea to Spec liefert Spezifikation und Arbeitspakete, keine Umsetzungsprompts. Implementierung, Tests, Review und Qualitätssicherung brauchen einen eigenen Auftrag, beginnen mit den Arbeitspaketen, den Agent-Anweisungen und den Gates und prüfen ihre Ergebnisse gegen die Spezifikation. Tatsächliche Prüfergebnisse werden dokumentiert; geplante Kommandos gelten nicht als ausgeführt. Setup, Paketinstallation, Deployment und Infrastrukturkäufe brauchen ebenfalls einen eigenen Auftrag.

## Begriffe

- **Spec-Driven Development:** Die abgestimmte Spezifikation ist die Grundlage für Planung, Umsetzung, Tests, Review und Abnahme.
- **EARS:** Satzschablonen für eindeutige Anforderungssätze.
- **Gherkin:** Abnahmekriterien in der Form Gegeben/Wenn/Dann, die sich prüfen lassen.
- **ADR / MADR:** festgehaltene Architekturentscheidung mit Optionen und Begründung.
- **arc42:** schlanke Gliederung für Architekturdokumentation.
- **ASVS:** OWASP-Katalog von Sicherheitsanforderungen; Stufe 2 ist der Standard für normale Webanwendungen.
- **STRIDE:** Denkschema für Bedrohungen (Fälschung, Manipulation, Abstreiten, Informationsabfluss, Dienstausfall, Rechteausweitung).
- **WCAG 2.2 AA:** Standard für barrierefreie Oberflächen.
- **DSGVO:** EU-Datenschutzrecht bei personenbezogenen Daten von Personen in der EU.
- **Gate:** eine Prüfung, die scheitern kann und eine Aussage belegt. Kette je Qualitätsziel: Ziel → Kriterium → Nachweis → Gate.
- **Baseline:** geprüfter, referenzierbarer Stand der Spezifikation.
- **PWA:** Webanwendung, die sich wie eine installierbare App verhält.
