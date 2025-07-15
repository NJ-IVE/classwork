class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        self.original_year = year
        self.month = month
        self.day = day
        self.year = year

    def calculate_weekday(self) -> str:

        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1

        q = self.day
        m = self.month
        K = self.year % 100
        J = self.year // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7


        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

    def print_result(self):
        weekday = self.calculate_weekday()
        print(f"{self.original_year}-{self.month if self.month <= 12 else self.month - 12}-{self.day} was a {weekday}.")



date = DateCalculator(2025,5,1)
date.print_result()
