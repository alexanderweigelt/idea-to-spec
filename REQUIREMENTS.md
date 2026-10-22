# Idea to Spec – Requirements und Zielbild

**Projekttitel:** Idea to Spec – Leitfaden und Fachprompts für Spec-Driven Development

**Stand:** 16.10.2026  
**Status:** Ausformulierung des gemeinsam festgelegten Zielbilds. Die Erfüllung durch den vorhandenen Projektstand ist damit nicht bewertet.

## 1. Oberstes Projektziel

Ziel von Idea to Spec ist es, eine Projektidee schrittweise in eine abgestimmte, konsistente und umsetzbare Spezifikation eines Webprojekts als verbindliche Grundlage für Spec-Driven Development zu überführen.

Rollenbasierte KI-Prompts unterstützen die Erarbeitung der benötigten Fachbeiträge. Jede Rolle erarbeitet ihren Beitrag gemeinsam mit dem Benutzer. Dafür wird eine eigene Session je Rolle empfohlen; eine gemeinsame Session muss ebenso funktionieren. Die Ergebnisse werden in Projektdateien dokumentiert, fachübergreifend abgestimmt und zu einer Gesamtspezifikation weiterentwickelt. Daraus entstehen überprüfbare Arbeitspakete für die anschließende Umsetzung.

Spec-Driven Development bedeutet für dieses Projekt: Die abgestimmte Spezifikation bildet die maßgebliche Grundlage für Planung, Implementierung, Tests, Review und Abnahme. Anforderungen und Entscheidungen müssen so konkret beschrieben sein, dass ihre Umsetzung und Erfüllung nachvollziehbar geprüft werden können.

Die Spezifikation wird bei bestätigten Änderungen weiterentwickelt. Betroffene Fachbeiträge und Arbeitspakete werden entsprechend aktualisiert.

Dieses Zielbild ist die oberste fachliche Grundlage des Projekts. Bestehende Prompts, Regeln und Ablaufbeschreibungen sind daran zu messen. Ihre bisherige Existenz macht sie nicht zu verbindlichen Anforderungen.

## 2. Produkt und Umfang

Das Produkt besteht aus:

- einer Library vollständiger, wiederverwendbarer und kopierbarer Prompts in `lib/`;
- einem praktischen Leitfaden außerhalb der einzelnen Promptvorlagen, der ihre Auswahl und Anwendung erklärt.

Zielgruppe sind Entwicklerinnen und Entwickler sowie Produktverantwortliche. Leitfaden und Prompts erklären die Begriffe der Methode und die technischen Begriffe, die Produktverantwortliche für ihre Entscheidungen benötigen. Grundlagen der Softwareentwicklung werden nicht erklärt.

Idea to Spec muss für unterschiedliche Webprojekte verwendbar sein. Webprojekte sind Projekte, deren Software über Webtechnologien bereitgestellt oder genutzt wird, also über Browser oder Webprotokolle wie HTTP. Kernfälle sind Websites, Webanwendungen, Progressive Web Apps (PWAs) und Web-APIs; für sie muss die Library nachweislich funktionieren. Angrenzende Projekte, etwa Hybrid-Apps oder Browsererweiterungen, können die Library nutzen; ihre Eignung gilt ohne eigenen Nachweis als ungeprüft. Technologien, Fachrollen und Prüftiefe richten sich nach dem jeweiligen Projekt. Kleine Projekte müssen einen schlanken Ablauf nutzen können.

Das zentrale Ergebnis der Anwendung ist eine zusammenhängende Projektspezifikation. Sie beschreibt das gewünschte Verhalten sowie die jeweils notwendigen gestalterischen, technischen und sicherheitsbezogenen Vorgaben. Weitere Fachgebiete werden nach Projektbedarf berücksichtigt.

Die Spezifikation kann aus mehreren verknüpften Dokumenten bestehen. Die daraus abgeleiteten Arbeitspakete machen ihre Umsetzung und Prüfung planbar.

