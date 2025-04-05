import logging
import statistics
from typing import List, Dict

# Configure logging to capture debug and error messages.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("edi_analytics_dashboard.log"),
        logging.StreamHandler()
    ]
)

# Simulated EDI Transaction Data (this can be replaced with real data in production)
SIMULATED_EDI_DATA: List[Dict] = [
    {"transaction_id": "T1001", "order_value": 1500.00, "status": "Completed", "error": False},
    {"transaction_id": "T1002", "order_value": 2500.00, "status": "Completed", "error": False},
    {"transaction_id": "T1003", "order_value": 1200.00, "status": "Failed",    "error": True},
    {"transaction_id": "T1004", "order_value": 1800.00, "status": "Completed", "error": False},
    {"transaction_id": "T1005", "order_value": 2200.00, "status": "Failed",    "error": True},
]

def analyze_edi_data(edi_data: List[Dict]) -> Dict:
    """
    Analyzes EDI transaction data and computes key performance indicators (KPIs).

    Args:
        edi_data (List[Dict]): A list of dictionaries containing EDI transaction data.

    Returns:
        Dict: A dictionary containing the total transactions, total order value, average order value
              (for completed transactions), error rate, completed count, and error count.
    """
    total_transactions = len(edi_data)
    total_order_value = sum(item["order_value"] for item in edi_data)
    completed_orders = [item["order_value"] for item in edi_data if item["status"] == "Completed"]
    error_transactions = [item for item in edi_data if item["error"]]
    avg_order_value = statistics.mean(completed_orders) if completed_orders else 0
    error_rate = (len(error_transactions) / total_transactions * 100) if total_transactions else 0

    analysis = {
        "total_transactions": total_transactions,
        "total_order_value": total_order_value,
        "avg_order_value": avg_order_value,
        "error_rate": error_rate,
        "completed_count": len(completed_orders),
        "error_count": len(error_transactions)
    }
    
    logging.debug(f"Analysis Result: {analysis}")
    return analysis

def generate_report(analysis: Dict) -> str:
    """
    Generates a formatted report summarizing the EDI analytics.

    Args:
        analysis (Dict): A dictionary of computed KPIs.

    Returns:
        str: A formatted string report.
    """
    report_lines = [
        "EDI Analytics Report",
        "====================",
        f"Total Transactions: {analysis['total_transactions']}",
        f"Total Order Value: ${analysis['total_order_value']:,.2f}",
        f"Average Order Value (Completed): ${analysis['avg_order_value']:,.2f}",
        f"Error Rate: {analysis['error_rate']:.2f}%",
        f"Completed Transactions: {analysis['completed_count']}",
        f"Error Transactions: {analysis['error_count']}",
    ]
    report = "\n".join(report_lines)
    logging.info("Report generated successfully")
    return report

def main():
    """
    Main function to execute the EDI analytics process.
    """
    logging.info("Starting EDI Analytics Dashboard")
    try:
        analysis = analyze_edi_data(SIMULATED_EDI_DATA)
        report = generate_report(analysis)
        print(report)
    except Exception as e:
        logging.error(f"Unexpected error in main: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
