#module file

sub TakeAttendance {

	# NOTES: fileio operators
		# < : reading
		# > : writing
		# >> : appending
		# +> : create file and write

	#create roster.txt
	open(FILEW, '+>', 'roster.txt') or die "$!\n";
	
	#ask for 10 names and write to roster.txt
	# for(set, check, change)
	for($i = 0; $i < 10; $i++){
		#ask user for name
		print("What is your name?\n");
		chomp($name = <>);

		#add name to roster
		print FILEW "$name \n";
	}	

	close(FILEW);

	#reopening roster.txt with reading
	open(DATA,'<','roster.txt') or die "$!\n";

	#print the contents
	@names = <DATA>;
	print("@names\n");

	close(DATA);
} 

#CheckName subroutine that takes in $name as a parameter
sub CheckName(){
	#asking user for name
	print"What name do you want to check for? \n";
	chomp($givenname = <>);

	#open file for reading
	open (FILER, '<','roster.txt') or die "$!\n";

	#iterate through contents of FILER (roster.txt) using array
	@names = <FILER>;
	foreach $n (@names) {
		#if any names in FILER matches $givenname
		if ($n =~ m/$givenname/) {
			#print found
			print "found\n";
		}
	}
}

1;
