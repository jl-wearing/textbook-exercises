<?php
#if statements execute if a condition is true.
#if (condition) statementToPerform;
$hourNumber = 10;
if ($hourNumber < 12) print 'Good Morning!' . "\n";

#statement group
unset($hourNumber);
$hourNumber = 10;
if ($hourNumber < 12) {
    print 'Good';
    print ' Morning!' . "\n";
}

#if-else statements.
$hourNumber = 14;
if ($hourNumber < 12) print 'Good Morning!' . "\n";
else print 'Good Afternoon!' . "\n";

#nested if-else statements.
unset($hourNumber);
$hourNumber = 18;
if ($hourNumber < 12) {
    print 'Good Morning!' . "\n";
}
else {
    if ($hourNumber < 17) {
        print 'Good Afternoon!' . "\n";
    }
    else {
        print 'Good Evening!' . "\n";
    }
}

#if-elseif-else statements.
unset($hourNumber);
$hourNumber = 10;
if ($hourNumber < 12) {
    print 'Good Morning!' . "\n";
}
elseif ($hourNumber < 17) {
    print 'Good Afternoon!' . "\n";
}
else {
    print 'Good Evening!' . "\n";
}

/*
 * alternative syntax:
 * PHP offers an alternative that uses colons rather than curly brackets.
 * The alternative syntax is useful for web applications, where HTML
 * template text could appear between the if and else statements.
 */
unset($hourNumber);
$hourNumber = 14;
if ($hourNumber < 12):
    print 'Good Morning!' . "\n";
elseif ($hourNumber < 17):
    print 'Good Afternoon!' . "\n";
else:
    print 'Good Evening!' . "\n";
endif;
print "\n";

/*
 * Logical Operators:
 * NOT -> !
 * AND -> and, &&
 * OR -> or, ||
 * XOR -> XOR
 */
$age = 15;
if (!($age >= 18)):
    print 'Sorry, you are too young to drive!' . "\n";
endif;
var_dump(is_bool(!$age));

$passedTheoryTest = true;
$monthsHeldLearnersLicense = 10;
$heldLearnersLicenseLongEnough = ($monthsHeldLearnersLicense >= 6);
if ($passedTheoryTest and $heldLearnersLicenseLongEnough) {
    print "You may apply for a driving test.\n";
}
else {
    print "Sorry, you don't meet all conditions to take a driver's test.\n";
}

$password = '1234';
$passwordContainsPassword = str_contains($password, 'password');
$passwordTooShort = (strlen($password) < 6);
if ($passwordTooShort or $passwordContainsPassword) {
    print "Your password does not meet minimal security requirements.\n";
}

$containsIceCream = true;
$containsCustard = false;
if ($containsIceCream xor $containsCustard) {
    print 'a nice creamy dessert' . "\n";
}
else {
    print 'either too creamy or not enough cream!' . "\n";
}
print "\n";

#switch statements
$day = 'Monday';
switch ($day) {
    case 'Monday':
        print "Today is Monday.\n";
        print "FFS!\n";
        break;
    case 'Tuesday':
        print "Today is Tuesday.\n";
        break;
    case 'Wednesday':
        print "Today is Wednesday.\n";
        break;
    case 'Thursday':
        print "Today is Thursday.\n";
        break;
    case 'Friday':
        print "Today is Friday.\n";
        print "Yaay, we made it!\n";
        break;
    case 'Saturday':
        print "Saturday is rest day.\n";
        break;
    case 'Sunday':
        print "Rest on Sunday and prepare for Monday.\n";
        break;
    default:
        print "$day not recognized.\n";
}

$country = 'Spain';
switch ($country) {
    case 'UK':
        print "The pound is the currency of $country.\n";
        break;
    case 'Ireland':
    case 'France':
    case 'Spain':
        print "The euro is the currency of $country.\n";
        break;
    case 'USA':
        print "The dollar is the currency of $country.\n";
        break;
    default:
        print "$country not recongized.\n";
}

/*
 * a match statement chooses a value for a variable based on the value
 * of another variable.
 */
unset($country);
$country = 'Ireland';
$currency = match ($country) {
    'UK' => 'pound',        #this expression is called an arm
    'Ireland' => 'euro',
    'France' => 'euro',
    'Spain' => 'euro',
    'USA' => 'dollar',
    default => 'country not recognized.'
};
print "The currency of $country is the $currency.\n";


/*
 * ternary operator:
 * booleanExpression ? valueIfTrue : valueIfFalse;
 */
$region = 'USA';
$currency = ($region === 'Europe' ? 'euro' : 'dollar');
print "The currency of $region is the $currency.\n";

/*
 * null-coalescing operator (??):
 * $variable = value ?? valueIfNull;
 */
$lastName = $lastNameFromUser ?? 'Anonymous';
print "Hello, Mr. $lastName\n";

$lastNameFromUser = 'Smith';
$lastName = $lastNameFromUser ?? 'Anonymous';
print "Hello, Mr. $lastName\n";