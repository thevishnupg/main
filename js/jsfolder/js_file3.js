
// Question: area
function area()
{
    var num1,num2,r;
    num1 = document.getElementById('input1').value;
    num2 = document.getElementById('input2').value;

    r = num1*num2;
    document.getElementById('result1').value=r;

}

// Question2 : Factorial
function fact()
{
    var i,input,j;
    j = 1;
    input = document.getElementById('input3').value;
    if (input==0){
        document.getElementById('result2').value=0;
    }else{
        for(i=1;i<=input;i++){
        j = j*i;
    }
    document.getElementById('result2').value=j;
    }
}


// Find the price of fruits
function price_fruit()
{
    var fruits,price;
    fruits = document.getElementById('input4').value;
    switch(fruits){
        case 'Apple':
            price=60;
            break;
        case 'Mango':
            price=40;
            break;
        case 'Grapes':
            price=45;
            break;
        case 'Banana':
            price=30;
            break;
        case 'Watermelon':
            price=20;
            break;
    }
    price = document.getElementById('result3').value=price;
}

// Email and Password validation 
function validation()
{

    var u,p1,p2,e,m;
    u = document.getElementById('input5').value;
    p1 = document.getElementById('input6').value;
    p2 = document.getElementById('input7').value;
    e = document.getElementById('input8').value;
    m = document.getElementById('input9').value;


    // txt1 = len(x)
    // txt2 = re.search(r'[a-z]',x)
    // txt3 = re.search(r'[A-Z]',x)
    // txt4 = re.search(r'[0-9]',x)
    // txt5 = re.search(r'\s',x)
    // txt6 = re.search(r'[@#$%&_*]',x)


    // if txt1>8:
    //     print('Not valid, Password should not grater than 8 letter')
    // if not txt2:
    //     print('Not valid , Password should contain one lower case letter')
    // if not txt3:
    //     print('Not valid, Password should contain one capital letter ')
    // if not txt4:
    //     print('Not valid, Password should contain one digit')
    // if txt5:
    //     print('Not valid, Password should not contain white space')
    // if not txt6:
    //     print('Not valid, Password should contain special charecter')
    // else:
    //     print('Password obtained.')

   
    // r = num1*num2;
    // document.getElementById('result1').value=r;

}

// Hide and show the content using jquery

$("#hide").click(function(){
    $("div").hide();
  });
  
  $("#show").click(function(){
    $("div").show();
  });