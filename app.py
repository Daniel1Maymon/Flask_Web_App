from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Register', form=form)

if __name__ == "__main__":
    import os
    path = '/root/Environments/Flask_blog'
    os.chdir(path)
    # from pathlib import Path
    # print("File      Path:", Path(__file__).absolute())
    # print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__  
    app.run(debug=True)