Der Leitfaden erklärt den Übergang in die Umsetzung: wie Implementierung, Tests, Review und Qualitätssicherung mit den Arbeitspaketen, den Agent-Anweisungen und den Gates beginnen. Eigene Prompts für diese Schritte gehören nicht zum Produkt. Die Umsetzung baut auf der Spezifikation auf und benötigt einen eigenen Umsetzungsauftrag.

Diese Datei beschreibt Anforderungen an Idea to Spec selbst. Die mit der Library erzeugten Anforderungen, Designs und Architekturunterlagen gehören jeweils in das bearbeitete Zielprojekt.

## 3. Fachliches Arbeitsmodell

Der grundsätzliche Weg lautet:

**Projektidee → fachliche Ausarbeitung → gemeinsame Abstimmung → umsetzbare Spezifikation → Arbeitspakete**

Die fachliche Ausarbeitung kann beispielsweise folgende Beiträge umfassen:

| Fachrolle | Beitrag | Mögliche Ergebnisdatei |
| --- | --- | --- |
| Produktverantwortung / Anforderungsanalyse | Ziele, Nutzer, Umfang, Funktionen und beobachtbares Verhalten | `REQUIREMENTS.md` |
| UX/UI-Design | Nutzerabläufe, Bedienung, Layout, Komponenten und Oberflächenzustände | `DESIGN.md` |
| Architektur | Technischer Aufbau, Technologien, Schnittstellen und Datenhaltung | `ARCHITECTURE.md` |
| Sicherheit | Bedrohungen, Schutzanforderungen, Durchsetzungspunkte und geplante Verifikation | `SECURITY.md` |
| Recht (Datenschutz und Lizenzen) | Rechtlicher Rahmen, daraus folgende Projektanforderungen sowie Vorgaben für Lizenzen, Abhängigkeiten und Drittanbieter | beispielsweise `LEGAL.md` |
| Barrierefreiheit | Anforderungen an zugängliche Nutzung und deren Prüfung | eigener Beitrag oder Bestandteil des Designs |

Der Beitrag Recht wird empfohlen vor Design und Architektur erarbeitet, damit Entscheidungen etwa zu Schriften und Bibliotheken innerhalb seines Rahmens fallen. Design und Architektur berücksichtigen ihn, sofern vorhanden.

Sicherheit wird früh und durchgängig einbezogen. Der Anforderungsbeitrag beschreibt, welche Daten verarbeitet werden und wer sie sehen oder ändern darf; Schutzbedarf und Schutzanforderungen legt der Sicherheitsbeitrag fest. Der Sicherheitsbeitrag klärt Bedrohungen und Schutzanforderungen im Gespräch mit dem Benutzer; der Leitfaden empfiehlt ihn direkt nach der Architektur. Jeder Fachbeitrag prüft seine Änderungen auch auf Sicherheitsfolgen (REQ-006). Bedrohungsanalyse und Sicherheitsanforderungen erhalten vor der Umsetzung ein menschliches Review.

Die Rollen und Dateinamen sind Beispiele. Benötigte Fachgebiete können ergänzt und zusammengehörige Beiträge passend zum Projekt gebündelt werden.

Ergänzend zu den Fachbeiträgen bietet die Library begleitende Arbeitsschritte an:

| Arbeitsschritt | Beitrag | Mögliche Ergebnisdatei |
| --- | --- | --- |
| Anforderungsvorlage | Einheitliches, prüfbares Format für Anforderungen; vorhandene Anforderungen werden ohne Bedeutungsänderung darauf vereinheitlicht | `docs/requirements/TEMPLATE.md` |
| Entscheidungen und Baseline | Blockierende Entscheidungen schließen und einen geprüften, referenzierbaren Spezifikationsstand festhalten | `docs/baseline-review.md` |
| Projekt-README | Stabile Einstiegsseite mit Projektzweck, Phase und Navigation zu den Projektunterlagen | `README.md` |
| Agent-Anweisungen | Kompakte, agentenneutrale Entwicklungsregeln sowie konkrete Prüfkommandos und Gates für die spätere Umsetzung | `AGENTS.md` |

