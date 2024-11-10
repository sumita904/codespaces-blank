//console.log("Hello world");
//console.log(9 - "5");  
//console.log("sumita" - "kumari");
//console.log(" "+0);
//console.log(false-true);
// var iAmuseless = null;
// console.log(iAmuseless);
// console.log(typeof(iAmuseless)); //bug/ limitation of JS
// var iAmStandBy;
// console.log(iAmStandBy);

//NAN - not a number
// var myPhoneNo= 9470035428;
// var myName= "sumita sinha";

// console.log(isNaN(myPhoneNo));
// console.log(isNaN(myName));

// if(isNaN(myName)){
//     console.log("plz enter correct phone no");
// }

//NaN Practice

// NaN===NaN;
// Number.NaN===NaN;
// isNaN(NaN);
// isNaN(Number.NaN);
// Number.isNaN(NaN);

// console.log(Number.isNaN(NaN));

// var x=5;
// var y=5;

// //console.log("is both x an y are equal or not" + x==y);
// console.log('is both x and y are equal or not : ${x==y}');

// var num=15;
// var newNum= num++;
// console.log(num);
// console.log(num++);
// console.log(newNum);

// var a=30;
// var b=10;

// console.log(a!=b);
// console.log(a>b || b<0 || b>0); //use command+ D for removing and adding duplicate codes
// console.log(!(a>b || b<a));  //Logical NOT ! takes Truth to Falsity (it's called logical omplement,negation)
// console.log(!true);

// var a = true+true+true*3;
// console.log(a);

// var a=10;
// var b=20;
// var c=b;
// b=a;
// a=c;
// console.log("value of a is:" + a);
// console.log("value of b is:" + b);

// var a=10;
// var b='10';

// console.log(a==b);
// console.log(typeof(b));
// console.log(typeof(a===b));

// var tomr='rain';

// if (tomr=='rain'){
//     console.log('take a raincoat');
// }else{
//     console.log('donot take a raincoat');
// }

var year=1000;
debugger;
if(year% 4==0){
    if(year%100==0){
        if(year%400==0){
        console.log("The year "+ year +"is a leap year");
        }else{
            console.log("The year "+ year +"is not a leap year");
        }
    }else{
        console.log("The year "+ year +"is a leap year");
    }
}else{
    console.log("The year "+ year +"is not a leap year");
}
