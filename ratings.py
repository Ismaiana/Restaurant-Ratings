"""Restaurant rating lister."""


# put your code here

data = open("scores.txt")

ratings_restaurant = {}

name = " "

score = 0

def new_restaurant(name, score):

    name = input("Please type the restaurante name > ")
    score = input("Please type the rate > ")

    ratings_restaurant[name] = score

new_restaurant(name, score)


def sorted_ratings(data):

    for line in data:
        #Florean Fortescue's Ice Cream Parlour:4

        sections = line.split(":")
        
        if sections[0] not in ratings_restaurant:
            ratings_restaurant[sections[0]] = sections[1]

        # if line not in ratings_restaurant:

        # ratings_restaurant[string_restaurant_name] = rating_integer

        #     ratings_restaurant[line] = 1

        # else:
        #     ratings_restaurant[string_restaurant_name] += 1 rating_integer

    for restaurant, rate in sorted(ratings_restaurant.items()):
        print(f'restaurant is {restaurant} and rate is {rate}')
        

    

sorted_ratings(data)