Die begleitenden Arbeitsschritte werden nach Projektbedarf genutzt. Der Leitfaden erklärt, wann ein Schritt sinnvoll ist.

Die Fachrollen beschreiben unterschiedliche Perspektiven und Arbeitsaufträge. Sie können nacheinander mit derselben KI in verschiedenen Sessions bearbeitet werden. Eine automatische Mehragentensteuerung ist keine Voraussetzung.

Der Ablauf enthält Rückkopplungen: Erkenntnisse aus Design, Architektur oder Sicherheit können Anforderungen verändern und eine erneute fachliche Abstimmung auslösen.

## 4. Funktionale Anforderungen

### REQ-001 – Einstieg aus einer Projektidee

Die Library muss den Einstieg mit einer noch unvollständigen Projektidee ermöglichen.

**Akzeptanzkriterien:**

- Der Einstieg erfasst Problem, Ziel, Nutzer, wesentliche Funktionen mit messbarem Qualitätsziel der Kernfunktionen, typische Abläufe, übliche Fälle der Zielplattform (etwa Rückkehr in die Anwendung oder Zurück-Navigation), Rahmenbedingungen und Ausschlüsse.
- Vorhandene Projektunterlagen werden berücksichtigt; fehlende Angaben bleiben sichtbar.
- Optional kann der Benutzer jedem Fachprompt im Chat Projektunterlagen und ein Vorgabendokument übergeben, etwa Unternehmensstandards oder vertraglich vereinbarte Details. Seine Vorgaben haben Vorrang vor den Defaults nach Q-006.
- Daraus entsteht ein erster Anforderungsstand mit stabilen Kennungen und beobachtbaren Akzeptanzkriterien. Unzureichend geklärte Anforderungen erhalten einen erkennbaren Entwurfsstatus.

### REQ-002 – Fachliche Beiträge durch eigene Prompts

Die Library muss die benötigten Fachbeiträge durch gezielt auswählbare Prompts erarbeiten lassen.

**Akzeptanzkriterien:**

- Jeder Fachprompt benennt Rolle, Zweck, Arbeitsauftrag und erwartetes Ergebnis.
- Der Prompt nutzt die relevanten vorhandenen Unterlagen und legt seinen Beitrag in einer eindeutig zugeordneten Ergebnisdatei ab oder entwickelt diese weiter.
- Die Auswahl der Fachbeiträge richtet sich nach dem Projektbedarf; die Beispielrollen bilden keine verpflichtende Checkliste.

### REQ-003 – Eigenständig nutzbare Arbeitsaufträge

Jeder Prompt muss als vollständiger Arbeitsauftrag in einer neuen oder laufenden Session verwendbar sein.

**Akzeptanzkriterien:**

- Der kopierbare Prompt enthält die notwendigen Anweisungen und eindeutig bezeichnete Eingabefelder.
- Fachliche Voraussetzungen und benötigte Unterlagen sind erkennbar. Gleichwertige vorhandene Ergebnisse können unabhängig von ihrer Entstehung verwendet werden.
- Fehlende Voraussetzungen werden gezielt geklärt oder als Lücke benannt.
- Der Prompt liefert das angeforderte Ergebnis beziehungsweise einen nachvollziehbaren Zwischenstand mit den noch notwendigen Klärungen.

### REQ-004 – Zusammenarbeit über Projektdateien

Die Library muss die Fortsetzung der Arbeit ohne Zugriff auf frühere Chats ermöglichen.

**Akzeptanzkriterien:**

