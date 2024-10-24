<?php
// Database connection details
$servername = "localhost";
$username = "root";
$password = "123456";
$database = "endpoints";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to count the number of rows where "hash" is "match"
$sql = "SELECT COUNT(*) AS match_count FROM endpoints WHERE hash = 'match'";
$result = $conn->query($sql);

// Get the number of matching rows
$match_count = $result->fetch_assoc()["match_count"];

// SQL query to count the number of rows where "hash" is not "match"
$sql = "SELECT COUNT(*) AS not_match_count FROM endpoints WHERE hash <> 'match'";
$result = $conn->query($sql);

// Get the number of non-matching rows
$not_match_count = $result->fetch_assoc()["not_match_count"];

// Calculate the total number of rows
$total_count = $match_count + $not_match_count;

// Calculate the percentages
$match_percentage = round(($match_count / $total_count) * 100, 2);
$not_match_percentage = round(($not_match_count / $total_count) * 100, 2);

// Check if the delete button was clicked
if (isset($_POST['delete'])) {
    // SQL query to delete all rows from the endpoints table
    $sql = "TRUNCATE TABLE endpoints";

    if ($conn->query($sql) === TRUE) {
//        echo "Endpoints deleted successfully";
    } else {
        echo "Error deleting endpoints: " . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Endpoints Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
.button_style{
font:20px cursive ;

 color :#20639B;
 position: absolute;
  top: 70%;
  right: 730px;
  transform: translateY(20%);
 transform: translateX(20%);
}



</style>
</head>

<body >
   
    <div class="dashboard-item">
        <h2>Matching Hashes</h2>
        <p><?php echo $match_percentage . '%' . "&nbsp;&nbsp;&nbsp;"; ?>
        <?php echo $match_count . ' devices'; ?></p>
    </div>
    <div class="dashboard-item">
        <h2>Non-Matching Hashes</h2>
        <p><?php echo $not_match_percentage . '%' . "&nbsp;&nbsp;&nbsp;"; ?>
        <?php echo $not_match_count . ' devices'; ?></p>
    </div>
    <div class="chart-container">
        <canvas id="myPieChart"></canvas>
    </div>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <input class="button_style" type="submit" name="delete" value="Delete Endpoints" >
    </form>

    <script>
        // Get the canvas element
        var ctx = document.getElementById('myPieChart').getContext('2d');

        // Prepare the data
        var data = {
            labels: ['Non-Matching Hashes', 'Matching Hashes'],
            datasets: [{
                data: [<?php echo $not_match_percentage; ?>, <?php echo $match_percentage; ?>],
                backgroundColor: ['#20639B', '#C73341']
                 
            }]
        };

        // Create the pie chart
        var myPieChart = new Chart(ctx, {
            type: 'pie',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    </script>
</body>
</html>
