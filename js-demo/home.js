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