class Movie:
    def __init__(self, name, *, rating=None, release_date=None, budget=None, box_office=None):
        self.name=name
        self.rating=rating
        self.release_date=release_date
        self.budget=budget
        self.box_office=box_office

    def earnings(self):

        # If the box office or the budget is unknown, return None
        if self.box_office is None or self.budget is None:
            return
        return self.box_office - self.budget
    
    def __eq__(self, other):
        return (
            self.name == other.name and
            self.rating == other.rating and
            self.release_date == other.release_date and
            self.budget == other.budget and
            self.box_office == other.box_office
        )


def test_equality():
    t1 = Movie("Movie 1")
    t2 = Movie("Movie 1")

    assert t1==t2

def test_basic_movie_creation():
    testmovie = Movie("Movie 1")

    assert testmovie.name == "Movie 1"
    assert testmovie.rating == None
    assert testmovie.release_date == None
    assert testmovie.budget == None
    assert testmovie.box_office == None

def test_earnings_error_without_budget_box_offict():
    t1 = Movie("Movie 1",
        budget=None,
        box_office=None)

    assert t1.earnings() == None

    t2 = Movie("Movie 2",
        budget=100,
        box_office=None)

    assert t2.earnings() == None

    t3 = Movie("Movie 3",
        budget=None,
        box_office=100)

    assert t3.earnings() == None

def test_movie_creation():
    name = "Movie 1"
    rating = 6.7
    release_date = "2018-09-19"
    budget = 100000
    box_office = 200000
    
    testmovie = Movie(name, 
        rating=rating, 
        release_date=release_date, 
        budget=budget, 
        box_office=box_office)
    
    assert testmovie.name == name
    assert testmovie.rating == rating
    assert testmovie.release_date == release_date
    assert testmovie.budget == budget
    assert testmovie.box_office == box_office

    assert testmovie.earnings() == box_office - budget

