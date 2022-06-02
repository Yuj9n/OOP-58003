print()
print("\tAverage Grade Solver in Python");
print()
subject = input('\tWhat is the subject? ');
prelim = float(input('\tGive Prelim Grade : '));
midterm = float(input('\tGive Midterm Grade : '));
final = float(input('\tGive Final Grade : '));
solve_grade= (prelim * 0.20) + (midterm * 0.30) + (final * 0.50);
print();
print("\t===== DISPLAY RESULTS =====");
print();
print("\tThe subject is" ,subject,'.');
print();
print("\tThe subject grade is {:2.2f}".format(solve_grade));
print();
print("\tEND OF PROGRAM");