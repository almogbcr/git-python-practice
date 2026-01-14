import datetime 

def greet(name):
	cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	return f"Hello , {name} {cTime}!"


if __name__ == "__main__":
	
	user = "Newbie"
	print(greet(user))
