fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let num1 = 5;
    let num2 = 10;
    let sum = add_numbers(num1, num2);
    println!("The sum of {} and {} is: {}", num1, num2, sum);
}