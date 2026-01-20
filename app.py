from datetime import datetime


def greet(name):
	now = datetime.now().strftime("%Y-%m-%d %H:%M")

	return f"{now}: Hello , {name}!"


if __name__ == "__main__":
	user = "Almog"
	print(greet(user))
