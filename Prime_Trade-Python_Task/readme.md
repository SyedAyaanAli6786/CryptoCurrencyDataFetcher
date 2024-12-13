# Cryptocurrency Data Fetching and Analysis

This project fetches real-time cryptocurrency data for the top 50 cryptocurrencies by market capitalization using the CoinGecko API, analyzes the data, and stores it in a live-updating Excel sheet. The project also provides insights such as the top 5 cryptocurrencies by market cap, the average price, and the highest and lowest 24-hour percentage price changes.

---

## **Features**
1. Fetches real-time cryptocurrency data using the CoinGecko API.
2. Analyzes the data to:
   - Identify the top 5 cryptocurrencies by market capitalization.
   - Calculate the average price of the top 50 cryptocurrencies.
   - Find the highest and lowest 24-hour percentage price changes.
3. Saves the data to an Excel file (`crypto_data.xlsx`) for easy access.
4. Updates the data every 5 minutes automatically.

---

## **Technologies Used**
- **Python**
- Libraries:
  - `requests` (for API requests)
  - `pandas` (for data analysis)
  - `openpyxl` (for Excel file handling)
  - `schedule` (for periodic updates)

---

## **Setup Instructions**

### **1. Prerequisites**
- Install Python (v3.7 or higher) from the [official Python website](https://www.python.org/downloads/).
- Install a code editor like [Visual Studio Code](https://code.visualstudio.com/).

### **2. Install Required Libraries**
Run the following commands in your terminal:
```bash
pip install requests pandas openpyxl schedule
```

### **3. Clone or Create the Project**
- Create a new folder for the project.
- Add the provided Python script (`crypto_task.py`) into this folder.

### **4. Run the Script**
- Open a terminal and navigate to the project folder:
  ```bash
  cd path/to/your/project/folder
  ```
- Run the script:
  ```bash
  python crypto_task.py
  ```

---

## **Usage**

### **Output File**
- The script generates an Excel file named `crypto_data.xlsx` that contains real-time data for the top 50 cryptocurrencies.

### **Insights Provided**
- Top 5 cryptocurrencies by market capitalization.
- Average price of the top 50 cryptocurrencies.
- Highest and lowest 24-hour percentage price changes.

### **Live Updates**
- The script fetches new data every 5 minutes and updates the Excel file.

---

## **Project Structure**
```
project-folder/
|
|-- crypto_task.py       # Main Python script
|-- crypto_data.xlsx     # Excel file with fetched data (auto-generated)
|-- README.md            # Documentation
```

---

## **Known Issues and Limitations**
1. **Rate Limits:**
   - CoinGecko’s free API tier allows up to 50 requests per minute. Ensure you don’t exceed this limit.

2. **Data Updates:**
   - The script fetches data every 5 minutes but is dependent on CoinGecko’s backend update frequency.

3. **Excel File:**
   - Ensure the Excel file (`crypto_data.xlsx`) is closed while the script is running to avoid conflicts.

---

## **Future Enhancements**
1. Add support for generating a PDF summary report.
2. Integrate with additional APIs for enhanced data accuracy.
3. Provide a GUI for easier user interaction.

---

## **Contact**
For any issues or feedback, feel free to reach out via [syed.23bcs10094@ms.sst.scaler.com].

