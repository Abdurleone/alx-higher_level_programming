#!/usr/bin/node
if (process.argv.length <= 3) {
	console.log('0');
} else {
<<<<<<< HEAD
	const arr = process.argv.slice(2).map(Number);
	const second = arr.sort(function (a, b) {return b -a})[1];
	console.log(second);
}

=======
    const arr = process.argv.slice(2).map(Number);
    const second = arr.sort(function (a, b) {return b -a})[1];
    console.log(second);
}
>>>>>>> 8c2debe26ce4680c835bf83d9c9f779c9ed86c5f
