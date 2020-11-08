class Lecture(object):
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id", 0)
        self.lecturer: Lecturer = kwargs.get("lecturer", None)
        self.students: list = []


class Lecturer(object):
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("id", 0)
        self.name: str = kwargs.get("name", "Jimmy Johnjohn")
        self.lecture: Lecture = kwargs.get("lecture", None)
        self.minifig: dict = kwargs.get("minifig", {
            "hair": None,
            "face": None,
            "body": None,
            "legs": None,
        })


class Student(Lecturer):
    def __init__(self, **kwargs):
        Lecturer.__init__(self, **kwargs)
        self.notes: list = []
        self.hand_up: bool = False
        self.depressed: bool = True
