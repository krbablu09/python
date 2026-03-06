# Analyzing Customer Orders Using Python
# → Use basic Python to analyze order data (loops, functions, file handling)

def read_order(project_a):
    with open('project_a.txt', 'r') as f:
        return f.readlines()
    
def analyze_order(lines):
    total_sales =0
    product_count = {}
    customer_spending = {}

    for line in lines:
        order_id, customer, product, price = line.strip().split(",")
        price = int(price)

        total_sales += price

        product_count[product] = product_count.get(product, 0) + 1
        customer_spending[customer] = customer_spending.get(customer, 0) + price

        return total_sales, product_count, customer_spending
    
line = read_order("project_a")
total_sales, product_count, customer_spending = analyze_order(line)

print("Total Sales: ", total_sales) 
print("Most Sold Product: ", max(product_count, key = product_count.get))
print("Highest Spending Customer: ", max(customer_spending, key = customer_spending.get))   
      