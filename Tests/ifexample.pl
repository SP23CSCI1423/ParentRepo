#!/usr/bin/perl

print("Please give me a number: ");
$num = <>;
chomp($num);

if($num == 2) {
	print("The number you chose was 2\n");
}
elsif($num == 5){
	print("The number you chose was 5\n");
}
elsif($num == 7){
	print("The number you chose was 7\n");
}
else{
	print("The number you chose was not 2, 5, or 7\n");
}

#Note use == to check number values, eq to check string (word) values
