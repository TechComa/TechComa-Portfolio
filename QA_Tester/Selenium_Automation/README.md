# 🧪 Selenium Automation Framework

This project demonstrates a **professional QA Automation Framework** built with Selenium WebDriver, Page Object Model (POM), TestNG, and advanced features like network fault injection, visual regression, and accessibility testing.  
It simulates **real-world QA workflows** used by automation engineers in enterprise teams.



## Framework 

**Flow Explanation**:
1. **Selenium WebDriver** – Automates user interactions with the browser (clicks, form inputs, navigation).  
2. **Page Object Model (POM)** – Keeps test code clean and maintainable by separating *page elements* from *test logic*.  
3. **TestNG** – Organizes and executes test cases with parallel runs, groups, and parametrization.  
4. **Allure Reports** – Generates rich HTML reports with screenshots and test history for easy review.  
5. **Advanced Testing** – Covers resilience (network throttling, server faults), accessibility (axe-core), and visual regression (AShot).  
6. **CI/CD Pipeline** – Runs tests automatically in GitHub Actions or Jenkins for continuous integration.  
7. **Managers & Devs** – Access easy to read reports and dashboards to make informed decisions.  



##  Key Features
-  **Cross-browser support** (Chrome, Firefox, Headless mode).  
-  **Parallel execution** with TestNG.  
-  **Page Object Model (POM)** for scalability.  
-  **Allure reporting** with screenshots on failure.  
-  **Network fault injection** using Chrome DevTools.  
-  **Visual regression testing** with pixel comparison.  
-  **Accessibility scans** (axe-core).  
-  **CI/CD ready** with GitHub Actions workflow.  



##  How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/TechComa/TechComa-Portfolio.git
   cd QA_Tester/Selenium_Automation

2. Install dependencies with Maven
   '''bash
   mvn clean install

3. Run Tests
   '''bash
   mvn test -Dheadleass=true -Dbrowser=chrome

4. Generate Allure Report
   '''bash
   mvn allure:serve

## Use Cases
- Smoke test of login & checkout flow 
- Validate app behavior under slow network or server errors.
- Verify UI layout hasn't regressed between builds.
- Ensure accessibility compliance for all users.
