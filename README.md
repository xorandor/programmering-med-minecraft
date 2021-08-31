# Programmering med Minecraft: Sådan kommer du i gang

## Del 1, alt det der skal gøres én gang

For at komme i gang skal du have installeret nogle programmer på din computer. Dette dokument beskriver hvordan.

Når du har fulgt guiden, vil du have installeret:

- Java (nødvendig for at kunne starte en Spigot Minecraft server)
- Python 3 (nødvendig for at kunne skrive programmer)
- Minecraft 1.17.1
- Spigot Minecraft server
- Visual Studio Code (benyttes til at skrive programmerne)

### 1. Installation af Java

1. Gå ind på https://www.oracle.com/java/technologies/javase-jdk16-downloads.html
2. Find den der hedder 'Windows x64 Installer' og download den
4. Gem installationsfilen på din computer
5. Åbn installationsfilen og følg guiden (benyt standardindstillinger)

### 2. Installation af Python 3

1. Gå ind på www.python.org
2. Klik på Downloads > Windows
3. Tryk på **Latest Python 3 Release**
4. Scroll ned til bunden af siden
5. Vælg **Windows installer (64-bit)**
6. Gem installationsfilen på din computer.
7. Åbn installationsfilen og følg guiden (**Husk at sætte kryds i 'Add python to environment variables'**)

### 3. Installation af Minecraft 1.15.2

**Hvis Minecraft ikke allerede er installeret**

1. Gå ind på www.minecraft.net
2. Du skal være logget ind med en konto med adgang til spillet
3. Vælg **Hent Minecraft**
4. Vælg **Computer**
5. Vælg **PC**
6. Vælg **Minecraft: Java edition**
7. Gem installationsfilen på din computer.
8. Åbn installationsfilen og følg guiden (benyt standardindstillinger)

**Når Minecraft er installeret**

1. Åbn Minecraft
2. Vælg fanen **Installations**
3. Tryk på **New...**
4. Skriv "1.15.2" som **Name**
5. Vælg "release 1.15.2" under **Version**
6. Tryk **Create**
7. Minecraft 1.15.2 hentes nu ned og kan vælges i bunden af fanen **Play**.

### 4. Installation af Visual Studio Code

1. Gå ind på [code.visualstudio.com](code.visualstudio.com)
2. Vælg **Download for Windows**
3. Gem installationsfilen på din computer.
4. Åbn installationsfilen og følg guiden (benyt standardindstillinger)

### 5. Installation af Spigot

1. Spigot ligger klar til brug i mappen **Spigot** i denne zip-fil.
2. Åbn **Spigot** mappen.
3. Åbn **start_spigot.bat**
4. Serveren startes nu for første gang, hvilket kan tage lidt tid, fordi der skal genereres en verden.

## Del 2, Tjek om det hele virker

### 1. Start din første verden med vores eksempel

1. Start **Spigot**
2. Åbn Minecraft og vælg Multiplayer
3. Hvis serveren ikke dukker op, skal ud tilføje en ny server med adressen **localhost**
4. Åbn Visual Studio Code (_vscode_)
5. Åbn **code** mappen fra _vscode_
6. Vælg **Terminal** > **New terminal** i top-menuen.
7. I terminalen skriver du `python example.py`
8. Du kan nu i Minecraft se at der er blevet bygget en bygning, som efter kort tid eksploderer.

Tillykke! Du er klar til at programmere i Minecraft med Python!

## Del 3, Alt det der skal gøres hver gang du skal kode

1. Start **Spigot**
2. Åbn Minecraft og vælg Multiplayer
3. Åbn Visual Studio Code (_vscode_)
4. Åbn **code** mappen fra _vscode_
5. Vælg **View** > **Terminal** i top-menuen.
6. Lav en ny `.py` fil, eller arbejd videre på en eksisterende
7. Når du er klar, kør dit program ved at skrive `python mitfilnavn.py`

Husk at lukke serveren når du er færdig med dagens arbejde :-)

## Del 4, Nyttige tips

### 1. Lad Minecraft forblive aktiv selvom du åbner et andet program

Minecraft har det med at åbne pause-menuen, når du skifter til et andet program. Du kan slå dette fra ved at ændre en indstilling i Minecraft.

1. Tryk på **Start** -> **Kør**
2. Skriv `%APPDATA%\.minecraft` og tryk Enter
3. Åbn options.txt
4. Find den linie hvor der står `pauseOnLostFocus:true`
5. Ret den til `pauseOnLostFocus:false` og gem filen
6. Genstart Minecraft

### 2. Nulstil din verden

Hvis du vil starte din verden helt forfra (slette **alt** der er bygget), kan du gøre følgende:

1. Åbn **Spigot** mappen
2. Slet mapperne `world`, `world_nether`, `world_the_end`
3. Genstart **Spigot**

### 3. Sådan ændrer du indstillingerne på din Minecraft server

1. Åbn **Spigot** mappen
2. Åbn filen `server.properties`

Du kan ændre forskellige ting:

- Type af verden:
  - `default`: Standard verden med bakker, dale, vand osv.
  - `flat`: Helt flad verden
  - **OBS:** Hvis du ændrer typen, skal du derefter nulstille din verden, så serveren kan generere en ny med den valgte type. Se ovenfor under overskriften _Nulstil din verden_
- Spil-tilstand:
  - `survival`
  - `creative`
  - `adventure`

Der er mange andre muligheder for at konfigurere serveren. Alle indstilliger kan findes på denne hjemmeside: https://www.spigotmc.org/wiki/spigot-configuration-server-properties/

- Happy hacking
