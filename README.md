# 2025-ITELEC2-LAB020
Week 05 - Working with Functions

Laboratory # 20 - Group Activity # 01 - Problem 02: Even or Odd Checker with Input and Logic Functions

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 20 - Group Activity # 01 - Problem 02: Even or Odd Checker with Input and Logic Functions**

   **Objective:**
   This challenge aims to strengthen your understanding of function design, input handling, and basic mathematical operations. You will practice:
   - Creating functions with specific responsibilities.
   - Using the modulo operator (%) for divisibility checks.
   - Handling user input and converting it to the appropriate data type.
   - Returning values from functions and using them in the main program.

   **Desired Output (Examples):**
   ```bash
   Enter an integer: 17
   17 is an Odd number.
   
   Enter an integer: 24
   24 is an Even number.
   ```
   
   **Notable Observations (to be discussed after completing the exercise):**
   - Function Specialization: The get_integer_input function focuses solely on obtaining and validating integer input, while the check_even_odd function handles the logic of determining whether a number is even or odd.
   - Modulo Operator: The check_even_odd function uses the modulo operator (%) to check if the number is divisible by 2, which is the key to determining evenness or oddness.
   - String Formatting: The check_even_odd function constructs and returns a formatted string that includes the number and its even/odd status.

   **Python Best Practices**
   - Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables (e.g., get_integer_input, check_even_odd, number).
   - Docstrings: Include docstrings for each function to explain its purpose, parameters, and return value.
   - Type Hints (Optional but Recommended): Use type hints to specify the expected data types for function parameters and return values.
   - Input Validation (Challenge Extension): Consider adding robust input validation to the get_integer_input function to handle cases where the user enters non-integer input. You could use a loop and a try-except block to repeatedly prompt the user until a valid integer is entered.
   - Test Thoroughly: Test your program with various inputs, including positive and negative integers, zero, and potentially invalid input (if you implement input validation) to ensure it works correctly in all cases.

   **Challenge Requirements:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `even_odd_checker_functions.py`
      
   2. get_integer_input() Function:
      - Purpose: Handles user input to obtain an integer.
      - No parameters.
      - Prompts the user to enter an integer.
      - Reads and converts the input to an integer data type.
      - Returns the integer.
      
   3. check_even_odd(number) Function:
      - Purpose: Determines if a given number is even or odd.
      - Takes one parameter: number (integer).
      - Uses the modulo operator (%) to check if the number is divisible by 2.
      - Returns a formatted string message indicating whether the number is "Even" or "Odd" (e.g., "17 is an Odd number.").

   4. Main Program Flow:
      - Calls get_integer_input() to obtain an integer from the user.
      - Calls check_even_odd(), passing the obtained integer as an argument.
      - Displays the message returned by check_even_odd() to the user.

   **Conclusion**
   This challenge reinforces the importance of breaking down problems into smaller, more manageable functions. By separating the input handling from the even/odd logic, you create more modular and reusable code. This approach also makes your code easier to understand, test, and debug.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 05 - Laboratory # 20"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
