<?php

function wordCount($str)
{
    $words = str_word_count(strtolower($str), 1);
    return array_count_values($words);
}

// Example string
$input = "Hello world! Hello PHP world.";

// Get word counts
$wordCounts = wordCount($input);

// Display word count on the webpage
echo "<h2>Word Count:</h2><ul>";
foreach ($wordCounts as $word => $count) {
    echo "<li>$word: $count</li>";
}
echo "</ul>";

