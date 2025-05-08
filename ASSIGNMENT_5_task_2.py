def main():
    # Create a list of numbers from 1 to 10
    numbers = list(range(1, 11))
    print("Original list:", numbers)

    # Extract the first five elements
    extracted_numbers = numbers[:5]
    print("Extracted first five elements:", extracted_numbers)

    # Reverse the extracted elements
    reversed_numbers = extracted_numbers[::-1]
    print("Reversed extracted elements:", reversed_numbers)

if __name__ == "__main__":
    main()