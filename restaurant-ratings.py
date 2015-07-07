
# make dictionary - split on ':'
restaurant_ratings = {}
ratings_file = open('scores.txt')

for line in ratings_file:
    stripped_line = line.rstrip()
    line_list = stripped_line.split(":")
    restaurant = line_list[0]
    rating = line_list[1]
    restaurant_ratings[restaurant] = rating

sorted_restaurant_ratings = sorted(restaurant_ratings)

for restaurant in sorted_restaurant_ratings:
    print "%s is rated at %s." % (restaurant, restaurant_ratings[restaurant])




# convert to formatted list
# sort list
# print list
