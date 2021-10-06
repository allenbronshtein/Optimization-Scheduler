import gui
# GRADE 0 - 59 for bad . less clashes -> higher score
# GRADE 60 - 99 for good . less windows and more function -> higher score
# GRADE 100 for optimal
BAD = 0
GOOD = 1
OPTIMAL = 2
EVENING_START_TIME = 14

def format_day_time(str):
  try:
    date = str.split(" ")
    day = date[0].strip()
    time = date[1].split("-")
    start_hour = int(time[0].strip())
    end_hour = int(time[1].strip())
    return day,start_hour,end_hour
  except Exception:
    gui.print_error("Error formating day time")
    return None  
def reformat_day_time(day_time):
  return str(day_time[0]) + " " + str(day_time[1]) + "-" + str(day_time[2])
def clashing(day_time_1,day_time_2):
  if day_time_1[0] == day_time_2[0]:
    if day_time_1[1] == day_time_2[1]:
      return True
    elif day_time_1[1] < day_time_2[1] and day_time_1[2] > day_time_2[1]:
        return True
    elif day_time_2[1] < day_time_1[1] and day_time_2[2] > day_time_1[1]:
        return True
  else:
    return False

class Schedule():
  def __init__(self,groups_list):
    self.updated = False
    self.grade = 0
    self.table = []
    self.groups = []
    self.clashing_hours = 0
    self.type = BAD
    self.windows = 0
    self.window_list = []
    self.morning_hours = 0
    self.evening_hours = 0
    self.days = 0
    for i in range(0,73):
      self.table.append(0)
    self.update(groups_list)

  def __eq__(self, other):
      return self.grade == other.grade   
  def __lt__(self, other):
      return self.grade < other.grade
  def __gt__(self,other):
      return self.grade > other.grade
  def __le__(self,other):
      return self.grade<=other.grade
  def __ge__(self,other):
      return self.grade>=other.grade
  def __ne__(self,other):
      return self.grade != other.grade


  def dayTime_to_index(self,day_time):
    day = day_time[0]
    start = day_time[1]
    finish = day_time[2]
    if start<8 or start>21 or finish<8 or finish>21:
      gui.print_error("Invalid indexing for " + str(day_time) + " daytime")
    else:
      if day == "sunday":
        return 0 + start - 8, 0 + finish - 9
      elif day == "monday":
        return 13 + start - 8, 13 + finish - 9
      elif day == "tuesday":
        return 26 + start - 8, 26 + finish - 9
      elif day == "wednesday":
        return 39 + start - 8 , 39 + finish - 9
      elif day == "thursday":
        return 52 + start - 8 , 52 + finish - 9
      elif day == "friday":
        return 65 + start - 8 , 65 + finish - 9
    return -1,-1

  def index_to_dayTime(self,index):
    start = index[0]
    finish = index[1]
    try:
      start = int(start)
      finish = int(finish)
    except Exception:
      gui.print_error("Bad non-integer indexes given")
      return ""
    if start < 0 or finish < 0 :
      gui.print_error("Start or finish time cannot be negative")
      return ""
    if start > 72 or finish > 72:
      gui.print_error("Start or finish time cannot be larger than length")
    if finish < start :
      gui.print_error("Finish index cannot be smaller than start index")

    #SUNDAY
    if 0<=start and start <=12:
      if 0<=finish and finish <=12:
        return "sunday " + str(start+8) + "-" + str(finish+9)
      else:
        return ""
    
    #MONDAY
    if 13<=start and start<=25:
      if 13<=finish and finish<=25:
        return "monday " + str(start-13+8) + "-" + str(finish-13+9)
      else:
        return ""
    
    #TUESDAY
    if 26<=start and start<=38:
      if 26<=finish and finish<=38:
        return "tuesday " + str(start-26+8) + "-" + str(finish-26+9)
      else:
        return ""

    #WEDNESDAY
    if 39<=start and start<=51:
      if 39<=finish and finish<=51:
        return "wednesday " + str(start-39+8) + "-" + str(finish-39+9)
      else:
        return ""
    
    #THURSDAY
    if 52<=start and start<=64:
      if 52<=finish and finish<=64:
        return "thursday " + str(start-52+8) + "-" + str(finish-52+9)
      else:
        return ""
    
    #FRIDAY
    if 65<=start and start<=72:
      if 65<=finish and finish<=72:
        return "friday " + str(start-65+8) + "-" + str(finish-65+9)
      else:
        return ""
  
  def count_windows(self):
    inCollege = False
    count = 0
    for i in range(0,13):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<12 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1

    inCollege = False  
    for i in range(13,26):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<25 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1

    inCollege = False
    for i in range(26,39):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<38 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1

    inCollege = False
    for i in range(39,52):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<51 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1

    inCollege = False
    for i in range(52,65):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<64 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1

    inCollege = False
    for i in range(65,73):
      if self.table[i] == 0 and not inCollege:
        continue
      elif self.table[i] == 1 and not inCollege:
        inCollege = True
      elif i<72 and inCollege == True:
        if self.table[i] == 0 and self.table[i+1] == 1:
          index = i,i
          daytime = self.index_to_dayTime(index)
          self.window_list.append(daytime)
          count += 1
    return count

  def count_day_mor_eve(self):
    morning_count = 0
    evening_count = 0
    days = []
    for i in range (0,73):
      if self.table[i] == 1:
        index = i,i
        day_time = self.index_to_dayTime(index)
        day_time = format_day_time(day_time)
        if day_time[0] not in days:
          days.append(day_time[0])
        if day_time[1] < EVENING_START_TIME:
          morning_count += 1
        else:
          evening_count += 1
    self.morning_hours = morning_count
    self.evening_hours = evening_count
    self.days = len(days)

  def update(self,groups_list):
    if not self.updated:
      self.updated = True
      for group in groups_list:
        index = self.dayTime_to_index(format_day_time(group))
        if index == (-1,-1):
          gui.print_error("Cannot index group " + str(group))
        else:
          self.groups.append(group)
          for i in range(index[0],index[1]+1):
            self.insert(i)
      if self.clashing_hours == 0:
        self.type = GOOD
        self.windows = self.count_windows()
        self.count_day_mor_eve()
    
  def insert(self,hour):
    if self.table[hour] == 1:
      self.clashing_hours += 1
    elif self.table[hour] == 0:
      self.table[hour] = 1

  def get_schedule_for(self,day,hour):
    if self.type == BAD:
      return None
    else:
      total_groups_number = len(self.groups)
      for i in range(0,total_groups_number):
        daytime = format_day_time(self.groups[i])
        group_day = daytime[0]
        group_start_hour = daytime[1]
        group_end_hour = daytime[2]
        if day == group_day and group_start_hour <= hour and group_end_hour > hour:
          return i
      return None
    