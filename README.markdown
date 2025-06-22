# ICICI Direct Data Scraper

This Python script uses Selenium WebDriver to automate data extraction from the ICICI Direct website. It logs into the ICICI Direct platform, switches between specified sub-accounts, and downloads data such as Trade Book, Portfolio Summary, Order Book (displayed as a table and saved as CSV), and additional data (My Portfolio and Orderbook) for a specific account. The script organizes downloaded files into account-specific directories, includes logging, error handling, and file consolidation features.

## Features
- Logs into ICICI Direct with provided credentials.
- Switches between multiple sub-accounts specified in the configuration.
- Downloads Trade Book and Portfolio Summary CSVs for each account.
- Extracts and displays Order Book data from the GTT tab in a formatted table, saving it to CSV.
- For the `IN303028-76957826-7510072528-NPNRO` account, downloads My Portfolio and Orderbook CSVs.
- Organizes downloaded files into account-specific subdirectories under `downloads` (e.g., `downloads/IN303028-76957800-6500081466-NRE/`).
- Consolidates downloaded CSVs by data type into the base `downloads` directory (if enabled).
- Includes retry logic for robust handling of transient errors.
- Logs all actions and errors to a file (`icici_extract.log`).

## Prerequisites
- **Python 3.6+**: Ensure Python is installed on your system.
- **Google Chrome**: The script uses Chrome WebDriver for browser automation.
- **Required Python Packages**:
  - `selenium`
  - `webdriver_manager`
  - `python-dotenv`
  - `retrying`
  - `tabulate`
- **ICICI Direct Credentials**: A valid username and password for the ICICI Direct platform.
- **Environment File**: A `.env` file with your ICICI Direct credentials.

