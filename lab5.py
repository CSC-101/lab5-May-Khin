import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#The function two Time objects as inputs and returns
# a new Time object that represents the sum of the two times
#input: Two Time objects
#output: Sum of those two Time objects
def time_add(time1, time2):
    # Calculate total seconds and minutes
    total_seconds = time1.second + time2.second
    total_minutes = time1.minute + time2.minute
    total_hours = time1.hour + time2.hour

    if total_seconds >= 60:
        total_minutes += total_seconds // 60
        total_seconds %= 60
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes %= 60

    return data.Time(total_hours, total_minutes, total_seconds)


# Part 4
#The function checks if the elements in the provided
# list are in strictly descending order.
#input: A list of floats
#output: True if the list is strictly descending and False if its not.
def is_descending(list_a: list) -> bool:
    for i in range(len(list_a)-1):
        if list_a[i] <= list_a[i+1]:
            return False
    return True


# Part 5
#takes a list of integers and two indices (lower and upper).
# The function should return the index of the largest value within the specified range in the list
# If the range is invalid, return None
#input: list of int, and lower bound and upper bound
def large_between(nums: list[int], lower: int, upper: int):
    lower_num = max(lower, 0)
    upper_num = min(upper, len(nums) - 1)

    if lower_num > upper_num:
        return None

    largest_index = lower_num
    for i in range(lower_num, upper_num + 1):
        if nums[i] > nums[largest_index]:
            largest_index = i

    return largest_index


# Part 6
def furthest_from_origin(points:list):
    if not points:
        return None

    furthest_index = 0
    max_distance = points[0].distance_from_origin()

    for i in range(1, len(points)):
        distance = points[i].distance_from_origin()
        if distance > max_distance:
            max_distance = distance
            furthest_index = i

    return furthest_index

