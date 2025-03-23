<?php
$vehicle = 'helicopter';
$message = match ($vehicle) {
    'bus' => 'Beep beep',
    'train' => 'Runs on tracks',
    'car' => 'Has at least three wheels',
    'helicopter' => 'Can fly',
    'bicycle' => 'You never forget once you\'ve learned',
    default => 'You\'ve chosen the road less travelled.'
};
print "Mode of transportation: $vehicle\n";
print "Message: $message\n";