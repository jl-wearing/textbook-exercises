<?php
/*
 * PHP has 10 data types, grouped into 3 categories:
 * Scalar Types:
 *  string, int, float, bool
 *
 * Special Types:
 *  NULL, resource
 *
 * Compound Types:
 *  array, object, callable, iterable
 */

/*
 * You can run interactive mode like this: php -a
 */

/*
 * gettype() function returns the type of a variable.
 *
 * PHP is a loosely-typed language, meaning that the same variable can
 * store values of different data types at different times.
 * The PHP engine will automatically infer the data type from the
 * type of input.
 *
 * We can also explicitly declare data types.
 */
$username = "matt";
$age = 23;
$price = 9.99;
print gettype($username) . "\n";
print gettype($age) . "\n";
print gettype($price) . "\n\n";

$isDutyFree = true;
print gettype($isDutyFree) . "\n";
print $isDutyFree . "\n";
/*
 * Notice that when we print the value of $isDutyFree, we see 1 instead
 * of true. This is because the print construct expects a string as its
 * argument, so it converts the bool true to string "1".
 * false is converted to the empty string "".
 *
 * To see the actual value, use the var_dump() function.
 * It is used to output information about a variable.
 */
var_dump($isDutyFree);
var_dump($age);
var_dump($username);
print "\n\n";

/*
 * The NULL Type:
 *
 * Case-insensitive (null or NULL)
 * A variable is null in 3 situations:
 * 1)If it was never assigned a value.
 * 2)If you assign it to null.
 * 3)If you clear (unset) a variable of its value using the unset() function.
 * NULL type is important to deal with when working with databases and users logging in.
 */
$lastName = NULL;
var_dump($lastName);
unset($lastName);
#var_dump($lastName);
print "\n\n";

/*
 * PHP has functions that return true of false based on whether
 * the argument provided is of a certain data type:
 * is_int(), is_string(), is_float(), is_bool(), is_null()
 */
$gpa = 3.5;
var_dump(is_string($gpa));
var_dump(is_int($gpa));
var_dump(is_float($gpa));
var_dump(is_bool($gpa));
print "\n";

/*
 * Some functions are used to check for a broader category of data types.
 * is_numeric() is true for variables of type int or float.
 * is_numeric() is also true for strings that contain only numeric characters.
 *
 * is_string()
 * is_scalar()
 */
$age = 23;
$price = "9.99";
var_dump(is_numeric($gpa));
var_dump(is_numeric($age));
var_dump(is_numeric($price));
var_dump(is_scalar($gpa));
print "\n";

/*
 * In some situations, the PHP engine automatically converts a value from one
 * data type to another. This is called type juggling.
 * There are 6 situations in which the PHP engine automatically juggles expressions
 * into different types:
 * 1)numeric contexts
 * 2)string contexts
 * 3)comparative contexts
 * 4)logic contexts
 * 5)function contexts
 * 6)bitwise contexts
 */
$answer = "1" + 3;
var_dump($answer);
print $answer . "\n";

/*
 * When an expression includes arithmetic operators, PHP will try to juggle the operands into integers and floats.
 * bool true is also juggled into 1.
*/
$answer = 2 + true;
var_dump($answer);
print $answer . "\n\n";

/*
 * PHP differentiates between numeric strings, whose entire contents are numeric,
 * leading numeric strings, which begin with numeric characters but also contain non-numeric characters.
 * When a leading numeric string is juggled, the non-numeric characters are dropped.
 * If a string starts with a non-numeric character, the whole string is considered non-numeric.
 */
$answer = "4" + 4;
print $answer . "\n";
$answer = 4 + "1 dollar";
var_dump(is_numeric($answer));
print "\n\n";

//. is the string concatenation operator.
$answer = 4 . "4";
print $answer . "\n";

//Type juggling also occurs when comparing two values of different data types.
/*
 * Identical vs. Equal Values:
 * 2 expressions are identical if they are of the same data type and contain the same value.
 * 2 expressions are equal if they contain the same value after type juggling.
 * === ==! (identical operator) tests for identity.
 * == =! <> (equal operator) tests for equality.
 */
var_dump("1" === 1);
var_dump("1" == 1);
var_dump(1 <> 1.0);
print "\n";

var_dump(1 != "1 dollar");      //1 is juggled to "1"

/*
 * Logical Operators:
 * < <= > >=
 * && || ?
 */
var_dump(true > false);
var_dump(true > NULL);
var_dump(false == NULL);
print "\n";

/*
 * The spaceship operator <=> returns either -1, 0, 1 depending on the expressions being compared.
 * If both expressions are the same, it returns 0.
 * If the first expression is greater than the second, it returns 1.
 * Otherwise, it returns -1.
 */
var_dump(11 <=> 22);
var_dump(55 <=> 22);
var_dump("22" <=> 22);
print "\n";

/*
 * Type Casting
 */
$age = (int)20.5;
print $age . "\n";
$age = (int)9.99;
print "$age\n";
print "$age\n";