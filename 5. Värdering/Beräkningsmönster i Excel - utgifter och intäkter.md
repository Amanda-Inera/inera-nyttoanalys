# Beräkningsmönster i Excel: utgifter och intäkter

## Räkna på förändrade utgifter och intäkter

Jämför den årliga utgiften eller intäkten i Alternativ A och Alternativ B när du känner till totalvärdena. Bygg i stället upp beräkningen från antal händelser och värdet per händelse när totalvärden saknas.

Redovisa minskade utgifter och ökade intäkter som finansiella nyttor. Redovisa ökade utgifter och minskade intäkter som finansiella kostnader.

## Jämför en extern utgift mellan alternativen

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Årlig utgift i Alternativ A, kronor | [värde] | Avtal eller ekonomidata |
| Årlig utgift i Alternativ B, kronor | [värde] | Offert, avtal eller uppskattning |
| Minskad utgift per år, kronor | `=[utgift i A]-[utgift i B]` | Beräkning |
| Årligt värde (kr) | `=[minskad utgift]` | Beräkning |

Om utgiften ökar använder du **utgift i Alternativ B minus utgift i Alternativ A** och lägger värdet som en kostnad. Om Alternativ A saknar utgiften kan du använda hela utgiften i Alternativ B som kostnad.

## Välj upplägg när utgifter upphör och nya tillkommer

Använd en differens när det är klarlagt att förändringen ökar eller minskar utgiften. Med 2 miljoner kronor i Alternativ A och 3 miljoner i Alternativ B redovisar du exempelvis 1 miljon som ökad kostnad.

Om riktningen är osäker kan du särredovisa utgifter som faktiskt upphör i Alternativ B som en finansiell nytta och utgifter som tillkommer i Alternativ B som en finansiell kostnad. Använd separata N- och K-block och anpassa årsprofilen till när respektive förändring sker. Räkna bara den del av A-utgiften som faktiskt försvinner. En utgift som kvarstår är ingen besparing.

Räkna inte samma besparing både som nytta och som avdrag i kostnadsblocket. Dokumentera valet av upplägg: särredovisning och differens ger samma nettonytta för samma belopp och årsprofiler, men olika summor av nyttor och kostnader och därmed olika nettonytta per satsad krona. Använd en konsekvent redovisningsprincip för jämförbara utgifter i analysen.

## Beräkna fler eller färre kostsamma händelser

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Förändrat antal händelser per år | [värde] | Statistik eller uppskattning |
| Kostnad per händelse, kronor | [värde] | Ekonomidata eller uppskattning |
| Årligt värde (kr) | `=[förändrat antal händelser]*[kostnad per händelse]` | Beräkning |

Färre händelser ger en nytta och fler händelser ger en kostnad. Ta bara med de utgifter eller den arbetstid som faktiskt förändras när händelsen inträffar eller undviks.

## Beräkna en förändrad intäkt

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal enheter per år | [värde] | Statistik eller prognos |
| Förändrad intäkt per enhet, kronor | [värde] | Ekonomidata eller uppskattning |
| Årligt värde (kr) | `=[antal enheter]*[förändrad intäkt per enhet]` | Beräkning |

En ökad intäkt är en finansiell nytta och en minskad intäkt är en finansiell kostnad. Använd inte beräkningen för frigjord arbetstid eller andra värden som inte innebär en faktisk intäkt.

## Beräkna en extern utgift per person eller enhet

| Faktor | Troligt | Källa |
| --- | --- | --- |
| Antal personer eller enheter | [värde] | Planering, statistik eller avtal |
| Utgift per person eller enhet, kronor | [värde] | Offert eller avtal |
| Årligt värde (kr) | `=[antal]*[utgift per person eller enhet]` | Beräkning |

Beräkna deltagarnas arbetstid, resor och andra kostnader separat om de också förändras.