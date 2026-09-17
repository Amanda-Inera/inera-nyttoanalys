# Excelguide – läkemedelsautomater

# Excelguide – läkemedelsautomater

Syfte: Beskriva Excelmallens fältlogik, fältordning, analysspecifika kunskap och kontrollpunkter för läkemedelsautomater.

## 1. Analysens ram

### Jämförelse

- **Alternativ A:** Personal besöker brukaren fysiskt för att ge läkemedel.
- **Alternativ B:** Brukaren använder en läkemedelsautomat för läkemedelsgivningen, så att besök eller delar av besök som enbart behövs för läkemedelsgivning kan tas bort.

### Avgränsning

- Analysen gäller användning av läkemedelsautomater för brukare med läkemedelsgivning, där automaten gör att vissa fysiska besök kan tas bort.
- Ett helt besök ska bara räknas bort när alla moment i besöket försvinner eller kan samplaneras på annat sätt. Besök med andra nödvändiga insatser ska inte automatiskt räknas bort.
- Om personal fortfarande behöver vara på plats vid varje läkemedelstillfälle behöver jämförelsen och besöksnyttan kontrolleras.
- Analysen omfattar hyra för läkemedelsautomater, förändringsledning, utbildning, installation och information samt drift och support. Om den lokala lösningen har en annan kostnadsmodell behöver kostnadsblocken och avgränsningen kontrolleras.

### Vad som främst driver resultatet

- antalet brukare med läkemedelsgivning och andelen som kan ha läkemedelsautomat,
- hur många besök per brukare och dag som faktiskt kan tas bort,
- tidsåtgången för de besök som tas bort, inklusive resor,
- andelen besök med bil, körsträcka och andra färdsätt,
- hyran per läkemedelsautomat,
- lokala antaganden om arbets- och schemaplanering samt läkemedelsavvikelser,
- omfattningen av förändringsledning, utbildning, installation, information, drift och support.

Den största värderade nyttan är ofta frigjord personaltid, medan den finansiella nyttan främst består av minskade drivmedelskostnader. Tekniken skapar inte nyttan på egen hand: den behöver följas av ändrade arbetssätt för urval av brukare, planering, samordning av insatser och hantering av larm och avvikelser. Kvalitetsnyttor ska därför behållas i helhetsbilden även när de inte värderas i pengar.

## 2. Fältguide

Följ den gemensamma guidens regler för status, guidningsordning, källor, periodgenomsnitt och hantering av grå fält. Tomma reservblock för egna nyttor och kostnader ingår inte i den ordinarie guidningen.

### Flik: Nyttokalkyl start

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| — | Namn på förändringen | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med `Användning av läkemedelsautomater`. | Om användaren beskriver en annan teknik eller en lösning där läkemedelsautomaten inte minskar fysiska besök: kontrollera om rätt referensmall används. |
| — | Vilket år vill ni räkna från? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Följ den gemensamma regeln för startår. | — |
| — | Diskonteringsränta | Grått | Förklara vid behov – ingen inmatning | Förinställd på 3 %. Förklara diskontering kort om användaren frågar. Fältet är låst och ska inte ändras i guidningen. | — |
| Lista intressenterna | <Kommunens namn> | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Platshållaren är inte ett giltigt värde. Ersätt den med den aktuella kommunens namn. Kommunnamnet återanvänds automatiskt på andra flikar. | — |
| Lista intressenterna | Brukare; Personal; Samhället | Grått | Förklara vid behov – ingen inmatning | Förifyllda och låsta intressenter. | Om användaren behöver lägga till breda nya intressenter: kontrollera om referensmallen fortfarande passar. |

