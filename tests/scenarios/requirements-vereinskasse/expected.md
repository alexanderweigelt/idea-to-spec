# Lösungsblatt – nur für den Richter, nach dem Lauf

Szenario: Belege-App für einen Sportverein. Die Eingabe enthält zwei Fallen. Die getestete KI muss beide ungefragt ansprechen, bevor sie die betroffene Entscheidung festschreibt ([AC-DIALOG-13]), mit Empfehlung ([AC-DIALOG-16]) und sofort, nicht erst am Ende ([AC-DIALOG-17]).

## T1 – Grenze der Plattform: PWA im App Store
Eine reine Web-App (PWA) lässt sich nicht einfach in Apples App Store stellen. Sie braucht eine native Hülle, und Apple lehnt Apps ab, die nur eine Website verpacken (Richtlinie zu Mindestfunktionen). Bei Google Play geht es über eine Trusted Web Activity leichter.
Erwarteter Befund: Die KI weist darauf hin, dass „PWA“ und „im App Store“ nicht ohne Weiteres zusammenpassen, und empfiehlt einen Weg (z. B. ohne App Store starten und die Web-App über einen Link verteilen, oder eine native Hülle mit Mehraufwand einplanen, oder eine Machbarkeitsprobe).
Nicht bestanden: Die KI übernimmt „im App Store“ als Anforderung, ohne den Konflikt zu nennen.
Warnwörter: Richtlinie, Guideline, abgelehnt, Ablehnung, Wrapper, Hülle, nativ, native, Capacitor, Review, Mindestfunktion

## T2 – Rechtliche Folge: Belegfotos bei einem Dienst außerhalb der EU
Belegfotos enthalten personenbezogene Daten (Name, Bankdaten, Kaufort). Google Cloud Vision verarbeitet sie bei einem US-Anbieter. Das erfordert Datenschutz-Prüfung (DSGVO: Auftragsverarbeitung, Übermittlung in ein Drittland oder EU-Region wählen).
Erwarteter Befund: Die KI spricht den Datenschutz bei der Texterkennung an und empfiehlt etwas (z. B. EU-Region oder Verarbeitung auf dem Gerät, oder den Legal-Prompt vor Design und Architektur). Ein Verweis auf den Legal-Prompt mit konkretem Grund genügt.
Nicht bestanden: Die KI übernimmt Google Cloud Vision, ohne den Datenschutz zu nennen.
Warnwörter: DSGVO, GDPR, Datenschutz, Drittland, USA, personenbezogen, Auftragsverarbeitung, AVV, EU-Region, Privacy
