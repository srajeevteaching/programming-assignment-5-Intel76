# Programmer:Hanna Magan
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5

import math

# Index file
ID = 1
TripStart = 2
TripEnd = 3
Duration = 4
Distance = 5
TotalCost = 6
Paymentchoice = 7
Company = 8
LatitudePickUp = 9
LongitudePickUp = 10
LatitudeDropOff = 11
LongitudeDropOff = 12

def list_of_list(filename):
    taxi_info = []
    try:
        file = open(filename, "r")
        line_count = 1
        for line in file:
            try:
                line_count += 1

            except ValueError:
                print(line_data)
        file.close()
    except FileNotFoundError:
        print("error: File", filename, "not found")
    return taxi_info

def average_cost(list_of_list, payment_choice):
    total_cost = 0
    line_counter = 0

    if list_of_list[7][Paymentchoice] == paymentchoice:
            cost_of_trip = list_of_list[7][TotalCost]
            total_cost += cost_of_trip
            line_counter += 1

def trip_tracker(list_of_list, date):
    day_trips = 0
    line_counter = 0

    return day_trips

def find_distance(latit1, long1, latit2, long2):

    lat1 = math.radians(latit1)
    lat2 = math.radians(latit2)
    lon1 = math.radians(long1)
    lon2 = math.radians(long2)
    total_distance = math.acos(
        math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * 3959

    return total_distance

def main():
    month = input("Load data from September or October? ")

    if month == "september":
        taxi_month = list_of_list("2016_09.csv")
    elif month == "october":
        taxi_month = list_of_list("2016_10 (1).csv")
    else:
        print("Error: Invalid month")

    print("Average Cost, Total Distance,  Date")
    task = input("Which data would you like to find? > ")

    if task == "average cost":
        average_cost = input("Cash or Credit Card: ")
    elif task == "total distance":
        total_distance = input("please input distance" )
    elif task == "date":
        date = input("Please input a date (year/month/day")
        trip_tracker(list_of_list, date)

    second_task = input("Do something else? >")

    if second_task == "yes":
        task = input("Which data would you like to find? > ")

    elif second_task == "no":
        print("Thanks for using code")

main()