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

### Attributes for each function
	Bool-string show_messages
	Bool-string show_db_actions

LoginUser (string username, string password)
    Example: 

    ---shell
    python WebCrawler.py action=LoginUser user_name=USERNAME user_password=USERPASSWORD
    ---

SignupUser (string username, string password)
    Example: 

    ---shell
    python WebCrawler.py action=SignupUser user_name=USERNAME user_password=USERPASSWORD
    ---

AddHabit (string user_id, string name, string description, string timespan, string date_start, string date_end, string target_time_start, string target_time_end, string target_duration, string target_repeats)
    Example: 

    ---shell
    python WebCrawler.py action=AddHabit user_id="USER_ID" habit_name="HABIT_NAME" timespan="dayly"<-OR->timespan="weekly"<-OR->timespan="monthly"<-OR->timespan="yearly"
	date_start="2023-01-01" date_end="2023-12-31" target_time_start="07:00" target_time_end="08:00" target_duration="00:30" target_repeats="1"
    ---

AddAction (string user_id, string habit_id, DateTime-string start_datetime, DateTime-string end_datetime, DateTime-string created)
    Example: 

    ---shell
    python WebCrawler.py action=AddAction user_id="USER_ID" habit_id="HABIT_ID" start_datetime="2023-01-01 07:21:21" end_datetime="2023-01-01 07:21" created="2022-12-25 09:12"
    ---


GetHabitsOfUser (string user_id)
    Example: 

    ---shell
    python WebCrawler.py action=GetHabitsOfUser user_id="USER_ID"
    ---

GetDoneHabitsOfUser (string user_id, string habit_id)
    Example: 

    ---shell
    python WebCrawler.py action=GetDoneHabitsOfUser user_id="USER_ID" habit_id="HABIT_ID"
    ---

ShowAll (string user_id)
ShowAllOfUser (string user_id)
    Example: 

    ---shell
    python WebCrawler.py action=ShowAllOfUser user_id="USER_ID"
    ---

TestEverything (string user_id)
    Example: 

    ---shell
    python WebCrawler.py action=TestEverything user_id="USER_ID"
    ---

TestEverythingAutomatic (string user_id, string automatic_tests="true")
    Example: 

    ---shell
    python WebCrawler.py action=TestEverythingAutomatic user_id="USER_ID" automatic_tests="False"
    ---

## Tests

---shell
python HabitTracker.py action=TestEverything automatic_tests=True
---

---shell
pytest
---