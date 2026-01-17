import json

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
    database = {}
    
    print(f"Generating database for numbers 1 to {max_number}...")
    
    for num in range(1, max_number + 1):
        divisors = find_divisors(num)
        prime = is_prime(num)
        
        database[num] = {
            "divisors": divisors,
            "is_prime": prime,
            "divisor_count": len(divisors)
        }
        
        if num % 1000 == 0:
            print(f"Processed {num} numbers...")
    
    return database

# Generate database
max_num = 10000
db = generate_database(max_num)

# Save to JSON file
output_file = "numbers_database.json"
with open(output_file, 'w') as f:
    json.dump(db, f, indent=2)

print(f"\nDatabase created successfully!")
print(f"File: {output_file}")
print(f"Total numbers: {len(db)}")
print(f"Prime numbers: {sum(1 for data in db.values() if data['is_prime'])}")
