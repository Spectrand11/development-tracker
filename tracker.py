class Tracker:
    def __init__(self):
        self.all_activities = []
        
    def add_activity(self,activity):
        self.all_activities.append(activity)
        return "Added successfully!!"
    
    def view_activities(self):
        return self.all_activities
    
track = Tracker()