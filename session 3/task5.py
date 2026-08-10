ratings = ['4.5', '3.0', '5', '4.2']

ratings_float = [float(rating) for rating in ratings]

highest_rating = max(ratings_float)

print("Ratings:", ratings_float)
print("Highest Rating:", highest_rating)