# FR-SPEC-04 – Einheitliches Dokumentgerüst
Owner: REQUIREMENTS.md · Group: SPEC · Status: confirmed
## Statement
Jedes Dokument muss dem Gerüst folgen, das sein Prompt vorgibt (Zuständigkeit oben, Inhalt nach Themengruppen, Katalog mit ID, Gruppe, Titel und Status Entwurf/bestätigt sowie offene Fragen am Ende, Verweise als Link, dessen sichtbarer Text nur die ID ist), ausgenommen AGENTS.md.
## Rationale
source: user
## Acceptance criteria
### AC-SPEC-07
```gherkin
Given ein Dokument außer AGENTS.md
When man seine Gliederung prüft
Then folgen Zuständigkeit, Themengruppen, Katalog und offene Fragen in dieser Reihenfolge.
```
### AC-SPEC-08
```gherkin
Given ein Katalog
When man seine Spalten prüft
Then sind es ID, Gruppe, Titel und Status mit den Werten Entwurf oder bestätigt.
```
### AC-SPEC-09
```gherkin
Given ein beliebiger Verweis
When man ihn liest
Then ist er ein Link, dessen sichtbarer Text nur die ID ist.
```
### AC-SPEC-10
```gherkin
Given AGENTS.md
When man sie prüft
Then ist sie eine Gebrauchsanweisung ohne Katalog, und Offenes steht als OQ im Fachdokument.
```
## Failure cases in real use
- keine benannt
## References
[FR-SPEC-05](FR-SPEC-05.md)
