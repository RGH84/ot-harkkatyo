# Arkkitehtuurikuvaus

## Sovelluslogiikka

Pakkausrakenne ja luokat:

![Pakkausrakenne ja luokat](./kuvat/pakkauskaaviotoka.png)

## Päätoiminnalisuudet

### Kirjautuminen

Käyttäjä on jo luonut tunnuksen ja salasanan. Käyttäjä antaa komennon 3. Sovellus etenee tästä seuraavanlaisesti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant HouseDiaryService
  participant UserRepository
  User->>UI: command = "3"
  UI->>HouseDiaryService: login("Juho", "1919")
  HouseDiaryService->>UserRepository: find_by_username("Juho")
  UserRepository-->>HouseDiaryService: user
  HouseDiaryService-->>UI: user
  UI->UI: _login()
```
Käyttäjä kirjoittaa käyttäjätunnuksensa ja salasanansa, minkä jälkeen käyttöliittymä pyytää HouseDiaryService-palvelulta kirjautumista. Tämä palvelu tarkistaa UserRepositoryn avulla, ovatko annetut tunnus ja salasana oikein. Mikäli kirjautuminen onnistuu, HouseDiaryService välittää käyttäjätiedot takaisin käyttöliittymään, joka päivittyy näyttämään kirjautumisen jälkeisen käyttöliittymän.

### Aikatauluttoman tehtävän luominen

Kun käyttäjä on kirjautunut sisään ja valinnut komennon 1, sovellus toimii seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant HouseDiaryService
  participant UnscheduledTaskRepository
  participant UnscheduledTask
  User->>UI: command = "1"
  UI->>HouseDiaryService: create_u_task("Maalaa seinät")
  HouseDiaryService->>UnscheduledTask: UnscheduledTask("Maalaa seinät", Juho)
  HouseDiaryService->>UnscheduledTaskRepository: create_new_u_task(u_task)
  UnscheduledTaskRepository-->>HouseDiaryService: u_task
  HouseDiaryService-->>UI: u_task 
  UI->>UI: Tehtävä luotu onnistuneesti
```
UnscheduledTask saa myös muita tietoja, kuten luontiajan, muita tietoja ei tässä yhteydessä käsitellä tarkemmin. Kun tehtävä on onnistuneesti luotu, käyttöliittymä ilmoittaa tästä käyttäjälle ja päivittää tehtävälistan, kun käyttäjä antaa asianmukaisen komennon.
