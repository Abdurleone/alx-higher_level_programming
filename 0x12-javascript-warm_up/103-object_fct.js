#!/usr/bin/node
const myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);
myObject.incr = function () {
	this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
<<<<<<< HEAD
console.log(myObject);

=======
console.log(myObject);
>>>>>>> 8c2debe26ce4680c835bf83d9c9f779c9ed86c5f
