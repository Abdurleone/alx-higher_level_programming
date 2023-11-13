#!/usr/bin/node
if (ProcessingInstruction.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
} else {
<<<<<<< HEAD
	const x = Number(process.argv[2]);
	let i = 0;
	while (i < x) {
		console.log('C is fun');
		i++;
	}
}

=======
    const x = Number(process.argv[2]);
    let i = 0;
    while (i < x) {
        console.log('C is fun');
        i++;
    }
}
>>>>>>> 8c2debe26ce4680c835bf83d9c9f779c9ed86c5f
