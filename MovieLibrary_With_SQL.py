import sqlite3

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
             director = MovieLibrary.search_director(new_director_name_surname)
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
        self.connect = sqlite3.connect("movie.db")
        self.cursor = self.connect.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(100),
                SURNAME VARCHAR(100),
                EMAIL VARCHAR(100),
                USERNAME VARCHAR(100),
                PASSWORD VARCHAR(50)
            )                                                        
            ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS DIRECTORS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DIRECTOR_NAME_SURNAME VARCHAR(200),
                BIRTH_DATE INTEGER
            )                
            ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS MOVIES(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE TEXT,
                DIRECTOR_NAME_SURNAME VARCHAR(200),
                RELEASE_DATE INTEGER,
                GENRE VARCHAR(30),
                FOREIGN KEY (DIRECTOR_NAME_SURNAME) REFERENCES DIRECTORS(NAME_SURNAME)
            )
            ''')
        self.connect.commit()
        
    def add_user(self, user):
        self.cursor.execute('INSERT INTO USERS(NAME, SURNAME, USERNAME, EMAIL, PASSWORD) VALUES(?, ?, ?, ?, ?)', (user.name, user.surname, user.email, user.username, user.password))
        self.connect.commit()
        print(f"{user.username} has been added to the system.")
    
    def add_director(self, director):
        self.cursor.execute('INSERT INTO DIRECTORS(DIRECTOR_NAME_SURNAME, BIRTH_DATE) VALUES(?, ?), (director.director_name_surname, director.birth_date)')
        self.connect.commit()
        print(f"{director.director_name_surname} has been added to the system.")
        
    def add_movie(self, movie):
        self.cursor.execute('INSERT INTO MOVIES(TITLE, DIRECTOR_NAME_SURNAME, RELEASE_DATE, GENRE) VALUES(?, ?, ?, ?)', (movie.title, movie.director_name_surname, movie.release_date, movie.genre))
        self.connect.commit()
        print(f"{movie.title} has been added to the system.")
        
    def show_movies(self):
        rows = self.cursor.execute('SELECT * FROM MOVIES').fetchall()
        if len(rows) > 0:
            for row in rows:
                movie = Movie(row[1], row[2], row[3], row[4])
                movie.show_info()
        else:
            print("You have not added any movies to the system.")
            
    def show_users(self):
        rows = self.cursor.execute('SELECT * FROM USERS').fetchall()
        if len(rows) > 0:
            for row in rows:
                user = User(row[1], row[2], row[3], row[4], row[5])
                user.show_info()
        else:
            print("You have not added any user to the system.")
            
    def show_directors(self):
        rows = self.cursor.execute('SELECT * FROM DIRECTORS').fetchall()
        if len(rows) > 0:
            for row in rows:
                director = Director(row[0], row[1])
                director.show_info()
        else:
            print("You have not addded any director the system.")
                
    def delete_user(self, username):
        self.cursor.execute('DELETE FROM USERS WHERE USERNAME = ?', (username,))
        self.connect.commit()
        print(f"{username} has been deleted from the system.")
        
    def delete_director(self, director_name_surname):
        self.cursor.execute('DELETE FROM DIRECTORS WHERE DIRECTOR_NAME_SURNAME = ?', (director_name_surname))
        self.connect.commit()
        print(f"{director_name_surname} has been deleted from the system.")
        
    def delete_movie(self, title):
        self.cursor.execute('DELETE FROM MOVIES WHERE TITLE = ?', (title,))
        self.connect.commit()
        print(f"{title} has been deleted from the system.")
        
    def search_film(self, title):
        movie = self.cursor.execute('SELECT * FROM MOVIES WHERE TITLE = ?', (title, )).fetchone()
        if movie:
            return Movie(movie[0], movie[1], movie[2], movie[3], movie[4])
        return None

    def search_director(self, director_name_surname):
        director = self.cursor.execute('SELECT * FROM DIRECTORS WHERE DIRECTOR_NAME_SURNAME = ?', (director_name_surname,)).fetchone()
        if director:
            return Director(director[0], director[1])
        return None
    
    def update_user(self, username):
        row = self.cursor.execute('SELECT * FROM USERS WHERE USERNAME = ?', (username,)).fetchone()
        if row:
            user = User(row[0], row[1], row[2], row[3], row[4])
            user.update_information()
            self.cursor.execute('UPDATE USERS SET NAME = ?, SURNAME = ?, USERNAME = ?, EMAIL = ?, PASSWORD = ? WHERE USERNAME = ?', (user.name, user.surname, user.username, user.email, user.password, username))
            self.connect.commit()
        else:
            print("User could not been found.")
            
    def update_movie(self, title):
        row = self.cursor.execute('SELECT * FROM MOVIES WHERE TITLE = ?', (title, )).fetchone()
        if row:
            movie = Movie(row[0], row[1], row[2], row[3])
            movie.update_information()
            self.cursor.execute('UPDATE MOVIES SET TITLE = ?, DIRECTOR_NAME_SURNAME, RELEASE_DATE = ?, GENRE = ?, WHERE TITLE = ?', (movie.title, movie.director_name_surname, movie.release_date, movie.genre, title)).fetchone()
            self.connect.commit()
        else:
            print("Movie could not been found.")
            
    def update_director(self, director_name_surname):
        row = self.cursor.execute('SELECT * FROM DIRECTORS WHERE DIRECTOR_NAME_SURNAME = ?', (director_name_surname)).fetchone()
        if row:
            director = Director(row[0], row[1])
            director.update_information()
            self.cursor.execute('UPDATE DIRECTORS SET DIRECTOR_NAME_SURNAME = ?, BIRTH_DATE = ?, WHERE DIRECTOR_NAME_SURNAME = ? ', (director.director_name_surname, director.birth_date, director_name_surname))
            self.connect.commit()
        else:
            print("Director could not been found.")
            
    def close_connection(self):
        self.connect.close()
        
movieLibrary = MovieLibrary()
while True:
    print(20 * "*", "Movie Library Management System", 20 * "*")
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
          13. Search Film
          14. Search Director
          15. Rate the Movie
          16. Exit
          """)
    action = input("Please enter the action you wanted to perform: ")
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
        movieLibrary.add_movie(movie)
        
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
        MovieLibrary.delete_movie(title)
        
    elif action == "9":
        director_name_surname = input("Enter the name surname of the director you wanted to delete: ")
        movieLibrary.delete_director(director_name_surname)
    
    elif action == "10":
        username = input("Enter the username you wanted to update: ")
        movieLibrary.update_user(username)
        
    elif action == "11":
        title = input("Enter the title you wanted to update: ")
        movieLibrary.update_movie(title)
        
    elif action == "12":
        director_name_surname = input("Enter the name surname of the director you wanted to update: ")
        movieLibrary.update_director(director_name_surname)
    
    elif action == "13":
        title = input("Search film: ")
        movie = movieLibrary.search_film(title)
        if movie:
            movie.show_info()
        else:
            print("You have entered a wrong title.")
            
    elif action == "14":
        director_name_surname = input("Search Director: ")
        director = movieLibrary.search_director(director_name_surname)
        if director:
            director.show_info()
        else:
            print("You have entered a wrong title.")
            
    elif action == "15":
        print("You are exiting the system.")
        movieLibrary.close_connection()
        break
    
    else:
        print("You have entered a wrong action, please try again.")