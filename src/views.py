
from datetime import datetime
from flask import render_template
from src import app

@app.context_processor
def inject_globals():
    company = "Thriftable"
    return {
        "company": company,
        "year": 2025,
        "phone": '+27 (0) 78 735 2242',
        "title": 'Your Gateway to Adventure!',
        "email": 'hello@thriftable.co.za',
        "address": "395 Francis Baard Street</p><p>Pretoria Central, 0001/2</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/features")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/tos")
def tos():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

