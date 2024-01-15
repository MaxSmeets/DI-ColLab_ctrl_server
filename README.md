# DI-ColLab_ctrl_server
Een test opzet die meerdere clients ondersteund en async communicatie.

## Hoe moet da?
Start de server, open meerdere browser instanties, je ziet in de console nu meerdere berichten komen met hierin het volgende staan: C,User.
Dit is een welkomstbericht en laat aan de server weten dat er een nieuwe user moet worden ingespawnd.
Als je vervolgens op de letter 'w' duwt in de browser omgeving, zul je zien dat er het volgende bericht wordt gestuurd naar de server:
U,User,Coordinaten. Dit is een update van een specifieke speler zijn coordinaten. Om aan te tonen dat de server ook dit ondersteund.
Je zult ook zien dat zowel de instantie waarin je de letter w in duwt een bericht op het scherm krijgt, maar alle andere instanties krijgen ook een update over jouw coordinaten.
