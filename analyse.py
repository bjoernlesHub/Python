def analyse_user_records_by_id(path, settings_json, return_json="True"):
    """
    Calculate the event of the counter

    :param path: path to database file
    :param settings_json: the new settings_json
    :param return_json: bool like "True"

    :return:
    """
    import sqlite
    from datetime import timedelta
    from datetime import datetime
    from datetime import time
    from datetime import date
    import json
    rows = []
    user_id = settings_json["user"][0]["user_id"]
    show_db_actions = settings_json["runtime_settings"][0]["show_db_actions"]
    user = sqlite.get_sqlite_vals_by_columns_and_values(path, "users", "id", user_id, show_db_actions)
    print(len(user))
    if len(user) != 0:
        name = user[0][1]
        print()
        print("user :" + name)
        habits = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits", "user_id", user_id,
                                                              show_db_actions)
        print()
        print("habits:")
        for habit in habits:

            habit_id = habit[0]
            habit_name = habit[2]
            habit_description = habit[3]
            habit_timespan = habit[4]
            start_date = datetime.strptime(habit[5], '%Y-%m-%d')
            end_date = datetime.strptime(habit[6], '%Y-%m-%d')
            target_time_start = datetime.strptime(habit[7], '%H:%M').time()
            target_time_end = datetime.strptime(habit[8], '%H:%M').time()
            target_duration = datetime.strptime(habit[9], '%H:%M').time()
            target_repeats = int(habit[10])

            full_target_duration = timedelta()
            x = target_repeats
            while x != 0:
                full_target_duration = full_target_duration + timedelta(hours=target_duration.hour, minutes=target_duration.minute)
                x = x - 1

            print()
            print("Habit: " + habit_name+" ("+habit_description+")")
            print("Habit done last times: ")
            habit_dones = sqlite.get_sqlite_vals_by_columns_and_values(path, "habits_lasttime", "habit_id",
                                                                       str(habit_id), show_db_actions)

            days_since = date.today() - datetime.date(start_date)
            days_left = datetime.date(end_date) - date.today()
            actions_count = len(habit_dones)
            actions_left = str(target_repeats-actions_count)
            print(str(days_since.days) + " days since startdate. (" + str(start_date) + ")")
            print("days left: " + str(days_left.days) + " to enddate. ("+str(end_date)+")")
            print("You have "+str(actions_count)+" of "+str(target_repeats)+" needed actions. (" + actions_left + " left)")

            print("Actions:")
            counter = 0
            full_done_duration = timedelta()
            for done_habit in habit_dones:

                counter = counter+1
                from_time = datetime.strptime(done_habit[2], '%Y-%m-%d %H:%M')
                to_time = datetime.strptime(done_habit[3], '%Y-%m-%d %H:%M')
                created = datetime.strptime(done_habit[3], '%Y-%m-%d %H:%M')
                timespan_done_habit = to_time - from_time
                difference_start = from_time - datetime.combine(from_time.date(), target_time_start)
                difference_end = datetime.combine(to_time.date(), target_time_end) - to_time
                target_duration_delta = timedelta(hours=target_duration.hour, minutes=target_duration.minute, seconds=target_duration.second, microseconds=target_duration.microsecond)
                difference_duration = timespan_done_habit - target_duration_delta

                full_done_duration += timespan_done_habit

                print(str(counter)+". of needed "+str(target_repeats)+" entries, created: "+str(created)+"):")
                print(done_habit)
                print()
                print("difference to planned start time ("+str(target_time_start)+") "+str(difference_start))
                print("difference to planned end time (" + str(target_time_end) + ") " + str(difference_end))
                print(str(timespan_done_habit)+" of "+str(target_duration)+" ("+str(difference_duration)+")")
                print("-------------------------------------------------------------------")
                print()
                # [habit_name].append(done_habit)
            print("Full duration: "+str(full_done_duration)+" (of total "+str(full_target_duration)+")")
            print()
    #if return_json:
    #    return json.dumps(rows)
    #else:
    #    for row in rows:
    #        print(row)

