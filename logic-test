# Now using while loops to improve this process and support more than 3 events. This is still the foundation of the logic however.

list_events = ["MSA Meeting","Columbia Weekly Review","Internal CC Meeting"]
count_events = len(list_events) -1

print("It's time to track your time!")

if count_events == 2:
  event2 = list_events[2]
  track_e2 = input("\nWant to add " +list_events[2]+ " to your timecard?\n")
    
  if track_e2 == "Yes":
    time_e2 = input("\nHow much time do you want to add (in minutes)?\n")
    billable_e2 = input("\nIs this event billable?\n")

    if billable_e2 == "Yes":
      company_e2 = input("\nWhat company is this for?\n")
      milestone_e2 = (company_e2+" February 2021")
      print("\nNext:")
      count_events = count_events-1

    else:
      company_e2 = "Computacenter"
      milestone_e2 = "Computacenter PS Admin"
      print("\nNext:")
      count_events = count_events-1
  else:
    time_e2 = 0
    billable_e2 = "NA"
    company_e2 = "NA" 
    milestone_e2 = "NA"   
    print("\nNext:")
    count_events = count_events-1


if count_events == 1:
  event1 = list_events[1]
  track_e1 = input("\nWant to add " +list_events[1]+ " to your timecard?\n")
    
  if track_e1 == "Yes":
    time_e1 = input("\nHow much time do you want to add (in minutes)?\n")
    billable_e1 = input("\nIs this event billable?\n")

    if billable_e1 == "Yes":
      company_e1 = input("\nWhat company is this for?\n")
      milestone_e1 = (company_e1+" February 2021")
      print("\nNext:")
      count_events = count_events-1

    else:
      company_e1 = "Computacenter"
      milestone_e1 = "Computacenter PS Admin"
      print("\nNext:")
      count_events = count_events-1
  else:
    time_e1 = 0
    billable_e1 = "NA"
    company_e1 = "NA" 
    milestone_e1 = "NA"    
    print("\nNext:")
    count_events = count_events-1    


if count_events == 0:
  event0 = list_events[0]
  track_e0 = input("\nWant to add " +list_events[0]+ " to your timecard?\n")
    
  if track_e0 == "Yes":
    time_e0 = input("\nHow much time do you want to add (in minutes)?\n")
    billable_e0 = input("\nIs this event billable?\n")

    if billable_e0 == "Yes":
      company_e0 = input("\nWhat company is this for?\n")
      milestone_e0 = (company_e0+" February 2021")
      print("\nNext:")
      count_events = count_events-1

    else:
        company_e0 = "Computacenter"
        milestone_e0 = "Computacenter PS Admin"
        print("\nNext:")
        count_events = count_events-1
  else:
    time_e0 = 0
    billable_e0 = "NA"
    company_e0 = "NA" 
    milestone_e0 = "NA" 
    print("\nNext:")
    count_events = count_events-1

if count_events == -1:
  
  print("\n")
  print(event2)
  print(time_e2)
  print(billable_e2)
  print(company_e2)
  print(milestone_e2)
  
  print("\n")
  print(event1)
  print(time_e1)
  print(billable_e1)
  print(company_e1)
  print(milestone_e1)
  
  print("\n")
  print(event0)
  print(time_e0)
  print(billable_e0)
  print(company_e0)
  print(milestone_e0)
