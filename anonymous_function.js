let my_function = function(a,b) {
    let result = a + b;
    return result;
}

let foo = my_function;

result = my_function(123, 42);
console.log(result);

my_number_1 = 123;
my_number_2 = 42;
result = foo(my_number_1, my_number_2);
console.log(result);


