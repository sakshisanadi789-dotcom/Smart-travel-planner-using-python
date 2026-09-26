"""Smart Travel Planner

A simple console-based Python program that collects trip information,
validates the input, calculates travel costs, and prints a formatted summary.
"""


def get_positive_integer(prompt):
    """Get a positive integer from the user and validate it."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if value <= 0:
            print("The value must be greater than 0.")
            continue

        return value


def get_non_negative_float(prompt):
    """Get a non-negative number from the user and validate it."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value < 0:
            print("Cost cannot be negative.")
            continue

        return value


def calculate_total_transportation_cost(transport_cost_per_traveler, number_of_travelers):
    """Return total transportation cost for the whole group."""
    return transport_cost_per_traveler * number_of_travelers


def calculate_total_hotel_cost(hotel_cost_per_day, number_of_days, number_of_travelers):
    """Return total hotel cost for all travelers across the trip."""
    return hotel_cost_per_day * number_of_days * number_of_travelers


def calculate_hotel_food_cost(total_hotel_cost, food_cost_rate=0.25):
    """Estimate food cost based on the hotel stay cost."""
    return total_hotel_cost * food_cost_rate


def calculate_total_activity_cost(activity_cost_per_traveler, number_of_travelers):
    """Return total activity cost for the whole group."""
    return activity_cost_per_traveler * number_of_travelers


def calculate_overall_trip_cost(total_transportation_cost, total_hotel_cost, hotel_food_cost, total_activity_cost):
    """Return combined trip cost."""
    return total_transportation_cost + total_hotel_cost + hotel_food_cost + total_activity_cost


def calculate_cost_per_traveler(overall_trip_cost, number_of_travelers):
    """Return the average cost per traveler."""
    return overall_trip_cost / number_of_travelers


def calculate_average_daily_cost(overall_trip_cost, number_of_days):
    """Return average daily cost across the trip."""
    return overall_trip_cost / number_of_days


def display_summary(travel_info, totals):
    """Print a friendly formatted trip summary."""
    print("\n" + "=" * 68)
    print("                      SMART TRAVEL PLANNER SUMMARY")
    print("=" * 68)
    print(f"Traveler Name:         {travel_info['traveler_name']}")
    print(f"Destination:           {travel_info['destination']}")
    print(f"Number of Travelers:   {travel_info['number_of_travelers']}")
    print(f"Travel Days:           {travel_info['number_of_days']}")
    print("=" * 68)
    print(f"Total Transportation:  ${totals['total_transportation_cost']:,.2f}")
    print(f"Total Hotel Cost:      ${totals['total_hotel_cost']:,.2f}")
    print(f"Hotel Food Cost:       ${totals['hotel_food_cost']:,.2f}")
    print(f"Total Activity Cost:   ${totals['total_activity_cost']:,.2f}")
    print(f"Overall Trip Cost:     ${totals['overall_trip_cost']:,.2f}")
    print(f"Cost Per Traveler:     ${totals['cost_per_traveler']:,.2f}")
    print(f"Average Daily Cost:    ${totals['average_daily_cost']:,.2f}")
    print("=" * 68)
    print("Happy travels and safe adventures!")
    print("=" * 68)


def main():
    """Collect travel information, calculate costs, and present the summary."""
    print("=" * 68)
    print("          Welcome to the Smart Travel Planner!")
    print("=" * 68)

    traveler_name = input("Enter traveler name: ").strip()
    if not traveler_name:
        traveler_name = "Traveler"

    destination = input("Enter destination: ").strip()
    if not destination:
        destination = "TBD"

    number_of_travelers = get_positive_integer("Number of travelers: ")
    number_of_days = get_positive_integer("Number of travel days: ")
    transportation_cost_per_traveler = get_non_negative_float("Transportation cost per traveler ($): ")
    hotel_cost_per_day = get_non_negative_float("Hotel cost per day ($): ")
    activity_cost_per_traveler = get_non_negative_float("Activity cost per traveler ($): ")

    travel_info = {
        "traveler_name": traveler_name,
        "destination": destination,
        "number_of_travelers": number_of_travelers,
        "number_of_days": number_of_days,
        "transportation_cost_per_traveler": transportation_cost_per_traveler,
        "hotel_cost_per_day": hotel_cost_per_day,
        "activity_cost_per_traveler": activity_cost_per_traveler,
    }

    total_transportation_cost = calculate_total_transportation_cost(
        transportation_cost_per_traveler, number_of_travelers
    )
    total_hotel_cost = calculate_total_hotel_cost(
        hotel_cost_per_day, number_of_days, number_of_travelers
    )
    hotel_food_cost = calculate_hotel_food_cost(total_hotel_cost)
    total_activity_cost = calculate_total_activity_cost(
        activity_cost_per_traveler, number_of_travelers
    )
    overall_trip_cost = calculate_overall_trip_cost(
        total_transportation_cost,
        total_hotel_cost,
        hotel_food_cost,
        total_activity_cost,
    )
    cost_per_traveler = calculate_cost_per_traveler(overall_trip_cost, number_of_travelers)
    average_daily_cost = calculate_average_daily_cost(overall_trip_cost, number_of_days)

    totals = {
        "total_transportation_cost": total_transportation_cost,
        "total_hotel_cost": total_hotel_cost,
        "hotel_food_cost": hotel_food_cost,
        "total_activity_cost": total_activity_cost,
        "overall_trip_cost": overall_trip_cost,
        "cost_per_traveler": cost_per_traveler,
        "average_daily_cost": average_daily_cost,
    }

    display_summary(travel_info, totals)


if __name__ == "__main__":
    main()
