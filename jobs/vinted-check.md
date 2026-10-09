# Job: Vinted-Check (low token, standardisiert)

Modell: haiku/sonnet-klein. Ziel: neue Vinted-Angebote prüfen und kurz bewerten.

## Ablauf
1. `python3 -I jobs/vinted_fetch.py` ausführen: ruft die Suchen aus `jobs/suchen.txt` ab (nur Seite 1, max. 20 Treffer, Kategorie Objektive, Titelfilter). Bei 403 wiederholt das Skript selbst; Vinted braucht einen Browser-User-Agent, die Domain `www.vinted.de` muss freigegeben sein. Priorität: erst Tele, dann Makro.
2. Pro Treffer nur extrahieren: Titel, Preis, Zustand, Link. Keine Beschreibungen/Bilder laden, außer Treffer ist Kandidat.
3. Gegen `jobs/bewertung.md` bewerten.
4. Ergebnis anhängen an `jobs/ergebnisse/YYYY-MM-DD.md`, nur Treffer mit Urteil ✅ oder 🤔. Bereits gemeldete Links (in früheren Ergebnissen) überspringen.
5. Commit + Push auf den Arbeitsbranch.

## Ausgabeformat (je Treffer, eine Zeile)
`✅|🤔 | Modell | Preis | Zustand | Link | 1 Satz Begründung`
