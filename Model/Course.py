class Course:
    def __init__(self, courseID, description, short_description, duration, image, learning_outcome, level, name, price, rating, reviews, students_count, trainer, video_link,tag):
        self.courseID = courseID
        self.description = description
        self.short_description = short_description
        self.duration = duration
        self.image = image
        self.learning_outcome = learning_outcome
        self.level = level
        self.name = name
        self.price = price
        self.rating = rating
        self.reviews = reviews
        self.students_count = students_count
        self.trainer = trainer
        self.video_link = video_link
        self.tag = tag
        
class Course_For_Search(Course):
    def __init__(self, courseID, description, short_description, duration, image, learning_outcome, level, name, price, rating, reviews, students_count, trainer, video_link,tag, search_points):
        Course.__init__(self, courseID, description, short_description, duration, image, learning_outcome, level, name, price, rating, reviews, students_count, trainer, video_link,tag)
        self.search_points = search_points
