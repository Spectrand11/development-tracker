from activity import Activity
import json
def activity_to_dict(activity):
    mod_activity = {}
    mod_activity["id"] = activity.id
    mod_activity["title"] = activity.title
    mod_activity["category"] = activity.category
    mod_activity["description"] = activity.description
    mod_activity["date"] = activity.date
    mod_activity["status"] = activity.status
    
    return mod_activity

def dict_to_activity(data):
    the_activity = Activity(data["id"],data["title"],data["category"],data["description"],data["date"],data["status"])
    return the_activity

def save_activities(activities):
    data = []
    for activity in activities:
        new_activity = activity_to_dict(activity)
        data.append(new_activity)
    with open("activities.json","w") as file:
        json.dump(data,file, indent=4)
        
def load_activities():
    with open()