- Eine neue Session kann die relevanten Fachbeiträge, bestätigten Entscheidungen, offenen Fragen und den nächsten sinnvollen Arbeitsschritt aus den gespeicherten Projektunterlagen erkennen.
- Jeder Prompt benennt die für seinen Auftrag benötigten Unterlagen und berücksichtigt deren tatsächliche Zugänglichkeit.
- Bestätigte Inhalte und vorhandene Änderungen bleiben erhalten; Widersprüche werden sichtbar gemacht.
- Bei fehlendem Dateizugriff wird ein vollständiger Markdown-Entwurf zur Übernahme bereitgestellt und die fehlende Speicherung ausdrücklich benannt.

### REQ-005 – Nachvollziehbare Klärung und Entscheidungen

Die Prompts müssen offene Entscheidungen mit dem Benutzer klären und deren Ergebnis nachvollziehbar festhalten.

**Akzeptanzkriterien:**

- Bereits beantwortete Fragen werden wiederverwendet. Neue Erkenntnisse, die eine Entscheidung erneut betreffen, werden erklärt.
- Blockierende Fragen werden priorisiert und jeweils verständlich gestellt. Bei geeigneten Entscheidungen werden Optionen, Auswirkungen und eine begründete Empfehlung angeboten.
- Vorgaben, Defaults, Annahmen, KI-Vorschläge, offene Entscheidungen und ausdrücklich delegierte Entscheidungen bleiben unterscheidbar.
- Antworten werden in derselben Runde in die zuständigen Fachunterlagen und alle betroffenen Stellen und Verweise übernommen, auch in Dateien anderer Beiträge; unterbrochene Klärungen können fortgesetzt werden.
- Offene Projektentscheidungen werden nur innerhalb einer ausdrücklichen Delegation eigenständig getroffen. Bereits geklärte Arbeit benötigt keine erneute Bestätigung.
- Vorgaben aus dem Prompt, dem Vorgabendokument oder vorhandenen Projektunterlagen werden ohne Rückfrage übernommen und mit Quelle als Vorgabe oder Default gekennzeichnet. Dem Benutzer wird nur vorgelegt, was keine dieser Stellen beantwortet, jeweils einzeln und mit begründeter Empfehlung.

### REQ-006 – Fachübergreifende Rückkopplungen

Die Library muss Änderungen zwischen den Fachbeiträgen nachvollziehbar bearbeiten lassen.

**Akzeptanzkriterien:**

- Jeder Fachprompt prüft, ob seine Ergebnisse andere vorhandene Fachbeiträge betreffen.
- Betroffene Stellen werden aktualisiert. Eine bestätigte Entscheidung gilt als Autorisierung, sie an allen betroffenen Stellen einzutragen. Benötigt eine Stelle eine neue inhaltliche Entscheidung eines anderen Beitrags, wird sie dort als offene Frage festgehalten. Nur was nicht gespeichert werden kann, wird als notwendige Folgearbeit konkret benannt.
- Eine bestätigte Änderung nach Konsolidierung oder Arbeitsplanung wird über den zuständigen Fachprompt eingebracht. Betroffene Fachbeiträge und Arbeitspakete werden aktualisiert oder konkret benannt.
- Der Leitfaden erklärt sinnvolle Rücksprünge und die Voraussetzungen für die Fortsetzung.

### REQ-007 – Gemeinsame Konsolidierung

Die Library muss einen eigenen Arbeitsschritt zur gemeinsamen Prüfung und Abstimmung der Fachbeiträge anbieten.

**Akzeptanzkriterien:**

- Anforderungen, Design, Architektur, Sicherheit und weitere vorhandene Beiträge werden auf Widersprüche, Lücken und gegenseitige Abhängigkeiten geprüft.
- Jede verbindliche Vorgabe besitzt eine eindeutige zuständige Stelle. Andere Dokumente verweisen darauf.
- Lehnt ein Fachprompt eine bestätigte Entscheidung eines anderen Beitrags ab, überschreibt er sie nicht. Er hält den Widerspruch als offene Frage (OQ) mit Bezug auf die betroffene Entscheidung (ADR) oder Anforderung (SEC, FR) fest, und der Benutzer entscheidet.
- Offene Punkte werden mit Bezug, Auswirkung und notwendiger Klärung festgehalten.
- Das Ergebnis ist eine konsistente Gesamtspezifikation. Diese darf aus mehreren verknüpften Dokumenten bestehen.

