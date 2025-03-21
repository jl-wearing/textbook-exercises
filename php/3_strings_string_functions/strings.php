<?php
/*
 * Almost all PHP programs involve text, thus it is important to understand how
 * to create & work with strings.
 */

/*
 * There are 4 ways to construct strings in PHP:
 * 1)single-quotation marks
 * 2)double-quotation marks
 * 3)heredocs
 * 4)nowdocs
 */

/*
 * Whitespace consists of characters you can't see, i.e. -> characters that won't
 * use any ink when printing.
 */

//everything enclosed in single-quotes is treated literally.
$age = 23;
print 'hello, I am $age\n
';
print 'matt smith\'s string

';
unset($age);

//concatenation operator: (.)
$name = 'Matt Smith';
print 'my name is ' . $name . "\n";
print 'my name is '
    . $name
    . ', I\'m pleased to meet you!'
    . PHP_EOL;

//If a variable contains a string, we can use the concatenating assignment
//operator (.=) to append another string to the end of that variable.
$name = 'Justin';
$name .= ' Wearing';
print 'my name is ' . $name . "\n";
unset($name);
print "\n";

/*
 * Double-quoted strings allow variables to be processed by their values.
 * They also allow escape sequences to be embedded into string literals.
 * You can't include constants, since the PHP engine can't tell the difference
 * between characters that are part of the string and the name of the constant.
 */
$name = 'Matt Smith';
print "My name is $name\nI'm pleased to meet you. \n";

/*
 * Punctuation marks following variables are ok because they are not
 * valid characters to include in variable names.
 * escape sequences are valid too.
 *
 * However, if you want other characters to immediately follow a variable,
 * you have to enclose the variable in curly braces.
 */
print "My name is $name. I'm pleased to meet you.\n";
$weight = 80.00;
print "My weight is {$weight}kg.\n\n";

/*
 * To use a Unicode character, start with \u then provide the
 * character's hexadecimal code in curly braces.
 */
$smiley = "\u{1F60A}";
$elephant = "\u{1F418}";
$cherokeeTSV = "\u{13E8}";
$coding = "👨‍💻";
print "this is a smiley unicode character: $smiley\n";
print "followed by some elephants of course: $elephant\n";
print "cherokee letter TSV: $cherokeeTSV\n";
print "an actual emoji as a variable: $coding\n\n";

/*
 * Heredocs are an alternative to double-quoted strings.
 * They are just like double-quoted strings int that they are parsed,
 * but they are typically used to span multiple lines.
 * Heredoc operator: (<<<), followed by a sequence of characters that
 * will serve as your delimiter.
 *
 * It makes code more readable to choose a meaningful delimiter that
 * matches the heredoc's content, like EOT, SQL, or HTML.
 * You can include \n and \t in heredocs.
 */
$age = 22;
$weight = 70.00;
$message = <<<EOT
my age is $age
my weight is {$weight}kg

EOT;
print $message;

$message = <<<UNICODE
this is a smiley unicode character: $smiley
followed by some elephants of course: $elephant $elephant $elephant
Cherokee letter TSV: $cherokeeTSV

UNICODE;
print $message . "\n\n";

/*
 * With heredocs, if indentation appears before the closing delimiter, the PHP engine
 * will attempt to remove the same amount of indentation from all lines of the heredoc.
 *
 * If any lines have more indentation than the line with the closing delimiter, that
 * extra bit of indentation will remain in the output.
 *
 * If any lines in a heredoc have less indentation than the closing delimiter,
 * an error will occur.
 */
$message = <<<TEXT
    If the closing delimiter is indented
    then that amount of indentation
    is removed from the lines of the string.
    
    TEXT;
print $message . "\n";

$message = <<<END
    I'm the same indentation as the ending delimiter (4 spaces)
      I have 2 extra spaces
      So have I
    I'm back to 4 spaces again
    
    END;
print $message . "\n\n";

/*
 * The nowdoc is for unparsed strings, which is similar in function to
 * single-quoted strings.
 * The only difference between declaring a nowdoc and a heredoc is that the
 * opening delimiter for the nowdoc must be enclosed in single quotes, like <<<'EOL'
 *
 * One use of nowdocs is for printing out PHP code.
 */
unset($name);
$name = "Matt Smith";

$codeSample = <<<'PHP'
    $message = "hello \n world \n on 3 lines!";
    $age = 21;
    print $name;
    print $age;
    
    PHP;
print $codeSample;