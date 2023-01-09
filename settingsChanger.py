def set_new_settings(settings, parameters):
    """ get the given attributes and changes the settings_json

    :param parameters: parameters that was given
    :param settings: the original settings from textfiles

    :return: the new settings_json
    """

    count_of_values = 0
    count_of_onekey_parameter = 0
    onekey_parameters_string = ""
    # print("------------")
    
    for parameter in parameters:

        if parameter != "HabitTracker.py":

            key_val = parameter.split("=")

            if len(key_val) > 1:
                #print(key_val[0]+"="+key_val[1])
                if key_val[1] != "":
                    count_of_values = count_of_values+1

                    # get
                    if key_val[0] == "action":
                        print("using-action:" + key_val[1])
                        settings["action"] = key_val[1]

                    elif key_val[0] == "habit_id":
                        print("Using habit-id:" + key_val[1])
                        settings["habit_id"] = key_val[1]
                    elif key_val[0] == "user_name":
                        print("user:" + key_val[1])
                        settings["user"][0]["user_name"] = key_val[1]
                    elif key_val[0] == "user_password":
                        # print("Password:" + key_val[1])
                        settings["user"][0]["user_password"] = key_val[1]
                    elif key_val[0] == "user_id":
                        print("User ID:" + key_val[1])
                        settings["user"][0]["user_id"] = key_val[1]

                    elif key_val[0] == "habit_name":
                        print("Habit Name:" + key_val[1])
                        key_val[1] = key_val[1].replace("³", " ")
                        settings["habit"][0]["name"] = key_val[1]
                    elif key_val[0] == "habit_description":
                        key_val[1] = key_val[1].replace("³", " ")
                        print("Habit description:" + key_val[1])
                        settings["habit"][0]["description"] = key_val[1]
                    elif key_val[0] == "habit_timespan":
                        print("Habit timespan:" + key_val[1])
                        settings["habit"][0]["timespan"] = key_val[1]

                    elif key_val[0] == "habit_date_start":
                        print("Habit date start:" + key_val[1])
                        settings["habit"][0]["date_start"] = key_val[1]
                    elif key_val[0] == "habit_date_end":
                        print("Habit date end:" + key_val[1])
                        settings["habit"][0]["date_end"] = key_val[1]

                    elif key_val[0] == "habit_target_time_start":
                        print("Habit target time start:" + key_val[1])
                        settings["habit"][0]["target_time_start"] = key_val[1]
                    elif key_val[0] == "habit_target_time_end":
                        print("Habit target time end:" + key_val[1])
                        settings["habit"][0]["target_time_end"] = key_val[1]
                    elif key_val[0] == "habit_target_duration":
                        print("Habit target duration:" + key_val[1])
                        settings["habit"][0]["target_duration"] = key_val[1]
                    elif key_val[0] == "habit_target_repeats":
                        print("Habit target repeats:" + key_val[1])
                        settings["habit"][0]["target_repeats"] = key_val[1]

                    elif key_val[0] == "habit_id":
                        print("Habit ID:" + key_val[1])
                        settings["habit_lasttime"][0]["habit_id"] = key_val[1]
                    elif key_val[0] == "start_datetime":
                        print("Habit start datetime:" + key_val[1])
                        settings["habit_lasttime"][0]["start_datetime"] = key_val[1]
                    elif key_val[0] == "end_datetime":
                        print("Habit start datetime:" + key_val[1])
                        settings["habit_lasttime"][0]["end_datetime"] = key_val[1]
                    elif key_val[0] == "created":
                        print("Habit created:" + key_val[1])
                        settings["habit_lasttime"][0]["created"] = key_val[1]

                    elif key_val[0] == "wait":
                        print("Wait seconds:" + key_val[1])
                        settings["runtime_settings"][0]["wait"] = key_val[1]
                    elif key_val[0] == "automatic_tests":
                        print("Automatic tests:" + key_val[1])
                        settings["runtime_settings"][0]["automatic_tests"] = key_val[1]
                    elif key_val[0] == "return_json":
                        print("Return json (to website):" + key_val[1])
                        settings["runtime_settings"][0]["return_json"] = key_val[1]
                    else:
                        print("A key wasn't known ("+key_val[0]+"..")

            elif len(key_val) == 1:
                count_of_onekey_parameter += 1
                onekey_parameters_string += "'"+key_val[0]+"', "
    onekey_parameters_string = onekey_parameters_string[:-2]
    print(str(count_of_values)+" given key-value pairs for running this Job.")
    if count_of_onekey_parameter > 1:
        print(str(count_of_onekey_parameter)+" given values for running this Job. ("+onekey_parameters_string+")")

    # for parameter in parameters:
        # print(parameter+"\n")

    return settings
