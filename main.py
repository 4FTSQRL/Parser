"""
    Author: 4FTSQRL
    
    Usage: python main.py
    
    Description: Parser for converting CSV file to JSON
"""
# Import statements
# Panads
import pandas

# json
import json

# request
import requests

# url lib
import urllib

# Main Function
def main():
    
    # Calling functions
    data = addCountry()
    createJSON(data)

# add country Function
def addCountry():
    
    # File Path (change if needed)
    filePath = 'vernlog.csv'
    # reading data
    result = pandas.read_csv(filePath)
    
    # Country list
    country = []
    # Get the geolocations
    for addr in result['clientaddr']:
        country.append(geolocator(addr))
    
    result['Country']=country
    jsonConvesion = (result.to_json(orient="index",indent=4))
    return jsonConvesion
    
# add geocator
def geolocator(ipAddr):
    
    # Get the API info from ipINFO
    with urllib.request.urlopen('https://ipinfo.io/' + ipAddr + '/json') as url:
        data=json.loads(url.read().decode())
        # Return the country only
        return data['country']
    
# Create JSON file
def createJSON(csvData):
    # Get a file name (change if needed)
    jsonName = 'vernlog.json'
    
    with open(jsonName, 'w') as file:
        file.write(csvData)
    

# Python Incantation
if __name__ == "__main__":
    main()