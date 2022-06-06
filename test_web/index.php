<!DOCTYPE html>
<html>

<head>
    <title> Case Study Group 17
    </title>
</head>

<body>

    <h1> Case Study Group 17 Database </h1>
    <?php

    $username = "root";
    $password = "";
    $dbname = "test";
    $host = "localhost";
    $tablename = "example2";

    // Establish connection
    $conn = new mysqli($host, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection Error: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM " . $tablename . " ORDER BY timestamp DESC";

    echo '<table cellspacing="5" cellpadding="5">
    <tr>
    <th>timestamp</th>
    <th>id</th>
    <th>value</th>
    </tr>';

    if ($result = $conn->query($sql)) {
        while ($row = $result->fetch_assoc()) {
            $row_timestamp = $row["timestamp"];
            $row_id = $row["id"];
            $row_value = $row["value"];

            echo '<tr>
            <td>' . $row_timestamp . '</td>
            <td>' . $row_id . '</td>
            <td>' . $row_value . '</td>
            </tr>';
        }

        $result->free();
    }

    $conn->close();
    ?>

</body>

</html>