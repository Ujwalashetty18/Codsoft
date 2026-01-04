ratings = {
    "Alice": {"Avengers": 5, "Titanic": 3, "Inception": 4},
    "Bob": {"Avengers": 4, "Titanic": 5, "Notebook": 4},
    "Charlie": {"Inception": 5, "Interstellar": 4, "Avengers": 4},
    "David": {"Titanic": 4, "Notebook": 5}
}

def similarity(user1, user2):
    common_movies = set(user1.keys()) & set(user2.keys())

    if not common_movies:
        return 0

    score = 0
    for movie in common_movies:
        score += 1 - abs(user1[movie] - user2[movie]) / 5

    return score


def recommend_movies(target_user, ratings):
    target_ratings = ratings[target_user]
    scores = {}

    for user, user_ratings in ratings.items():
        if user != target_user:
            sim = similarity(target_ratings, user_ratings)
            scores[user] = sim

    similar_user = max(scores, key=scores.get)

    recommendations = []
    for movie in ratings[similar_user]:
        if movie not in target_ratings:
            recommendations.append(movie)

    return recommendations, similar_user


# -------- MAIN PROGRAM --------
user_name = input("Enter user name (Alice/Bob/Charlie/David): ")

if user_name in ratings:
    recs, similar_user = recommend_movies(user_name, ratings)

    print(f"\nMost similar user: {similar_user}")

    if recs:
        print("Recommended movies:")
        for movie in recs:
            print("-", movie)
    else:
        print("No new recommendations available.")
else:
    print("User not found.")
