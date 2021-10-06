import gui
class ErrorHandler:
    def check_year(self,year,msg,err_codes):
        try:
            year = int(year)
        except Exception:
            msg += year + " is not a valid year\n"
            err_codes.append(0)
        return msg,err_codes

    def check_courses(self,type,courses,msg,err_codes):
        for course in courses:
            try:
                course = int(course)
            except Exception:
                msg += course + " is not a valid course number\n"
                err_codes.append((type,course))
        return msg,err_codes

    def check_times(self,times,msg,err_codes,appData):
        for time in times:
            has_err = False
            try:
                form = time.split(" ")
                hours = form[1].split("-")
                day = form[0].strip()
                start_hour = hours[0].strip()
                end_hour = hours[1].strip()
                if day not in appData.DAYS:
                    has_err = True
                start_hour = int(start_hour)%24
                end_hour = int(end_hour)%24   
                if start_hour>end_hour:
                    has_err = True         
            except Exception:
                has_err = True
            if has_err:
                msg += time + " is not a valid time format\n"
                err_codes.append((3,time))
        return msg,err_codes

    def check_args(self,appData):
        msg = ""
        err_codes = []
        year = appData.user_args[0].strip()
        redo_courses = appData.user_args[1]
        optional_courses = appData.user_args[2]
        unavailable = appData.user_args[3]
        msg,err_codes = self.check_year(year,msg,err_codes)
        msg,err_codes = self.check_courses(1,redo_courses,msg,err_codes)
        msg,err_codes = self.check_courses(2,optional_courses,msg,err_codes)
        msg,err_codes = self.check_times(unavailable,msg,err_codes,appData)
        return msg,err_codes

    def fix_args(self,appData,err_codes):
        year = appData.user_args[0]
        redo_courses = appData.user_args[1]
        optional_courses = appData.user_args[2]
        unavailable = appData.user_args[3]
        for error in err_codes:
            if error == 0:
                gui.print_title("Please insert your current year number")
                gui.request_user_input(appData)
                year = appData.buffer
            elif error[0] == 1:
                course = error[1]
                gui.print_title("Redo Courses : Would you like to fix " + str(course) + gui.str_y_n)
                gui.request_user_input(appData)
                command = appData.buffer
                redo_courses.remove(course)
                if command != 'n':
                    gui.request_user_input(appData)
                    new_course = appData.buffer
                    redo_courses.append(new_course)
            elif error[0] == 2:
                course = error[1]
                gui.print_title("Choice Courses : Would you like to fix " + str(course) + gui.str_y_n)
                gui.request_user_input(appData)
                command = appData.buffer
                optional_courses.remove(course)
                if command != 'n':
                    gui.request_user_input(appData)
                    new_course = appData.buffer
                    optional_courses.append(new_course)
            elif error[0] == 3:
                time = error[1]
                gui.print_title("Time : Would you like to fix " + str(time) + gui.str_y_n)
                gui.request_user_input(appData)
                command = appData.buffer
                unavailable.remove(time)
                if command != 'n':
                    gui.request_user_input(appData)
                    new_time = appData.buffer
                    unavailable.append(new_time)
        appData.set_user_args((year,redo_courses,optional_courses,unavailable))

    def args_controller(self,appData):
        arg_check_response = self.check_args(appData)
        err_msg = arg_check_response[0]
        err_codes = arg_check_response[1]
        while err_msg != "":
            gui.print_error(err_msg)
            gui.print_title("Would you like to fix issues ? y/n")
            gui.request_user_input(appData)
            command = appData.buffer
            if command != "n":
                self.fix_args(appData,err_codes)
                arg_check_response = self.check_args(appData)
                err_msg = arg_check_response[0]
                err_codes = arg_check_response[1]
            else:
                gui.print_title("Shuting down system")
                return 0
        return 1