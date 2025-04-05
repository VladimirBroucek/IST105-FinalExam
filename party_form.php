<?php
$items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service",
    "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
    "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
];

$output = "";

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['items'])) {
    $selected = $_POST['items'];
    $indices = implode(",", $selected);

    $command = escapeshellcmd("python3 /var/www/html/party_planner.py " . escapeshellarg($indices));
    $output = shell_exec($command);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Party Planner</title>
</head>
<body>
<h1>Select Party Items</h1>
<form method="POST">
    <?php foreach ($items as $index => $item): ?>
        <input type="checkbox" name="items[]" value="<?= $index ?>" id="item<?= $index ?>">
        <label for="item<?= $index ?>"><?= $item ?></label><br>
    <?php endforeach; ?>
    <br>
    <input type="submit" value="Plan the Party.">
</form>

<?php if (!empty($output)): ?>
    <hr>
    <h2>Result:</h2>
    <?= $output ?>
<?php endif; ?>
</body>
</html>