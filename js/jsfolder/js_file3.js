function area()
{
    var num1,num2,r;
    num1 = document.getElementById('input1').value;
    num2 = document.getElementById('input2').value;

    r = num1*num2;
    document.getElementById('result').value=r;

}

function fact()
{
    var num,input,i;
    num = 1
    input = document.getElementById('input').value;
    for(i=0;i<input;i++){
        num = num*i
    }
    
    document.getElementById('result').value=num;

}
