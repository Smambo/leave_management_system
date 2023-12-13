<?php
$servername = "localhost";
$username = "smambo";
$password = "Bokang_13";
$database = "leave_mngt_db";

$mysqli = new mysqli("localhost", $username, $password, $database);

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $employee_name = $_POST['employee_name'];
    $leave_type = $_POST['leave_type'];
    $start_date = $_POST['start_date'];
    $end_date = $_POST['end_date'];
    $reason = $_POST['reason'];

    // Prepare and execute SQL query to insert data into the database
    $sql = "INSERT INTO leave_requests (employee_name, leave_type, start_date, end_date, reason)
    VALUES ('$employee_name', '$leave_type', '$start_date', '$end_date', '$reason')";

    if ($mysqli->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $mysqli->error;
    }
}

$sql = "SELECT * FROM leave_requests";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
    // Output data of each row
    while ($row = $result->fetch_assoc()) {
        echo "Employee Name: " . $row["employee_name"] . "<br>";
        echo "Leave Type: " . $row["leave_type"] . "<br>";
        echo "Start Date: " . $row["start_date"] . "<br>";
        echo "End Date: " . $row["end_date"] . "<br>";
        echo "Reason: " . $row["reason"] . "<br><br>";
    }
} else {
    echo "0 results";
}

$mysqli->close();
?>