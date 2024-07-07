# TASK-03 Password Complexity Checker
- Here we have to build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Moreover, it should provide feedback to users on the password's strength.
- In this python program we have kept the password length crietria as **12 characters**. However keeping **14 or more characters** is better.
- Please find the python program named **password_complexity_checker.py** attached.

# Password Complexity
Password complexity refers to the diversity and variety of characters used in a password. A complex password typically includes a combination of uppercase and lowercase letters, numbers, and special characters. The idea is that the more diverse the character set and the more unpredictable the password, the harder it will be for attackers to guess or crack it.

**Key Components of Password Complexity**

1. **Character Types:**
   - **Uppercase Letters (A-Z):** Adds complexity by requiring the use of uppercase letters in addition to lowercase ones.
   - **Lowercase Letters (a-z):** Essential for creating a diverse mix of characters.
   - **Numbers (0-9):** Including numbers makes the password harder to guess.
   - **Special Characters (@, #, $, etc.):** These add an extra layer of complexity and are often required for secure passwords.

2. **Length:**
   - Longer passwords are inherently more complex because they provide more space for combining different character types. A recommended minimum length is 12-16 characters.

3. **Unpredictability:**
   - Avoiding predictable patterns like sequences (`1234`, `abcd`) or repeated characters (`aaaa`, `1111`) is key to complexity.
   - Using a mix of characters in a random order reduces predictability.

4. **No Common Words or Phrases:**
   - Avoiding dictionary words or common phrases (`password`, `admin`) ensures that passwords are not easily guessable or susceptible to dictionary attacks.

**Example**

- **Simple Password:** `password123` (Weak, lacks variety and is predictable)
- **Complex Password:** `P@55w0rD!23#` (Strong, includes uppercase and lowercase letters, numbers, and special characters)

**Benefits of Password Complexity**

1. **Enhanced Security:** 
   - Complex passwords are harder to guess through brute-force or dictionary attacks.
   - They provide better protection against automated attack scripts that test common passwords or variations.

2. **Compliance:**
   - Many security policies and regulatory requirements mandate the use of complex passwords to protect sensitive data.

3. **Reduced Risk:**
   - Complex passwords reduce the likelihood of unauthorized access to accounts and sensitive information.
