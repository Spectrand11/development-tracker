class Tracker:
    def __init__(self):
        self.all_activities = []
        
    def add_activity(self,activity):
        self.all_activities.append(activity)
        return "Added successfully!!"
    
    def view_activities(self):
        return self.all_activities
    
    def delete_activity(self,id):
        for activity in self.all_activities:
            if activity.id == id:
                self.all_activities.remove(activity)
                return f"Deleted successfully!!"
        return f"An activity with the id was not found, view all activities and try again!!"
        
    def search_activity(self,keyword):
        found = []
        for activity in self.all_activities:
            search_word = ""
            search_word = activity.title + " " + activity.category + " " + activity.description + " "
            if keyword in search_word:
                found.append(activity)
        return found
    
    def current(self,id):
        for activity in self.all_activities:
            if activity.id == id:
                return activity
    def progress_sum(self):
        completed = 0
        in_progress = 0
        not_started = 0
        
        for activity in self.all_activities:
            if activity.status ==  "Not Started":
                not_started += 1
            elif activity.status == "In Progress":
                in_progress += 1
            else:
                completed += 1
        return completed, in_progress, not_started 
        
        
        
        
                    
    def update_activity(self,id,update,num):
        for activity in self.all_activities:
            if activity.id == id:
                if num == 1:
                    activity.title = update
                    return f"Changed successfully!!"
                elif num == 2:
                    activity.category = update
                    return f"Changed successfully!!"
                elif num == 3:
                    activity.description = update
                    return f"Changed successfully!!"
                elif num == 4:
                    activity.date = update
                    return f"Changed successfully!!"
                else:
                    activity.status = update
                    return f"Changed successfully!!"
                    
        
        
            
            
track = Tracker()