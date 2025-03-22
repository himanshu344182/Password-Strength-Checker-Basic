import re
import math
from collections import Counter

def calculate_entropy(password):
    char_count = len(password)
    unique_chars = len(set(password))
    entropy = char_count * math.log2(unique_chars) if unique_chars > 0 else 0
    return entropy

def check_password_strength(password):
    length_score = min(len(password) / 8, 1)  # Normalized length score (max 1)
    
    lowercase = bool(re.search(r"[a-z]", password))
    uppercase = bool(re.search(r"[A-Z]", password))
    digits = bool(re.search(r"[0-9]", password))
    special_chars = bool(re.search(r"[^a-zA-Z0-9]", password))
    
    diversity_score = sum([lowercase, uppercase, digits, special_chars]) / 4  # Max 1
    entropy_score = min(calculate_entropy(password) / 40, 1)  # Normalized entropy
    
    overall_score = (length_score * 0.4) + (diversity_score * 0.3) + (entropy_score * 0.3)
    
    if overall_score > 0.8:
        strength = "Very Strong"
    elif overall_score > 0.6:
        strength = "Strong"
    elif overall_score > 0.4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, overall_score * 100

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, score = check_password_strength(password)
    print(f"Password Strength: {strength} ({score:.2f}%)")