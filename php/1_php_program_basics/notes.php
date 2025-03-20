<?php
echo "Hello, world!\n";

/*
 * A statement is a command that instructs the computer to perform an action.
 * PHP is an interpreted programming language.
 * The name of the PHP interpreter is the PHP engine.
 * index.php serves as the default file a server opens automatically.
 */


/*
 * PHP has 2 ways to display content in the terminal:
 * print
 * echo
 * You can enclose the arguments in parentheses, if you want.
 */
print "Hello, again!\n";

/*
 * PHP comes built-in with a web server for web development projects.
 * You can see information about the server using phpinfo() function.
 * You can launch PHP's built in web server: php -S localhost:8000
 * ctrl-c terminates the web server.
 */

/*
 * Template Text vs. PHP Code:
 * Unchanging/Static parts of a page is called template text.
 * Other parts are dynamically generated through the execution of PHP.
 *
 * Any text outside the <?php ?> tags is template text.
 * If the script contains entirely of PHP, then ?> is not required.
 * ?> is only needed when there is additional template text.
 */

/*
 * Comments are useful for 3 reasons:
 * 1) They explain how some code works.
 * 2) They can be used to temporarily disable code.
 * 3) They are used for preprocessing tools like documentation generation.
 *
 * There are 3 ways to add comments in php:
 * //
 * #
 * /* *\/
 */

//This is a single-line comment.
#This is also a single-line comment.
/* This is a block comment. */

//variable names must begin with a $
$age = 23;
$name = "Justin Wearing";
print "\nMy age is " . $age . "\n";
print "My name is " . $name . "\n";

$timestamp = time();
print "The timestamp is " . $timestamp . "\n";

/*
 * PHP variable names are case-sensitive.
 * PHP constructs like if, for, switch, print, ...etc are case insensitive.
 */

/*
 * There are 2 ways to define constants in PHP:
 * 1)By using the define() function.
 * 2)By using the const construct.
 *
 * Note that constants don't start with a $ sign.
 * Some constants are built into the PHP language:
 *  M_PI
 *  M_E
 *  PHP_INT_MAX
 */
const PI = 3.14159265358979;
define("PI_2", 3.14159265358979);
print "\nThe value of PI is " . PI . "\n";
print "Another PI is " . PI_2 . "\n";

/*
 * Math Operators:
 * Operators are the constructs used to manipulate data.
 * Operands are the literals an operator works on.
 * + - * / % **
 */

/*
 * Assignment Operators:
 * += -= /= *= %= **=
 * ++ --
 */