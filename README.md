# 2025-ITELEC2-LAB022
Week 05 - Working with Functions

Laboratory # 22 - Group Activity # 01 - Problem 04: Simple Menu-Driven Program with Function-Based Operations

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

**Laboratory # 22 - Group Activity # 01 - Problem 04: Simple Menu-Driven Program with Function-Based Operations**

   **Objective:**
   This challenge focuses on creating a menu-driven program, demonstrating how to structure a program with multiple functionalities using functions. You will practice:
   - Designing functions with specific purposes.
   - Using a while loop for continuous program execution.
   - Handling user input and menu choices.
   - Using conditional statements (if, elif, else) for decision-making.
   - (Optionally) Creating helper functions for better modularity.

   **Desired Output:**
   ```bash
   Menu:
   1. Greet User
   2. Check Even/Odd
   3. Exit
   Enter your choice (1-3): 1
   Hello! Welcome!
   
   Menu:
   1. Greet User
   2. Check Even/Odd
   3. Exit
   Enter your choice (1-3): 2
   Enter an integer: 33
   33 is an Odd number.
   
   Menu:
   1. Greet User
   2. Check Even/Odd
   3. Exit
   Enter your choice (1-3): 3
   Exiting program. Goodbye!
   ```
   
   **Notable Observations:**
   - Menu-Driven Structure: The program uses a loop to repeatedly display a menu and process user choices, providing a basic interactive user interface.
   - Function Decomposition: Different functionalities are separated into functions (display_menu, handle_menu_choice, and potentially greet_user and even_odd_checker_action), making the code more organized and easier to understand.
   - Code Reusability: You can potentially reuse the check_even_odd function from a previous challenge, demonstrating the benefits of modular function design.

   **Python Best Practices**
   - Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables.
   - Docstrings: Include docstrings for each function to explain its purpose, parameters, and return value.
   - Type Hints (Optional but Recommended): Use type hints to specify the expected data types for function parameters and return values.
   - Input Validation (Challenge Extension): Consider adding input validation to handle invalid menu choices (e.g., non-numeric input, choices outside the valid range).
   - Clear Menu Structure: Display the menu options in a clear and organized way to make it user-friendly.
   - Helper Functions: Use helper functions to break down complex tasks (like handling the even/odd check) into smaller, more manageable units.
   - Test Thoroughly: Test your program with various menu choices and inputs to ensure it works correctly in all cases.

   **Challenge Requirements:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `menu_driven_program_functions.py`
      
   2. display_menu() Function:
      - Purpose: Displays the program's menu options to the user.
      - No parameters.
      - Prints the menu options in a clear and numbered format.
      
   3. handle_menu_choice(choice) Function:
      - Purpose: Executes the corresponding action based on the user's menu choice.
      - Takes one parameter: choice (integer representing the menu option).
      - Uses conditional statements (if, elif, else) to determine the action:
         - If choice is 1, call a helper function greet_user() (if you create one) to display a greeting message.
         - If choice is 2, call a helper function even_odd_checker_action() (if you create one) to get an integer input and check if it's even or odd.
         - If choice is 3, print an exit message and return a signal to terminate the program loop (e.g., True).
         - For any invalid choice, print an error message and return a signal to continue the program loop (e.g., False).

   4. (Optional) Helper Functions:
      - greet_user(): Prints a greeting message.
      - even_odd_checker_action(): Handles the logic for the even/odd check, including getting input and potentially reusing the check_even_odd() function from a previous challenge.

   5. Main Program Flow:
      - Uses a while True loop to continuously display the menu and process user choices.
      - Inside the loop:
         - Calls display_menu() to show the menu.
         - Gets the user's menu choice.
         - Calls handle_menu_choice() with the user's choice.
         - If handle_menu_choice() returns a signal to terminate (e.g., True), break out of the loop to end the program.

   **Conclusion**
   This challenge helps you understand how to structure a program with multiple functionalities using a menu-driven approach. By separating different operations into functions, you can create more organized and modular code. This approach also improves code reusability and makes it easier to add or modify features in the future.

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
git commit -m "Submitting Python Week 05 - Laboratory # 22"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
