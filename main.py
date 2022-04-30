from flask import Flask,render_template,request
import requests
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weathercity.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Weather(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    city = db.Column(db.String(50),nullable=False)

@app.route("/",methods=['GET','POST'])
def main():
    if request.method=='POST':
        city_searched = request.form['city']
        if city_searched:
            city_alreadypresent = Weather.query.filter_by(city = city_searched).first()
            if city_alreadypresent == None:
                new_city_inDB = Weather(city = city_searched)
                db.session.add(new_city_inDB)
                db.session.commit()
    cities = Weather.query.all()
    all_city_data = []
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city.city}&units=metric&appid=16f1ae461349d7fd01609f794ed8c775" # Get API key on openweathermaporg
        response = requests.get(url)
        text = response.json()
        print(text)
        try:
            city_data = {
                'city':text['name'],
                'description':text['weather'][0]['description'],
                'temperature':text['main']['temp'],
                'country': text['sys']['country'],
                'icon':text['weather'][0]['icon']
            }
        except:
            city_data = {
                'city': "The city is not available on the API, Make sure you have entered the correct city name",
                'description': "city not available",
                'temperature': "NA",
                'country': "NA",
                'icon': ""
                
            }
        all_city_data.append(city_data)
            
    print(all_city_data)
    return render_template("index.html",all_city_data=all_city_data)


if __name__=="__main__":
    app.run(debug=True)
