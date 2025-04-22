import PyPDF2
import re
import glob
import csv

directory_path = "C:\\Users\\habib\\OneDrive\\Downloads\\Flipkart Labels April 2025\\" 
pdf_files = glob.glob(directory_path + "/*.pdf")

# Create a CSV file to store the extracted information name csv as current date and time
import datetime

current_date_time = datetime.datetime.now()
current_date = current_date_time.strftime("%Y-%m-%d")
current_time = current_date_time.strftime("%H-%M-%S")
csv_file_name = current_date + "_" + current_time
csv_file_name = csv_file_name + ".csv"
csv_file_path =  csv_file_name
data_list = []

def extract_info(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    else:
        return None

def parse_info(text): 
    # Extract relevant details using regular expressions
    # sold_by = extract_info(r"Sold By:\s+([^,]+)", text)
    # address = extract_info(r"Address:\s+([^,]+)", text)
    # gstin = extract_info(r"GSTIN No:\s+([^,]+)", text)
    # tracking_id = extract_info(r"Tracking ID:\s+([^,]+)", text)
    # cod_amount = extract_info(r"COD Collect amount :\s+([^,]+)", text)
    order_id = extract_info(r"(OD[0-9]{18})", text) 
    # order_date = extract_info(r"Order Date:\s+([^,]+)", text)
    invoice_no = extract_info(r"Invoice No:\s+([^,]+)", text)
    invoice_date = extract_info(r"Invoice Date:\s+([^,]+)", text)
    # delivery_name = extract_info(r"DELIVERY ADDRESS:\s+([^,]+)", text)
    # delivery_address = extract_info(r"DELIVERY ADDRESS:\s+[^,]+,([^,]+)", text)
    # courier_name = extract_info(r"Courier Name:\s+([^,]+)", text)
    courier_awb_no = extract_info(r"Courier AWB No:\s+([^,]+)", text)
    # billing_name = extract_info(r"Billing Address\s+([^,]+)", text)
    # billing_address = extract_info(r"Billing Address\s+[^,]+,([^,]+)", text)
    # shipping_name = extract_info(r"Shipping ADDRESS\s+([^,]+)", text)
    # shipping_address = extract_info(r"Shipping ADDRESS\s+[^,]+,([^,]+)", text)
    # seller_registered_address = extract_info(r"Seller Registered Address:\s+([^\.]+)", text)
    # product_description = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n(.+)\n", text)
    # product_qty = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+[\n\|]+(\d+)", text)
    # product_gross_amount = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n(\d+\.\d+)", text)
    # product_discount = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n\d+\.\d+\n(\d+\.\d+)", text)
    # product_taxable_value = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n\d+\.\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    # product_cgst = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    # product_sgst = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    # product_total = extract_info(r"Product\nDescription\nQty\n[^|]+\n\w+\n.+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    # shipping_handling_qty = extract_info(r"Shipping and Handling\nCharges\n(\d+)", text)
    # shipping_handling_price = extract_info(r"Shipping and Handling\nCharges\n\d+\n(\d+\.\d+)", text)
    # shipping_handling_cgst = extract_info(r"Shipping and Handling\nCharges\n\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    # shipping_handling_sgst = extract_info(r"Shipping and Handling\nCharges\n\d+\n\d+\.\d+\n\d+\.\d+\n(\d+\.\d+)", text)
    total_qty = extract_info(r"TOTAL QTY:\s+(\d+)", text)
    total_price = extract_info(r"TOTAL PRICE:\s+(\d+\.\d+)", text)
    awb_no = extract_info(r"AWB No\.?\s*([A-Z0-9]+)", text)
    sku = extract_info(r"SKU ID\s*\|\s*Description.*?\n(?:.*\n){2}([^\s|]+)\s*\|", text)

    # Create a dictionary to store the extracted information
    data = {
        # "Sold By": sold_by,
        # "Address": address,
        # "GSTIN No": gstin,
        # "Tracking ID": tracking_id,
        # "COD Collect amount": cod_amount,
        "Order ID": order_id,
        # "Order Date": order_date,
        "Invoice No": invoice_no,
        "Invoice Date": invoice_date,
        # "Delivery Name": delivery_name,
        # "Delivery Address": delivery_address,
        # "Courier Name": courier_name,
        "Courier AWB No": courier_awb_no if courier_awb_no else awb_no,
        # "Billing Name": billing_name,
        # "Billing Address": billing_address,
        # "Shipping Name": shipping_name,
        # "Shipping Address": shipping_address,
        # "Seller Registered Address": seller_registered_address,
        # "Product Description": product_description,
        # "Product Qty": product_qty,
        # "Product Gross Amount": product_gross_amount,
        # "Product Discount": product_discount,
        # "Product Taxable Value": product_taxable_value,
        # "Product CGST": product_cgst,
        # "Product SGST": product_sgst,
        # "Product Total": product_total,
        # "Shipping and Handling Qty": shipping_handling_qty,
        # "Shipping and Handling Price": shipping_handling_price,
        # "Shipping and Handling CGST": shipping_handling_cgst,
        # "Shipping and Handling SGST": shipping_handling_sgst,
        "Total Qty": total_qty,
        "Total Price": total_price,
        "SKU": sku
    }

    parsed_data = {
        "Invoice No": data['Invoice No'].split('\n')[0],
        "Order ID": data['Order ID'].split('\n')[0].strip(),
        "SKU": data['SKU'],
        "Total Price": data['Total Price'],
        "Invoice Date": data["Invoice Date"],
        "Total Qty": data["Total Qty"],
        "Courier AWB No": data['Courier AWB No'].split('\n')[0]
    }
    return parsed_data

def extract_details_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        try:
            all_data =[]
            pdf_reader = PyPDF2.PdfReader(file)
            for pages in pdf_reader.pages:
                data = pages.extract_text()
                
                all_data.append(parse_info(data))
            return all_data  # <--- Add this line
        except PyPDF2.errors.PdfReadError as e:
            print("Error: PDF file could not be read:", str(e))
            return []


# Iterate over your PDF files and extract details
for file in pdf_files:
    extracted_data = extract_details_from_pdf(file)
    if extracted_data:
        data_list.extend(extracted_data)

# Define the field names for the CSV file
field_names = ["Invoice No","Order ID","SKU","Total Price","Invoice Date","Total Qty","Courier AWB No"]


# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writerows(data_list)

print("Details saved to", csv_file_path)