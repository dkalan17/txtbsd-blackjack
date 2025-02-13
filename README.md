# txtbsd-blackjack
Text-based blackjack

## Opis projekta
To je preprosta verzija igre Blackjack, napisana v Pythonu, kot del seminarske naloge za splošno maturo iz informatike. Projekt omogoča igranje igre med igralcem in računalniškim delivcem, pri čemer so upoštevana osnovna pravila Blackjacka.

## Zahteve
Za zagon igre potrebujete:
- Python 3.x

Dodatne knjižnice niso potrebne, saj igra uporablja le standardne Pythonove knjižnice.


## Pravila igre
- Igralec in delivec začneta z dvema kartama.
- Cilj igre je doseči vsoto kart čim bližje 21, ne da bi jo presegli.
- Igralec lahko izbere „Hit” (vzame dodatno karto) ali „Stand” (obdrži trenutno kombinacijo kart).
- Delivec mora vleči karte, dokler ne doseže vsaj 17 točk.
- Če igralec preseže 21, izgubi igro.
- Če delivec preseže 21 ali ima igralec več točk kot delivec, igralec zmaga.

## Struktura kode
Glavne komponente programa:
- `blackjack.py`: glavna skripta za zagon igre
- `deck.py`: modul, ki upravlja s kompletom kart
- `player.py`: modul, ki vsebuje logiko igralca in delivca
- `game.py`: glavni mehanizem igre

## Avtor
**Ime:** [Domen Kalab]  
**Datum:** [17.4.2024]



