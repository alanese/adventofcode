use std::fs;
use std::collections::HashMap;
use advent2019::Intcode;

fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-09.txt").expect("Unable to read file");

    let mut program: HashMap<i64, i64> = HashMap::new();

    for (i, num) in data.split(",").enumerate() {
        program.insert(i as i64, num.parse().expect("Bad parse"));
    }

    //Part 1
    let mut machine = Intcode::create(program.clone());
    machine.push_input(1);

    machine.run();

    println!("{:?}", machine.pop_output().unwrap());

    //Part 2
    machine = Intcode::create(program.clone());
    machine.push_input(2);

    machine.run();

    println!("{:?}", machine.pop_output().unwrap());
}