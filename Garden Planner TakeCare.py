import tkinter as tk

# Initialize the garden plot as a 2D grid
garden_width = 10
garden_height = 10
garden = [["Empty" for _ in range(garden_width)] for _ in range(garden_height)]

# Updated plant database with emojis, care instructions, and suitability conditions
plant_database = {
    "Tomato": {
        "emoji": "🍅",
        "care": "Tomatoes require full sun and regular watering. Use stakes for support as they grow.",
        "suitable_weather": ['Sunny'],
        "suitable_soil": ['Loamy', 'Sandy']
    },
    "Carrot": {
        "emoji": "🥕",
        "care": "Carrots need well-drained soil and consistent watering. Thin seedlings to avoid crowding.",
        "suitable_weather": ['Sunny', 'Cloudy'],
        "suitable_soil": ['Loamy']
    },
    # Add more plants with emojis, care instructions, and suitability conditions as needed
}

# Function to get suitable plants based on weather and soil conditions
def get_suitable_plants(weather, soil):
    suitable_plants = []
    for plant, info in plant_database.items():
        if 'suitable_weather' in info and 'suitable_soil' in info:
            if weather in info['suitable_weather'] and soil in info['suitable_soil']:
                suitable_plants.append(plant)
    return suitable_plants

# Function to display the care instructions for a selected plant
def display_care_instructions(event=None):
    selection_index = plant_listbox.curselection()
    if selection_index:  # Check if a selection is made
        selected_plant = plant_listbox.get(selection_index[0])  # Get the selected plant
        if selected_plant in plant_database:
            care_instructions = plant_database[selected_plant]["care"]
            care_instructions_label.config(text=f"Care Instructions for {selected_plant.capitalize()}:\n{care_instructions}")

# Function to display the garden plot
def display_garden():
    for y in range(garden_height):
        for x in range(garden_width):
            plant_info = garden[y][x]
            if plant_info != "Empty":
                plant_emoji = plant_database.get(plant_info, {}).get("emoji", "🌱")
                cell_label = tk.Label(main_frame, text=plant_emoji, borderwidth=1, relief="solid", width=8, height=2)
                cell_label.grid(row=y, column=x)
            else:
                cell_label = tk.Label(main_frame, text="Empty", borderwidth=1, relief="solid", width=8, height=2)
                cell_label.grid(row=y, column=x)

# Updated function to plant suitable crops in an entire row or column based on conditions
def plant_specific_plants():
    selected_weather = weather_dropdown.get()
    selected_soil = soil_dropdown.get()
    selected_plants = get_suitable_plants(selected_weather, selected_soil)

    row = int(row_entry.get())
    column = int(column_entry.get())

    planting_choice = planting_choice_var.get()  # Get planting choice (row or column)

    for plant in selected_plants:
        if planting_choice == "Row":
            for x in range(garden_width):
                if garden[row][x] == "Empty":
                    garden[row][x] = plant
        elif planting_choice == "Column":
            for y in range(garden_height):
                if garden[y][column] == "Empty":
                    garden[y][column] = plant

    # Update the garden display
    display_garden()

# Create the main application window
root = tk.Tk()
root.title("Virtual Garden Planner")

# Create a main frame for the application
main_frame = tk.Frame(root)
main_frame.pack()

# Layout GUI components
plant_listbox_label = tk.Label(main_frame, text="Select a plant:", bg="#DAE0E6", font=("Arial", 14), fg="black")
plant_listbox_label.grid(row=0, column=0)

plants = list(plant_database.keys())
plant_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=("Arial", 12))
for plant in plants:
    plant_listbox.insert(tk.END, plant)
plant_listbox.grid(row=0, column=1)

row_label = tk.Label(main_frame, text="Enter the row number:", bg="#DAE0E6", font=("Arial", 14), fg="black")
row_label.grid(row=1, column=0)
row_entry = tk.Entry(main_frame, font=("Arial", 12))
row_entry.grid(row=1, column=1)

column_label = tk.Label(main_frame, text="Enter the column number:", bg="#DAE0E6", font=("Arial", 14), fg="black")
column_label.grid(row=2, column=0)
column_entry = tk.Entry(main_frame, font=("Arial", 12))
column_entry.grid(row=2, column=1)

# Create a StringVar to hold the planting choice (row or column)
planting_choice_var = tk.StringVar(main_frame)
planting_choice_var.set("Row")  # Set a default value (can be "Row" or "Column")

# Add radio buttons or dropdowns to choose between planting in a row or column
radio_button_row = tk.Radiobutton(main_frame, text="Plant in Row", variable=planting_choice_var, value="Row", font=("Arial", 12), fg="black")
radio_button_row.grid(row=3, column=0)
radio_button_column = tk.Radiobutton(main_frame, text="Plant in Column", variable=planting_choice_var, value="Column", font=("Arial", 12), fg="black")
radio_button_column.grid(row=3, column=1)

plant_specific_button = tk.Button(main_frame, text="Plant at Specific Position", command=plant_specific_plants, font=("Arial", 12))
plant_specific_button.grid(row=4, column=0, columnspan=2)

care_instructions_label = tk.Label(main_frame, text="Care Instructions for selected plant will be displayed here.", bg="#DAE0E6", font=("Arial", 12), fg="black")
care_instructions_label.grid(row=5, column=0, columnspan=2)

# Create a frame for weather and soil conditions
conditions_frame = tk.Frame(main_frame, pady=10)  # Adjust the padding as needed
conditions_frame.grid(row=6, column=0, columnspan=2)

weather_conditions = ['Sunny', 'Rainy', 'Cloudy', 'Windy']
soil_conditions = ['Clay', 'Sandy', 'Loamy', 'Rocky']

weather_label = tk.Label(conditions_frame, text="Select Weather Condition:", bg="#DAE0E6", font=("Arial", 14), fg="black")
weather_label.grid(row=0, column=0)
weather_dropdown = tk.StringVar(conditions_frame)
weather_dropdown.set(weather_conditions[0])  # Set a default weather condition
weather_menu = tk.OptionMenu(conditions_frame, weather_dropdown, *weather_conditions)
weather_menu.grid(row=0, column=1)

soil_label = tk.Label(conditions_frame, text="Select Soil Condition:", bg="#DAE0E6", font=("Arial", 14), fg="black")
soil_label.grid(row=1, column=0)
soil_dropdown = tk.StringVar(conditions_frame)
soil_dropdown.set(soil_conditions[0])  # Set a default soil condition
soil_menu = tk.OptionMenu(conditions_frame, soil_dropdown, *soil_conditions)
soil_menu.grid(row=1, column=1)

# Bind the function to the plant_listbox selection event
plant_listbox.bind('<<ListboxSelect>>', display_care_instructions)

# Display the garden initially
display_garden()

# Start the GUI event loop
root.mainloop()
