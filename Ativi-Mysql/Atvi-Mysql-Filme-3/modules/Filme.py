class film:
    film_id = ""
    title = ""
    release_year = ""
    length = ""
    
    def __init__(self, film_id, title, release_year, length):
        try:
            self.film_id = film_id
            self.title = title
            self.release_year = release_year
            self.length - length
        except Exception as e:
            print(str(e))
            
    def get_film(self):
        return self.length