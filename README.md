# Digikala Incredible Offers Automated Checkout Bot 🚀

An automated Selenium-based bot designed to scan Digikala's "Incredible Offers" (شگفت‌انگیز), filter products based on a user-defined discount percentage, add matching items to the shopping cart, and navigate through the checkout and login workflow.

## ✨ Features
- **Dynamic Filtering:** Promptly asks the user for the preferred discount percentage right in the terminal.
- **Smart Scanning:** Smoothly scrolls through the promotional page and avoids interacting with already visited products using a tracking set.
- **Fail-safe Termination:** Automatically closes the browser and stops execution if no products match the specified criteria, preventing useless checkout operations.
- **Interactive Execution:** Structured with code cell markers (`#%%`) allowing step-by-step or cell-by-cell execution within VS Code or Jupyter.
- **Streamlined Checkout:** Automatic shopping cart interaction and dynamic terminal prompt for entering your phone number/email directly into the login state.

---

## 🛠️ Prerequisites

Before running the script, make sure you have the following installed:
- Python 3.x
- Google Chrome Browser
- ChromeDriver (Matching your current Chrome version and placed in the project root directory)

### Required Libraries
Install the necessary dependencies using pip:
```bash
pip install selenium