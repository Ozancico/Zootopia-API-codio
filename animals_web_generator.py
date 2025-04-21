import data_fetcher  # Module to handle API requests


# Converts a dictionary representing an animal into a styled HTML list item
def serialize_animal(animal):
    """
    Converts a single animal dictionary into a formatted HTML <li> card,
    listing all available attributes of the animal.
    """
    output = '  <li class="cards__item">\n'

    # Add the animal name as the card title if available
    if 'name' in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    output += '    <p class="card__text">\n'

    # Loop through each key in the animal dictionary
    for key, value in animal.items():
        if isinstance(value, dict):
            # Handle nested dictionary (e.g., taxonomy or characteristics)
            for sub_key, sub_value in value.items():
                output += f'      <strong>{sub_key.capitalize()}:</strong> {sub_value}<br/>\n'
        elif isinstance(value, list):
            # Handle list values (e.g., locations)
            for item in value:
                output += f'      <strong>{key.capitalize()}:</strong> {item}<br/>\n'
        else:
            # Handle simple key-value pairs
            output += f'      <strong>{key.capitalize()}:</strong> {value}<br/>\n'

    output += '    </p>\n'
    output += '  </li>\n'
    return output



def generate_animal_output(data):
    """Converts a list of animal data into one HTML block"""
    return ''.join(serialize_animal(animal) for animal in data)


def load_html_template(html_template_path):
    """Loads the HTML template from file"""
    with open(html_template_path, "r") as template_file:
        return template_file.read()


def replace_template(html_template_path, output_text):
    """Replaces the placeholder in the HTML template with animal content"""
    return html_template_path.replace("__REPLACE_ANIMALS_INFO__", output_text)


def save_result(final_html, result_path):
    """Saves the final HTML content to a new file"""
    with open(result_path, "w") as result_file:
        return result_file.write(final_html)



def main():
    """
    Prompts the user for an animal name, retrieves data using an API,
    and generates an HTML file with the animal information. If no data
    is found, it writes an empty HTML.

    :return: None
    """

    # Prompt user to enter an animal name
    user_animal_name = input("Please enter the name of an animal: ")

    # Fetch animal data from the API
    animal_data = data_fetcher.fetch_data(user_animal_name)

    if not animal_data:
        # If no data is found, show message and do not proceed with generation
        print(f"No data found for animal: {user_animal_name}")
        replace_template("animals_template.html", "")
    else:
        # If data is found, process it and generate the HTML
        animal_info = generate_animal_output(animal_data)
        template = load_html_template("animals_template.html")
        final_html = replace_template(template, animal_info)
        result_path = "animals.html"
        save_result(final_html, result_path)
        print(f"✅ HTML successfully written to {result_path}")


# Only run main if this file is executed directly
if __name__ == "__main__":
    main()