### REQ-008 – Erkennbarer Übergang zur Umsetzungsplanung

Die Library muss prüfbar beschreiben, wann ein Projektumfang ausreichend spezifiziert ist, um Arbeitspakete daraus abzuleiten.

**Akzeptanzkriterien:**

- Für den betrachteten Umfang sind Verhalten, relevante Gestaltung, technische Verträge und Schutzanforderungen ausreichend konkret beschrieben.
- Anforderungen besitzen beobachtbare Akzeptanzkriterien. Relevante Fehler-, Grenz- und Berechtigungsfälle sind beschrieben oder als offene Punkte erfasst.
- Blockierende Entscheidungen und Widersprüche sind für diesen Umfang geklärt. Verbleibende Lücken und ihr betroffener Umfang bleiben sichtbar.
- Noch benötigte reale Betriebsangaben werden als solche benannt und vor dem jeweils davon abhängigen Arbeitsschritt geklärt.
- Werte, die erst durch Messung am realen System entstehen, etwa Ressourcengrenzen oder Antwortzeiten, blockieren den Übergang nicht. Sie erhalten einen als Annahme gekennzeichneten Startwert mit nachvollziehbarer Grundlage, etwa einem Standard oder einer Herstellerangabe, und werden als Arbeitspaket „messen, dann festlegen“ geplant. Fehlt eine solche Grundlage, bleibt der Wert bis zur Messung offen.

### REQ-009 – Überprüfbare Arbeitspakete

Die Library muss aus der abgestimmten Spezifikation konkrete Arbeitspakete ableiten lassen.

**Akzeptanzkriterien:**

- Jedes Paket beschreibt Ziel, Umfang, relevante Spezifikationsstellen, Abhängigkeiten, Abnahmekriterien und geplante Prüfungen.
- Der Zuschnitt ermöglicht ein nachvollziehbar prüfbares Ergebnis.
- Jedes Arbeitspaket nennt seine Vorgänger und eine grobe Komplexität (klein, mittel, groß). Pakete mit Komplexität groß werden weiter geschnitten.
- Die fachliche Abdeckung und notwendige Ausführungsreihenfolge sind nachvollziehbar.
- Die Umsetzung benötigt keine stillschweigenden neuen Produkt-, Architektur- oder Sicherheitsentscheidungen.
- Ein Arbeitspaket zum Messen und Festlegen eines Werts übernimmt sein Ergebnis über den zuständigen Fachbeitrag in die Spezifikation (REQ-006).

### REQ-010 – Praktischer Leitfaden

Der Leitfaden muss den Benutzer durch Auswahl, Anwendung und Prüfung der Prompts führen.

**Akzeptanzkriterien:**

- Für jeden Arbeitsschritt sind Zweck und Zeitpunkt, Vorbereitung und Eingaben, erforderliche Entscheidungen, erwartete Ergebnisse und Prüfkriterien beschrieben.
- Der passende vollständige Prompt ist eindeutig auffindbar.
- Der Leitfaden erklärt den Umgang mit offenen Fragen und Widersprüchen sowie die Voraussetzungen für den nächsten Schritt.
- Wichtige Begriffe werden anwendungsbezogen und verständlich erklärt.
- Der Benutzer kann erkennen, welchen fachlichen Beitrag er gerade erarbeitet und wie dieser zur Gesamtspezifikation beiträgt.

## 5. Übergreifende Qualitätsanforderungen und Grenzen

### Q-001 – Allgemeine und angemessene Anwendung

Die Vorlagen müssen für Webprojekte allgemein verwendbar bleiben. Projektspezifische Funktionen, Technologien, Rollenrechte, regulatorische Pflichten und Betriebsmodelle werden aus dem jeweiligen Projekt hergeleitet.

