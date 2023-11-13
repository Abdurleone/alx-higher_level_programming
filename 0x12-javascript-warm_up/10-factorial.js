#!/usr/bin/node
function factorial (n) {
	if (n < 0) {
		return (-1);
	}
	if (n === 0 || isNaN(n)) {
		return (1);
	}
	return (n * factorial(n - 1));
}

<<<<<<< HEAD
console.log(factorial(Number(process.argv[2])));

=======
console.log(factorial(Number(process.argv[2])));
>>>>>>> 8c2debe26ce4680c835bf83d9c9f779c9ed86c5f
