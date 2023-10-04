MOD = 1000000007

def calculate_number(X, Y):
    binary_str = '1' * X + '0' * Y  # Create a binary string with X ones followed by Y zeros
    num = int(binary_str, 2)  # Convert binary string to an integer
    return num % MOD

def main():
    inputs = int(input())
    for _ in range(inputs):
        X, Y = map(int, input().split())
        result = calculate_number(X, Y)
        print(result)

if __name__ == "__main__":
    main()
