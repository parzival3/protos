import json
from datetime import datetime

def find_divisors(n):
    """Find all divisors of a number (excluding 1 and the number itself)."""
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                divisors.append(n // i)
    return sorted(divisors)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_database(max_number):
    """Generate database of numbers with their divisors and prime status."""
    database = {
        "_metadata": {
            "max_number": max_number,
            "total_count": max_number,
            "generated_date": None,  # Will be set when saving
            "perfect_squares": []  # Will be populated
        }
    }
    
    print(f"Generating database for numbers 1 to {max_number}...")
    
    prime_count = 0
    perfect_squares = []
    
    # Calculate all perfect squares up to max_number
    i = 1
    while i * i <= max_number:
        perfect_squares.append(i * i)
        i += 1
    
    for num in range(1, max_number + 1):
        divisors = find_divisors(num)
        prime = is_prime(num)
        if prime:
            prime_count += 1
        
        database[str(num)] = {
            "divisors": divisors,
            "is_prime": prime,
            "divisor_count": len(divisors)
        }
        
        if num % 1000 == 0:
            print(f"Processed {num} numbers...")
    
    database["_metadata"]["prime_count"] = prime_count
    database["_metadata"]["perfect_squares"] = perfect_squares
    
    return database

# Generate database
max_num = 100000
db = generate_database(max_num)

# Add timestamp
db["_metadata"]["generated_date"] = datetime.now().isoformat()

# Save to JSON file
output_file = "numbers_database.json"
with open(output_file, 'w') as f:
    json.dump(db, f, indent=2)

print(f"\nDatabase created successfully!")
print(f"File: {output_file}")
print(f"Total numbers: {db['_metadata']['total_count']}")
print(f"Prime numbers: {db['_metadata']['prime_count']}")
print(f"Perfect squares: {len(db['_metadata']['perfect_squares'])}")
