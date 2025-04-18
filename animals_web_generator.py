import data_fetcher


def serialize_animal(animal):
    """
    Converts a single animal dictionary into a formatted HTML <li> card,
    listing all available attributes of the animal.
    """
    output = '  <li class="cards__item">\n'

    if 'name' in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    output += '    <p class="card__text">\n'

    for key, value in animal.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                output += f'      <strong>{sub_key.capitalize()}:</strong> {sub_value}<br/>\n'
        elif isinstance(value, list):
            for item in value:
                output += f'      <strong>{key.capitalize()}:</strong> {item}<br/>\n'
        else:
            output += f'      <strong>{key.capitalize()}:</strong> {value}<br/>\n'

    output += '    </p>\n'
    output += '  </li>\n'
    return output


def generate_animal_output(data):
    return ''.join(serialize_animal(animal) for animal in data)


def replace_template(html_template_path, output_text, result_path):
    with open(html_template_path, "r") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output_text)

    with open(result_path, "w") as result_file:
        result_file.write(final_html)

    print(f"✅ HTML successfully written to {result_path}")

def main():

    user_animal_name = input("Please enter the name of an animal: ")
    animal_data = data_fetcher.fetch_data(user_animal_name)

    if not animal_data:
        print(f"No data found for animal: {user_animal_name}")
        # Schreiben Sie eine leere HTML-Datei, wenn keine Daten gefunden wurden
        replace_template("animals_template.html", "", "animals.html")
    else:
        animal_info = generate_animal_output(animal_data)
        replace_template("animals_template.html", animal_info, "animals.html")


if __name__ == "__main__":
    main()