from datetime import datetime


def greet(name):
	cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	return f"Hello , {name} {cTime}!"


if __name__ == "__main__":
	user2 = "John"
	print(greet(user2))
	user = "Almog"
	print(greet(user))
