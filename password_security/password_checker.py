"""
Password Strength Checker
A tool to analyze password security and provide feedback
"""

import re

def check_password_strength(password):
    """
    Analyze a password and return its strength level with feedback
    
    Criteria:
    - Length: At least 8 characters (strong: 12+)
    - Uppercase: At least one A-Z
    - Lowercase: At least one a-z
    - Numbers: At least one 0-9
    - Special chars: At least one !@#$%^&*
    """
    
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  Consider using 12+ characters for extra security")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*)")
    
    # Check for common patterns (weak passwords)
    common_patterns = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        score = max(0, score - 2)
        feedback.append("❌ Your password contains common patterns - avoid these!")
    
    # Determine strength level
    if score <= 2:
        strength = "🔴 WEAK"
    elif score <= 4:
        strength = "🟡 MEDIUM"
    else:
        strength = "🟢 STRONG"
    
    return {
        "password": password,
        "strength": strength,
        "score": f"{score}/6",
        "feedback": feedback
    }


def display_result(result):
    """Display password analysis in a nice format"""
    print("\n" + "="*50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("="*50)
    print(f"\nPassword: {'*' * len(result['password'])}")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}")
    print("\nFeedback:")
    if result['feedback']:
        for item in result['feedback']:
            print(f"  {item}")
    else:
        print("  ✅ Excellent password! No improvements needed.")
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("Enter passwords to check their security strength")
    print("(Type 'quit' to exit)\n")
    
    while True:
        password = input("Enter a password to check: ")
        
        if password.lower() == 'quit':
            print("Goodbye! Stay secure! 🔒")
            break
        
        if not password:
            print("Please enter a password\n")
            continue
        
        result = check_password_strength(password)
        display_result(result)
