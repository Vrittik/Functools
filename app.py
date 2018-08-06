from flask import Flask,render_template
app=Flask(__name__)
posts=[

    {
        "author":"Vrittik Sharma",
        "Title":"Love and lust",
        "Content":"The first blog",
        "date":"May 29, 2000"
    },
    {
        "author": "Vishakha Sharma",
        "Title": "deepak's story",
        "Content": "The second blog",
        "date": "August 29, 1998"
    }
]


@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def verify():
    return render_template("home.html",title="bk",posts=posts) #provide an argument to the html

@app.route("/about",methods=["GET"])
def about():
    return render_template("about.html",title="HERO",posts=posts)

app.run()