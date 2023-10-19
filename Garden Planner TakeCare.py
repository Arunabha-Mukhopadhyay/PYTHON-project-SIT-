import random
import tkinter as tk

# Initialize the garden plot as a 2D grid
garden_width = 10
garden_height = 10
garden = [["Empty" for _ in range(garden_width)] for _ in range(garden_height)]

# Define a dictionary to store plant information
plant_database = {
    "Tomato": {
        "spacing": 12,
        "care": "Tomatoes need full sun and regular watering. Provide support for the vines, prune as needed, and watch for pests."
    },
    "Carrot": {
        "spacing": 3,
        "care": "Plant carrots in loose, well-drained soil. Keep the soil consistently moist and thin seedlings to the recommended spacing."
    },
    # Add more plants and their care instructions here
}


# Function to display the garden plot
def display_garden():
    for y in range(garden_height):
        for x in range(garden_width):
            cell_value = garden[y][x]
            cell_label = tk.Label(main_frame, text=cell_value, borderwidth=1, relief="solid", width=10, height=2)
            cell_label.grid(row=y, column=x)


# Function to display care instructions for a plant
def display_care_instructions():
    selected_plant = plant_listbox.get(plant_listbox.curselection())
    if selected_plant in plant_database:
        care_instructions = plant_database[selected_plant]["care"]
        care_instructions_label.config(text=f"Care Instructions for {selected_plant}:\n{care_instructions}")


# Function to plant multiple plants at random positions
def plant_random_plants():
    selected_plant = plant_listbox.get(plant_listbox.curselection())
    num_plants = int(num_plants_entry.get())

    for _ in range(num_plants):
        while True:
            x = random.randint(0, garden_width - 1)
            y = random.randint(0, garden_height - 1)
            if garden[y][x] == "Empty":
                garden[y][x] = selected_plant
                break

    display_garden()


# Create the main application window
root = tk.Tk()
root.title("Virtual Garden Planner")

# Create a main frame for the application
main_frame = tk.Frame(root)
main_frame.pack()

# Create and layout GUI components
main_frame.config(bg="#DAE0E6")
plant_listbox_label = tk.Label(main_frame, text="Select a plant:", bg="#DAE0E6", font=("Algerian", 14))
plant_listbox_label.grid(row=0, column=0)

plants = list(plant_database.keys())
plant_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=("Algerian", 12))
for plant in plants:
    plant_listbox.insert(tk.END, plant)
plant_listbox.grid(row=0, column=1)

display_button = tk.Button(main_frame, text="Display Garden", command=display_garden, font=("Algerian", 12))
display_button.grid(row=0, column=2)

care_instructions_label = tk.Label(main_frame, text="Care Instructions for selected plant will be displayed here.",
                                   bg="#DAE0E6", font=("Algerian", 12))
care_instructions_label.grid(row=1, column=0, columnspan=3)

num_plants_label = tk.Label(main_frame, text="Enter the number of plants to plant randomly:", bg="#DAE0E6",
                            font=("Algerian", 14))
num_plants_label.grid(row=2, column=0)
num_plants_entry = tk.Entry(main_frame, font=("Algerian", 12))
num_plants_entry.grid(row=2, column=1)

plant_button = tk.Button(main_frame, text="Plant Random Plants", command=plant_random_plants, font=("Algerian", 12))
plant_button.grid(row=2, column=2)

# Start the GUI event loop
root.mainloop()
