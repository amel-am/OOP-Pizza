from math import pi
from typing import Union, Optional


class Circle:
    def __init__(self, radius: Optional[Union[int, float]] = None, diameter: Optional[Union[int, float]] = None):
        if radius:
            if radius < 0:
                raise ValueError("Radius cannot be zero or negative.")
            self.__radius = radius
        elif diameter:
            if diameter < 0:
                raise ValueError("Diameter cannot be zero or negative.")
            self.__radius = diameter
        else:
            raise ValueError(
                "A non zero-negative value has to be provided to either radius or diameter. Make also sure to provide the right type, either int or float.")
        self.__diameter = self.__radius / 2
        # Has to be floating value, because of type checker.
        self.__area = 0.0

    def calculate_area(self) -> Union[float]:
        # Calculates the area of the circle and round by 2.
        self.__area = round(self.__radius ** 2 * pi, 2)
        return self.__area

    @property
    def radius(self) -> Optional[Union[int, float]]:
        # Returns value of radius attribute.
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[int, float]) -> None:
        # Raises ValueError if radius is either equal to zero or less (negative number).
        if radius <= 0:
            raise ValueError(
                "The provided value has to be positive and not zero.")
        self.__radius = radius

    @property
    def diameter(self) -> Optional[Union[int, float]]:
        # Returns value of diameter attribute.
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: Union[int, float]) -> None:
        # Raises ValueError if diameter is either equal to zero or less (negative number).
        if diameter <= 0:
            raise ValueError(
                "The provided value has to be positive and not zero.")
        else:
            self.__diameter = diameter
            self.__radius = self.__diameter / 2

    @property
    def area(self) -> Optional[Union[int, float]]:
        return self.__area


class PizzaComparison(Circle):
    def __init__(self, small_pizza_radius: Optional[Union[int, float]] = None, small_pizza_diameter: Optional[Union[int, float]] = None,
                 large_pizza_radius: Optional[Union[int, float]] = None, large_pizza_diameter: Optional[Union[int, float]] = None):
        super().__init__(small_pizza_radius, small_pizza_diameter)
        self.__small_pizza_area = self.calculate_area()
        super().__init__(large_pizza_radius, large_pizza_diameter)
        self.__large_pizza_area = self.calculate_area()

    def compare_pizzas_price(self, small_pizza_price: Union[int, float],  large_pizza_price: Union[int, float],
                             small_pizza_amount: Union[int, float] = 1, large_pizza_amount: Union[int, float] = 1) -> Optional[str]:
        if small_pizza_price <= 0 or large_pizza_price <= 0:
            raise ValueError(
                "The price for the small pizza or the large pizza cannot be equal to zero or a negative number.")
        elif small_pizza_amount <= 0 or large_pizza_amount <= 0:
            raise ValueError(
                "The amount of the small pizza or large pizza cannot be equal to zero or a negative number.")
        small_pizza_total_cost = small_pizza_price * small_pizza_amount
        small_pizza_amount_area = self.__small_pizza_area * small_pizza_amount
        small_pizza_area_cost = small_pizza_total_cost / small_pizza_amount_area
        large_pizza_amount_area = large_pizza_price * large_pizza_amount
        large_pizza_total_cost = self.__large_pizza_area * large_pizza_amount
        large_pizza_area_cost = large_pizza_total_cost / large_pizza_amount_area
        if large_pizza_area_cost < small_pizza_area_cost:
            result = "The large pizza offers better value for the price."
        else:
            result = "The small pizza offers better value for the price."
        price_difference = abs(small_pizza_area_cost - large_pizza_total_cost)
        area_difference = abs(small_pizza_amount_area -
                              large_pizza_amount_area)
        return result + f"The price difference is ${price_difference:.2f} and the area difference is {area_difference:.2f}cm"


        # Example usage
pizza = PizzaComparison(small_pizza_radius=6, large_pizza_radius=4)
print(pizza.compare_pizzas_price(7, 4, 1, 1))
# prints -> "The small pizza is definitely worth it."