## Setup Instructions
1. **Install Python**:
   - Download and install Python 3.6 or higher from [python.org](https://www.python.org/downloads/).
   - Ensure `pip` is available.

2. **Install Dependencies**:
   - Run the following command to install required Python packages:
     ```bash
     pip install selenium webdriver_manager python-dotenv retrying tabulate
     ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the same directory as the script with the following content:
     ```plaintext
     ICICI_USERNAME=your_icici_username
     ICICI_PASSWORD=your_icici_password
     ```
   - Replace `your_icici_username` and `your_icici_password` with your actual ICICI Direct credentials.

4. **Install Google Chrome**:
   - Ensure Google Chrome is installed on your system, as the script uses the Chrome WebDriver.

5. **Directory Setup**:
   - The script creates a `downloads` directory in the same folder as the script to store downloaded CSVs.
   - For each account, a subdirectory is created (e.g., `downloads/IN303028-76957800-6500081466-NRE/`) to store account-specific files.
   - Consolidated CSVs (if enabled) are saved directly in the `downloads` directory.

## How to Run the Script
1. **Save the Script**:
   - Save the provided Python script as `icici_scraper.py` (or another name of your choice).

2. **Prepare the Environment**:
   - Ensure the `.env` file is correctly configured with your ICICI Direct credentials.
   - Verify that all dependencies are installed.

3. **Run the Script**:
   - Open a terminal or command prompt in the directory containing the script.
   - Execute the script using Python:
     ```bash
     python icici_scraper.py
     ```

4. **Manual OTP Entry**:
   - The script navigates to the ICICI Direct login page and enters the username and password.
   - If an OTP is required, the script waits up to 3 minutes (`login_timeout`) for you to manually enter the OTP on the website.
   - Monitor the browser window to input the OTP when prompted.

5. **Output**:
   - **Downloaded Files**: CSVs for Trade Book, Portfolio Summary, Order Book, My Portfolio, and Orderbook are saved in account-specific subdirectories under `downloads` (e.g., `downloads/IN303028-76957800-6500081466-NRE/IN303028-76957800-6500081466-NRE_tradebook_1234567890.csv`).
   - **Order Book Table**: The Order Book data for each account is displayed in the terminal as a formatted table.
   - **Consolidated CSVs**: If `CONFIG['consolidate_output']` is `True`, consolidated CSVs for each data type are created in the `downloads` directory (e.g., `downloads/all_orders_1234567890.csv`).
   - **Log File**: All actions and errors are logged to `icici_extract.log` in the script directory.

## Configuration
The script includes a `CONFIG` dictionary with the following options:
- `download_base_dir`: Base directory to store downloaded CSVs (default: `downloads` in the script directory). Account-specific subdirectories are created under this.
- `tradebook_period`: Time period for Trade Book downloads (default: `1 Week`).
- `max_download_wait`: Maximum time to wait for downloads (default: 30 seconds).
- `consolidate_output`: Whether to combine CSVs for each data type into a single file in the base `downloads` directory (default: `True`).
- `login_timeout`: Maximum time to wait for login and OTP entry (default: 180 seconds).
- `switch_timeout`: Maximum time to wait for account switching (default: 60 seconds).

You can modify these settings in the `CONFIG` dictionary within the script to suit your needs.

## Sub-Accounts
The script processes the following sub-accounts (defined in `SUB_ACCOUNTS`):
- `IN303028-76957800-6500081466-NRE`
- `IN303028-76957818-7500062485-NRO`
- `IN303028-76957826-7510072528-NPNRO`

For the `NPNRO` account, the script additionally downloads My Portfolio and Orderbook CSVs.

To process different sub-accounts, update the `SUB_ACCOUNTS` list in the script with the appropriate account IDs.

## Notes
- **Manual OTP Handling**: The script relies on manual OTP entry on the ICICI Direct website. Ensure you are available to enter the OTP when prompted.
- **Browser Automation**: The script opens a Chrome browser window. Do not interact with the browser while the script is running, except to enter the OTP.
- **Error Handling**: The script includes retry logic (up to 3 attempts) for account switching, downloading Trade Book, Portfolio, My Portfolio, and Orderbook. If an error occurs, the script logs the error and continues with the next account.
- **File Naming**: Downloaded files include the account ID, data type, and a timestamp to avoid conflicts (e.g., `IN303028-76957800-6500081466-NRE_tradebook_1234567890.csv`).
- **Order Book Cleaning**: The Order Book CSV has its `Stock` column cleaned (removing "Single" and extra spaces) and saved as a separate file in the account’s subdirectory (e.g., `<account_id>_orders_cleaned.csv`).
- **Dependencies**: The `webdriver_manager` package automatically downloads the appropriate ChromeDriver version, so no manual ChromeDriver installation is required.
- **Logging**: Detailed logs are saved to `icici_extract.log`, including timestamps, function names, line numbers, and error stack traces.
- **Directory Structure**: Each account’s files are stored in a dedicated subdirectory under `downloads` for better organization.

## Troubleshooting
- **Login Fails**: Ensure your credentials in the `.env` file are correct. Check `icici_extract.log` for error details.
- **OTP Timeout**: If the script times out waiting for OTP entry, increase `CONFIG['login_timeout']`.
- **Download Issues**: Verify that the `downloads` directory and account subdirectories are writable. Check `CONFIG['max_download_wait']` if downloads take longer than expected.
- **Account Switching Fails**: Ensure the account IDs in `SUB_ACCOUNTS` match the dropdown options on the ICICI Direct website. Partial matching is supported, but exact matches are preferred.
- **Browser Issues**: Ensure Google Chrome is installed and up to date. Close any unnecessary Chrome instances before running the script.

## Example Output
When running the script, you might see output like this in the terminal:
```
Order Book for Account IN303028-76957800-6500081466-NRE:
+--------+----------------+--------+-------------------+
| Stock  | Order Type     | Status | Date              |
+--------+----------------+--------+-------------------+
| ABC    | Buy            | Active | 2025-05-27 10:00  |
| XYZ    | Sell           | Pending| 2025-05-27 11:00  |
+--------+----------------+--------+-------------------+
```

Downloaded files will be saved in account-specific subdirectories under `downloads`, and logs will be written to `icici_extract.log`.

## License
This script is provided as-is for personal use. Ensure compliance with ICICI Direct's terms of service when using this script for data scraping.