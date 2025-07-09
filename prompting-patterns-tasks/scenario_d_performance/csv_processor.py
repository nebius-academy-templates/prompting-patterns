#!/usr/bin/env python3
"""
CSV Data Processor - Deliberately Slow Implementation
=====================================================

This processes sales data from CSV files but is very slow.
Multiple performance issues make it unsuitable for large datasets.

Practice Challenge: Use the "Performance" prompt pattern to optimise this
"""

import csv
import time
from datetime import datetime

class SlowCSVProcessor:
    def __init__(self):
        self.data = []
        self.processed_data = []
        
    def load_csv(self, filename):
        """Load CSV file - inefficiently!"""
        print(f"Loading {filename}...")
        start_time = time.time()
        
        # PERFORMANCE ISSUE 1: Reading file line by line instead of using pandas
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # PERFORMANCE ISSUE 2: Processing each row individually
                processed_row = self.process_single_row(row)
                self.data.append(processed_row)
                
                # PERFORMANCE ISSUE 3: Unnecessary delay
                time.sleep(0.001)  # Simulates slow processing
        
        load_time = time.time() - start_time
        print(f"Loaded {len(self.data)} rows in {load_time:.2f} seconds")
        
    def process_single_row(self, row):
        """Process a single row - with unnecessary calculations"""
        # PERFORMANCE ISSUE 4: Repeated type conversions
        processed = {}
        processed['date'] = str(row['date'])
        processed['product'] = str(row['product'])
        processed['sales'] = float(row['sales'])
        processed['quantity'] = int(row['quantity'])
        
        # PERFORMANCE ISSUE 5: Unnecessary calculations for each row
        processed['sales_per_unit'] = processed['sales'] / processed['quantity']
        processed['processed_at'] = datetime.now().isoformat()
        
        return processed
    
    def calculate_totals(self):
        """Calculate totals - very inefficient!"""
        print("Calculating totals...")
        start_time = time.time()
        
        totals = {}
        
        # PERFORMANCE ISSUE 6: Multiple passes through the same data
        for row in self.data:
            product = row['product']
            
            # PERFORMANCE ISSUE 7: Inefficient dictionary operations
            if product not in totals:
                totals[product] = {
                    'total_sales': 0,
                    'total_quantity': 0,
                    'count': 0
                }
            
            totals[product]['total_sales'] += row['sales']
            totals[product]['total_quantity'] += row['quantity']
            totals[product]['count'] += 1
        
        # PERFORMANCE ISSUE 8: Another pass for averages
        for product in totals:
            totals[product]['avg_sales'] = totals[product]['total_sales'] / totals[product]['count']
            totals[product]['avg_quantity'] = totals[product]['total_quantity'] / totals[product]['count']
        
        calc_time = time.time() - start_time
        print(f"Calculated totals in {calc_time:.2f} seconds")
        
        return totals
    
    def find_top_products(self, n=5):
        """Find top products - slow sorting algorithm"""
        print(f"Finding top {n} products...")
        start_time = time.time()
        
        # PERFORMANCE ISSUE 9: Inefficient sorting with multiple passes
        product_sales = {}
        for row in self.data:
            product = row['product']
            if product not in product_sales:
                product_sales[product] = 0
            product_sales[product] += row['sales']
        
        # PERFORMANCE ISSUE 10: Bubble sort instead of built-in sort
        items = list(product_sales.items())
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j][1] < items[j + 1][1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        
        sort_time = time.time() - start_time
        print(f"Found top products in {sort_time:.2f} seconds")
        
        return items[:n]
    
    def generate_report(self):
        """Generate final report - with unnecessary file operations"""
        print("Generating report...")
        start_time = time.time()
        
        # PERFORMANCE ISSUE 11: Multiple file writes instead of batching
        with open('sales_report.txt', 'w') as f:
            f.write("Sales Report\n")
            f.write("=" * 50 + "\n\n")
        
        totals = self.calculate_totals()
        top_products = self.find_top_products()
        
        # PERFORMANCE ISSUE 12: Writing line by line
        for product, data in totals.items():
            with open('sales_report.txt', 'a') as f:
                f.write(f"Product: {product}\n")
                f.write(f"Total Sales: ${data['total_sales']:.2f}\n")
                f.write(f"Average Sales: ${data['avg_sales']:.2f}\n\n")
        
        with open('sales_report.txt', 'a') as f:
            f.write("Top Products:\n")
            for i, (product, sales) in enumerate(top_products, 1):
                f.write(f"{i}. {product}: ${sales:.2f}\n")
        
        report_time = time.time() - start_time
        print(f"Generated report in {report_time:.2f} seconds")

def create_test_csv(filename, num_rows=1000):
    """Create test CSV file with sample data"""
    products = ['Widget A', 'Widget B', 'Widget C', 'Gadget X', 'Gadget Y']
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'product', 'sales', 'quantity'])
        
        for i in range(num_rows):
            import random
            date = f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            product = random.choice(products)
            quantity = random.randint(1, 50)
            sales = quantity * random.uniform(10, 100)
            
            writer.writerow([date, product, f"{sales:.2f}", quantity])
    
    print(f"Created {filename} with {num_rows} rows")

def main():
    print("CSV Processor - Slow Version")
    print("=" * 40)
    
    # Create test data
    test_file = "sales_data.csv"
    create_test_csv(test_file, 2000)  # 2000 rows to show the slowness
    
    # Process the data (this will be slow!)
    processor = SlowCSVProcessor()
    
    overall_start = time.time()
    
    processor.load_csv(test_file)
    processor.generate_report()
    
    overall_time = time.time() - overall_start
    print(f"\nTotal processing time: {overall_time:.2f} seconds")
    print("Report saved to sales_report.txt")

if __name__ == "__main__":
    main() 