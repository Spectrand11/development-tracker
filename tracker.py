class Tracker:
    def __init__(self):
        self.all_activities = []
        
    def add_activity(self,activity):
        self.all_activities.append(activity)
        return "Added successfully!!"
    
    def view_activities(self):
        return self.all_activities
    
    def search_activity(self,keyword):
        found = []
        for activity in self.all_activities:
            search_word = ""
            search_word = activity.title + " " + activity.category + " " + activity.description
            if keyword in search_word:
                found.append(activity)
        return found
            
            
            
track = Tracker()