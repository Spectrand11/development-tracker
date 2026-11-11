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
while True:  
    try:
        option = int(input("Select an option(1-6): "))
        if option <= 0 or option > 8:
            print("Enter a valid option(1-8)!!")
            continue
    except ValueError:
        print("Enter a valid option(1-8)!!")
        continue