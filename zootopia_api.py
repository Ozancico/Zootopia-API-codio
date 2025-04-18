import requests
import json
from dotenv import load_dotenv
import os

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hol den API-Schlüssel aus der Umgebungsvariablen
API_KEY = os.getenv("API_KEY")
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches animal data from the API using the provided animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list[dict]: A list of animal data dictionaries returned by the API.
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        animals = response.json()  # The response is parsed as JSON
        return animals  # Return as a list of animals
    else:
        print(f"⚠️ Error fetching data: {response.status_code}")
        return []  # Return an empty list if an error occurs


def load_data(file_path):
    """
    Loads a JSON file and returns its content as a Python object.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list[dict]: A list of animal data dictionaries.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Converts a single animal dictionary into a formatted HTML <li> card,
    listing all available attributes of the animal.

    Args:
        animal (dict): A dictionary containing animal data.

    Returns:
        str: An HTML string representing the animal card with all attributes.
    """
    output = '  <li class="cards__item">\n'

    # Animal name as the card title
    if 'name' in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    # Begin card description
    output += '    <p class="card__text">\n'

    # Dynamically list all available attributes of the animal
    for key, value in animal.items():
        if isinstance(value, dict):  # Handle nested dictionaries (e.g., characteristics)
            for sub_key, sub_value in value.items():
                output += f'      <strong>{sub_key.capitalize()}:</strong> {sub_value}<br/>\n'
        elif isinstance(value, list):  # Handle lists (e.g., locations)
            for item in value:
                output += f'      <strong>{key.capitalize()}:</strong> {item}<br/>\n'
        else:
            output += f'      <strong>{key.capitalize()}:</strong> {value}<br/>\n'

    # End description and list item
    output += '    </p>\n'
    output += '  </li>\n'
    return output


def generate_animal_output(data):
    """
    Generates the full HTML block with cards for all animals in the dataset.

    Args:
        data (list[dict]): A list of animal dictionaries.

    Returns:
        str: A concatenated HTML string with all animal cards.
    """
    return ''.join(serialize_animal(animal) for animal in data)


def replace_template(html_template_path, output_text, result_path):
    """
    Replaces a placeholder in the HTML template with generated animal HTML,
    and writes the result to a new file.

    Args:
        html_template_path (str): Path to the template HTML file.
        output_text (str): Generated HTML for animals.
        result_path (str): Output path for the final HTML file.
    """
    with open(html_template_path, "r") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with generated content
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output_text)

    # Write final HTML to file
    with open(result_path, "w") as result_file:
        result_file.write(final_html)

    print(f"✅ HTML successfully written to {result_path}")


# Entry point of the script
if __name__ == "__main__":
    # Ask the user for an animal name
    user_animal_name = input("Please enter the name of an animal: ")

    # Fetch the animal data from the API
    animal_data = fetch_data(user_animal_name)

    if len(animal_data) == 0:
        print(f"No data found for animal: {user_animal_name}")
    else:
        # Generate animal cards HTML
        animal_info = generate_animal_output(animal_data)

        # Replace placeholder in template with the generated animal cards HTML
        replace_template("animals_template.html", animal_info, "animals.html")