Umfang und Dokumentation müssen zum Vorhaben passen. Feste Anzahlen von Fachrollen, Diagrammen, Akzeptanzkriterien, Reviewrunden oder Modellen sind keine allgemeinen Pflichten.

Für kleine Änderungen und Fehlerbehebungen beschreibt der Leitfaden einen kurzen Weg. Er lässt Schritte weg, deren Beitrag für den kleinen Umfang keinen Nutzen hat. Betroffene Anforderungen, Abnahmekriterien und Arbeitspakete werden trotzdem aktualisiert (REQ-006).

### Q-002 – Verlässliche Aussagen

Die Prompts dürfen keine Funktionen, Fakten, Entscheidungen, Rollenrechte, Standardskennungen oder Prüfergebnisse erfinden.

Fachliche Empfehlungen benötigen eine nachvollziehbare Grundlage. Fehlende reale Fakten werden gezielt erfragt oder offen ausgewiesen.

Spezifiziert, implementiert und tatsächlich geprüft bleiben unterscheidbar. Geplante Kommandos gelten nicht als vorhanden oder ausgeführt. Dokumentierte Sicherheitsregeln gelten nicht als technisch durchgesetzt.

### Q-003 – Konzentrierte Vorlagen

Die fertigen Promptvorlagen enthalten ausschließlich die für ihre Verwendung notwendigen Inhalte.

Es gibt keinen gemeinsamen Grundtext („COMMON CONTRACT“), der in jeden Prompt kopiert wird. Regeln aus Q-001 bis Q-005 gelten für das Ergebnis; jeder Prompt formuliert nur die Regeln, die er für seinen Auftrag braucht, in eigenen Worten und so knapp wie möglich.

Entstehungsgeschichte, Schulungsbezüge, PR-Herkunft, rekonstruierte Originalprompts und Änderungshistorien gehören nicht in die Vorlagen. Projektunterlagen zu lesen und fachliche Aussagen zu prüfen bleibt Bestandteil ihrer Arbeit.

### Q-004 – Kontrollierter Übergang zur Umsetzung

Die Fach- und Planungsaufträge erzeugen Spezifikationen und Pläne. Setup, Paketinstallation, Implementierung, Infrastrukturkäufe und Deployment benötigen einen entsprechenden eigenen Auftrag.

Der Leitfaden beschreibt, dass die anschließenden Schritte für Implementierung, Tests, Review und QA ihre Ergebnisse gegen die maßgebliche Spezifikation prüfen und tatsächliche Prüfergebnisse dokumentieren.

Veröffentlichungen, Pushes, Pull Requests und Nachrichten benötigen eine entsprechende Autorisierung.

### Q-005 – Prüfbare Qualitätsziele

Jedes übergreifende Qualitätsziel des Zielprojekts muss als Kette Ziel → Kriterium → Nachweis → Gate festgelegt werden. Der Fachprompt, der für das Qualitätsziel zuständig ist, erarbeitet die Kette und hält sie in seiner Fachdatei fest. Gemeinsame Vorgaben für alle Prompts enthalten keine Qualitätsziele.

Der Arbeitsschritt Agent-Anweisungen sammelt die Gates aus den Fachdateien und legt dafür konkrete Prüfkommandos fest. Arbeitspakete verweisen in ihren geplanten Prüfungen auf diese Gates.

Der Sicherheitsbeitrag formuliert zusätzlich kurze, imperative Sicherheitsregeln für den gewählten Technologiestack, die ein Agent beim Programmieren befolgt. Jede Regel nennt eine überprüfbare Quelle, etwa die OWASP Cheat Sheet Series oder die offizielle Dokumentation des eingesetzten Frameworks; eine Regel ohne Quelle wird nicht aufgenommen. Der Arbeitsschritt Agent-Anweisungen verweist je Aufgabenart auf diese Regeln, statt sie zu wiederholen.

