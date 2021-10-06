import random

# Course number first year : 1 - 73
# Course number second year : 74 - 118
# Course number third year : 119 - 128
# Optional courses : 150 - 200
class Data:
  def __init__(self):
    self.DAYS = ["sunday","monday","tuesday","wednesday","thursday","friday"]
    self.TIMES = ["08","09","10","11","12","13","14","15","16","17","18","19","20","21"]
    self.FIRST_YEAR_COURSES_NUM = 73
    self.SECOND_YEAR_COURSES_NUM = 45
    self.THIRD_YEAR_COURSES_NUM = 10
    self.TOTAL_HOURS_WEEK = 13
    self.TOTAL_HOURS_WEEKEND = 8
    self.ADMIN_KEY = "admin"
    self.db_controller = None
    self.user_args = None
    self.buffer = None
    self.local = None
    self.function = None
    
  def auto_generate_courses(self):
    time_slots = self.create_time_slots()
    courses = []
    for i in range(1,74):
      course = {}
      course["_id"] = i
      course["name"] = "MUST " + str(i)
      course["year"] = 1
      course["is_must"] = True
      course["groups"] = time_slots
      course["pre-courses"] = []
      courses.append(course)
    for i in range(74,119):
      course = {}
      course["_id"] = i
      course["name"] = "MUST " + str(i)
      course["year"] = 2
      course["is_must"] = True
      course["groups"] = time_slots
      course["pre-courses"] = [i-73]
      courses.append(course)
    for i in range(119,129):
      course = {}
      course["_id"] = i
      course["name"] = "MUST " + str(i)
      course["year"] = 3
      course["is_must"] = True
      course["groups"] = time_slots
      course["pre-courses"] = [i-45]
      courses.append(course)
    for i in range(150,201):
      course = {}
      course["_id"] = i
      course["name"] = "OPTIONAL " + str(i)
      course["year"] = 0
      course["is_must"] = False
      course["groups"] = time_slots
      course["rating"] = random.randint(1,10)
      course["pre-courses"] = []
      courses.append(course)
    return courses

  def create_time_slots(self):
    available = []
    for i in range(0,6):
      if self.DAYS[i] != "friday":
        for j in range (0,self.TOTAL_HOURS_WEEK):
          date = self.DAYS[i] + " " + self.TIMES[j] + "-" + self.TIMES[j+1]
          available.append(date)
      else:
        for j in range (0,self.TOTAL_HOURS_WEEKEND):
          date = self.DAYS[i] + " " + self.TIMES[j] + "-" + self.TIMES[j+1]
          available.append(date)
    return available
  
  def set_db_controller(self,db_controller):
    self.db_controller = db_controller

  def set_user_args(self,user_args):
    self.user_args = user_args