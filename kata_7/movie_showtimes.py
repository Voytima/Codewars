"""
You just started working at a local cinema, and your first task is to write a function that returns
the showtimes of a specific movie, given its length. In order to make your job easier,
you will work with 24-hour format throughout this kata.

Your function receives three parameters, all of them being integers:
>> open - Hour at which the cinema opens.
>> close - Hour at which the cinema closes.
>> length - Length of the movie, in minutes.

It must return an array of times, with each time being in the format (hour, minute).
For example, (19, 30) means 19:30, and (2, 0) means 02:00.
The last session in the array cannot end after the cinema closes.
Also, the times in the array must be sorted from earliest to latest.

There's also a 15-minute window between a session's end and the beginning of the following one,
in order to give enough time for users to take a seat.
"""


def movie_times(open, close, length):
    if close < open:
        close += 24

    schedule = []

    start = open * 60
    end = close * 60
    movie_total = length + 15

    for i in range(start, end, movie_total):
        if (i + length) > end:
            break
        h = i % 1440 // 60
        m = i % 1440 % 60
        schedule.append((h, m))

    return schedule
