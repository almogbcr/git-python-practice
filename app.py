from datetime import datetime


def greet(name):
	timenow = datetime.now().strftime("%Y-%m-%d %H:%M")

	return f"Hello , {name} {timenow}!"


if __name__ == "__main__":
	user = "Almog"
	print(greet(user))
