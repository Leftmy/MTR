rate = {"Very bad": 1, "Bad": 3, "Average": 6, "Good": 10}

rain_prob = float(input("Enter rain probability: "))
dry_prob = 1-rain_prob
print(f"Rain probability:{rain_prob}; dry probability:{dry_prob}")
forest_prob = rain_prob*rate["Very bad"] + dry_prob*rate["Good"]
house_prob = rain_prob*rate["Bad"] + dry_prob*rate["Average"]
print("Forest probability:",forest_prob,"; house probability:", house_prob)

if(forest_prob < house_prob):
    print("You better stay home today")
else:
    print("You might go to forest")
