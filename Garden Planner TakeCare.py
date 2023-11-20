import random
import tkinter as tk

# Initialize the garden plot as a 2D grid
garden_width = 10
garden_height = 10
garden = [["Empty" for _ in range(garden_width)] for _ in range(garden_height)]

# a dictionary to store plant information
plant_database = {
    "Tomato": {
        "color": "red",
        "care": "Tomatoes need full sun and regular watering. Provide support for the vines, prune as needed, and watch for pests."
    },
    "Carrot": {
        "color": "orange",
        "care": "Plant carrots in loose, well-drained soil. Keep the soil consistently moist and thin seedlings to the recommended spacing."
    },
    "Potato": {
        "color": "brown",
        "care": "Potatoes thrive in loose, well-drained soil. Plant them in early spring. Keep the soil consistently moist, but avoid overwatering. Hill the soil up around the plants as they grow to encourage tuber development. Potatoes are susceptible to certain pests and diseases, so monitor for issues and take appropriate action if necessary."
    },
    "Brinjal": {
       "color": "purple",
       "care": "Brinjals thrive in warm climates and well-drained soil. Plant them after the last frost date. Provide full sun and consistent watering. Mulch around the plants to retain soil moisture and suppress weeds. Watch for common pests like aphids and use appropriate pest control measures when needed. Harvest when the fruit is glossy and firm."
    },
    "Cabbage": {
        "color": "green",
        "care": "Cabbage prefers cool, well-drained soil and grows best in spring and fall. Plant seeds or seedlings in rows with adequate spacing. Keep the soil consistently moist. Use mulch to retain soil moisture and control weeds. Cabbage is susceptible to cabbage worms; use row covers or natural predators to protect your plants. Harvest when heads are firm and fully developed."
    },
    "Spinach": {
        "color": "blue",
        "care": "Spinach thrives in cool weather and well-drained soil. Plant in early spring or late summer. Keep the soil consistently moist, and provide shade during hot weather to prevent bolting. Harvest the outer leaves as soon as they reach a usable size for a continuous harvest."
    },
    "Zucchini": {
        "color": "yellow",
        "care": "Zucchini needs warm, well-drained soil and plenty of sunlight. Plant seeds or seedlings after the last frost date. Keep the soil consistently moist. Be vigilant for pests like squash bugs and powdery mildew. Harvest when the fruit is young and tender for the best flavor."
    },

    "Cucumber": {
        "color": "light green",
        "care": "Cucumbers thrive in warm weather and well-drained soil. Plant seeds or seedlings after the last frost date. Keep the soil consistently moist. Cucumbers are susceptible to cucumber beetles and mildew; use row covers and natural predators. Harvest when the fruit is firm and of the desired size."
    },

    "wheat": {
        "color": "light yellow",
        "care": "Care for wheat by planting in well-drained soil, providing consistent moisture, fertilizing appropriately, managing weeds, pests, and diseases, and practicing crop rotation to maintain soil health."
    }
    # Add more plants and their care instructions here
}


# Function to display the garden plot
def display_garden():
    for y in range(garden_height):
        for x in range(garden_width):
            plant_info = garden[y][x]
            if plant_info != "Empty":
                plant_color = plant_database[plant_info]["color"]
                cell_label = tk.Label(main_frame, text="  ", bg=plant_color, borderwidth=1, relief="solid", width=3,
                                      height=1)
                cell_label.grid(row=y, column=x)
            else:
                cell_label = tk.Label(main_frame, text="Empty", borderwidth=1, relief="solid", width=10, height=2)
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

# layout GUI components
main_frame.config(bg="#DAE0E6")
plant_listbox_label = tk.Label(main_frame, text="Select a plant:", bg="#DAE0E6", font=("Arial", 14))
plant_listbox_label.grid(row=0, column=0)

plants = list(plant_database.keys())
plant_listbox = tk.Listbox(main_frame, selectmode=tk.SINGLE, font=("Arial", 12))
for plant in plants:
    plant_listbox.insert(tk.END, plant)
plant_listbox.grid(row=0, column=1)

display_button = tk.Button(main_frame, text="Display Garden", command=display_garden, font=("Arial", 12))
display_button.grid(row=0, column=2)

care_instructions_label = tk.Label(main_frame, text="Care Instructions for selected plant will be displayed here.",
                                   bg="#DAE0E6", font=("Arial", 12))
care_instructions_label.grid(row=1, column=0, columnspan=3)

num_plants_label = tk.Label(main_frame, text="Enter the number of plants to plant randomly:", bg="#DAE0E6",
                            font=("Arial", 14))
num_plants_label.grid(row=2, column=0)
num_plants_entry = tk.Entry(main_frame, font=("Arial", 12))
num_plants_entry.grid(row=2, column=1)

plant_button = tk.Button(main_frame, text="Plant Random Plants", command=plant_random_plants, font=("Arial", 12))
plant_button.grid(row=2, column=2)

# Start the GUI event loop
root.mainloop()
