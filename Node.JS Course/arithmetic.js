counter=function counter(arr)
{
    var sum=0;
    arr.forEach(element => {
        sum=sum+element;
    });
    return `The sum of the elements in ${arr} is ${sum}`;
};
add=function(a,b)
{
    return `The sum of ${a} and ${b} is ${a+b}`;
};
sub=function(a,b)
{
    return `The difference of ${a} and ${b} is ${a-b}`;
};
mul=function(a,b)
{
    return `The product of ${a} and ${b} is ${a*b}`;
};
div=function(a,b)
{
    return `The quoteint of ${a} and ${b} is ${a/b}`;
};
mod=function(a,b)
{
    return `The remainder/modulo of ${a} and ${b} is ${a%b}`;
};
module.exports={
    c:counter,
    a:add,
    s:sub,                //Can also use module.exports={counter,add,...,mod} if the property and the value names are the same
    m:mul,
    d:div,
    mod:mod
};
