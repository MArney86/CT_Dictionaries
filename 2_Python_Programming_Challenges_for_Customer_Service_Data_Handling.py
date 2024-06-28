def new_service_ticket(tickets,ticket_id):
    if ticket_id not in tickets:
        tickets[ticket_id] = {}
        print(f"New ticket {ticket_id} created")
    else:
        "That Ticket ID already exists"

def update_customer(tickets, ticket_id, customer):
    if ticket_id in tickets:
        tickets[ticket_id]["Customer"] = customer
        print(f"The customer for {ticket_id} has been updated to {customer}")
    else:
        "That Ticket ID was not found"

def update_issue(tickets, ticket_id, issue):
    if ticket_id in tickets:
        tickets[ticket_id]["Issue"] = issue
        print(f"The issue for {ticket_id} has been updated to {issue}")
    else:
        "That Ticket ID was not found"

def update_status(tickets, ticket_id, status = "Open"):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"The status for {ticket_id} has been updated to {status}")
    else:
        "That Ticket ID was not found"

def display_tickets(tickets, status_filter = "all"):
    if status_filter.lower() == "all":
        print(f"\033[4mAll Tickets:\033[0m")
        for id, ticket_info in tickets.items():
            print(f"\033[7m{id}\033[0m")
            for label, info in ticket_info.items():
                print(f"\t\033[1m{label}\033[0m: {info}")
        print("")
    else:
        found = False
        print(f"\033[4m{status_filter} Tickets:\033[0m")
        for id, ticket_info in tickets.items():
            if tickets[id]["Status"].lower() == status_filter.lower():
                found = True
                print(f"\033[7m{id}\033[0m")
                for label, info in ticket_info.items():
                    print(f"\t\033[1m{label}\033[0m: {info}")
        if not found:
            print("That Status is unused")

service_tickets = { #service ticket dictionary with example tickets
    "Ticket001": {"Customer": "Gerald", "Issue": "Account locked", "Status": "Open"}, 
    "Ticket002": {"Customer": "Janine", "Issue": "Password reset", "Status": "Closed"},
    "Ticket003": {"Customer": "Carolyn", "Issue": "Login issues", "Status": "Open"}
}

display_tickets(service_tickets, "all")
new_service_ticket(service_tickets, "Ticket004")
update_customer(service_tickets,"Ticket004", "James")
update_issue(service_tickets,"Ticket004", "Hard drive issues")
update_status(service_tickets, "Ticket004", "Open")
display_tickets(service_tickets, "all")
display_tickets(service_tickets, "Open")
display_tickets(service_tickets, "Closed")
display_tickets(service_tickets, "In Progress")
update_issue(service_tickets, "Ticket003", "Profile Corruption")
display_tickets(service_tickets)


