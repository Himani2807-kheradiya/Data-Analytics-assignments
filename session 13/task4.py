def count_likes(posts):
    total = posts.get("likes", 0)

    replies = posts.get("replies", [])

    for reply in replies:
        total += count_likes(reply)

    return total


posts = {
    "likes": 100,
    "replies": [
        {
            "likes": 50,
            "replies": [
                {
                    "likes": 20,
                    "replies": []
                },
                {
                    "likes": 10,
                    "replies": []
                }
            ]
        },
        {
            "likes": 30,
            "replies": []
        }
    ]
}

print("Total likes:", count_likes(posts))