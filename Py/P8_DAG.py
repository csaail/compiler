class DAG:
    def __init__(self):
        self.i = self.j = self.k = 0
        self.count = -1
        self.str = [None] * 10  # Store input code sequences
        self.table = [[""] * 10 for _ in range(10)]  # Initialize table for DAG

        print("Saail Chavan KFPMSCCS016\n")
        print("Enter the sequence of code:")
        print("Enter 'q' to Quit")

        # Input the sequence of code lines
        for self.i in range(len(self.str)):
            self.str[self.i] = input()
            if self.str[self.i] == "q":
                break
            else:
                self.count += 1

        # Display the sequence of code
        print("\nThe sequence of code is:")
        for line in self.str:
            if line == "q":
                break
            print(line)

    def tablestruct(self):
        # Fill the table based on code
        for self.i in range(self.count + 1):
            if len(self.str[self.i]) == 3:  # Case for D=A
                self.table[self.i][0] = self.str[self.i][0]
                self.table[self.i][1] = self.str[self.i][1]
                self.table[self.i][2] = self.str[self.i][2]
            elif len(self.str[self.i]) == 5:  # Case for A=B+C
                self.table[self.i][0] = self.str[self.i][0]
                self.table[self.i][1] = self.str[self.i][3]
                self.table[self.i][2] = self.str[self.i][2]
                self.table[self.i][3] = self.str[self.i][4]

        # Optimization: Removing redundant computations
        for self.i in range(self.count + 1):
            for self.j in range(self.i + 1, self.count + 1):
                if len(self.str[self.i]) == 5 and len(self.str[self.j]) == 5:
                    if self.str[self.i][2:5] == self.str[self.j][2:5]:
                        self.table[self.i][0] += f",{self.str[self.j][0]}{self.str[self.j][4]}"
                        self.table[self.j] = [""] * 10

        # Handle case for D=A
        for self.i in range(self.count + 1):
            if len(self.str[self.i]) == 3:
                for self.j in range(self.count):
                    if self.str[self.i][2] == self.str[self.j][0]:
                        self.table[self.j][0] += f",{self.str[self.i][0]}"
                        self.table[self.i] = [""] * 10

        # Print the table
        print("\nLabel\tOperator\tLeft\tRight")
        for row in self.table[:self.count + 1]:
            print("\t".join(row[:self.count + 2]))

if __name__ == "__main__":
    dag = DAG()
    dag.tablestruct()
