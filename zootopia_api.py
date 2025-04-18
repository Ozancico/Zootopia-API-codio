import data_fetcher

def make_animal_card(animal):
    card = "<li class='cards__item'>"
    card += "<div class='card__title'>" + animal['name'] + "</div>"
    card += "<div class='card__text'>"

    # Location
    if animal['locations']:
        location_text = ", ".join(animal['locations'])
    else:
        location_text = "Unknown"
    card += "<strong>Location:</strong> " + location_text + "<br>"

    # Loop through all characteristics
    for key in animal['characteristics']:
        value = animal['characteristics'][key]
        card += "<strong>" + key.replace("_", " ").capitalize() + ":</strong> " + value + "<br>"

    card += "</div></li>"

    return card

def replace_template(template_file_path, animal_list, output_file_path, animal_name):
    # Open the template file using 'with'
    with open(template_file_path, "r") as file:
        html_text = file.read()

    if len(animal_list) > 0:
        cards_html = ""
        for animal in animal_list:
            cards_html += make_animal_card(animal)
        full_html = html_text.replace("__REPLACE_ANIMALS_INFO__", cards_html)
    else:
        message = "<h2>The animal \"" + animal_name + "\" doesn't exist.</h2>"
        full_html = html_text.replace("__REPLACE_ANIMALS_INFO__", message)

    # Write the output HTML file using 'with'
    with open(output_file_path, "w") as output:
        output.write(full_html)

    print("Website was created and saved to animals.html.")

# === Start of the program ===
user_animal_name = input("Please enter the name of an animal: ")
animal_data = data_fetcher.fetch_data(user_animal_name)
replace_template("animals_template.html", animal_data, "animals.html", user_animal_name)
