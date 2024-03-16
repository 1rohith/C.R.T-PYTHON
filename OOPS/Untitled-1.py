
class CarShowroom:
    cgst = 0.08  # 8%
    sgst = 0.08  # 8%
    insurance = 5000  # Common insurance value for all cars

    def __init__(self):
        self.cars = []

    def add_car(self, make, model, year, ex_showroom_price):
        self.cars.append({
            'make': make,
            'model': model,
            'year': year,
            'ex_showroom_price': ex_showroom_price
        })
        print(f"{make} {model} added to the showroom.")

    def display_cars(self):
        if self.cars:
            print("Cars available in the showroom:")
            for idx, car in enumerate(self.cars, start=1):
                print(f"{idx}. {car['make']} {car['model']} ({car['year']})")
        else:
            print("No cars available in the showroom.")

    def model_name(self, company):
        print(f"Welcome to {company} showroom!")
        model = input(f"Please enter the model name for {company} (e.g., GNS, GDI, etc.): ")
        return model

    def variant(self, company, model):
        print(f"Select variant for {company} {model}:")
        variant = input("1. Petrol\n2. Diesel\nEnter your choice (1/2): ")
        return variant

    def display_price(self, company, model, variant):
        found = False
        for car in self.cars:
            if car['make'].lower() == company.lower() and car['model'].lower() == model.lower():
                found = True
                print(f"Ex-showroom price of {company} {model}: ${car['ex_showroom_price']}")
                onroad_price = car['ex_showroom_price'] + self.cgst * car['ex_showroom_price'] + self.sgst * car['ex_showroom_price'] + self.insurance
                print(f"On-road price of {company} {model}: ${onroad_price}")
                break
        if not found:
            print("Invalid company name or model.")

if __name__ == "__main__":
    showroom = CarShowroom()

    # Adding some cars
    showroom.add_car("Toyota", "Corolla", 2022, 25000)
    showroom.add_car("Honda", "Civic", 2023, 28000)
    showroom.add_car("Ford", "Mustang", 2024, 45000)

    # Displaying available cars
    showroom.display_cars()

    # Taking input from user
    company = input("Enter the car company name (Toyota/Honda/Ford): ")

    # Model selection
    model = showroom.model_name(company)

    # Variant selection
    variant = showroom.variant(company, model)

    # Displaying price
    showroom.display_price(company, model, variant)
