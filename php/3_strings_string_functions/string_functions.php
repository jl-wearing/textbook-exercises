<?php

/*
 * Converting uppercase and lowercase:
 * strtolower() AND strtoupper() functions
 * ucfirst() capitalizes the first letter of a string
 * lcfirst() lowercases the first letter of a string
 * ucwords() capitalizes the first letter of every word in a string.
 */
$myString = 'the CAT sat on the Mat';
print strtolower($myString) . "\n";
print strtoupper($myString) . "\n";
$badGrammar = 'some people don\'t type with capital letters.';
print ucfirst($badGrammar) . "\n";
$upperCase = strtoupper($myString);
print $upperCase . " $myString\n";
$worseGrammar = 'SOME PEOPLE TYPE WITH ALL CAPS';
PRINT lcfirst($worseGrammar) . "\n";
$mixedCaps = 'some peoPLE use CAPS spoRADically';
print ucwords(strtolower($mixedCaps)) . "\n\n";

/*
 * Analytical string functions:
 * strlen() returns the length of a string.
 * substr_count(haystack, needle) counts the number of times a substring appears within a string.
 * strpos() returns the starting position of the first occurrence
 *  of a substring within a string.
 * You can provide an offset to the strpos() function that tells it to start
 * searching for the substring from a different position.
 * if strpos() doesn't find any occurrences, it returns false.
 */
unset($myString);
$myString = 'cat scat';
print strlen($myString) . "\n";
print substr_count($myString, 'cat') . "\n";
print substr_count($myString, 'a') . "\n";
print strpos($myString, 'cat') . "\n";
$sol =  strpos($myString, 'S') . "\n";
print gettype($sol);
print "\n";
var_dump(is_string($sol));
print strlen($sol) . "\n";
unset($myString);
$myString = 'cat scat';
print strpos($myString, 'cat', 2) . "\n";
$found = strpos($myString, 'z');
var_dump($found);
print "\n";

/*
 * count_chars() analyzes which characters are, and are not, included in a string.
 * mainly used to evaluate the complexity of passwords, and data encryption.
 * count_chars() has a few modes:
 *
 * mode 3 returns a string of the unique characters used on a string.
 */
unset($myString);
$myString = 'cat scat';
print count_chars($myString, 3) . "\n\n";

/*
 * Other PHP functions manipulate strings by extracting a portion of the string
 * or replacing a portion with something else.
 *
 * substr() extracts part of a string.
 * If you supply a negative number, substr() extracts from the end of the string.
 * for example, -2 retrieves the last 2 characters.
 * a second argument specifies the number of characters to extract.
 */
$warning = 'do not enter';
print substr($warning, 7);
print "\n" . substr($warning, -2) . "\n";
print substr($warning, 7, 3) . "\n";

/*
 * strstr() extracts a substring using a character(s) that is part
 * of the string. It searches for the first occurrence of a substring
 * within a string, and extracts the contents of the string from that substring
 * on.
 *
 * We can also retrieve everything before the first occurrence by passing a
 * true argument to the strstr() function.
 * stristr() is the case insensitive version of strstr()
 */
$email = 'the.cat@aol.com';
print strstr($email, '@') . "\n";
print strstr($email, '@', true) . "\n";

/*
 * str_replace() finds all occurrence of a substring and replaces them
 * with a different string.
 */
$foodchain = 'dogs eat cats, cats eat mice, mice eat cheese';
print str_replace('eat', 'help', $foodchain) . "\n";
print $foodchain . "\n";
print str_replace('eat', 'poo', $foodchain) . "\n\n";

/*
 * substr_replace() lets you specify the position in the string at which
 * the replacement should occur.
 * By setting the replacement length to 0, we can use the function to
 * insert a substring into a string without altering it.
 */
print substr_replace($foodchain, 'help', 5, 3) . "\n";
print substr_replace($foodchain, 'don\'t ', 5, 0) . "\n\n";

/*
 * Trimming functions:
 * trim()
 * ltrim()
 * rtrim()
 *
 * You can optionally control which whitespace characters are trimmed by
 * specifying them in a double-quoted string.
 *
 * To remove whitespace from throughout a string, not just the edges,
 * use the str_replace() function to find all instances of a particular
 * whitespace character and replace them with empty strings.
 */
$tooSpacey = "     \n\nCAT\nDOG\t\n";
print trim($tooSpacey) . "\n";
$tooSpacey = "\n\n     CAT\nDOG\n\n";
print ltrim($tooSpacey, "\n");
$tooTabby = "\tCat \tDog \t\tMouse";
print $tooTabby . "\n";
print str_replace("\t", '', $tooTabby) . "\n\n";

/*
 * To repeat a string a given number of times, use str_repeat()
 */
$lonely = "cat";
print str_repeat($lonely, 5) . "\n";

/*
 * Padding repeatedly adds to the beginning or end of a string until the
 * string reaches a desired length.
 * padding is used to display numbers of different lengths such that their
 * digits line up.
 * str_pad() is used for padding tasks
 *
 * By default, PHP adds padding to the right of the string.
 * constants STR_PAD_LEFT or STR_PAD_BOTH arguments can be supplied to
 * the str_pad() function.
 */
$tooShort = 'cat';
print str_pad($tooShort, 20, '-') . "\n";
print str_pad($tooShort, 20, '-', STR_PAD_LEFT) . "\n";
print str_pad($tooShort, 20, '-', STR_PAD_BOTH) . "\n";