### Flik: Räkna på nyttor

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Faktorer som används i flera beräkningar / Antal läkemedelsautomater | Hur många brukare har läkemedelsgivning i kommunen? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokal verksamhetsstatistik eller annat lokalt underlag för de brukare som omfattas av läkemedelsgivning. Antalet påverkas bland annat av kommunens storlek och av hur samarbetet med primärvården kring övertagande till kommunal hemsjukvård har sett ut. Ge inget generellt antal. | Kontrollera att antalet avser den målgrupp som analysen gäller och inte alla brukare i hemtjänsten eller kommunen. |
| Faktorer som används i flera beräkningar / Antal läkemedelsautomater | Hur stor andel av dem tror ni skulle kunna ha läkemedelsautomater? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 65 %. SKR Kompetenscenter har sett nivån i arbetet med kommuner som använder läkemedelsautomater. Den beskriver en möjlig potential på sikt, inte en självklar startnivå. Bedöm ett rimligt periodgenomsnitt utifrån lokal målgrupp och införandetakt. | Om 65 % används direkt: kontrollera att det är ett rimligt genomsnitt för hela analysperioden och inte bara en möjlig nivå på sikt. En andel över 65 % kräver stark lokal motivering. Vid mycket låg andel: fråga vad som begränsar införandet. Konstruera inte generella förklaringar till kommunens målgrupp om lokalt underlag saknas. |
| Faktorer som används i flera beräkningar / Antal läkemedelsautomater | Antal läkemedelsautomater | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen utifrån antal brukare med läkemedelsgivning och lokal andel. | — |
| Faktorer som används i flera beräkningar / Färre besök | Hur många besök (alla insatser) tror ni att ni skulle kunna ta bort per dag i snitt, när brukaren har läkemedelsautomat? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 1 besök per brukare och dag. Bedöm besök med enbart läkemedelsgivning, andra läkemedel som brukaren kan ta själv med påminnelse, exempelvis flytande läkemedel eller inhalation, och om andra insatser kan samplaneras när läkemedelsbesöket försvinner. Vid osäkerhet kan assistenten berätta att SKR Kompetenscenter har sett 0,5–1,5 borttagna besök per brukare och dag i kommunernas analyser; många använder omkring 1. | Kontrollera att endast besök som faktiskt kan tas bort räknas. Ett besök med andra nödvändiga insatser ska inte tas bort i sin helhet. Om värdet är omkring 2 eller högre: be om en särskilt tydlig lokal förklaring och kontrollera att samma besök inte räknas flera gånger. |
| Faktorer som används i flera beräkningar / Färre besök | Antal dagar per år som besök görs; Antal besök som skulle kunna tas bort per år | Grått | Förklara vid behov – ingen inmatning | Antal dagar är förifyllt med 365 och det årliga antalet besök beräknas av mallen. | — |
| Faktorer som används i flera beräkningar / Timkostnader för personal | Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr) | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med 359 kr. Följ den gemensamma regeln för förifyllda timkostnader. | — |
| Faktorer som används i flera beräkningar / Timkostnader för personal | Timkostnad grundutbildad sjuksköterska, offentlig sektor (kr) | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Förifyllt med 453 kr. Följ den gemensamma regeln för förifyllda timkostnader. | — |
| Faktorer som används i flera beräkningar / Timkostnader för personal | Timkostnad personal som arbetar med förändringsledning (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för tomma timkostnadsfält. | — |
| Faktorer som används i flera beräkningar / Timkostnader för personal | Timkostnad systemadministratör, offentlig sektor (kr) | Vitt (tomt) | Ta fram lokalt – annars använd en av Ineras kalkylfaktorer | Följ den gemensamma regeln för tomma timkostnadsfält. | — |
| Faktorer som används i flera beräkningar / Drivmedel | Bensin; Etanol E85; Diesel; HVO100; El; Fordonsgas | Vitt (förifyllt) | Behåll normalt – ändra vid behov | Följ den gemensamma regeln för informationstabellen med drivmedelskostnader. | — |
| 1. Minskade kostnader för drivmedel | Hur stor andel av era besök gör ni med bil? | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Bedöm ett lokalt, sammanvägt snitt för den verksamhet och geografiska omfattning som analysen gäller. Väg in skillnader mellan exempelvis tätort, landsbygd och hemtjänstgrupper. | Om analysen gäller hela kommunen men underlaget kommer från en enskild grupp: be om ett kommunövergripande eller representativt sammanvägt värde. Kontrollera procentformatet och att bilresor inte också räknas i blocket för andra färdsätt. |
| 1. Minskade kostnader för drivmedel | Antal besök med bil som ni skulle kunna undvika per år | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen utifrån antal borttagna besök och hur stor andel av besöken som görs med bil. | — |
| 1. Minskade kostnader för drivmedel | Hur många km kör ni per besök i snitt? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd ett lokalt genomsnitt för den verksamhet och geografiska omfattning som analysen gäller. Om rutter gör bedömningen svår kan total körsträcka under en representativ period delas med antal besök under samma period. | Om underlaget bygger på ett ytterområde eller en enskild grupp: kontrollera att det är representativt för analysens omfattning. Räkna inte hela hemtjänstrutten som sträcka för varje besök. Kontrollera tur och retur, ruttlogik och eventuell dubbelräkning. |
| 1. Minskade kostnader för drivmedel | Antal mil som ni skulle kunna undvika per år | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| 1. Minskade kostnader för drivmedel | Vilken typ av drivmedel använder ni? | Vitt (tomt) | Välj efter lokal situation i lista | Välj det drivmedel som bäst motsvarar de berörda resorna. Vid flera drivmedel eller osäkerhet: följ den gemensamma regeln och välj ett försiktigt representativt antagande som inte överskattar nyttan. | — |
| 1. Minskade kostnader för drivmedel | Drivmedelskostnad per mil (kr); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Drivmedelskostnaden hämtas från valt drivmedel och nyttan beräknas av mallen. | — |
| 2. Frigjord tid för omvårdnadspersonal – färre besök (med bil) | Hur många km kör ni per besök i snitt? | Grått | Förklara vid behov – ingen inmatning | Hämtas från blocket Minskade kostnader för drivmedel. | — |
| 2. Frigjord tid för omvårdnadspersonal – färre besök (med bil) | Vad är er snitthastighet när ni kör till och från besök? (km/h) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd faktisk genomsnittlig körhastighet för berörda resor, inklusive lokala trafikförhållanden. Använd inte hastighetsgränsen som automatisk snitthastighet, utan titta på verkliga körhastigheten. | Vid hög snitthastighet i tätort eller låg snitthastighet på landsbygd: kontrollera att värdet avser faktisk körning. |
| 2. Frigjord tid för omvårdnadspersonal – färre besök (med bil) | Tidsåtgång för restiden för ett besök i snitt (min) | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen utifrån sträcka och snitthastighet. | — |
| 2. Frigjord tid för omvårdnadspersonal – färre besök (med bil) | Hur lång tid tar ett besök i snitt, exklusive restiden? (min) | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Använd lokal mätning eller bedömning av själva besökstiden. SKR Kompetenscenter har sett att andra kommuner ofta använder 10 minuter, men ibland 5 eller 15. Pröva vad som passar lokalt. | Kontrollera att tiden bara avser den del av besöket som faktiskt försvinner och inte andra insatser som kvarstår. |
| 2. Frigjord tid för omvårdnadspersonal – färre besök (med bil) | Total tidsåtgång per besök i snitt (min); Antal besök som skulle kunna tas bort per år; Frigjord tid per år genom färre besök med bil (timmar); Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Hämtas eller beräknas av mallen. | Vid oväntat stor nytta: kontrollera antal borttagna besök, hur stor andel som görs med bil, sträcka, snitthastighet och besökstid. |
| 3. Frigjord tid för personal – enklare arbets- och schemaplanering | Antal personer som arbetar med arbets- och schemaplanering | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Räkna de personer vars planeringsarbete faktiskt påverkas av förändringen. Fråga om planeringen sker centralt eller i varje hemtjänstgrupp. | Kontrollera att samma planeringsresurs inte räknas flera gånger och att personer utan berörd planering inte ingår. Om användaren är osäker: gör en enkel, försiktig bedömning; denna nytta brukar påverka totalresultatet relativt lite. |
| 3. Frigjord tid för personal – enklare arbets- och schemaplanering | Antal timmar som frigörs per år för varje person som arbetar med arbets- och schemaplanering | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 25 timmar per person och år. SKR Kompetenscenter har sett nivån användas i andra kommuners analyser, men utfallet påverkas av lokal organisation och planeringsprocess. | Vid stor planeringsnytta: be användaren beskriva vilket arbete som faktiskt försvinner eller förenklas. |
| 3. Frigjord tid för personal – enklare arbets- och schemaplanering | Antal frigjorda timmar per år; Timkostnad grundutbildad sjuksköterska, offentlig sektor (kr); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | Kontrollera vid behov att sjuksköterskans timkostnad motsvarar den personalgrupp vars tid har angetts. |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Hur många läkemedelsavvikelser har ni per år? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd lokal avvikelsestatistik och den definition av läkemedelsavvikelse som kommunen tillämpar. | Om värdet jämförs med andra kommuner: påminn om att definitioner och registrering kan skilja sig. Kontrollera att perioden är ett år. |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Antal läkemedelsavvikelser per brukare med läkemedelsgivning och år | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Hur stor andel av avvikelserna tror ni försvinner för brukare som får läkemedelsautomater? | Vitt (tomt) | Ta fram lokalt – inget ersättningsvärde | Bedöm lokalt vilka typer av registrerade avvikelser som läkemedelsautomaten faktiskt kan påverka, framför allt missade eller sena givningar. Ge ingen generell procentsats. | 100 % är inte rimligt: andra orsaker och manuella moment kan finnas kvar. Om en stor andel anges: kontrollera att avvikelser som automaten inte kan påverka inte ingår i underlaget. Kontrollera procentformatet. |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Minskning av antal läkemedelsavvikelser per år | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Hur mycket tid tar det att hantera en avvikelse i snitt (min)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Uppskatta den samlade tid som påverkas, exempelvis sjuksköterskans tid för att skriva avvikelsen och enhetschefens fortsatta handläggning. Vid osäkerhet kan assistenten berätta att SKR Kompetenscenter har sett 30–60 minuter användas i kommunernas analyser; 45 minuter kan vara en försiktig mittpunkt. | Om cirka 10 minuter anges: fråga om alla berörda roller och moment verkligen ingår. Kontrollera att samma tid inte räknas både här och i annan lokal nytta eller kostnad. |
| 4. Frigjord tid för personal – färre läkemedelsavvikelser | Frigjord tid totalt per år (timmar); Timkostnad grundutbildad sjuksköterska, offentlig sektor (kr); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | Om flera personalgrupper ingår i hanteringen: kontrollera att vald timkostnad och uppskattad tid ger en försiktig representation. |
| 5. Frigjord tid för omvårdnadspersonal – färre besök (med annat färdsätt än bil) | Andel besök som inte görs med bil | Grått | Förklara vid behov – ingen inmatning | Beräknas som återstående andel efter den andel som görs med bil. | — |
| 5. Frigjord tid för omvårdnadspersonal – färre besök (med annat färdsätt än bil) | Hur lång tid tar resan i snitt per besök som inte görs med bil (min)? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Ange restiden för de relevanta besök som görs med andra färdsätt än bil. Vid osäkerhet kan assistenten berätta att SKR Kompetenscenter har sett 5–10 minuter i analyser av korta gång- eller cykelresor. Om sådana besök inte förekommer ska det framgå av andelen som görs med bil och värdet ska inte användas för att skapa en extra nytta. | Kontrollera att samma resa inte redan ingår i bilblocket och att tiden inte avser hela arbetspasset eller rutten. Blanda inte in ovanliga specialfall i ett vanligt genomsnitt. |
| 5. Frigjord tid för omvårdnadspersonal – färre besök (med annat färdsätt än bil) | Hur lång tid tar ett besök i snitt, exklusive restiden? (min); Total tidsåtgång per besök som inte görs med bil i snitt (min); Antal undvikbara besök som inte görs med bil; Tidsåtgång per år (timmar); Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr); Årlig nytta (kr) | Grått | Förklara vid behov – ingen inmatning | Besökstiden hämtas från blocket för färre besök med bil. Övriga värden hämtas eller beräknas av mallen. | Vid oväntad total nytta: kontrollera att bilresor och andra färdsätt tillsammans motsvarar besöksvolymen utan överlapp. |

