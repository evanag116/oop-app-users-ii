from datetime import datetime

class User:
    all_posts = {}
    def __init__(self, name, email_address, phone_number, age):
        self.name = name
        self.email_address = email_address
        self.phone_number = str(phone_number)
        self.age = age

    def post(self, str):
        time = (datetime.now()).strftime("%H:%M:%S")
        self.all_posts[str] = time

    def delete(self, str):
        self.all_posts.pop(str)

    def get_all_posts(self):
        return self.all_posts


    
    


nathan = User("Nathan", "nathan@codeplatoon.org", 1231231230)


evan = User("Evan", "evan@codeplatoon.org", 5027152210, 23)

evan.post("my first post")
evan.post("my second post")
evan.post("my third post")
evan.delete("my second post")

print(evan.get_all_posts())
