# LoL Champion ARAM Build Scraper 🛡️
Provides a tool to fetch ARAM build details for champions from a source website.

## Features 🚀:
- 📖 Fetch the **title** of the champion-specific page.
- 🗡️ List **weapons/items** for the champion in ARAM mode.
- 🌀 Display the primary **rune** for the champion.
- 📊 Show the **skill order** up to Level 18.

## Sample Output 🖥️:
```
Enter the champion name: singed

[INFO] Title of the page for singed is: Singed ARAM Build 13.19 - Runes & Items - LoL
'
Weapons for SINGED:
 - Rod of Ages
 - Mercury's Treads
 - Rylai's Crystal Scepter
 - Demonic Embrace
 - Dead Man's Plate
 - Force of Nature

----------------------------------------

Runes for SINGED: CONQUEROR

----------------------------------------

Skill Order for SINGED:
Level 1: Q
Level 2: W
Level 3: E
...
Level 18: W

----------------------------------------
```


## Requirements 🔧:
- BeautifulSoup4
- Requests

## Usage 🎮:
1. Install necessary libraries.
2. Run `python main.py`.
3. Input the champion's name.
4. View results in the terminal.

## Contributions ✨:
Open to contributions and bug fixes. For major changes, open an issue first.
