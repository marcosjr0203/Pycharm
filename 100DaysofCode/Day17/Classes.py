class User:
    def __init__(self, user_id, username):
        # initialize attributes
        self.id = user_id
        self.username = username
        self.followers = 235  # If there's a default value, it doesn't have to be declared when the class is called.
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "marcosjr0203")  # everytime you call the class, the function __init__ will be called
print(user_1.id, "-", user_1.username, user_1.followers)

user_2 = User("002", "sabertulucci")  # everytime you call the class, the function __init__ will be called
print(user_2.id, "-", user_2.username, user_2.followers)

user_1.follow(user_2) # command to set a new follower to the user 2
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")
