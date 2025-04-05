party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11),
]

def display_items():
    print("Available Party Items:\n")
    for idx, (item, _) in enumerate(party_items):
        print(f"{idx}: {item}")
    print()

def get_user_selection():
    indices = input("Enter item indices separated by commas (0, 2): ")
    try:
        selected_indices = [int(i.strip()) for i in indices.split(",")]
        for idx in selected_indices:
            if idx < 0 or idx >= len(party_items):
                raise ValueError
        return selected_indices
    except ValueError:
        print("Invalid input. Please enter valid indices.")
        exit()

def calculate_party_code(selected_indices):
    selected_values = [party_items[i][1] for i in selected_indices]
    selected_names = [party_items[i][0] for i in selected_indices]

    base_code = selected_values[0]
    for val in selected_values[1:]:
        base_code &= val

    return base_code, selected_names, selected_values

def adjust_code(base_code):
    if base_code == 0:
        final_code = base_code + 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        final_code = base_code - 2
        message = "Lets keep it classy"
    else:
        final_code = base_code
        message = "Chill vibes only"
    return final_code, message

def render_html(selected_names, selected_values, base_code, final_code, message):
    html_output = f"""
    <html>
    <head><title>Party Planner</title></head>
    <body>
        <h1>Selected Items:</h1>
        <p>{', '.join(selected_names)}</p>
        <h2>Base Party Code:</h2>
        <p>{' & '.join(map(str, selected_values))} = {base_code}</p>
        <h2>Final Party Code:</h2>
        <p>{final_code}</p>
        <h2>Message:</h2>
        <p>{message}</p>
    </body>
    </html>
    """
    return html_output

if __name__ == "__main__":
    display_items()
    selected_indices = get_user_selection()
    base_code, selected_names, selected_values = calculate_party_code(selected_indices)
    final_code, message = adjust_code(base_code)
    html = render_html(selected_names, selected_values, base_code, final_code, message)

    print("\nGenerated HTML Output:\n")
    print(html)












