#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # intialize the array to have starting point
    # loop through
    # have start point

    route_start = {}
    route = []

    for ticket in tickets:
        route_start[ticket.source] = ticket.destination

    new_destination = route_start["NONE"]

    while new_destination != "NONE":
        route.append(new_destination)
        new_destination = route_start[new_destination]

    route.append("NONE")

    return route
