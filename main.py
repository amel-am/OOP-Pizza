from math import pi
from typing import Union, Optional


class Circle:
    def __init__(self, radius: Optional[Union[int, float]] = None, diameter: Optional[Union[int, float]] = None):
        if isinstance(radius, (int, float)):
            self.__radius_diameter = radius
        elif isinstance(diameter, (int, float)):
            self.__radius_diameter = diameter

    def calculate_area(self) -> float:
        # Calculates the area of the circle and round by 2.
        return round(self.__radius ** 2 * pi, 2)

    @property
    def radius(self) -> Optional[Union[int, float]]:
        # Returns value of radius attribute.
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[int, float]) -> None:
        # Raises ValueError if radius is either equal to zero or less (negative number).
        if not isinstance(radius, (int, float)):
            raise ValueError("The value provided is not of type float or int.")
        elif radius <= 0:
            raise ValueError(
                "The provided value has to be positive and not zero.")
        else:
            self.__radius = radius
            self.__diameter = self.__radius * 2

    @property
    def diameter(self) -> Optional[Union[int, float]]:
        # Returns value of diameter attribute.
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: Union[int, float]) -> None:
        # Raises ValueError if the newly assigned value of diameter is not of type float or int.
        if not isinstance(diameter, (int, float)):
            raise ValueError("The value provided is not of type float or int.")
        # Raises ValueError if diameter is either equal to zero or less (negative number).
        elif diameter <= 0:
            raise ValueError(
                "The provided value has to be positive and not zero.")
        else:
            self.__diameter = diameter
            self.__radius = self.__diameter / 2


class PizzaCalculator(Circle):
    def __init__(self, small_pizza_radius: Union[int, float] = 1, small_pizza_diameter: Union[int, float] = 1,
                 large_pizza_radius: Union[int, float] = 1, large_pizza_diameter: Union[int, float] = 1):
        self.__small_pizza_radius = small_pizza_radius
        self.__small_pizza_diameter = small_pizza_diameter
        self.__large_pizza_radius = large_pizza_radius
        self.__large_pizza_diameter = large_pizza_diameter
        super().__init__(self.__small_pizza_radius, self.__small_pizza_diameter)
        self.__small_pizza_area = self.calculate_area()
        super().__init__(self.__large_pizza_radius, self.__large_pizza_diameter)
        self.__large_pizza_area = self.calculate_area()

    @property
    def small_pizza_area(self):
        return self.__small_pizza_area

    @property
    def small_pizza_radius(self):
        return self.__small_pizza_radius

    @property
    def small_pizza_diameter(self):
        return self.__small_pizza_diameter

    @property
    def large_pizza_radius(self):
        return self.__large_pizza_radius

    @property
    def large_pizza_diameter(self):
        return self.__large

    @property
    def large_pizza_area(self):
        return self.__large_pizza_area

    def compare_price(self, small_pizza_amount: Union[int, float] = 1, small_pizza_price: Union[int, float] = 4,
                      large_pizza_amount: Union[int, float] = 1, large_pizza_price: Union[int, float] = 6):
        if isinstance(small_pizza_amount, (int, float)) and isinstance(large_pizza_amount, (int, float)):
            if small_pizza_amount <= 0 or large_pizza_amount <= 0:
                raise ValueError(
                    "Amount of large pizza or small can't be equal to zero or negative.")
        if isinstance(small_pizza_price, (int, float)) and isinstance(large_pizza_price, (int, float)):
            if small_pizza_amount <= 0 or large_pizza_amount <= 0:
                raise ValueError(
                    "Cost of large pizza or small can't be equal to zero or negative.")
        small_pizza_price_amount = small_pizza_amount * small_pizza_price
        large_pizza_price_amount = large_pizza_amount * large_pizza_price
        small_pizza_area_amount = self.small_pizza_area * small_pizza_amount
        large_pizza_area_amount = self.large_pizza_area * large_pizza_amount
        if small_pizza_price_amount > large_pizza_price_amount:
            if small_pizza_area_amount > large_pizza_area_amount:
                return "You are getting more pizza but it costs more."
            else:
                return "You are getting less pizza and it even costs more, what a waste."
        else:
            print("hello")

            # Example usage
kreis = Circle(5)
pizza = PizzaCalculator(small_pizza_radius=3, large_pizza_radius=6)
print(pizza.small_pizza_area)
print(pizza.large_pizza_area)
