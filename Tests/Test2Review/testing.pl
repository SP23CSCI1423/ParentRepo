#perl running file

#calling review.pm module

use Cwd;
use lib "/workspaces/ParentRepo/Tests/Test2Review";
use review;

#calling TakeAttendance
TakeAttendance();

#calling CheckName
CheckName();