### Q-006 – Standards als Default

Jeder Fachprompt legt für seinen Beitrag einen anerkannten Standard als Default fest und benennt ihn mit Version im Defaults-Feld des Eingabeblocks. Die Fachrolle verantwortet ihren Standard; es gibt keine übergreifende Standardliste, die für alle Prompts gilt. Der Default gilt auch für die inhaltlichen Entscheidungen des Beitrags: Inhaltliche Entscheidungen, die ein im Prompt genannter Standard oder das Vorgabendokument beantwortet, werden ohne Rückfrage übernommen. Entscheidungen ohne eine solche Quelle werden dem Benutzer mit einer Empfehlung nach dem anerkannten Standard des Fachgebiets vorgelegt; die Empfehlung muss die offene Frage schließen können. Abweichungen sind während der Erarbeitung erlaubt und werden mit Begründung als Entscheidung in der Fachdatei festgehalten; vorgesehen sind vor allem Absenkungen für kleinere Projekte, eine Verschärfung benötigt einen Projektgrund. Vorgaben aus einem eingebrachten Vorgabendokument (REQ-001) haben Vorrang vor dem Default. Ein Standard, der für das Projekt nicht zutrifft, etwa WCAG ohne Benutzeroberfläche, entfällt mit Begründung.

Defaults (Stand 16.10.2026):

| Beitrag | Default | Hinweis |
| --- | --- | --- |
| Anforderungen | EARS für Anforderungssätze, Gherkin für Abnahmekriterien | |
| Arbeitspakete | Abnahmekriterien als Gherkin | gleiches Kriterienformat wie bei den Anforderungen |
| Design | design.md-Format (google-labs-code), Status alpha 0.3.0 | Version pro Projekt festhalten |
| Architektur | arc42, schlank; Entscheidungen als MADR 4.0.0; Diagramme als Mermaid, nur bei Bedarf | bei kleinen Projekten nur nötige Abschnitte, Canvas |
| Sicherheit | OWASP ASVS 5.0, Stufe 2; Bedrohungsanalyse mit STRIDE | ASVS-Version nennen; Stufe 3 oder Abweichung nur begründet |
| Barrierefreiheit | WCAG 2.2 Stufe AA | nur bei Benutzeroberfläche |
| Recht | DSGVO bei Personenbezug von Personen in der EU; Lizenzprüfung für Projekt und Abhängigkeiten | keine Rechtsberatung; rechtliche Prüfung bleibt beim Menschen |
| Agent-Anweisungen | AGENTS.md, agentenneutral, mit kurzem Verweis für Agenten mit anderer Eingabedatei; bei mehreren Spezifikationsdateien je Aufgabenart ein Verweis auf die zu lesende Datei | Gates nach Q-005 als konkrete Kommandos |

### Q-007 – Form der Promptdateien

Jeder Prompt liegt in einer eigenen Markdown-Datei in `lib/`.

