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
        # Initializes area with 0.0. Has to be floating value, because of type checker.
        self.__area = 0.0

    def calculate_area(self) -> float:
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
        # Returns value of diameter property.
        return self.__radius * 2

    @diameter.setter
    def diameter(self, diameter: Union[int, float]) -> None:
        # Raises ValueError if diameter is either equal to zero or less (negative number).
        if diameter <= 0:
            raise ValueError(
                "The provided value has to be positive and not zero.")

        self.__radius = self.__radius / 2

    @property
    def area(self) -> Union[int, float]:
        return self.__area

    @area.setter
    def area(self, area: Union[int, float]) -> None:
        if area <= 0:
            raise ValueError(
                "The area of a circle cannot be zero or negative.")
        else:
            self.__area = float(area)


class PizzaComparison():
    def __init__(self, small_pizza_radius: Optional[Union[int, float]] = None, small_pizza_diameter: Optional[Union[int, float]] = None,
                 large_pizza_radius: Optional[Union[int, float]] = None, large_pizza_diameter: Optional[Union[int, float]] = None):
        self.__small_pizza_instance = Circle(
            small_pizza_radius, small_pizza_diameter)
        self.__small_pizza_area = self.__small_pizza_instance.calculate_area()
        self.__large_pizza_instance = Circle(
            large_pizza_radius, large_pizza_diameter)
        self.__large_pizza_area = self.__large_pizza_instance.calculate_area()

    @property
    def small_pizza_radius(self) -> Optional[Union[int, float]]:
        return self.__small_pizza_instance.radius

    @small_pizza_radius.setter
    def small_pizza_radius(self, radius: Union[int, float]) -> None:
        self.__small_pizza_instance.radius = radius
        self.__small_pizza_area = self.__small_pizza_instance.calculate_area()

    @property
    def small_pizza_diameter(self) -> Optional[Union[int, float]]:
        return self.__small_pizza_instance.diameter

    @small_pizza_diameter.setter
    def small_pizza_diameter(self, diameter: Union[int, float]) -> None:
        self.__small_pizza_instance.diameter = diameter
        self.__small_pizza_area = self.__small_pizza_instance.calculate_area()

    @property
    def small_pizza_area(self) -> Union[int, float]:
        return self.__small_pizza_area

    @small_pizza_area.setter
    def small_pizza_area(self, area: Union[int, float]) -> None:
        if area <= 0:
            raise ValueError(
                "The area of the small Pizza cannot be zero or negative.")
        else:
            self.__small_pizza_area = area

    @property
    def large_pizza_radius(self) -> Optional[Union[int, float]]:
        return self.__large_pizza_instance.radius

    @large_pizza_radius.setter
    def large_pizza_radius(self, radius: Union[int, float]) -> None:
        self.__large_pizza_instance.radius = radius
        self.__large_pizza_area = self.__large_pizza_instance.calculate_area()

    @property
    def large_pizza_diameter(self) -> Optional[Union[int, float]]:
        return self.__large_pizza_instance.diameter

    @large_pizza_diameter.setter
    def large_pizza_diameter(self, diameter: Union[int, float]) -> None:
        self.__large_pizza_instance.diameter = diameter
        self.__large_pizza_area = self.__large_pizza_instance.calculate_area()

    @property
    def large_pizza_area(self) -> Union[int, float]:
        return self.__large_pizza_area

    @large_pizza_area.setter
    def large_pizza_area(self, area: Union[int, float]) -> None:
        if area <= 0:
            raise ValueError(
                "The area of the small Pizza cannot be zero or negative.")
        else:
            self.__large_pizza_area = area

    def compare_pizzas_price(self, small_pizza_price: Union[int, float],  large_pizza_price: Union[int, float],
                             small_pizza_amount: Union[int, float] = 1, large_pizza_amount: Union[int, float] = 1) -> str:
        if small_pizza_price <= 0 or large_pizza_price <= 0:
            raise ValueError(
                "The price for the small pizza or the large pizza cannot be equal to zero or a negative number.")
        elif small_pizza_amount <= 0 or large_pizza_amount <= 0:
            raise ValueError(
                "The amount of the small pizza or large pizza cannot be equal to zero or a negative number.")
        print(self.__large_pizza_area)
        print(self.__small_pizza_area)
        small_pizza_total_cost = small_pizza_price * \
            small_pizza_amount  # Total cost of all small pizzas
        small_pizza_total_area = self.__small_pizza_area * \
            small_pizza_amount  # Area combined with all small pizzas
        small_pizza_area_cost = small_pizza_total_cost / \
            small_pizza_total_area  # Cost per area
        large_pizza_total_cost = large_pizza_price * \
            large_pizza_amount  # Total cost of all large pizzas
        large_pizza_total_area = self.__large_pizza_area * \
            large_pizza_amount  # Area combined with all large pizzas
        large_pizza_area_cost = large_pizza_total_cost / \
            large_pizza_total_area  # Cost per area
        if large_pizza_area_cost < small_pizza_area_cost:
            result = "The large pizza offers better value for the price."
        elif large_pizza_area_cost > small_pizza_area_cost:
            result = "The small pizza offers better value for the price."
        else:
            result = "Both offer the same value for the price."
        price_difference = abs(small_pizza_area_cost - large_pizza_area_cost)
        area_difference = abs(small_pizza_total_area -
                              large_pizza_total_area)
        return result + f"The price difference is ${price_difference:.2f} and the area difference is {area_difference:.2f}cm"


        # Example usage
pizza = PizzaComparison(small_pizza_radius=3, large_pizza_radius=3)
print(pizza.compare_pizzas_price(small_pizza_price=5, large_pizza_price=4))
# prints -> "The large pizza offers better value for the price."
