# Vaatimusmäärittely 

## Sovelluksen tarkoitus 

Tämä sovellus on suunniteltu helpottamaan omakotitalojen ylläpitoa tarjoamalla käyttäjille mahdollisuuden luoda ja hallita henkilökohtaista huoltopäiväkirjaa. Sovellus palvelee erityisesti pientaloasujia. Se on kuitenkin käyttökelpoinen kaiken tyyppisten kiinteistöjen ylläpidossa. Jokainen rekisteröitynyt käyttäjä saa käyttöönsä oman huoltopäiväkirjan, mikä tekee kodin huoltotoimenpiteiden seurannasta ja suunnittelusta vaivatonta.  

## Käyttäjät 

Tällä hetkellä sovellus tukee yhtä käyttäjätyyppiä, _normaali käyttäjä_, joka pääsee hyödyntämään kaikkia perustoimintoja. Tulevaisuudessa käyttäjärooleja saatetaan laajentaa toteuttamalla _pääkäyttäjä_, jolle annetaan laajemmat oikeudet. 

## Sovelluksen toiminnot 

### Ennen kirjautumista 

- Käyttäjä voi luoda sovellukseen käyttäjätunnuksen ja salasanan 
	- Käyttäjätunnuksen tulee olla ainutlaatuinen ja sen pituuden on oltava vähintään 3 merkkiä 
 	- Salasanan pituuden tulee olla vähintään 4 merkkiä 
	- Järjestelmä ilmoittaa, jos käyttäjätunnus on jo käytössä, tai pituudet ovat väärin 
- Käyttäjä voi kirjautua sisään luotuaan onnistuneesti käyttäjätunnuksen ja salasanan 
	- Järjestelmä ilmoittaa, mikäli käyttäjätunnusta ei löydy tai salasana on virheellinen 

### Kirjautumisen jälkeen 

- Käyttäjä tulee etusivulle, jossa on linkit tehdyt _aikatauluttomat_ ja _aikataulutetut tehtävät_ sivuille sekä molempien sivujen tekemättömät huoltotoimenpiteet listattuna

- Etusivulla voit:
  	- Lisätä uusia huoltotoimenpiteitä, jotka tulevat näkyviin etusivulle
  	- Merkitä huoltotoimenpiteitä tehdyksi, jolloin ne siirtyvät näkyviin omille sivuillensa
  	- Uusia aikataulutettuja tehtäviä
- Tehdyt sivuilla voit: 
	- Tarkastella tekemiäsi huoltotoimenpiteitä
 	- Poistaa jo tehtyjä huoltotoimenpiteitä
	
## Jatkokehitysideoita 

- Käyttöliittymän käyttökokemuksen ja visuaalisuuden parannus
- Huoltotoimenpiteiden muokkaaminen
- Toimenpiteet voi jakaa omiin ryhmiin, esim. IV- kone, ilmalämpöpumput, ulkotyöt, nuohous ym
- Käyttöliittymän muuttaminen esimerkiksi web-sovellukseksi mahdollistaisi sen käytön missä tahansa. Aion todennäköisesti jatkaa kehitystä tähän suuntaan omalla ajallani.

