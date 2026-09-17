# Beräkningsmönster i Excel: personaltid

## Räkna på personaltid utifrån de tidsuppgifter du har

Jämför tidsåtgången i Alternativ A och Alternativ B när båda går att uppskatta. Beräkna den förändrade tiden direkt om skillnaden redan är känd. För utveckling, införande, utbildning samt drift och förvaltning utgår du från hur tiden uppstår.

Beräkna förändringen i timmar per år och multiplicera därefter med en lokal timkostnad eller en relevant faktor från **Ineras kalkylfaktorer**. Ett positivt värde för minskad personaltid är en omfördelningsnytta. Ett positivt värde för ökad personaltid är en omfördelningskostnad.

## Jämför tidsåtgången mellan Alternativ A och Alternativ B

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal händelser per år | [värde] | [källa] |
| Tid per händelse i Alternativ A, minuter | [värde] | [källa] |
| Tid per år i Alternativ A, timmar | `=[antal händelser]*[minuter]/60` | Beräkning |
| Tid per händelse i Alternativ B, minuter | [värde] | [källa] |
| Tid per år i Alternativ B, timmar | `=[antal händelser]*[minuter]/60` | Beräkning |
| Förändrad tid per år, timmar | `=[tid i A]-[tid i B]` | Beräkning |
| Timkostnad, kronor | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Årligt värde (kr) | `=[förändrad tid]*[timkostnad]` | Beräkning |

Om tidsåtgången i Alternativ A är noll kan du använda hela tidsåtgången i Alternativ B som förändringen och lägga värdet som en kostnad.

## Beräkna en känd tidsförändring

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal berörda personer | [värde] | [källa] |
| Antal händelser per person och år | [värde] | [källa] |
| Förändrad tid per händelse, minuter | [värde] | [källa] |
| Förändrad tid per år, timmar | `=[personer]*[händelser]*[minuter]/60` | Beräkning |
| Timkostnad, kronor | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Årligt värde (kr) | `=[förändrad tid]*[timkostnad]` | Beräkning |

Anpassa faktorerna om tiden anges per vecka, månad eller organisation.

## Beräkna personaltid för utveckling och införande

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal medarbetare | [värde] | Planering eller uppskattning |
| Årsarbetstid per medarbetare, timmar | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Andel av året | [värde] | Planering eller uppskattning |
| Andel av arbetstiden | [värde] | Planering eller uppskattning |
| Total arbetstid, timmar | `=[medarbetare]*[årsarbetstid]*[andel av året]*[andel av arbetstiden]` | Beräkning |
| Timkostnad, kronor | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Årligt värde (kr) | `=[total arbetstid]*[timkostnad]` | Beräkning |

## Beräkna personaltid för utbildning

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal deltagare | [värde] | Planering eller uppskattning |
| Utbildningstid per deltagare, timmar | [värde] | Utbildningsplan eller uppskattning |
| Total utbildningstid, timmar | `=[deltagare]*[utbildningstid]` | Beräkning |
| Timkostnad, kronor | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Årligt värde (kr) | `=[total utbildningstid]*[timkostnad]` | Beräkning |

Beräkna olika personalgrupper var för sig om de har olika timkostnader. Beräkna kursavgifter, resor och andra externa utgifter separat om de också förändras.

## Beräkna personaltid för drift och förvaltning

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Arbetstid per månad, timmar | [värde] | Planering eller uppskattning |
| Arbetstid per år, timmar | `=[timmar per månad]*12` | Beräkning |
| Timkostnad, kronor | [värde] | Lokal uppgift eller Ineras kalkylfaktorer |
| Årligt värde (kr) | `=[arbetstid per år]*[timkostnad]` | Beräkning |

Beräkna bara den arbetstid som förändras jämfört med Alternativ A. Lägg engångsinsatser för utveckling och införande i en separat kostnad om de följer en annan utveckling över tid.