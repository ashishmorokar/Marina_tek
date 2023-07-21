import tkinter as tk
from tkinter import ttk

class MovieSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movies@Mariana Tek")
        self.movies_schedule = []
        self.filtered_movies = []

        self.filter_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.filter_var.trace("w", self.filter_movies)
        self.search_var.trace("w", self.search_movies)

        self.filter_options = []
        self.create_widgets()

    def create_widgets(self):
        self.filter_label = tk.Label(self.root, text="Filter by Genre:")
        self.filter_label.pack()
        self.filter_combo = ttk.Combobox(self.root, textvariable=self.filter_var, values=self.filter_options, state="readonly")
        self.filter_combo.pack()

        self.search_label = tk.Label(self.root, text="Search by Title:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.root, textvariable=self.search_var)
        self.search_entry.pack()

        self.movies_listbox = tk.Listbox(self.root, height=15, width=70)
        self.movies_listbox.pack()

        self.load_movies_schedule()

    def load_movies_schedule(self):
        # Simulated movie schedule data
        self.movies_schedule = [
            {"Title": "Movie A", "Poster": "Poster_A.jpg", "Genre": ["Action", "Adventure"], "Rating": "PG-13", "Year Release": 2021, "Metacritic Rating": 75, "Runtime": "2h 15m"},
            {"Title": "Movie B", "Poster": "Poster_B.jpg", "Genre": ["Comedy", "Romance"], "Rating": "PG", "Year Release": 2022, "Metacritic Rating": 82, "Runtime": "1h 45m"},
            {"Title": "Movie C", "Poster": "Poster_C.jpg", "Genre": ["Drama"], "Rating": "R", "Year Release": 2023, "Metacritic Rating": 88, "Runtime": "2h 5m"},
            # Add more movies here...
        ]

        self.filtered_movies = self.movies_schedule
        self.update_filter_options()
        self.update_movies_listbox()

    def update_filter_options(self):
        genres_set = set()
        for movie in self.movies_schedule:
            genres_set.update(movie["Genre"])

        self.filter_options = sorted(list(genres_set))
        self.filter_combo["values"] = self.filter_options

    def update_movies_listbox(self):
        self.movies_listbox.delete(0, tk.END)
        for movie in self.filtered_movies:
            self.movies_listbox.insert(tk.END, movie["Title"])

    def filter_movies(self, *args):
        selected_genre = self.filter_var.get()

        if selected_genre:
            self.filtered_movies = [movie for movie in self.movies_schedule if selected_genre in movie["Genre"]]
        else:
            self.filtered_movies = self.movies_schedule

        self.update_movies_listbox()

    def search_movies(self, *args):
        search_string = self.search_var.get()

        if search_string:
            self.filtered_movies = [movie for movie in self.movies_schedule if search_string.lower() in movie["Title"].lower()]
        else:
            self.filtered_movies = self.movies_schedule

        self.update_movies_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieSchedulerApp(root)
    root.mainloop()
