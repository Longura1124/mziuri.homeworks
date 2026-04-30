from flask import Flask, render_template

app = Flask(__name__)

profiles = [
    {"name": "jasurbeki", "surname": "iaxshiboevi", "img": "earth.jpg"},
    {"name": "iago", "surname": "xvichia", "img": "cat.jpg"}
]

movies = [
    {"id": 1,"title": "12 angry man", "rating": 4.3 , "img": "movie1.jpeg"},
    {"id": 2,"title": "Whiplash", "rating": 4.1 , "img": "movie2.jpg"},
    {"id": 3,"title": "12 angry man", "rating": 4.7 , "img": "movie3.jpg"}
]

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie_details.html", movie = movie)
    return "movie not found"

@app.route("/")
def home():
    return render_template("index.html", movies = movies)



@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template("profile.html", profile=profile)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/genre/<category>")
def show_genre(category):
    return render_template("genre.html", c=category)


app.run(debug=True)