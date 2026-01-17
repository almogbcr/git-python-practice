# Git Python Practice
## Base Assingment
## git log --oneline --graph
>* b7f870b forgot to commit deletions
>* 1409acb Set advanced logs on diffrent folder
>* 3f8c59c remove git-log.txt
>* d0fd01b changed file name
>* 7722b9f added gitdiff log
>* c51b36c added log of bonus
>*   13c72cd decided to go with feature changes
>|\  
>| * f9e0246 Changed string formating on add-time
>* | b07310d Changed app.py on main
>* | 15f5877 changing app on main
>* | b052394 Merge edited feature/add-time
>|\| 
>| * fc6a1cf Change user==Almog
>* | a02ebb2 Change Hello to Welcome
>|/  
>* 2ef79a8 on feature/add-time added time
>* d08fe94 fixed file name
>* c92eae0 Fixed app.py content
>* 5ff4229 Fixed app.py name
>* d200586 add app.py

## Advanced Assignment
## First task - Inspect History
### 1.git log --oneline
>#### 13c72cd decided to go with feature changes
>#### f9e0246 Changed string formating on add-time
>#### b07310d Changed app.py on main
>#### 15f5877 changing app on main
>#### b052394 Merge edited feature/add-time
>#### fc6a1cf Change user==Almog
>#### a02ebb2 Change Hello to Welcome
>#### 2ef79a8 on feature/add-time added time
>#### d08fe94 fixed file name
>#### c92eae0 Fixed app.py content
>#### ff4229 Fixed app.py name
>#### d200586 add app.py

### 1.git log --graph --all
>####  *   commit 13c72cda65bc85077d95d9c3ef8110980f31f64f
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### |\  Merge: b07310d f9e0246
>#### | | Date:   Wed Jan 14 09:11:25 2026 +0200
>#### | | 
>#### | |     decided to go with feature changes
>#### | | 
>#### | * commit f9e02465714e5665dc87ed5c420eeb5a04b6a058
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### | | Date:   Wed Jan 14 09:08:29 2026 +0200
>#### | | 
>#### | |     Changed string formating on add-time
>#### | | 
>#### * | commit b07310d967bf14977f5262a0dbb08b6ca8772475
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### | | Date:   Wed Jan 14 09:07:40 2026 +0200
>#### | | 
>#### | |     Changed app.py on main
>#### | | 
>#### * | commit 15f587770bd016be4e976e9ca1567df4cc7afada
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### | | Date:   Wed Jan 14 09:06:56 2026 +0200
>#### | | 
>#### | |     changing app on main
>#### | | 
>#### * | commit b0523942012c9cffbc8e160ae263707f25d341d4
>#### |\| Merge: a02ebb2 fc6a1cf
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### | | Date:   Wed Jan 14 09:03:41 2026 +0200
>#### | | 
>#### | |     Merge edited feature/add-time
>#### | | 
>#### | * commit fc6a1cfef3c2610a3adf1d7fee36ce1cf69f3204
>#### | | Author: Almog Bachar <almogbcr@gmail.com>
>#### | | Date:   Wed Jan 14 09:01:00 2026 +0200
>#### | | 
>#### | |     Change user==Almog
>#### | | 
>#### * | commit a02ebb285ffbd774cbd92019795fa61e2e637cdb
>#### |/  Author: Almog Bachar <almogbcr@gmail.com>
>#### |   Date:   Wed Jan 14 08:59:32 2026 +0200
>#### |   
>#### |       Change Hello to Welcome
>#### | 
>#### * commit 2ef79a85c84679a11cdd4d8f50622335ce81c4f2
>#### | Author: Almog Bachar <almogbcr@gmail.com>
>#### | Date:   Wed Jan 14 08:52:49 2026 +0200
>#### | 
>#### |     on feature/add-time added time
>#### | 
>#### * commit d08fe94922a19febf7b4b2be50abb20916fbf17a
>#### | Author: Almog Bachar <almogbcr@gmail.com>
>#### | Date:   Wed Jan 14 08:46:31 2026 +0200
>#### | 
>#### |     fixed file name
>#### | 
>#### * commit c92eae00279663c1e6e2630ecf02a32922b284d8
>#### | Author: Almog Bachar <almogbcr@gmail.com>
>#### | Date:   Wed Jan 14 08:45:24 2026 +0200
>#### | 
>#### |     Fixed app.py content
>#### | 
>#### * commit 5ff4229cfebac95379732f1c949ca48733de511f
>#### | Author: Almog Bachar <almogbcr@gmail.com>
>#### | Date:   Wed Jan 14 08:43:56 2026 +0200
>#### | 
>#### |     Fixed app.py name
>#### | 
>#### * commit d200586d46718e976164b1b71d9395c38ff9a494
>####   Author: Almog Bachar <almogbcr@gmail.com>
>####   Date:   Wed Jan 14 08:37:12 2026 +0200
>####   
>####       add app.py


### 1.git show 
>#### commit 13c72cda65bc85077d95d9c3ef8110980f31f64f
>#### Merge: b07310d f9e0246
>#### Author: Almog Bachar <almogbcr@gmail.com>
>#### Date:   Wed Jan 14 09:11:25 2026 +0200
>####
>####    decided to go with feature changes
>#### 
>#### diff --cc app.py
>#### index 8445c3e,3cdee47..3c3e887
>#### --- a/app.py
>#### +++ b/app.py
>#### @@@ -1,10 -1,10 +1,11 @@@
>####  import datetime 
>####  
>####  def greet(name):
>#### - 	cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
>#### - 	return f"Welcome , {name} {cTime}!"
>#### + 	cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
>#### + 	return f"Hello , {name} {cTime}!"
>#### + 
>#### +
>####  if __name__ == "__main__":
>####  	
>#### -	user = "Almog"
>#### +	user = "Newbie"
>####  	print(greet(user))
>####

## Task 2 - Diff Practice 
### Git diff local
>#### diff --git a/app.py b/app.py
>#### index 3c3e887..9f0559f 100644
>#### --- a/app.py
>#### +++ b/app.py
>#### @@ -7,5 +7,5 @@ def greet(name):
>####  
>####  if __name__ == "__main__":
>####  	
>#### -	user = "Newbie"
>#### +	user = "Almog"
>####  	print(greet(user))

### Git diff Stage
>#### diff --git a/app.py b/app.py
>#### index 3c3e887..9f0559f 100644
>#### --- a/app.py
>#### +++ b/app.py
>#### @@ -7,5 +7,5 @@ def greet(name):
>####  
>####  if __name__ == "__main__":
>####  	
>#### -	user = "Newbie"
>#### +	user = "Almog"
>####  	print(greet(user))
>#### 


## Task 3 - Undoing Commits
### Usage git commit -amend -m "Text to repalce the wrong commit"
>#### Change message of commit message,
>#### Fix typo or Fix message if you wrote the wrong message 

stash@{0}: WIP on main: 512d37b Update app.py
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   app.py
	modified:   lesson3/README.MD

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (625a2d1b9d43fad466ecc835bb4a2ea03ab56919)
