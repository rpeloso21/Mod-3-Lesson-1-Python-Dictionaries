# Task 1



def open_ticket(number, name, issue):
    if number not in service_tickets:
        service_tickets.setdefault(number, {"Customer":name, "Issue":issue, "Status":"open"})

def update_ticket(tickets, number, update):
    tickets[number]["Status"] = update


def display_tickets(tickets, status):
    if status.lower() == "all":
        print(f"{status} tickets:\n")
        for ticket, info in tickets.items():
            print(f"{ticket} \n{info}\n")

    elif status.lower() == "closed":
        print(f"{status} tickets:\n")
        for ticket, info in tickets.items():
            if tickets[ticket]["Status"] == "closed":
                print(f"{ticket} \n{info}\n")

    elif status.lower() == "open":
        print(f"{status} tickets:\n")
        for ticket, info in tickets.items():
            if tickets[ticket]["Status"] == "closed":
                print(f"{ticket} \n{info}\n")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

open_ticket("Ticket003", "Tim", "Error message")
open_ticket("Ticket004", "Ron", "Won't load")

update_ticket(service_tickets, "Ticket001", "closed")

display_tickets(service_tickets, "all")
display_tickets(service_tickets, "closed")


print(service_tickets)