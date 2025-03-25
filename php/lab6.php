<?php

function rollaDice()
{
    $roll = rand(1, 6); // simulate rolling a 6-sided die
    return $roll < 4;
}

// Display result on the webpage
if (rollaDice()):
    echo "<h1>You have won</h1>";
else:
    echo "<h1>You have lost</h1>";
endif;