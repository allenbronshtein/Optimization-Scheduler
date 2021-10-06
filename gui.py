str_y_n = " ? y/n"
def tostring(course_number):
    if course_number == None:
        return "     "
    course_number = str(course_number)
    trailing_zero_number = 5 - len(course_number)
    for i in range(0,trailing_zero_number):
        course_number = "0" + course_number
    return course_number


def welcome_page(appData):
    print_title("Would you like to enter as admin? " + str_y_n)
    request_user_input(appData)
    if appData.buffer != 'n':
        appData.set_user_args(appData.ADMIN_KEY)
    else:
        print_title("Please insert your current year number")
        request_user_input(appData)
        year = appData.buffer
        redo_courses = []
        optional_courses = []
        unavailable = []
        print_title("Please enter course numbers you must redo, press 'r' to finish")
        while True:
            request_user_input(appData)
            course = appData.buffer
            if course == 'r':
                break
            redo_courses.append(course)
        print_title("Please enter optional course numbers you would like to take , press 'r' to finish")
        while True:
            request_user_input(appData)
            course = appData.buffer
            if course == 'r':
                break
            optional_courses.append(course)
        print_title("Enter times you cant study ex. sunday 8-14 Press 'r' to finish")
        while True:
            request_user_input(appData)
            block = appData.buffer
            if block == 'r':
                break
            unavailable.append(block)
        appData.set_user_args((year,redo_courses,optional_courses,unavailable))

def print_title(msg):
    print(str(msg))

def print_body(msg):
    print(msg)

def print_error(msg):
    print(str(msg))

def admin_page(appData):
    print_title("[1]. Auto insert\n[2]. Clear Collection\n[3]. Break")
    request_user_input(appData)

def request_user_input(appData):
    appData.buffer = input(">>>").lower().strip()

def print_table(schedule,ordered_courses):
    for i in range (0,14):
        msg = ""
        flag = False
        for j in range (0,6):
            day = None
            sunday_hour = None
            monday_hour = None
            tuesday_hour = None
            wednesday_hour = None
            thursday_hour = None
            friday_hour = None
            hour = i+7
            if i == 0:
                if j == 0: day = "sunday"
                elif j == 1: day = "monday"
                elif j == 2: day = "tuesday"
                elif j == 3: day = "wednesday"
                elif j == 4: day = "thursday"
                elif j == 5: day = "friday"

                if j != 5: msg+= "       " + day + "       | "
                else: msg += "    friday"
            elif not flag:
                flag = True
                if hour < 10:
                    msg += "0" + str(hour)
                else:
                    msg+= str(hour)

                sunday_hour = schedule.get_schedule_for("sunday",hour)
                if sunday_hour is not None: sunday_hour = ordered_courses[sunday_hour].number
                monday_hour = schedule.get_schedule_for("monday",hour)
                if monday_hour is not None: monday_hour = ordered_courses[monday_hour].number
                tuesday_hour = schedule.get_schedule_for("tuesday",hour)
                if tuesday_hour is not None: tuesday_hour = ordered_courses[tuesday_hour].number
                wednesday_hour = schedule.get_schedule_for("wednesday",hour)
                if wednesday_hour is not None: wednesday_hour = ordered_courses[wednesday_hour].number
                thursday_hour = schedule.get_schedule_for("thursday",hour)
                if thursday_hour is not None: thursday_hour = ordered_courses[thursday_hour].number
                friday_hour = schedule.get_schedule_for("friday",hour)
                if friday_hour is not None: friday_hour = ordered_courses[friday_hour].number

                sunday_hour = tostring(sunday_hour)
                monday_hour = tostring(monday_hour)
                tuesday_hour = tostring(tuesday_hour)
                wednesday_hour = tostring(wednesday_hour)
                thursday_hour = tostring(thursday_hour)
                friday_hour = tostring(friday_hour)
                msg += "|     " +sunday_hour+ "       |        " +monday_hour+ "        |         " +tuesday_hour+ "        |         " +wednesday_hour+ "          |         " +thursday_hour+ "         |      " + friday_hour
        print(msg +"\n" +"------------------------------------------------------------------------------------------------------------------------------------")