use std::fs;

fn main() {
    let mut floor: i32 = 0;
    let mut hit_basement = false;
    let code = fs::read_to_string("input-01.txt").expect("Unable to read file");

    for (i, c) in code.chars().enumerate(){
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => ()
        }
        if !hit_basement && floor < 0 {
            println!("Hit basement at index {}", i+1);
            hit_basement = true;
        }
    }
    println!("{floor}")
}