import random
import tkinter as tk
from tkinter import ttk
import json
import csv


def generate_random_vector_between(start, end):
    return [random.uniform(start[i], end[i]) for i in range(len(start))]


def Vahiable_Definition():
    table_m_headers = ["v1", "v2", "v3", "v4", "v5"]
    m1 = [0, 0, 0, 0, +30]
    m2 = [-2, -2, -2, -2, +50]
    m3 = [-4, -3, -2, +1, +52]
    s1 = [generate_random_vector_between(m1, m2) for _ in range(15)]
    s2 = [generate_random_vector_between(m2, m3) for _ in range(15)]
    mp = {"table_m_headers": table_m_headers, "data": [m1] + s1 + [m2] + s2 + [m3]}
    return mp


def show_in_window():
    mp = Vahiable_Definition()

    window = tk.Tk()
    window.title("Measurement Data")

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Set the window dimensions
    window_width = int(screen_width * 0.8)  # You can adjust this as needed
    window_height = int(screen_height * 0.8)  # You can adjust this as needed

    window.geometry(f"{window_width}x{window_height}")

    # Create the treeview with the correct number of columns
    tree = ttk.Treeview(window, columns=("Measurement Data", *mp["table_m_headers"]))

    # Set the heading for the first column (Measurement Data)
    tree.heading("#1", text="Measurement Data")

    for i, header in enumerate(mp["table_m_headers"]):
        tree.heading("#{}".format(i + 2), text=header)
        tree.column("#{}".format(i + 2), width=60)  # Adjust the width as needed

    current_measurement = ""
    for data in mp["data"]:
        if isinstance(data, list):
            tree.insert("", "end", values=(current_measurement, *data))
        else:
            current_measurement = data
            tree.insert("", "end", values=(current_measurement,))

    tree.pack(fill=tk.BOTH, expand=True)

    window.mainloop()


def save_window_to_JSON(mp):
    with open("measurement_data.json", "w") as json_file:
        json.dump(mp, json_file, indent=4)


def save_window_to_csv(mp):
    with open("measurement_data.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(["Measurement Data", *mp["table_m_headers"]])

        current_measurement = ""
        for data in mp["data"]:
            if isinstance(data, list):
                csv_writer.writerow([current_measurement, *data])
            else:
                current_measurement = data
                csv_writer.writerow([current_measurement])


if __name__ == '__main__':
    mp = Vahiable_Definition()
    show_in_window()
    save_window_to_JSON(mp)
    save_window_to_csv(mp)

