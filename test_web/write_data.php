<!DOCTYPE html>
<html>

<body>
    <?php

    $username = "root";
    $password = "";
    $dbname = "test";
    $host = "localhost";
    $tablename = "example2";

    // establish connection to the database
    $conn = new mysqli($host, $username, $password, $dbname);

    // requirements
    $id = $value = "";
    if (isset($_POST["id"]) && isset($_POST["value"])) {

        // if received a POST request
        $id = test_input($_POST["id"]);
        $value = test_input($_POST["value"]);

        // check if connection is established
        if ($conn->connect_error) {
            die("Connection to database failed: " . $conn->connect_error);
        }

        $sql = "INSERT INTO " . $tablename . " (id, value) VALUES ('" . $id . "', '" . $value . "')";

        if ($conn->query($sql) == TRUE) {
            echo "Record inserted successfully.";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }

    $conn->close();

    function test_input($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    ?>
</body>

</html>