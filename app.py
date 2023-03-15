from flask import Flask , request , jsonify
import requests 
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

#Scrapping
def information(countryName):
    total_res = []
    country = countryName
    url = f"https://www.worldometers.info/coronavirus/country/{country}/"
    response = requests.get(url)
    #it's a HTTP status code , it means "OK"
    if response.status_code == 200 :
        soup = bs(response.content,'html.parser')
        result = soup.find_all('div',class_="maincounter-number")
        for i in result:
            total_res.append(i.find("span").text)
    else:
        total_res.append("No Result")
    return total_res



@app.route('/info/' , methods=["GET"])
def find_info():
    country = request.args.get("country")
    try:
        return jsonify({
            "Total Cases " : information(country)[0],
            "Total Deaths " : information(country)[1],
             "Total Recovered " : information(country)[2]
        })
    except:
        return jsonify({"No Country Found":""})


if __name__=="__main__":
    app.run(debug=True)