class MovieScheduler:
    def __init__(self):
        self.schedule = {}

    def add_movie(self, date, movie_choices):
        self.schedule[date] = movie_choices

    def display_schedule(self):
        for date, movie_choices in self.schedule.items():
            print(f"{date}:")
            for index, movie in enumerate(movie_choices, start=1):
                print(f"{index}. {movie}")
            print()

    def vote_movie(self, date, choice):
        if date in self.schedule and 1 <= choice <= len(self.schedule[date]):
            movie_choices = self.schedule[date]
            selected_movie = movie_choices[choice - 1]
            print(f"You voted for {selected_movie} on {date}.")
        else:
            print("Invalid date or choice. Please try again.")

if __name__ == "__main__":
    mariana_tek = MovieScheduler()

    # Add movie schedule here
    mariana_tek.add_movie("2023-07-22", ["Movie A", "Movie B", "Movie C"])
    mariana_tek.add_movie("2023-07-23", ["Movie X", "Movie Y", "Movie Z"])
    mariana_tek.add_movie("2023-07-24", ["Movie P", "Movie Q", "Movie R"])

    while True:
        print("Welcome to Movies@Mariana Tek!")
        print("1. View Movie Schedule")
        print("2. Vote for a Movie")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            mariana_tek.display_schedule()
        elif choice == "2":
            date = input("Enter the date of the movie you want to vote for (YYYY-MM-DD): ")
            choice = int(input("Enter the number corresponding to your movie choice: "))
            mariana_tek.vote_movie(date, choice)
        elif choice == "3":
            print("Thank you for participating! Have a great time at the movies!")
            break
        else:
            print("Invalid choice. Please try again.")
