import Components.schedule as schedule
class Course:
    def __init__(self,document):
        self.number = document["_id"]
        self.name = document["name"]
        self.year = document["year"]
        self.is_must = document["is_must"]
        self.groups = document["groups"]
        self.prior = document["pre-courses"]
        self.rating = self.get_rating(document)
        self.duration = self.get_duration()
        self.morning_groups = []
        self.evening_groups = []
        self.sunday_groups = []
        self.monday_groups = []
        self.tuesday_groups = []
        self.wednesday_groups = []
        self.thursday_groups = []
        self.friday_groups = []
    
    def __eq__(self, other):
        return self.number == other.number   
    def __lt__(self, other):
        return self.number < other.number
    def __gt__(self,other):
        return self.number > other.number
    def __le__(self,other):
        return self.number<=other.number
    def __ge__(self,other):
        return self.number>=other.number
    def __ne__(self,other):
        return self.number != other.number
    
    
    def get_duration(self):
        day_time = schedule.format_day_time(str(self.groups[0]))
        return day_time[2]-day_time[1]
    
    def get_rating(self,document):
        if "rating" in document:
            return document["rating"]
        else:
            return None
    
    def remove_unavailable_groups(self,time):
        unavailable_day_time = schedule.format_day_time(time)
        remove_list = []
        for group in self.groups:
            group_day_time = schedule.format_day_time(group)
            if schedule.clashing(unavailable_day_time,group_day_time):
                remove_list.append(group)
        for group in remove_list:
            if group in self.groups:
                self.groups.remove(group)
        remove_list.clear()
        self.get_split_groups()

    def clashing(self,other):
        for this_group in self.groups:
            for other_group in other.groups:
                this_group_day_time = schedule.format_day_time(this_group)
                other_group_day_time = schedule.format_day_time(other_group)
                if schedule.clashing(this_group_day_time,other_group_day_time):
                    return True
        return False

    def is_morning(self,group):
        daytime = schedule.format_day_time(group)
        start = daytime[1]
        finish = daytime[2]
        if start < 14 and finish <=14:
            return True
        elif start < 14 and finish > 14:
            if 14-start >= finish -14:
                return True
        return False
    
    def is_sunday(self,group):
        return schedule.format_day_time(group)[0] == "sunday"
    
    def is_monday(self,group):
        return schedule.format_day_time(group)[0] == "monday"

    def is_tuesday(self,group):
        return schedule.format_day_time(group)[0] == "tuesday"
    
    def is_wednesday(self,group):
        return schedule.format_day_time(group)[0] == "wednesday"
    
    def is_thursday(self,group):
        return schedule.format_day_time(group)[0] == "thursday"
    
    def is_friday(self,group):
        return schedule.format_day_time(group)[0] == "friday"

    def get_split_groups(self):
        self.morning_groups = []
        self.evening_groups = []
        self.sunday_groups = []
        self.monday_groups = []
        self.tuesday_groups = []
        self.wednesday_groups = []
        self.thursday_groups = []
        self.friday_groups = []
        for group in self.groups:
            if self.is_morning(group):
                self.morning_groups.append(group)
            else:
                self.evening_groups.append(group)
            
            if self.is_sunday(group):
                self.sunday_groups.append(group)
            elif self.is_monday(group):
                self.monday_groups.append(group)
            elif self.is_tuesday(group):
                self.tuesday_groups.append(group)
            elif self.is_wednesday(group):
                self.wednesday_groups.append(group)
            elif self.is_thursday(group):
                self.thursday_groups.append(group)
            elif self.is_friday(group):
                self.friday_groups.append(group)
        

        