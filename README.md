# Kom igång
För att lära dig Git ska du nu få jobba med ett repository! Du ska först skapa en *fork*, så att du har en egen kopia av repot. Se till att du är inloggad på ett eget GitHub-konto. Gå in på [repot](https://github.com/Fysiksektionen/gitgood) och klicka på "Fork". Se till att **INTE** välja "Copy the main branch only". Nu borde en fork av repot finnas under din egna profil! Gå in på denna och klicka på den gröna "Code"-knappen, och kopiera länken som står under Local, SSH. Öppna nu en terminal och skriv `git clone <link>`. Detta klonar repot till en mapp lokalt på din dator.

Repot innehåller en del filer. Bland annat finns en LaTeX-fil `main.tex` som innehåller en berättelse som du ska få utveckla! Kompilera den gärna till pdf om du kan och vill, alternativt läs den bara som den är.

# Uppgifter

1. I filen `main.tex`, radera kommentaren `% TODO lägg till ditt namn` och skriv in ditt namn. Skapa en commit för detta med meddelandet "Add my name".
2. I samma fil, radera kommentaren `% TODO beskriv programmet!` och skriv vad du vill istället :). Skapa en commit för detta och ge den ett lämpligt namn.
3. Bilden i dokumentet är just nu av en riktig anka, men Anki är ju en badanka. Hitta en ny bild av en badanka och lägg till den. Ändra också i `main.tex` så att den nya bilden används istället för `duck_that_is_not_anki.jpeg`. Ge committen ett lämpligt namn!
4. Skapa en commit där du raderar den gamla bilden `duck_that_is_not_anki.jpeg`. Den vill vi inte ha längre!
5. Kör pythonfilen `start.py` och njut av vad du ser. Men oj! Nu skapades en mapp som heter `__pycache__`. Den vill vi inte ha med i repot, så committa inte den! Skapa istället filen `.gitignore` och skriv där `__pycache__`. Spara detta som en commit. Nu kommer Git inte längre att hålla koll på mappen `__pycache__`!
6. DU BLIR TVINGAD AV HÖGRE MAKTER ATT RADERA FILEN `superviktigfil.txt` OCH KÖRA KOMMANDOT `git add .`. Åh nej!!! Nu har den superviktiga filen försvunnit! Hur ska vi få tillbaka den? Jo, kör `git reset` för att unstage:a ("motsatsen" till `git add`). Kör sen `git restore .` för att ställa tillbaka alla filer till sitt ursprungliga tillstånd. Filen borde nu vara tillbaka! Ingen commit behövs i denna uppgift.
7. Vi vill nu lägga till ett nytt kapitel i dokumentet. Denna finns färdigskriven, men existerar i en annan branch. Börja med att skriva `git checkout chapter-2` för att titta på den branchen. När du känner dig nöjd kan du gå tillbaka med `git checkout main`. Ingen commit behövs.
8. Nu vill vi föra över ändringarna till huvudbranchen. Detta borde kunna utföras smärtfritt med `git merge chapter-2`. Glöm inte att spara detta som en commit.
9. Det finns ett sista kapitel i branchen `chapter-3`. Merge:a in den i `main`-branchen på samma sätt. Åh nej! Blev det en merge conflict?! Ingen panik! Det går att lösa. Skriv `git help merge` för att få mer information. Med detta kan du säkert klura ut hur man gör själv. Vi tror på dig!

Grattis! Du är nu bättre på Git än samtliga slumpmässigt tillfrågade (2) f-teknologer på bokbytarpuben! :tada:

# Terminal basics
Har du ingen aning om hur man använder en terminal? Frukta ej, här kommer några av de viktigaste sakerna man bör kunna.
- Terminalen har alltid ett *working directory*. Detta är den nuvarande mappen som terminalen kommer utgå ifrån när du kör kommandon.
- `dir` (Windows) eller `ls` (de flesta andra operativsystem) - listar vad som finns i working directory.
- `cd <path>` - byter working directory. För att gå in i en mapp som finns i working directory, skriv mappnamnet som path. För att gå tillbaka till föregående mapp, använd ".." som path.

# Git cheat-sheet
## De vanligaste
- `git help <command>` - Ger en beskrivning av kommandot `<command>`.
- `git clone <link>` - Kopierar repot vid url:en `<link>` till din nuvarande mapp. 
- `git add <file>` - Stage:ar ändringarna i `<file>` för commit (lägger till filens ändringar till nästa commit).
- `git commit -m "<message>"` - Skapar en commit med meddelandet `<message>`.
- `git push` - Lägger till dina commits till github (ditt remote repo).
- `git pull` - Lägger till alla commits från github (ditt remote repo) till ditt lokala repo

## Andra vanliga
- `git init` - Gör mappen till ett git repo.
- `git restore <file>` - Återställer filen `<file>` till den senaste commit:en.
- `git reset <file>` - Unstage:ar ändringarna i filen `<file>`.

## För branches
- `git branch <name>` - Skapar en branch med namnet `<name>`.
- `git checkout <name>` - Tar dig till den branch med namnet `<name>`.
- `git merge <name>` - Merge:ar alla commits från den branch med namnet `<name>`, till din nuvarande branch.

# Extra kluriga saker
En del program är lite extra kluriga att lämna. Här kommer några exempel:
- `git log` - lämnas genom att trycka "q". Detta gäller även för många liknande program.
- `vim` - denna körs till exempel om du skriver `git commit` utan att specificera ett meddelande. Lämna utan att spara några ändringar genom att trycka Escape följt av "q!", Enter.
