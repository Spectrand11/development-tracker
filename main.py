import activity
import tracker

print("=============================")
print("PERSONAL DEVELOPMENT TRACKER")
print("=============================")
print(f"1, Add an activity\n"
          f"2. View all activities\n"
          f"3. Search activities\n"
          f"4. Update activity\n"
          f"5. Delete activity\n"
          f"6. Progress summary\n"
          f"7. Category summary\n"
          f"8. Exit"
         ) 
id = 1
while True:  
    try:
        option = int(input("Select an option(1-6): "))
        if option <= 0 or option > 8:
            print("Enter a valid option(1-8)!!")
            continue
    except ValueError:
        print("Enter a valid option(1-8)!!")
        continue
    if option == 1:
        unique_id = id
        title = input("Enter it's title: ")
        category = input("Enter it's category: ")
        description = input("Enter it's description: ")
        date = input("Enter it's date: ")
        status = "Not Started"
        id += 1
        the_activity = activity.Activity(unique_id,title,category,description,date,status)
        print(tracker.track.add_activity(the_activity))
    elif option == 2:
        all_activities = tracker.track.view_activities()
        for action in all_activities:
            print("-----------------------")
            print(f"--id: {action.id}")
            print(f"--title: {action.title}")
            print(f"--category: {action.category}")
            print(f"--description: {action.description}")
            print(f"--date: {action.date}")
            print(f"status: {action.status}")
    elif option == 3:
        search_word = input("Enter the search keyword: ")
        found_activity = tracker.track.search_activity(search_word)
        if found_activity == []:
            print("No matching activity was found, view all activities and try again!!")
        else:
            for action in found_activity:
                        print("-----------------------")
                        print(f"--id: {action.id}")
                        print(f"--title: {action.title}")
                        print(f"--category: {action.category}")
                        print(f"--description: {action.description}")
                        print(f"--date: {action.date}")
                        print(f"status: {action.status}")
    elif option == 4:
        pass                    
    