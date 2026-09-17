# Beräkningsmönster i Excel: kostnader och nyttor över tid

## Lägg en engångskostnad på rätt år

Lägg in hela engångskostnaden som **Årligt värde (kr)** och använd raden **Faktor** för att ange vilket år kostnaden uppstår:

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Engångskostnad, kronor | [värde] | Offert, avtal eller uppskattning |
| Årligt värde (kr) | `=[engångskostnad]` | Beräkning |

Sätt faktorn till `1` för året då kostnaden uppstår och till `0` för övriga år.

## Räkna om en månads- eller licenskostnad till årlig kostnad

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Månadskostnad, kronor | [värde] | Avtal eller offert |
| Årlig kostnad, kronor | `=[månadskostnad]*12` | Beräkning |
| Årligt värde (kr) | `=[årlig kostnad]` | Beräkning |

För en licenskostnad multiplicerar du antalet licenser med priset per licens och år. Om priset anges per månad multiplicerar du även med 12. Lägg en grundavgift, startavgift eller införandekostnad separat om den följer en annan utveckling över tid.

## Trappa upp en nytta eller kostnad över tid

Beräkna först det fulla årliga värdet och använd raden **Faktor** för att ange hur stor del som uppstår varje år. En successiv upptrappning kan exempelvis se ut så här:

| År | 1 | 2 | 3 | 4 och framåt |
| --- | --- | --- | --- | --- |
| Faktor | 0,25 | 0,5 | 0,75 | 1 |

Låt faktorn beskriva införandetakt, användning eller realisering, inte inflation eller framtida prisökningar.

## Räkna en del av det årliga värdet första året

Använd en faktor under `1` när nyttan eller kostnaden börjar under pågående år. Om den börjar vid halvår kan faktorn vara `0,5` första året och `1` följande år. Använd exempelvis `0,25` om ungefär en fjärdedel av det fulla årsvärdet ska räknas första året.

Utgå från när nyttan eller kostnaden faktiskt börjar, inte automatiskt från kalenderårets mitt.

## Avsluta en nytta eller kostnad när den upphör

Ändra faktorn till `0` från och med det år då nyttan eller kostnaden inte längre uppstår. En kostnad som gäller under de två första åren har exempelvis faktor `1` år 1 och 2 samt `0` från år 3.

Lägg nyttor eller kostnader som fortsätter efter införandet i separata beräkningsblock om de följer en annan utveckling över tid.