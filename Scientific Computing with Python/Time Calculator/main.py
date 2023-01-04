def add_time(start, duration, new_day=''):

    # split arguments to hours, minutes and AM/PM
    start, duration = start.split(), duration.split()
    start[0], duration[0] = start[0].split(':'), duration[0].split(':')
    start_hours, start_minutes = map(float, start[0])
    duration_hours, duration_minutes = map(float, duration[0])

    # convert to 24H format in order to easily know if the new time is in PM or AM
    if start[1] == 'PM':
        start_hours += 12

    # primitive calculation of final time
    final_minutes = start_minutes + duration_minutes
    final_hours = start_hours + duration_hours + int(final_minutes / 60)

    # set the final time to AM or PM according to 24H format hours value
    meridiem = ' PM' * (final_hours % 24 >= 12) + ' AM' * (final_hours % 24 < 12)

    # calculate how many days later is the final time, if any
    days_later = ' (next day)' * (24 <= final_hours < 48) +\
        ' ({} days later)'.format(int(final_hours / 24)) * (final_hours >= 48)

    # list of weekdays in case of passing the current day
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # configuring time to display correctly
    new_time = str(int(final_hours % 12)) + ':' + str(int(final_minutes % 60)).rjust(2, '0') + meridiem + days_later

    # handle the case when new time's hours is 0
    if new_time[0] == '0':
        new_time = new_time.replace('0', '12', 1)

    # adding final weekday if the current day is passed
    if new_day:
        # get the index of the new day to plug it in the week_days list
        day_index = (week_days.index(new_day.capitalize()) + int(final_hours / 24)) % 7
        new_day = ', ' + week_days[day_index]

        if days_later:
            new_time = new_time.replace('M', 'M' + new_day)
        else:
            new_time += new_day

    return new_time
