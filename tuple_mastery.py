def format_itineraries(itineraries):
    formatted_string = ""
    for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_string += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_string.strip()

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)
