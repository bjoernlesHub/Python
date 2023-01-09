#My little habit tracker

## What is it?

It's an app for tracking your habits.
You could run it directly by python, or you could use something like XAMPP PHP server.


## Installation of Python

https://www.python.org/downloads/


## Installation of requirements

---shell
pip install requirements.txt
---


## Installation of xampp (unnecessary)

https://www.apachefriends.org/


## Usage by php server:
copy the HabitTracker folder to your XAMPP "htdocs" folder.
In the XAMPP folder, click on xampp_start.exe

open http://localhost/HabitTracker by your webbrowser with enabled javascript

Follow instructions on screen


## Usage by python directly:

---shell
python WebCrawler.py action=YOURACTION ...........
---

for example a user signup:
---shell
python WebCrawler.py action=SignupUser user_name=YOURNAME user_password=YOURPASSWORD
---

## Actions (and attributes)

LoginUser (string username, string password)
SignupUser (string username, string password)

AddHabit (string user_id, string name, string description, string timespan, string target_time_start, string target_time_end, string target_duration, string target_repeats)
AddAction (string habit_id, DateTime-string start_datetime, DateTime-string end_datetime, DateTime-string created)

GetHabitsOfUser (string user_id, Bool-string show_db_actions)
GetDoneHabitsOfUser (string habit_id, Bool-string show_db_actions=False)
ShowAll
ShowAllOfUser

TestEverything
TestEverythingAutomatic




## Tests

---shell
python HabitTracker.py action=TestEverything automatic_tests=True
---

---shell
pytest
---