import matplotlib.pyplot as plt

def generate_collatz_sequence(n):
    """Generates the Collatz sequence starting from n."""
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

def plot_sequence(sequence, start_number):
    """Plots the generated Collatz sequence."""
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o', linestyle='-', color='b', markersize=4)

    plt.title(f"Collatz Sequence for {start_number}")
    plt.xlabel("Step Number")
    plt.ylabel("Value")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    """Handles user input, displays the string, and generates the plot."""
    print("--- The Collatz Conjecture Generator & Plotter ---")

    try:
        user_input = int(input("Enter a positive integer: "))

        if user_input <= 0:
            print("Please enter a strictly positive integer (greater than 0).")
            return

        # 1. Generate the sequence
        result = generate_collatz_sequence(user_input)

        # 2. Print the string output to the terminal
        sequence_string = " -> ".join(map(str, result))
        print(f"\nCollatz sequence for {user_input}:")
        print(sequence_string)
        print(f"Total steps taken: {len(result) - 1}")

        # 3. Plot the sequence
        print("\nGenerating plot... (Close the plot window to finish the program)")
        plot_sequence(result, user_input)

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Run the program
if __name__ == "__main__":
    main()