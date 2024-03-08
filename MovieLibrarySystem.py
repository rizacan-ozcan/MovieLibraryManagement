class User:
    def __init__(self, name, surname, username, email, password):
       self.name = name
       self.surname = surname
       self.username = username
       self.email = email
       self.password = password

    def show_info(self):
        print(f"""User Information
            Name : {self.name}
            Surname : {self.surname}
            Username : {self.username}
            E-Mail : {self.email}
            Password : ********* 
        """)

    def update_information(self):
        new_name = input("Enter the new name of the user (if you enter blank, it will remain same): ")
        new_surname = input("Enter the new surname of the user (if you enter blank, it will remain same): ")
        new_username = input("Enter the new username of the user (if you enter blank, it will remain same): ")
        new_email = input("Enter the new mail of the user (if you enter blank, it will remain same): ")
        new_password = input("Enter the new password of the user (if you enter blank, it will remain same): ")

        if new_name:
            self.name = new_name
        if new_surname:
            self.surname = new_surname
        if new_username:
            self.username = new_username
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        print("The user information has been successfully updated.")


class Director:
    def __init__(self, director_name_surname, birth_date):
        self.director_name_surname = director_name_surname
        self.birth_date = birth_date

    def show_info(self):
        print(f"""Director Information
            Director Name and Surname : {self.director_name_surname}
            Birth Date : {self.birth_date}
        """)

    def update_information(self):
        new_director_name_surname = input("Enter the new name and surname of the director (if you enter blank, it will remain same): ")
        new_birth_date = input("Enter the new birth date of the director (if you enter blank, it will remain same): ")

        if new_director_name_surname:
            self.director_name_surname = new_director_name_surname
        if new_birth_date:
            self.birth_date = new_birth_date
        print("The director information has been successfully updated")

class Movie:
    def __init__(self, title, director_name_surname, release_date, genre):
        self.title = title
        self.director_name_surname = director_name_surname
        self.release_date = release_date
        self.genre = genre

    def show_info(self):
        print("Movie Information: ")
        print(f"""
            Title : {self.title}
            Director : {self.director_name_surname}
            Release Date : {self.release_date}
            Genre : {self.genre}
        """)

    def update_information(self):
        new_title = input("Enter the new title of the movie (if you enter blank, it will remain same): ")
        new_director_name_surname = input("Enter the new director name and surname of the movie (if you enter blank, it will remain same): ")
        new_release_date = input("Enter the new release date of the movie (if you enter blank, it will remain same): ")
        new_genre = input("Enter the new genre of the movie (if you enter blank, it will remain same): ")
        if new_title:
            self.title = new_title
        if new_director_name_surname:
            director = next((director for director in movieLibrary.directors if new_director_name_surname == director.director_name_surname), None)
            if director:
                self.director_name_surname = new_director_name_surname
            else:
                print("The director you entered could not been found, please add a director then update the movie information.")
        if new_release_date:
            self.release_date = new_release_date
        if new_genre:
            self.genre = new_genre
        print("The movie information has been successfully updated.")

