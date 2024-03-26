# Vaatimusmäärittely 

## Sovelluksen tarkoitus 

Tämä sovellus on suunniteltu helpottamaan omakotitalojen ylläpitoa tarjoamalla käyttäjille mahdollisuuden luoda ja hallita henkilökohtaista huoltopäiväkirjaa. Sovellus palvelee erityisesti pientaloasujia. Se on kuitenkin käyttökelpoinen kaiken tyyppisten kiinteistöjen ylläpidossa. Jokainen rekisteröitynyt käyttäjä saa käyttöönsä oman huoltopäiväkirjan, mikä tekee kodin huoltotoimenpiteiden seurannasta ja suunnittelusta vaivatonta.  

## Käyttäjät 

Alkuvaiheessa sovellus tukee yhtä käyttäjätyyppiä, _normaali käyttäjä_, joka pääsee hyödyntämään kaikkia perustoimintoja. Tulevaisuudessa käyttäjärooleja saatetaan laajentaa toteuttamalla _pääkäyttäjä_, jolle annetaan laajemmat oikeudet. 

## Suunnitellut toiminnallisuudet 

### Ennen kirjautumista 

- Käyttäjä voi luoda sovellukseen käyttäjätunnuksen ja salasanan 
	- Käyttäjätunnuksen tulee olla ainutlaatuinen ja pituuden on oltava vähintään 3 merkkiä, salasanan pituus on oltava vähintään 4 merkkiä  
	- Järjestelmä ilmoittaa, jos käyttäjätunnus on jo käytössä, tai pituudet ovat väärin
- Käyttäjä voi kirjautua sisään luotuaan onnistuneesti käyttäjätunnuksen ja salasanan 
	- Järjestelmä ilmoittaa, mikäli käyttäjätunnusta ei löydy tai salasana on virheellinen 

### Kirjautumisen jälkeen 

- Käyttäjä tulee etusivulle, jossa on linkit _Huoltotoimenpiteet_ ja _Aikataulutetut huoltotoimenpiteet_ sivuille sekä molempien sivujen tekemättömät huoltotoimenpiteet listattuna 
- _Huoltotoimenpiteet_ sivulla: 
	- Näet tekemäsi huoltotoimenpiteet 
	- Pystyt lisäämään tekemättömän huoltotoimenpiteen, joka tulee näkyviin etusivulle 

- _Aikataulutetut huoltotoimenpiteet_ sivulla: 
	- Näet tekemäsi aikataulutetut huoltotoimenpiteet 
	- Pystyt lisäämään tekemättömän aikataulutetun huoltotoimenpiteen, joka tulee näkyviin etusivulle 
	- Aikataulutetussa huoltotoimenpiteessä tulee merkitä aika, mihin mennessä se pitäisi tehdä 

- Etusivulta voi merkitä huoltotoimenpiteitä tehdyksi, jolloin ne siirtyvät näkyviin omille sivuillensa 

## Jatkokehitysideoita 

- Huoltotoimenpiteiden muokkaaminen ja poistaminen 
- Aikataulutettujen huoltotoimenpiteiden automatisointi, sovellus osaa ehdottaa uutta aikaa seuraavalle huollolle, merkittäessä aikataulutettua huoltotoimenpidettä valmiiksi
- Toimenpiteet voi jakaa omiin ryhmiin, esim. IV- kone, ilmalämpöpumput, ulkotyöt, nuohous ym.
- Muutakin toiminnalisuutta voi tulla, jos aikaa jää

