import gui
import error_handler
import data
import Components.schedule as schedule
import db_controller
import Users.admin as admin
import Users.user as user 
import ast
import time
from sys import argv
def average(l):
    total = 0
    for item in l:
        total += item
    return total/len(l) 
if len(argv) == 1:
    appData = data.Data()
    error_handler = error_handler.ErrorHandler()
    gui.welcome_page(appData)
    if appData.user_args != appData.ADMIN_KEY:
        status = error_handler.args_controller(appData)
        if status == 0 :
            exit(status)
        appData.set_db_controller(db_controller.DataBaseController())
        user.User(appData).run()
    else:
        appData.set_db_controller(db_controller.DataBaseController())
        admin.Admin(appData).run()
    print("Press any key to exit")
    gui.request_user_input(appData)
elif argv[1] == "-t":
    flag = argv[1]
    test_times = int(argv[2])
    creation_parameters = ast.literal_eval(argv[3])
    generation_parameters = ast.literal_eval(argv[4])
    initial_population = ast.literal_eval(argv[5])
    mutation_parameters = ast.literal_eval(argv[6])
    mornings = []
    evenings = []
    days = []
    windows = []
    grades = []
    runtimes = []
    if argv[1] == "-t":
        user.STATISTICS_MODE = True
        print("Testing ... ")
        appData = data.Data()
        appData.set_user_args((1,[],[],[]))
        appData.function = 0
        appData.set_db_controller(db_controller.DataBaseController())
        msg = ""
        f = open("../Statistics Results.csv", "w")
    for creation_times in creation_parameters:
        for generations in generation_parameters:
            for population in initial_population:
                for mutation in mutation_parameters:
                    user.RECREATION_TIMES = creation_times
                    user.END_OF_TIMES = generations
                    user.INITIAL_POPULATION = population
                    user.MUTATION_PROB = mutation
                    iteration_msg = ""
                    mornings_msg = ""
                    evenings_msg = ""
                    days_msg = ""
                    windows_msg = ""
                    grade_msg = ""
                    runtime_msg = ""
                    for i in range(0,test_times):
                        user.FIRST_CREATION = True
                        t0 = time.time()
                        best = user.User(appData).run()
                        runtime = time.time() - t0
                        num_mornings = best.morning_hours
                        num_evenings = best.evening_hours
                        num_days = best.days
                        num_windows = best.windows
                        grade = best.grade
                        mornings_msg += str(num_mornings) + ","
                        evenings_msg += str(num_evenings) + ","
                        days_msg += str(num_days) + ","
                        windows_msg += str(num_windows) + ","
                        grade_msg += str(grade) + ","
                        runtime_msg += str(runtime) + ","
                        mornings.append(num_mornings)
                        evenings.append(num_evenings)
                        days.append(num_days)
                        windows.append(num_windows)
                        grades.append(best.grade)
                        runtimes.append(runtime)
                        iteration_msg += str(i)+","
                    msg += "Parameters" + "\n,Creation times,"+ str(creation_times)+"\n,Generations,"+str(generations)+"\n,Population,"+str(population)+"\n,Mutation,"+str(mutation) +"\nResults\n,Iteration," + iteration_msg + "\n,Mornings," + mornings_msg + ",,Mean," + str(average(mornings)) +"\n,Evenings," + evenings_msg + ",,Mean," + str(average(evenings)) +"\n,Days," + days_msg +",,Mean," + str(average(days)) +"\n,Windows,"+windows_msg+",,Mean," + str(average(windows)) +"\n,Grades," + grade_msg +",,Mean," + str(average(grades)) +"\n,Time," + runtime_msg + ",,Mean," + str(average(runtimes)) +"\n"
                    mornings = []
                    evenings = []
                    days = []
                    windows = []
                    grades = []
                    runtimes = []
    f.write(msg)
    f.close
            

    
