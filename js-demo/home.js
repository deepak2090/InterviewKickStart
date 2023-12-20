let mySymbol = Symbol();


let person = {
    name: "deepak",
    age: "32",
    showInfo: function(){
        console.log(age)
    }
}

let message = 'GET AN GRIP'
function changeMessage(abc){
    abc = 'hi';
}

changeMessage(message);

showMessage(message);
newOffer(45);

/* change color by accessing properties of element*/

const h1Element = document.getElementById('message');
h1Element.style.color = 'GREEN'
h1Element.style.fontWeight = '500'

const seeReviewButton = document.getElementById('see-review');

seeReviewButton.addEventListener('click', function(){
    const reviewcheck = document.getElementById('review');
    if (reviewcheck.classList.contains('d-none')){
        reviewcheck.classList.remove('d-none');
        seeReviewButton.textContent = 'CLOSE REVIEW';
    }
    else{
        reviewcheck.classList.add('d-none');
        seeReviewButton.textContent = 'ADD REVIEW';
    }


    
});

const values = ['a','b','c'];
console.log(values);
let values1 = Array.of(1,2,3,4);
values1.splice()

const values2 = [1,2,3,4,5,6];
const set1 = values2.filter(function(item){
    return item >2;
});
console.log("the values are", set1);

let app = {
    "name": "deepak"
}
console.log(app.name)

function Person(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.greet = function() {
      console.log("Hello, " + this.firstName + " " + this.lastName + "!");
    };
  }

// Creating an instance of the Person constructor
var newPerson = new Person("John", "Doe", 30);

// Accessing properties and calling a method
console.log(newPerson.firstName);  // Output: "John"
console.log(newPerson.age);        // Output: 30
newPerson.greet();                 // Output: "Hello, John Doe!"

