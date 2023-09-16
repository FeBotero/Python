class Film:
    def __init__(self, name, year,duration):
        self.__name = name
        self.__year = year
        self.__duration = duration
    
    def get_film_name(self):
        return self.__name
    def get_film_year(self):
        return self.__year
    def get_film_duration(self):
        return self.__duration
    def resume(self):
        print("O filme {} do ano {} tem a duração de {} minutos.".format(self.get_film_name(),self.get_film_year(),self.get_film_duration()))

class Series:
    def __init__(self,name, year,season):
        self.__name = name
        self.__year = year
        self.__season = season
    def get_series_name(self):
        return self.__name
    def get_series_year(self):
        return self.__year
    def get_series_season(self):
        return self.__season
    
    def resume(self):
        print("A serie {} do ano {} tem o total de {} temporadas".format(self.get_series_name(),self.get_series_year(),self.get_series_season()))