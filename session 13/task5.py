app_status = "Offline"


def check_status():
    user_status = "Online"

    print("During function - User status:", user_status)
    print("During function - App status:", app_status)


print("Before function - App status:", app_status)

check_status()

print("After function - App status:", app_status)
