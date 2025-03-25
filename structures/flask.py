FLASK_STRUCTURE = [
    "app/static",
    "app/templates",
    "app/models",
    "data",
    "notebooks"
]

FLASK_FILES = {
    "README.md": "# Real Estate Forecasting App\n\nThis project uses machine learning models to forecast housing prices across regions using historical data. Built with Flask and Plotly for interactive visualization.\n\n## Features\n- ML-based price forecasting\n- Interactive charts\n- Region-based filtering\n\n## Stack\n- Flask\n- scikit-learn\n- pandas\n- plotly",
    
    "requirements.txt": "flask\npandas\nscikit-learn\nplotly\n",

    "run.py": "from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)",

    "app/__init__.py": "from flask import Flask\n\napp = Flask(__name__)\n\nfrom app import routes",

    "app/routes.py": "from app import app\nfrom flask import render_template\n\n@app.route('/')\ndef index():\n    return render_template('index.html')",

    "app/templates/index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Real Estate Forecast</title>\n</head>\n<body>\n    <h1>Welcome to the Real Estate Forecasting App</h1>\n</body>\n</html>",

    "app/models/forecasting.py": "import pandas as pd\nfrom sklearn.linear_model import LinearRegression\n\ndef train_model(data_path):\n    df = pd.read_csv(data_path)\n    X = df[['year']]\n    y = df['price']\n    model = LinearRegression().fit(X, y)\n    return model",

    "notebooks/eda_and_modeling.ipynb": "",  # Leave empty to be filled manually or via Jupyter
}
