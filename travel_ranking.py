
import pandas as pd
data = pd.read_csv("Top Indian Places to Visit.csv")

def find_places(city):
    
    places = data[(data['City'].str.lower() == city.lower()) &
                  (data['time needed to visit in hrs'] <= 3.0)]
    
    if places.empty:
        return f"No quick places found in {city}"
    
    top_places = places.sort_values('Google review rating', ascending=False).head(5)
    result = f"Best Weekend Places in {city}:\n"
    
    for i, place in top_places.iterrows():
        result += f"- {place['Name']} (Rating: {place['Google review rating']})\n"
    return result

city_name = input("What city do you want to visit? ")
print(find_places(city_name))