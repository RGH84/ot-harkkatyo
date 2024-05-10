### Changelog

## Viikko 3

- Lisätty Users-luokka, joka vastaa käyttäjistä
- Lisätty HouseDiaryService-luokka, joka vastaa käyttöliittymästä
- Lisätty UserRepository-luokka, joka vastaa käyttäjien tietojen tallentamisesta tietokantaan
- Lisätty HouseDiary luokka, joka vastaa käyttöliittymästä sovelluksen alkutaipaleella
- Lisätty TestHouseDiaryService, joka vastaa tällä hetkellä HouseDiaryServicen testaamisesta
- Lisätty SQLite tietokannat käyttö/testi, joissa tällä hetkellä ainoastaan käyttäjätiedot
- Käyttäjä voi tehdä tunnuksen, kirjautua sisään/ulos ja tarkastaa muut käyttäjänimet
- Testattu pytestillä ohjelman tämän hetkinen toiminta
- Toiminta testattu Cubbli Linuxissa

## Viikko 4

- Lisätty UnscheduledTask-luokka, joka vastaa aikatauluttomista tehtävistä
- Lisätty UnscheduledTaskRepository-luokka, joka vastaa aikatauluttomien tehtävien tallentamisesta tietokantaan
- Lisätty uusia toimintoja, aikatauluttomien tehtävien luonti, merkitseminen tehtyiksi ja tehtävien poistaminen
- Luotu uusille toiminnoille testit ja testattu toiminta
- Lisätty riippuvuuksiksi pylint ja autopep8, koodin laatua on paranneltu

## Viikko 5

- Lisätty ScheduledTask-luokka, joka vastaa aikataulutetuista tehtävistä
- Lisätty ScheduledTaskRepository-luokka, joka vastaa aikataulutettujen tehtävien tallentamisesta tietokantaan
- Lisätty uusia toimintoja, aikataulutettujen tehtävien luonti, merkitseminen tehtyiksi ja tehtävien poistaminen
- Luotu uusille toiminnoille testit ja testattu toiminta

## Viikko 6

- Lisätty UI-luokka, joka vastaa graafisesta käyttöliittymästä sekä sen näkymäluokat
- Poistettu tekstipohjainen käyttöliittymä
- Lisätty docstringejä
- Korjattu tehtävien "tehty" ajan ilmaiseminen

## Lopullinen palautus

- Lisätty ominaisuus, kun aikataulutetun tehtävän merkitsee tehdyksi, kysyy ohjelma tehdäänkö tehtävä uudelleen
- Lisätty tietokantojen nimeämisen konfiguroinnin mahdollisuus .env tiedoston kautta
- Lisätty docstringejä
- Dokumentaatiota päivitetty


