def new_service_ticket(tickets,ticket_id): #a function to add a new service ticket to the dictionary
    if ticket_id not in tickets: #verify that the chosen ticketid doesn't already exist in the dictionary
        tickets[ticket_id] = {} #add a new (empty) ticket id to the dictionary
        print(f"New ticket {ticket_id} created\n") #notification of change to ticket dictionary
    else: #ticket id already exist
        "That Ticket ID already exists\n" #notification of already existing ticket id

def update_customer(tickets, ticket_id, customer): #a function to update the customer of a select ticket id
    if ticket_id in tickets: #verify that the chosen ticket id exists
        tickets[ticket_id]["Customer"] = customer #initialize or update the customer key/value pair
        print(f"The customer for {ticket_id} has been updated to {customer}\n") #notification of changes
    else: #Ticket ID not found
        "That Ticket ID was not found\n" #notification of failure to find Ticket ID

def update_issue(tickets, ticket_id, issue): #a funtion to update chosen ticket issues
    if ticket_id in tickets: #verify that the chosen ticket id exists
        tickets[ticket_id]["Issue"] = issue #initialize or update the issue key/value pair
        print(f"The issue for {ticket_id} has been updated to {issue}\n")#notification of changes
    else: #Ticket ID not found
        "That Ticket ID was not found\n" #notification of failure to find Ticket ID

def update_status(tickets, ticket_id, status = "Open"): #a funtion to update the chose ticket status defaulting to open
    if ticket_id in tickets: #verify that the chosen ticket id exists
        tickets[ticket_id]["Status"] = status #initialize or update the status key/value pair
        print(f"The status for {ticket_id} has been updated to {status}\n")#notification of changes
    else: #Ticket ID not found
        "That Ticket ID was not found\n" #notification of failure to find Ticket ID

def display_tickets(tickets, status_filter = "all"): #display the tickets with the option of a status filter defaulting with all tickets
    if status_filter.lower() == "all": #check if chosen filter is all
        print(f"\033[4mAll Tickets:\033[0m") #print the heading underlined
        for id, ticket_info in tickets.items(): #iterate through the outer dictionary
            print(f"\033[7m{id}\033[0m") #print heading for ticket id in inverted text
            for label, info in ticket_info.items(): #iterate the inner dictionary
                print(f"\t\033[1m{label}\033[0m: {info}") #print key/value pairs of ticket information
        print("") #formatting spacer
    else:
        found = False #flag to verify that the chosen filter is a user status
        print(f"\033[4m{status_filter} Tickets:\033[0m") #print the heading underlined
        for id, ticket_info in tickets.items(): #iterate the outer dictionary
            if tickets[id]["Status"].lower() == status_filter.lower(): #check if this ticket has the correct status
                found = True #set flag to status found
                print(f"\033[7m{id}\033[0m") #print the ticket id heading
                for label, info in ticket_info.items(): #iterate the inner dictionary
                    print(f"\t\033[1m{label}\033[0m: {info}") #print the key/value pairs of ticket information
        print("") #formatting spacer
        if not found: #check if the chosen status filter wasn't found
            print("That Status is unused\n") #notification that that chosen status wasn't used

service_tickets = { #service ticket dictionary with example tickets
    "Ticket001": {"Customer": "Gerald", "Issue": "Account locked", "Status": "Open"}, 
    "Ticket002": {"Customer": "Janine", "Issue": "Password reset", "Status": "Closed"},
    "Ticket003": {"Customer": "Carolyn", "Issue": "Login issues", "Status": "Open"}
}

display_tickets(service_tickets, "all") #print the current tickets
new_service_ticket(service_tickets, "Ticket004") #create a new ticket
update_customer(service_tickets,"Ticket004", "James") #add the customer info
update_issue(service_tickets,"Ticket004", "Hard drive issues") #add the issue info
update_status(service_tickets, "Ticket004", "Open") #add the current status
display_tickets(service_tickets, "all") #print all tickets with new ticket
display_tickets(service_tickets, "Open") #print open tickets only
display_tickets(service_tickets, "Closed") #print closed tickets only
display_tickets(service_tickets, "In Progress") #display in progress tickets only
update_issue(service_tickets, "Ticket003", "Profile Corruption") #change the issue in Ticket003 to profile corruption
display_tickets(service_tickets) #display ticket list again with changed ticket