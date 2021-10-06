import pymongo as mongo_client
import gui
class DataBaseController:
    def __init__(self):
        self.cluster = mongo_client.MongoClient("mongodb+srv://allen_bronshtein:_123456@optimization-project-cl.zpogl.mongodb.net/Optimization-DB?retryWrites=true&w=majority")
        self.db = self.cluster["Optimization-DB"]
        self.collection = self.db["Courses"]
    
    def auto_insert(self,appData):
        # items = appData.auto_generate_courses()
        items = [
            {"_id":19111,"name":"OOP Lecture","year":1,"is_must":True,"groups":["sunday 14-16","monday 11-13","monday 14-16"],"pre-courses":[0]},
            {"_id":29111,"name":"OOP Practice","year":1,"is_must":True,"groups":["sunday 16-18","sunday 18-20","monday 14-16","monday 16-18","monday 18-20","tuesday 10-12","tuesday 12-14","tuesday 14-16"],"pre-courses":[0]},
            {"_id":19113,"name":"Algebra 2 Lecture","year":1,"is_must":True,"groups":["monday 11-14","tuesday 9-12","wednesday 11-14"],"pre-courses":[0]},
            {"_id":29113,"name":"Algebra 2 Practice","year":1,"is_must":True,"groups":["monday 14-15","monday 15-16","monday 16-17","monday 17-18","wednesday 14-15","wednesday 15-16","wednesday 16-17","wednesday 17-18"],"pre-courses":[0]},
            {"_id":19120,"name":"Data Structure Lecture","year":1,"is_must":True,"groups":["sunday 14-16","tuesday 10-12","tuesday 14-16"],"pre-courses":[0]},
            {"_id":29120,"name":"Data Structure Practice","year":1,"is_must":True,"groups":["tuesday 10-12","tuesday 12-14","tuesday 16-18","tuesday 18-20","wednesday 10-12","wednesday 12-14","wednesday 16-18"],"pre-courses":[0]},       
            {"_id":19123,"name":"Models Lecture","year":1,"is_must":True,"groups":["sunday 12-14","sunday 16-18","monday 12-14"],"pre-courses":[0]}, 
            {"_id":29123,"name":"Models Practice","year":1,"is_must":True,"groups":["tuesday 12-14","tuesday 14-16","tuesday 16-18","wednesday 10-12","wednesday 14-16","wednesday 16-18","thursday 14-16","thursday 16-18"],"pre-courses":[0]}, 
            {"_id":19197,"name":"District Math Lecture","year":1,"is_must":True,"groups":["sunday 10-12","sunday 12-14","thursday 10-12"],"pre-courses":[0]}, 
            {"_id":29197,"name":"District Math Practice","year":1,"is_must":True,"groups":["sunday 12-13","sunday 13-14","sunday 14-15","sunday 15-16","thursday 12-13","thursday 13-14","thursday 14-15","thursday 15-16"],"pre-courses":[0]}, 
            ]
        try:
            self.collection.insert_many(items)
        except Exception:
            gui.print_error("Something went wrong while inserting to DB")

    def clear(self):
        try:
            self.collection.delete_many({})
        except Exception:
            gui.print_error("Something went wrong while clearing DB")

    def pull(self,appData):
        try:
            appData.local = self.collection.find({})
        except Exception:
            gui.print_error("Something went wrong while pulling from DB")
    
    def find(self,appData,value):
        try:
            appData.buffer = self.collection.find(value)
        except Exception:
            gui.print_error("Something went wrong while searching in DB")