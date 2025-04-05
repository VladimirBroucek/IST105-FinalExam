<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['items'])) {
    $selected = $_POST['items'];
    $indices = implode(",", $selected);

    $command = escapeshellcmd("python3 party_planner.py " . escapeshellarg($indices));
    $output = shell_exec($command);

    echo $output;
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Party Planner Form</title>
</head>
<body>
<h1>Select Party Items</h1>
<form method="POST" action="">
    <?php
    $items = [
        "Cake", "Balloons", "Music System", "Lights", "Catering Service",
        "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
        "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
    ];

    foreach ($items as $index => $item) {
        echo "<input type='checkbox' name='items[]' value='$index' id='item$index'>";
        echo "<label for='item$index'>$item</label><br>";
    }
    ?>
    <br>
    <input type="submit" value="Plan the Party">
</form>
</body>
</html>