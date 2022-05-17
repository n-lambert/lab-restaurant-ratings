"""Restaurant rating lister."""

# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant

def test_score():
    rating_list = [1, 2, 3, 4, 5]
    while True:
        try:
            score = int(input("What is its score? "))
            if score in rating_list:
                return score
            else:
                print("Please provide a number 1-5. ") 
                continue
        except ValueError:
                print("Not a valid number, please try again")



def restaurant_score(data_file):
    input_file = open(data_file)
    restaurants_rating = {}
    for line in input_file:
        line = line.rstrip()
        words = line.split(":")
        restaurants_rating[words[0]] = words[1]

    new_restaurant = input("What is the restaurant? ")

    new_score = test_score()
            
    restaurants_rating[new_restaurant] = new_score

    sorted_restaurants = sorted(restaurants_rating.keys())
    for restaurant in sorted_restaurants:
        print(f'{restaurant} is rated at {restaurants_rating[restaurant]}')

restaurant_score("scores.txt")

"""
ask the user for a restaurant name
if the restaurant name == one of our restaurants
then we need to reassign the value or add in the restauarnt with the value
"""
