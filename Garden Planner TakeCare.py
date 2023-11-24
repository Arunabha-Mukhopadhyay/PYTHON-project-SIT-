import tkinter as tk

# Initialize the garden plot as a 2D grid
garden_width = 10
garden_height = 10
garden = [["Empty" for _ in range(garden_width)] for _ in range(garden_height)]

# Plant database with emojis and care instructions for various plants
plant_database = {
    "Tomato": {
        "emoji": "🍅",
        "care": "Tomatoes require full sun and regular watering. Use stakes for support as they grow."
    },
    "Carrot": {
        "emoji": "🥕",
        "care": "Carrots need well-drained soil and consistent watering. Thin seedlings to avoid crowding."
    },
    "Potato": {
        "emoji": "🥔",
        "care": "Plant potatoes in loose, well-draining soil. Hill the soil around the plants as they grow."
    },
    "Lettuce": {
        "emoji": "🥬",
        "care": "Lettuce prefers partial shade and consistent moisture. Harvest outer leaves for continued growth."
    },
    "Cucumber": {
        "emoji": "🥒",
        "care": "Cucumbers need ample sunlight and regular watering. Provide support for climbing varieties."
    },
    "Bell Pepper": {
        "emoji": "🫑",
        "care": "Bell peppers require full sun and regular watering. Pick them when they reach desired size and color."
    },
    "Eggplant": {
        "emoji": "🍆",
        "care": "Eggplants need warm temperatures and well-drained soil. Harvest fruits before they become too mature."
    },
    "Zucchini": {
        "emoji": "🥒",
        "care": "Zucchinis require consistent watering and fertile soil. Harvest them when they're young for best flavor."
    },
    # Add more plants with emojis and care instructions as needed
}


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

# Function to plant a selected plant in an entire row or column
def plant_specific_plants():
    selected_plant = plant_listbox.get(tk.ACTIVE)
    row = int(row_entry.get())
    column = int(column_entry.get())

    planting_choice = planting_choice_var.get()  # Get planting choice (row or column)

    if selected_plant in plant_database:
        if planting_choice == "Row":
            for x in range(garden_width):
                if garden[row][x] == "Empty":
                    garden[row][x] = selected_plant
        elif planting_choice == "Column":
            for y in range(garden_height):
                if garden[y][column] == "Empty":
                    garden[y][column] = selected_plant

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

# Bind the function to the plant_listbox selection event
plant_listbox.bind('<<ListboxSelect>>', display_care_instructions)

# Display the garden initially
display_garden()

# Start the GUI event loop
root.mainloop()