class MovieLibrary:
    def __init__(self):
        self.users = []
        self.movies = []
        self.directors = []

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.username} has been added to the system.")

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"{movie.title} has been added to the system.")

    def add_director(self, director):
        self.directors.append(director)
        print(f"{director.director_name_surname} has been added to the system.")

    def show_users(self):
        print("\nAll Users: ")
        for user in self.users:
            user.show_info()

    def show_movies(self):
        print("\nAll Movies: ")
        for movie in self.movies:
            movie.show_info()

    def show_directors(self):
        print("\nAll Directors: ")
        for director in self.directors:
            director.show_info()

    def delete_user(self, username):
        user = next((user for user in self.users if username == user.username), None)
        if user:
            self.users.remove(user)
            print(f"{username} has been deleted from the system.")
        else:
            print("User could not been found.")

    def delete_movie(self, title):
        movie = next((movie for movie in self.movies if title == movie.title), None)
        if movie:
            self.movies.remove(movie)
            print(f"{title} has been deleted from the system.")
        else:
            print("Movie could not been found.")

    def delete_director(self, director_name_surname):
        director = next((director for director in self.directors if director.director_name_surname == director_name_surname), None)
        if director:
            self.directors.remove(director)
            print(f"{director_name_surname} has been deleted from the system.")
        else:
            print("Movie could not been found.")

    def search_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
            else:
                print(f"{title} could not been found.")

    def search_director(self, director_name_surname):
        for director in self.directors:
            if director.director_name_surname == director_name_surname:
                return director
            else:
                print(f"[{director_name_surname} could not been found.")

    def update_user(self, username):
        user = next((user for user in self.users if username == user.username), None)
        if user:
            user.update_information()
        else:
            print("User could not been found.")

    def update_movie(self, title):
        movie = next((movie for movie in self.movies if movie.title == title), None)
        if movie:
            movie.update_information()
        else:
            print("Movie could not been found.")

    def update_director(self, director_name_surname):
        director = next((director for director in self.directors if director.director_name_surname == director_name_surname), None)
        if director:
            director.update_information()
        else:
            print("Director could not been found.")


movieLibrary = MovieLibrary()

while True:
    print(20 * "*", "Movie Library System", 20 * "*")
    print("""
        1. Add User
        2. Add Movie
        3. Add Director
        4. User List
        5. Movie List
        6. Director List
        7. Delete User
        8. Delete Movie
        9. Delete Director
        10. Update User
        11. Update Movie
        12. Update Director
        13. Search Movie
        14. Search Director
        15. Exit
    """)

    action = input("Enter the action from the list you wanted to perform: ")
    if action == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        email = input("E-Mail: ")
        password = input("Password: ")
        user = User(name, surname, username, email, password)
        movieLibrary.add_user(user)

    elif action == "2":
        title = input("Title: ")
        director_name_surname = input("Director Name Surname: ")
        release_date = input("Release Date: ")
        genre = input("Genre: ")
        movie = Movie(title, director_name_surname, release_date, genre)
        director = next((director for director in movieLibrary.directors if director_name_surname == director.director_name_surname), None)
        if director:
            movie = Movie(title, director_name_surname, release_date, genre)
            movieLibrary.add_movie(movie)
        else:
            print("The director you entered could not been found, please add a director then update the movie information.")

    elif action == "3":
        director_name_surname = input("Director Name Surname: ")
        birth_date = input("Birth Date: ")
        director = Director(director_name_surname, birth_date)
        movieLibrary.add_director(director)

    elif action == "4":
        movieLibrary.show_users()

    elif action == "5":
        movieLibrary.show_movies()

    elif action == "6":
        movieLibrary.show_directors()

    elif action == "7":
        username = input("Enter the username you wanted to delete: ")
        movieLibrary.delete_user(username)

    elif action == "8":
        title = input("Enter the title you wanted to delete: ")
        movieLibrary.delete_movie(title)

    elif action == "9":
        director_name_surname = input("Enter the director name surname you wanted to delete: ")
        movieLibrary.delete_director(director_name_surname)

    elif action == "10":
        username = input("Enter the username you wanted to update: ")
        movieLibrary.update_user(username)

    elif action == "11":
        title = input("Enter the title you wanted to update: ")
        movieLibrary.update_movie(title)

    elif action == "12":
        director_name_surname = input("Enter the director name surname you wanted to update: ")
        movieLibrary.update_director(director_name_surname)

    elif action == "13":
        title = input("Search movie: ")
        movie = movieLibrary.search_movie(title)
        if movie:
            print(movie.show_info())
        else:
            print("You entered an invalid title, please try again.")

    elif action == "14":
        director_name_surname = input("Search director: ")
        director = movieLibrary.search_director(director_name_surname)
        if director:
            print(director.show_info)
        else:
            print("You entered an invalid director name, please try again.")

    elif action == "15":
        print("You are exiting the system... ")
        break

    else:
        print("You have entered an incorrect action, please try again.")