from flask import Flask, render_template, request
from Weather import main as get_weather_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    final_weather_data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        final_weather_data = get_weather_data(city, state, country)

    return render_template('index.html', final_weather_data=final_weather_data)

if __name__ == "__main__":
    app.run(debug=True)