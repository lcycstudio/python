"""Classes"""


class StarCookie:
    def __init__(self, color, weight) -> None:
        self.color = color
        self.weight = weight


star_cookie1 = StarCookie("Red", 16)
print(star_cookie1.weight)
print(star_cookie1.color)
print(star_cookie1.__dict__)
print(StarCookie.__dict__)


# star_cookie1.weight = 15
# star_cookie1.color = "Red"
# print(star_cookie1)
# print(star_cookie1.weight)
# print(star_cookie1.color)

# star_cookie2 = StarCookie()
# star_cookie2.weight = 16
# star_cookie2.color = "Blue"
# print(star_cookie2)
# print(star_cookie2.weight)
# print(star_cookie2.color)


class YouTube:
    def __init__(self, username, subscribers=0) -> None:
        self.username = username
        self.subscribers = subscribers


user1 = YouTube("Lewis", 0)
print(user1.username)
print(user1.subscribers)
