from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)  # __name__ is the module's name

app.config['SECRET_KEY'] = '17c07ed30ca9cfaecbe544a2a44c6175'

# test
# posts = [
#     {
#         "name": "Marcus Smart",
#         "position": "PG",
#         "HT_WT": "1.93 m, 99 kg",
#         "DRAFT_INFO": "2014: Rd 1, Pk 6 (BOS)",
#     },
#     {
#         "name": "Jaylen Brown",
#         "position": "SG",
#         "HT_WT": "1.98 m, 101 kg",
#         "DRAFT_INFO": "2016: Rd 1, Pk 3 (BOS)",
#     },
#     {
#         "name": "Jayson Tatum",
#         "position": "SF",
#         "HT_WT": "2.03 m, 95 kg",
#         "DRAFT_INFO": "2017: Rd 1, Pk 3 (BOS)",
#     },
#     {
#         "name": "Al Horford",
#         "position": "C",
#         "HT_WT": "2.06 m, 108 kg",
#         "DRAFT_INFO": "2007: Rd 1, Pk 3 (ATL)",
#     },
#     {
#         "name": "Robert Williams III",
#         "position": "C",
#         "HT_WT": "2.06 m, 107 kg",
#         "DRAFT_INFO": "2018: Rd 1, Pk 27 (BOS)",
#     },
# ]

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")  # the root page
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)

if __name__ == "__main__":
    app.run(debug=True)
