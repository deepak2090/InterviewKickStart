from flask import Flask, render_template

app = Flask(__name__)

# Hardcoded data for categories and items
data = {
    "Electronics": ["Laptop", "Smartphone", "Tablet"],
    "Books": ["Python Programming", "Data Science", "Machine Learning"],
    "Clothing": ["T-shirt", "Jeans", "Jacket"]
}

@app.route('/')
def index():
    categories = data.keys()  # Get all category names for the dropdown
    return render_template('index.html', categories=categories, data=data)

if __name__ == '__main__':
    app.run(debug=True)
