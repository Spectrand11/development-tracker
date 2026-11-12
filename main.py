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
        title = title.strip().lower()
        category = input("Enter it's category: ")
        category = category.strip().lower()
        description = input("Enter it's description: ")
        description = description.strip().lower()
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
        search_word = search_word.lower().strip()
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
        try:
            update_id = int(input("Enter the id of the item I want to update: "))
        except ValueError:
            print("Enter a valid id!!")                    
            continue
        found = tracker.track.current(update_id)
        if found == None:
            print("No matching activity was found, view all activities and try again!!")
        else:
            print("====ACTIVITY FOUND====")
            print("-----------------------")
            print(f"--id: {found.id}")
            print(f"--title: {found.title}")
            print(f"--category: {found.category}")
            print(f"--description: {found.description}")
            print(f"--date: {found.date}")
            print(f"status: {found.status}")
        
        
        print(f"Enter the field you want to change: \n"
              f"1. Title\n"
              f"2. Category\n"
              f"3. Description\n"
              f"4. Date\n"
              f"5. Status")
        try:
            field_no = int(input("Enter the field here: "))
            if field_no <= 0 or field_no > 5:
                print("Enter a valid field(1-5)!!")
                continue
        except ValueError:
            print("Enter a valid field(1-5)!!")
            continue
        
        if field_no == 1:
            new_title = input("Enter the new title: ")
            print(tracker.track.update_activity(id=update_id,update=new_title.strip().lower(),num=1))
        elif field_no == 2:
            new_category = input("Enter the new category: ")
            print(tracker.track.update_activity(id=update_id,update=new_category.strip().lower(),num=2))
        elif field_no == 3:
            new_desc = input("Enter the new description: ")
            print(tracker.track.update_activity(id=update_id,update=new_desc.strip().lower(),num=3))
        elif field_no == 4:
            new_date = input("Enter the new date: ")
            print(tracker.track.update_activity(id=update_id,update=new_date,num=4))
        elif field_no == 5:
            print("Select new status: \n"
                    f"1. Not Started\n"
                    f"2. In Progress\n"
                    f"3. Completed")
            try:
                new_status = int("Enter 1 ,2 or 3: ")      
                if new_status == 1:
                    print(tracker.track.update_activity(id=update_id,update="Not Started",num=5))
                elif new_status == 2:
                    print(tracker.track.update_activity(id=update_id,update="In Progress",num=5))
                elif new_status == 3:
                    print(tracker.track.update_activity(id=update_id,update="Completed",num=5))
                else:
                    print("Choose 1, 2 or 3!!")
            except ValueError:
                print("Choose 1, 2 or 3!!")
            
    