- **Dateinamen:** englisch, Kleinbuchstaben mit Bindestrich, nach Rolle oder Ergebnis benannt und ohne Nummern, zum Beispiel `security.md`. Die empfohlene Reihenfolge steht im Leitfaden. Die von den Prompts erzeugten Projektdateien behalten ihre üblichen Namen wie `REQUIREMENTS.md`.
- **Aufbau:** Oben steht ein kurzer deutscher Kopf mit Rolle, Zweck, Voraussetzungen, Eingaben und Ergebnisdatei, darunter genau ein englischer Prompt-Block zum Kopieren. Ausführliche Anleitungen stehen im Leitfaden.
- **Rollensatz:** Der Prompt-Block beginnt mit einem Satz, der Auftrag und Grenze der Rolle nennt, zum Beispiel: Act as the architecture contributor for this project; work only on the architecture and hand other topics back as open questions. Der Satz nennt keine Seniorität oder Expertenstufe.
- **Eingaben:** Direkt nach dem Rollensatz folgt ein Eingabeblock aus benannten Feldern mit Hinweis. Leere Felder sind erlaubt; fehlende Angaben klärt die KI gezielt oder benennt sie als Lücke. Der Eingabeblock enthält ein vorausgefülltes Feld mit den Defaults des Prompts (Standards mit Version). Der Benutzer kann sie vor dem Kopieren anpassen oder ersetzen; angepasste Werte gelten als seine Vorgabe.
- **Leitfaden:** Der Leitfaden steht in `lib/README.md`, zusammen mit der Prompt-Übersicht, und ist deutsch. Je Schritt nennt er Zeitpunkt in der empfohlenen Reihenfolge, nötige Entscheidungen und Prüfkriterien; die Prompts selbst bleiben eigenständig kopierbar.
- **Kennungen:** Beiträge verwenden stabile Kennungen: FR (Anforderung), AC (Abnahmekriterium), OQ (offene Frage), ADR (Architekturentscheidung), SEC (Sicherheitsanforderung), T (Test) und WP (Arbeitspaket). Eine Kennung wird nie neu vergeben; Verweise zwischen Beiträgen laufen über sie. Ein eigenes Klärungsprotokoll gibt es nicht: Klärungen stehen mit Begründung und Datum bei der offenen Frage (OQ) oder der Entscheidung (ADR).
- **Version:** Die neue Fassung beginnt unter dem Namen Idea to Spec mit Version 1.0. Die Version steht nur an einer Stelle, in `lib/README.md`, nicht in jedem Prompt.
- **Sprache:** Beschreibungen und Leitfaden sind deutsch, Anweisungen für Agenten (Prompts, AGENTS.md, CLAUDE.md) immer englisch. Im Gespräch spricht die KI die Sprache des Benutzers. Die Sprache der Projektdokumente wird einmal festgelegt, Standard ist die Sprache des Benutzers, und danach beibehalten. Kennungen, Dateinamen und Code sind immer englisch.

## 6. Maßstab für die Zielerreichung

Die Library erfüllt ihr Kernziel, wenn der Benutzer:

1. mit einer Projektidee beginnen kann;
2. die benötigten Fachbeiträge über die angebotenen Prompts erarbeiten und in Projektdateien festhalten kann;
3. die Arbeit in einer neuen Session anhand dieser Dateien fortsetzen kann;
4. die Beiträge zu einer konsistenten, ausreichend geklärten Spezifikation zusammenführen kann;
5. daraus überprüfbare Arbeitspakete als Grundlage der Entwicklung erhält.

Als erreicht gilt nur, was tatsächlich angewendet wurde. Nicht angewendete Module und nicht ausgeführte Prüfungen bleiben ungeprüft.

Ein Testlauf der Library verwendet ein festgelegtes Zielbild und bewertet Weg und Ergebnis mit schriftlich festgelegten, gleichbleibenden Prüfpunkten: Reihenfolge der Schritte, Fragen an den Benutzer, festgehaltene Entscheidungen, Rückprüfung, Einbindung der Sicherheit, Prüfbarkeit der Anforderungen und Umsetzbarkeit der Arbeitspakete. Der erste bewertete Lauf bildet die Vergleichsbasis. Eine geänderte Promptfassung wird mit der vorherigen verglichen und nur übernommen, wenn das Ergebnis nicht schlechter wird. Modell und Modellversion werden je Lauf festgehalten; nach einem Modellwechsel wird erneut getestet. Kleine Abweichungen zwischen Läufen sind zu erwarten; ist der Unterschied zur vorherigen Fassung knapp, wird der Lauf wiederholt, bevor entschieden wird. Antwortet eine KI anstelle des Benutzers, wird der Lauf als automatischer Lauf gekennzeichnet; ihre Antworten gelten nicht als Entscheidungen des Benutzers. Die Bewertung eines Laufs prüft ein Mensch. Optional kann ein zweites Modell den Lauf zusätzlich prüfen.
