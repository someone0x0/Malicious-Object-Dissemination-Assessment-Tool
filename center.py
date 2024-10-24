
import requests
import mysql.connector
import os
import json
from urllib.parse import urlparse

# Function to send data to the endpoint and write response to MySQL database
def send_data_to_endpoint_and_write_to_db(url, data):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Request to {url} successful!")
        response_data = response.json()
        # Extract IP address from the URL
        ip_address = extract_ip_from_url(url)
        
        # Write response data to MySQL database
        write_response_to_database(response_data, ip_address)
    else:
        print(f"Error: {response.status_code} for URL {url}")

# Function to extract IP address from URL
def extract_ip_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname

# Function to write response data to MySQL database
def write_response_to_database(response_data, ip_address):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="endpoints"
    )
    cursor = conn.cursor()

    # Define SQL query to insert response data into the table
    sql = "INSERT INTO endpoints (ip_address,hash, dll,hex,string) VALUES (%s, %s, %s, %s, %s)"
    values = (
        ip_address,
        response_data.get('HashResult', 'null'),
        response_data.get('DLLResult', 'null'),
        response_data.get('HexResult' , 'null'),
        response_data.get('StringResult' , 'null')
    )
    print(sql)
    # Execute SQL query
    cursor.execute(sql, values)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Response data written to MySQL database.")

def start_dll_detect():
    global start_arg
    DLL_choice=input("you are want enter dll name or dll path (N/P)??")
    if DLL_choice=="p" or DLL_choice=="P":
        fpath = input("Enter DLL PATH to search for:---> ").replace('\\', '\\\\')
        dll_name = os.path.basename(fpath)
    if DLL_choice =="n" or DLL_choice=="N":
        fpath=''
        dll_name=input("Enter DLL NAME to search for such as 'USER32.dll':--->")  
#    
    search_directory = input("Enter the directory path to search in:---> ").replace('\\', '\\\\')
    start_arg = {"fpath":fpath,"dll_name":dll_name,"search_directory":search_directory,"DLL_choice":DLL_choice}  

def start_hex_detect():
    global hex_arg
    hex_sequence = input("Enter the hex sequence to search for (e.g., 4D 5A 90 00) and if you not know hex digit can you represent it by '?' :\n ")
    hex_search_directory = input("Enter the directory path to search in: ").replace('\\', '\\\\')
    hex_arg = {"hex_sequence": hex_sequence, "hex_search_directory": hex_search_directory}

def hash_input_user():
    global hash_arg
    global hash_Directory
    global hash_value
    hash_Directory=input("Enter directory path to scan it : ")  
    hash_to_lower=input("Now enter the hash value : ")
    hash_value = hash_to_lower.lower()
    hash_arg = {"hash_Directory": hash_Directory, "hash_value": hash_value}     

def string_input_user():
    global string_arg
    global string_Directory
    global suspicious_string
    string_Directory=input("Enter directory path to scan it : ")  
    suspicious_string=input("Now enter the String value : ") 
    string_arg = {"string_Directory": string_Directory, "suspicious_string": suspicious_string}  

def main():
    global start_arg
    global string_arg
    global hex_arg
    global hash_arg
    dll_input = input("do you want to send dll (y/n)? ")
    if dll_input == 'y':
        start_dll_detect()
    else:
        start_arg = {"fpath": 'test', "dll_name": 'test', "search_directory": 'test','DLL_choice':'test'}
    ###########    
    hex_ = input ("do you want to send HEX (y/n)? ")

    if hex_ == 'y' :
        start_hex_detect()
    else:
        hex_arg = {"hex_sequence": 'test', "hex_search_directory": 'test'} 
    ###########
    hash_ = input ("do you want to send hash (y/n)? ")     
    if hash_ == 'y' :
        hash_input_user()
    else:
        hash_arg = {"hash_Directory": 'test', "hash_value": 'test'}  
    ###########
    string_ =input ("do you want to send string (y/n)? ")    
    if string_ == 'y' :
        string_input_user() 
    else:
        string_arg = {"string_Directory": 'test', "suspicious_string": 'test'}           
    endpoint_urls = [
        "http://192.168.1.65:5001/process" # Make sure to change the IP address #
    
    ]
    #hash_arg = {"hash_Directory": hash_Directory, "Suspicious_hash_value": Suspicious_hash_value}
    #string_arg = {"string_Directory": string_Directory, "suspicious_string": suspicious_string}  
    data = {
        "hash_value":hash_arg["hash_value"],
        "hash_Directory":hash_arg["hash_Directory"],
        "dll_name": start_arg["dll_name"], 
        "f_path": start_arg["fpath"],
        "search_directory": start_arg["search_directory"],
        "DLL_choice": start_arg["DLL_choice"],
        "hex_sequence": hex_arg["hex_sequence"],
        "hex_search_directory": hex_arg["hex_search_directory"],
        "string_Directory": string_arg["string_Directory"],
        "suspicious_string": string_arg["suspicious_string"]

        
        
    }

    for url in endpoint_urls:
        send_data_to_endpoint_and_write_to_db(url, data)

if __name__ == "__main__":
    main()
