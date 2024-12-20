# Malicious-Object-Dissemination-Assessment-Tool
## **Endpoints Dashboard**

This project is a simple PHP dashboard that interacts with a MySQL database to display the percentage and count of matching and non-matching hashes. It allows users to visualize the data through a pie chart and provides a button to delete all records from the `endpoints` table.

## **Features**
- Displays matching and non-matching hash percentages and device counts.
- Interactive pie chart using Chart.js.
- Option to delete all endpoint data from the database.
- Secure form handling with confirmation for deletion.

## **Technologies Used**
- PHP
- MySQL
- Chart.js (for the pie chart visualization)
- HTML & CSS (for the frontend)

## **Prerequisites**
Before you start, ensure you have the following software installed:
- **PHP** (>=7.4)
- **MySQL** (or MariaDB)
- **Apache** or **Nginx** (for serving PHP files)
- **Chart.js** (CDN included in the project)
###  **Set up the database**
   - Import the provided SQL file (`schema.sql`) into your MySQL database to create the `endpoints` table.
   - Update the `config.php` file with your database credentials.

###  **Run the application**
   - Place the project files in your web server’s root directory.
   - Access the dashboard in your browser.

### Contributors
   - [ahmaddahb36](https://github.com/ahmaddahb36)
   - [Ayahmdi](https://github.com/Ayahmdi)
   - [Palehab](https://github.com/Palehab)


## **Installation and Setup**

### 1. **Clone the repository**
```bash
git clone https://github.com/your-username/endpoints-dashboard.git
cd endpoints-dashboard```


