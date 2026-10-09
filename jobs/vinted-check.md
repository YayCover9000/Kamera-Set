# Job: Vinted-Check (low token, standardisiert)

Modell: haiku/sonnet-klein. Ziel: neue Vinted-Angebote prüfen und kurz bewerten.

## Ablauf
1. Suchen aus `jobs/suchen.txt` abrufen (nur Seite 1, max. 20 Treffer je Suche).
2. Pro Treffer nur extrahieren: Titel, Preis, Zustand, Link. Keine Beschreibungen/Bilder laden, außer Treffer ist Kandidat.
3. Gegen `jobs/bewertung.md` bewerten.
4. Ergebnis anhängen an `jobs/ergebnisse/YYYY-MM-DD.md`, nur Treffer mit Urteil ✅ oder 🤔. Bereits gemeldete Links (in früheren Ergebnissen) überspringen.
5. Commit + Push auf den Arbeitsbranch.

## Ausgabeformat (je Treffer, eine Zeile)
`✅|🤔 | Modell | Preis | Zustand | Link | 1 Satz Begründung`
