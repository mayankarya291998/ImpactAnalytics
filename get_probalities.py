class AttendanceCalculator:
    def __init__(self, num_days):
        self.num_days = num_days

    def count_ways(self):
        if self.num_days == 0:
            return 1, 0  # Base case

        # table_data[i][j] means the number of ways to arrange i days with j consecutive absents at the end
        table_data = [[0] * 4 for _ in range(self.num_days + 1)]
        table_data[0][0] = 1  # One way to have zero days with zero absences

        for i in range(1, self.num_days + 1):
            for j in range(4):
                if j == 0:
                    table_data[i][j] = sum(table_data[i - 1])
                else:
                    table_data[i][j] = table_data[i - 1][j - 1]

        total_ways = sum(table_data[self.num_days])
        miss_graduation_ways = sum(table_data[self.num_days - 1][:3]) if self.num_days > 0 else 0

        return total_ways, miss_graduation_ways

    def get_probability(self):
        total_ways, miss_graduation_ways = self.count_ways()
        return f"{miss_graduation_ways}/{total_ways}"



def main():
    # Run test cases
    # For 5 days
    calculator = AttendanceCalculator(5)
    print(calculator.get_probability())  # Output: 14/29

    # For 10 days
    calculator = AttendanceCalculator(10)
    print(calculator.get_probability())  # Output: 372/773

main()
