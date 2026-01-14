import datetime 

def greet(name):
	cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return f"Welcome , {name} {cTime}!"

if __name__ == "__main__":
	
	user = "World"
	print(greet(user))
