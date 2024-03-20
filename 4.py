class Apartment:
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms

    def show_apartment(self):
        return f"Квартира: {self.address}, Площадь: {self.area} кв.м, Количество комнат: {self.number_of_rooms}"


apartment = Apartment("ул. Пушкина, 38", 46, 2)
print(apartment.show_apartment())
