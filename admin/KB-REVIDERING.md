# Så uppdaterar vi kunskapsbasen

Den här instruktionen beskriver hur Amanda och den som hjälper henne granskar, ändrar och lämnar över kunskapsbasens texter.

Instruktionen ligger i mappen `admin`. Den ska inte ingå i kunskapsbasens artiklar, samlingsfil eller AI-assistentens metodstöd.

## 1. Utgå från rätt underlag

Amanda ansvarar för metoden och godkänner ändringar i kunskapsbasen.

Den godkända texten finns på `main` i detta repo. Ange vilken version granskningen utgår från. Om Amanda anger en annan arbetsversion används den i stället.

Appens beteende, utvecklingsförslag och kommentarer i ärenden är underlag för granskningen. De blir inte metodbeslut förrän Amanda har bekräftat dem.

## 2. Bestäm vad som ska ses över

Börja med den fråga eller del av metoden som Amanda vill arbeta med. Fråga om avgränsningen är oklar.

Läs de berörda artiklarna och kontrollera relevanta tidigare beslut och testfynd. Beskriv kort:

- vad texterna säger i dag,
- vad som är otydligt, saknas eller motsäger annat innehåll,
- vilka frågor Amanda behöver ta ställning till.

Kontrollera även ordlistan, gemensamma stödartiklar och andra texter som påverkas av ändringen. En artikel som används i flera sammanhang behöver fungera i samtliga.

Om tillgång till appens repo saknas kan metodgranskningen ändå genomföras. Ange då vilka frågor om appens användning av texten som Fabian behöver kontrollera.

## 3. Skriv begripliga och användbara artiklar

Artiklarna ska kunna läsas av människor och användas som stöd av AI-assistenten. Assistenten kan få tillgång till enstaka avsnitt, så varje avsnitt behöver vara begripligt för sig.

Följ dessa skrivregler:

- Lägg all brödtext under en underrubrik på nivå två, markerad med `##`. Det gäller även ingressen.
- Låt varje avsnitt behandla en tydlig fråga.
- Skriv 200–1 200 tecken per avsnitt. Sikta på 400–800.
- Använd högst sex sådana avsnitt per artikel.
- Håll varje tabell samlad inom ett avsnitt och under 1 200 tecken.
- Använd rubriker med bekanta ord som hjälper läsaren att hitta rätt.
- Lägg huvudbudskapet först och skriv så att avsnittet kan förstås utan omgivande text.

Skriv direkt till läsaren med du, dig och din. Använd ni när en uttalad grupp avses. Använd samma begrepp konsekvent och undvik onödiga fackord.

Använd imperativ när läsaren eller analysgruppen ska göra något: skriv exempelvis **”Dokumentera vilka perspektiv som ingår”** i stället för **”Valda perspektiv dokumenteras”**.

När instruktionen gäller någon annan, ange vem som ska göra vad, exempelvis **”Den ansvariga verksamheten ska följa upp om nyttorna uppstår”** i stället för **”Nyttorna följs upp”**. Skilj mellan en uppgift som ska utföras och något som faktiskt har genomförts eller kontrollerats. Aktiv form räcker inte om formuleringen ändå gör ansvaret eller uppgiftens status otydlig.

Beskriv hur metoden ska tillämpas och vilka avgränsningar som gäller. Frågor om exempelvis knappar, sparande och tekniska lösningar lämnas till utvecklingen.

## 4. Visa förslaget för Amanda

Visa de föreslagna texterna och förklara kort vad som ändras och varför. Skilj mellan språkliga förbättringar, förtydliganden av befintlig metod och nya metodbeslut.

Redovisa om något innehåll tas bort eller får en annan innebörd.

Amanda granskar och godkänner förslaget. Ändra filer, öppna en PR eller publicera ärenden och kommentarer när hon har bett om det. En PR är ett samlat ändringsförslag i GitHub och kan användas för granskningen om Amanda vill det.

Ändra originalartiklarna. Samlingsfilen `KB06-samlad.md` byggs automatiskt och ska inte redigeras direkt.

## 5. Kontrollera och dokumentera ändringen

Kontrollera före införandet att:

- texten följer Amandas metodbeslut och skrivreglerna,
- relevant innehåll finns kvar och borttagningar är redovisade,
- berörda artiklar använder begreppen konsekvent,
- texten fungerar i de sammanhang där den används,
- eventuella ändringar av artikelindelning och publika länkar är hanterade.

Beskriv ändringen kort i samma PR som innehåller artikeländringarna: berörda artiklar, viktigaste förändringar, medvetet borttaget innehåll och eventuella kvarstående frågor.

PR och GitHubs versionshistorik ger tillsammans spårbarheten. Ingen separat ändringslogg i ChatGPT behövs.

Amanda godkänner när ändringen får föras in i `main`.

## 6. Lämna över till Fabian

När godkända artikeländringar finns på `main`, skapa ett porteringsärende till Fabian om de ska föras över till appen. Länka till PR och de berörda artiklarna.

Porteringsunderlaget ska kort beskriva:

1. **Vad som ändrats och varför** – berörda artiklar, vilket problem eller vilken otydlighet förändringen ska lösa och vad den ska göra tydligare.
2. **Metodbeslut som appen ska följa** – reglerna som utvecklingen ska utgå från.
3. **Vad som inte har ändrats men lätt kan förväxlas** – viktiga avgränsningar, om sådana finns.

Underlaget ska gå att förstå utan att läsa tidigare chattar eller hela diskussionen i PR. Länka till PR och artiklarna för detaljer. Förklaringen av avsikten ska hjälpa mottagaren att förstå metodbesluten, utan att införa ytterligare krav som Amanda inte har godkänt.

Fabian ska föra över texterna och kontrollera att appen hittar och använder dem. Han ansvarar också för tekniska lösningar och tester. Tekniska frågor och testfynd kan beskrivas separat i ärendet, utanför metodunderlaget.

Skilj på att en text är godkänd i kunskapsbasen, överförd till appen och verifierad i användning. Ange vad som återstår och vem som ansvarar för det.

Den här förvaltningsinstruktionen ska inte föras över till appens metodstöd.