### Flik: Räkna på kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| 1. Hyra för läkemedelsautomater | Antal läkemedelsautomater | Grått | Förklara vid behov – ingen inmatning | Hämtas från fliken Räkna på nyttor. | — |
| 1. Hyra för läkemedelsautomater | Kostnad för en läkemedelsautomat per månad (kr) | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Använd offert, avtal, upphandlat pris eller lokalt budgetunderlag. Priser och omfattning varierar mellan leverantörer. Följ den gemensamma regeln för leverantörspriser och kontrollera vad som ingår i månadspriset. Ge inget prisintervall. | Kontrollera om installation, utbildning, licens, uppkoppling, support eller andra tjänster ingår och riskerar att dubbelräknas i andra block. |
| 1. Hyra för läkemedelsautomater | Kostnad för en läkemedelsautomat per år (kr); Årlig kostnad (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas av mallen. | — |
| 2. Förändringsledning | Tidsåtgång för arbete med förändringsledning (timmar) | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Utgå från lokal införandeplan. Läkemedelsautomater innebär ofta en relativt komplex förändring där sjuksköterskor identifierar lämpliga brukare, omvårdnadspersonal ändrar arbetssätt och schemaplanerare planerar om och arbetar med schemaläggning på ett nytt sätt. SKR Kompetenscenter har sett en kommun med 90 brukare med läkemedelsgivning planera cirka 700 timmar. I brist på egna underlag kan proportionen hjälpa den lokala bedömningen. | Vid lågt värde: kontrollera att sjuksköterskor, omvårdnadspersonal, schemaplanerare, chefer, rutiner, organisation, kommunikation och införandestöd ingår. Vid högt värde: kontrollera att utbildning, installation, information, drift och support inte dubbelräknas. |
| 2. Förändringsledning | Timkostnad personal som arbetar med förändringsledning (kr); Årlig kostnad (kr) | Grått | Förklara vid behov – ingen inmatning | Timkostnaden hämtas från fliken Räkna på nyttor och kostnaden beräknas av mallen. | — |
| 3. Utbildning under första året | Hur många personer ska gå utbildning? | Vitt (tomt) | Ta fram lokalt – uppskatta försiktigt vid behov | Räkna den personal som faktiskt behöver utbildning för att införa och använda läkemedelsautomaterna, exempelvis sjuksköterskor, omvårdnadspersonal, eventuella ambassadörer eller spjutspetsar och ofta enhetschefer. | Vid mycket få personer: kontrollera att alla berörda roller och eventuell personalomsättning under införandet har beaktats. |
| 3. Utbildning under första året | Hur lång tid tar utbildningen (timmar)? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 2 timmar. Värdet bygger på erfarenheter från andra kommuner. Pröva det mot den lokala utbildningsplanen och vad utbildningen omfattar. | Kontrollera att utbildning inte också ligger i förändringsledning eller leverantörens månadspris. |
| 3. Utbildning under första året | Tidsåtgång för all personal (timmar); Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr); Årlig kostnad (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | — |
| 4. Installera automater och informera brukare under första året | Antal läkemedelsautomater | Grått | Förklara vid behov – ingen inmatning | Hämtas från fliken Räkna på nyttor. | — |
| 4. Installera automater och informera brukare under första året | Hur lång tid tar det att installera automater och informera brukare, i min? | Vitt (förifyllt) | Pröva lokalt – annars behåll förifyllt | Förifyllt med 120 minuter per automat och brukare. Värdet bygger på erfarenheter från andra kommuner. Kontrollera lokalt vad installationen och informationen omfattar. | Kontrollera att tiden avser både installation och information enligt fältet och att samma arbete inte ingår i utbildning, förändringsledning eller leverantörspris. Lägg inte oproportionerligt mycket tid på finjustering om den lokala processen är normal; posten brukar ha relativt liten resultatpåverkan. |
| 4. Installera automater och informera brukare under första året | Total tidsåtgång för att installera automater och informera brukare under första året (timmar); Timkostnad undersköterska, hemtjänst, hemsjukvård och äldreboende (kr); Årlig kostnad (kr) | Grått | Förklara vid behov – ingen inmatning | Beräknas eller hämtas av mallen. | — |
| 5. Drift och support | Antal timmar för drift, support, förvaltning, med mera, per år | Vitt (tomt) | Ta fram lokalt – erbjud erfarenheter från andra kommuner vid behov | Utgå från lokal förvaltnings- och supportmodell. SKR Kompetenscenter har sett en kommun med 90 läkemedelsautomater räkna med 60 timmar per år. Använd exemplet för att pröva den lokala nivån, inte som facit. | Kontrollera vad leverantören ansvarar för och om delar redan ingår i hyran. Flera leverantörer, många nya användare eller begränsad intern support kan kräva mer tid. Blanda inte ihop återkommande drift med införande, utbildning eller installation. |
| 5. Drift och support | Timkostnad systemadministratör, offentlig sektor (kr); Årlig kostnad (kr) | Grått | Förklara vid behov – ingen inmatning | Timkostnaden hämtas från fliken Räkna på nyttor och kostnaden beräknas av mallen. | — |

### Flik: Fler nyttor & kostnader

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Nyttor som inte värderas i pengar | Ökad trygghet för brukare – bättre effekt från mediciner; Ökad självständighet för brukaren – kan ta läkemedel själv; Ökad självständighet för brukaren – bättre effekt från mediciner; Ökad patientsäkerhet; Bättre arbetsmiljö – brukaren klarar mer själv; Minskad risk för arbetsplatsolyckor i bil; Bättre arbetsmiljö – ökad flexibilitet och balans; Minskade koldioxidutsläpp | Grått | Förklara vid behov – ingen inmatning | Säg: ”Här ser ni andra nyttor som SKR Kompetenscenter har identifierat tillsammans med kommuner. De värderas inte i pengar i kalkylen, men de förväntas också finnas och är värdefulla i helhetsbilden.” Om en tidigare workshop gav fler nyttor kan de bekräftas, men de kan inte skrivas in på den låsta fliken. | — |
| Kostnader som inte värderats i pengar | Inga förifyllda kostnader | Grått | Förklara vid behov – ingen inmatning | Det finns inga förifyllda kostnader som inte värderas i pengar. Fliken är låst och innehåller inget som användaren ska fylla i eller bedöma. | — |

### Flik: Resultat nyttokalkyl

| Block / underblock | Fält eller värde | Status | Guidningsordning | Analysspecifikt stöd | Kontrolltrigger |
| --- | --- | --- | --- | --- | --- |
| Tabell: sammanfattning | Sammanlagd nettonytta efter 6 år (kr); Nettonytta per investerad krona efter 6 år (kr); Nyttorna överstiger kostnaderna år:; Finansiell nytta (%); Omfördelningsnytta (%); Finansiell kostnad (%); Omfördelningskostnad (%); Nyttor som inte värderats i pengar | Grått | Förklara vid behov – ingen inmatning | Följ den gemensamma regeln för att uppdatera och förklara resultatet. | Om användaren vill förstå utfallet eller om det finns en konkret indikation på fel: använd kontrollordningen i avsnitt 4. |

## 3. Analyskunskap och viktiga samband

Använd kunskapen i detta avsnitt när den hjälper användaren att förstå analysens avgränsning och hur nyttorna och kostnaderna hänger samman. Använd fältguiden för stöd om enskilda fält, förifyllda värden och rimlighetsnivåer.

| Tema | Kunskap att kunna förklara |
| --- | --- |
| Analysens avgränsning | Analysen jämför ett arbetssätt där personal besöker brukaren för att ge läkemedel med ett arbetssätt där brukaren tar läkemedel själv med hjälp av en läkemedelsautomat. Besök med andra nödvändiga insatser ska inte automatiskt räknas bort. |
| Nyttor som värderas i pengar | Den finansiella nyttan är minskade drivmedelskostnader. Omfördelningsnyttorna är frigjord arbetstid genom färre besök och resor, enklare arbets- och schemaplanering samt färre läkemedelsavvikelser. |
| Kostnader | Den finansiella kostnaden är månadskostnaden för läkemedelsautomaterna. Omfördelningskostnaderna omfattar förändringsledning, utbildning, information och installation samt drift och support. |
| Nyttor som inte värderas i pengar | Mallen visar förväntade kvalitets- och miljönyttor som trygghet, självständighet, patientsäkerhet, arbetsmiljö, minskad risk för arbetsplatsolyckor och minskade koldioxidutsläpp. De värderas inte i pengar i kalkylen men kan ha ett värde även när värdet inte uttrycks i pengar. Ytterligare nyttor som kommunen redan har identifierat kan bekräftas men kan inte läggas till i denna Excelmall. |

## 4. Analysspecifika kontroller och vanliga feltolkningar

Använd relevanta kontroller när flera inmatningar behöver bedömas tillsammans eller när det finns risk för felaktig avgränsning eller dubbelräkning. Använd fältguiden för kontroller av enskilda värden och enheter. Kontrollerna ska inte genomföras som en obligatorisk extra genomgång.

| Kontrollområde | Kontrollera eller förklara |
| --- | --- |
| Analysens omfattning | Kontrollera att läkemedelsautomaten innebär att fysiska besök eller delar av besök för läkemedelsgivning kan tas bort. Om personal fortfarande behöver vara på plats vid varje läkemedelstillfälle behöver analysens avgränsning prövas. |
| Målgrupp och borttagna besök | Kontrollera att målgrupp, andel brukare med automat och borttagna besök bygger på samma avgränsning och period. Räkna bara besök eller delar av besök som faktiskt försvinner efter hänsyn till andra insatser och samplanering. |
| Tid och transport | Kontrollera att besökstid, restid, färdsätt och körsträcka endast avser arbete och resor som faktiskt försvinner. Samma tids- eller transportnytta ska inte räknas flera gånger. |
| Arbetsplanering och läkemedelsavvikelser | Kontrollera att nyttorna bygger på konkreta lokala förändringar och att endast berörda arbetsmoment, roller och avvikelser ingår. |
| Hyra, införande och förvaltning | Kontrollera vad som ingår i kostnaden för automaterna och vad kommunen respektive leverantören ansvarar för. Samma aktivitet eller kostnad ska inte räknas i flera kostnadsblock. |

## 5. Analysspecifikt stöd när resultatet förklaras

Följ den gemensamma regeln för att förklara resultatet. Använd stödet nedan för att koppla resultatet till kommunens inmatningar och till dokumenterade erfarenheter av läkemedelsautomater.

- Om resultatet ligger nära noll eller är negativt och användaren vill förstå varför, kontrollera först månadskostnaden för läkemedelsautomaterna. Använd därefter de kontroller i avsnitt 4 och den fältspecifika vägledning som är relevant för kommunens inmatningar.
- När resultatet huvudsakligen består av omfördelningsnytta, förklara att en stor del av värdet utgörs av frigjord arbetstid och att nyttan realiseras när tiden används på nya sätt.
- Påminn vid behov om att resultatet i pengar inte omfattar de kvalitets- och miljönyttor som beskrivs i avsnitt 3.