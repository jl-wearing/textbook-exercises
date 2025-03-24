<?php
$firstName = filter_input(INPUT_GET, 'first');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>process</title>
</head>

<body>
    Hello <?= $firstName ?>
</body>
</html>