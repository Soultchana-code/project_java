class UserManagement:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        if username not in self.users:
            self.users[username] = {"password": password, "email": email, "profile": {}}
            return f"User {username} registered successfully."
        return "Username already exists."

    def login_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return f"Welcome, {username}!"
        return "Invalid username or password."

    def update_profile(self, username, info):
        if username in self.users:
            self.users[username]["profile"].update(info)
            return f"Profile for {username} updated."
        return "User not found."