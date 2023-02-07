from flask import Flask, render_template

app = Flask(__name__)  # __name__ is the module's name

posts = [
    {
        "name": "Marcus Smart",
        "position": "PG",
        "HT_WT": "1.93 m, 99 kg",
        "DRAFT_INFO": "2014: Rd 1, Pk 6 (BOS)",
    },
    {
        "name": "Jaylen Brown",
        "position": "SG",
        "HT_WT": "1.98 m, 101 kg",
        "DRAFT_INFO": "2016: Rd 1, Pk 3 (BOS)",
    },
    {
        "name": "Jayson Tatum",
        "position": "SF",
        "HT_WT": "2.03 m, 95 kg",
        "DRAFT_INFO": "2017: Rd 1, Pk 3 (BOS)",
    },
    {
        "name": "Al Horford",
        "position": "C",
        "HT_WT": "2.06 m, 108 kg",
        "DRAFT_INFO": "2007: Rd 1, Pk 3 (ATL)",
    },
    {
        "name": "Robert Williams III",
        "position": "C",
        "HT_WT": "2.06 m, 107 kg",
        "DRAFT_INFO": "2018: Rd 1, Pk 27 (BOS)",
    }
]

# cancel this commit
@app.route("/")  # the root page
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
