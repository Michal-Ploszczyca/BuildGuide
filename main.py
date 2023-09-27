import requests
from bs4 import BeautifulSoup
import os

def fetch_champion_data(champion_name):
    base_url = "https://www.metasrc.com/lol/aram/build/"
    full_url = base_url + champion_name.lower()
    page = requests.get(full_url)
    # Ensure the request was successful
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    else:
        print('Failed to fetch the champion data.')
        return None


def extract_champion_title(soup):
    title = soup.title.string
    return title


def extract_weapons_from_div(soup):
    # Navigate to the specific div containing the weapons
    div_with_weapons = soup.find('div', style="display: flex;align-items: center;justify-content: center;")

    # Find all weapon images within that div
    weapon_images = div_with_weapons.find_all('img', class_='lozad')

    weapon_names = []
    for img in weapon_images:
        weapon_name = img.get('alt')  # Get the value of the 'alt' attribute
        weapon_names.append(weapon_name)

    return weapon_names


def extract_runes_from_div(soup):
    """Extract the primary rune's name from a BeautifulSoup object containing a champion's page content.

       Parameters:
           soup (BeautifulSoup): BeautifulSoup object with the parsed HTML of the champion's page.

       Returns:
           list: List containing the primary rune's name or an empty list if rune's name is not found.
       """

    runes_names = []
    div_with_runes = soup.find('div', id='perks')

    if div_with_runes: #  If the div is found, proceed to extract the rune's name
        rune_image = div_with_runes.find('image', class_='lozad')
        # If the rune image is found, attempt to extract its URL
        if rune_image:
            rune_url = rune_image.get('data-xlink-href')

            # If the URL is successfully extracted, deduce the rune's name from it
            if rune_url:
                rune_name = rune_url.split('/')[-2]
                # Format the rune name to have each word capitalized and store it in the list
                formatted_rune_name = " ".join(word.capitalize() for word in rune_name.split(' '))
                runes_names.append(formatted_rune_name)
    return runes_names


def extract_skills(soup):
    skills_order = []


    # Skip the header row and select the rows with skills
    rows = soup.select('tr._eveje5')[1:]

    # Go column by column (champion level by champion level)
    for i in range(1, 19):  # Levels 1 through 18
        for row in rows:
            # Check each skill's cell for that level
            cell = row.select(f'td._w77rgh:nth-child({i + 1})')
            if cell and cell[0].text in ['Q', 'W', 'E', 'R']:
                skills_order.append(cell[0].text)

                break

    return skills_order



def main():
    champion_name = input('Enter the champion name: ')
    soup = fetch_champion_data(champion_name)

    if not soup:
        print("Couldn't fetch data. Please try again.")
        return

    # Display Title
    title = extract_champion_title(soup)
    print(f"\n[INFO] Title of the page for {champion_name} is: {title}\n")

    # Display Weapons
    weapons = extract_weapons_from_div(soup)
    print(f"Weapons for {champion_name.upper()}:")
    for weapon in weapons:
        print(f" - {weapon}")
    print("\n" + "-"*40 + "\n")  # A separator line

    # Display Runes
    runes = extract_runes_from_div(soup)
    runes_str = ', '.join(runes)
    print(f"Runes for {champion_name.upper()}: {runes_str.upper()}\n")
    print("\n" + "-"*40 + "\n")  # A separator line

    # Display Skill Order
    print(f"Skill Order for {champion_name.upper()}:")
    skills = extract_skills(soup)
    for level, skill in enumerate(skills, start=1):
        print(f"Level {level}: {skill}")
    print("\n" + "-"*40 + "\n")  # A separator line

if __name__ == "__main__":
    main()

