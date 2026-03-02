use std::fs;
use std::collections::HashMap;
use advent2019::Intcode;

fn main() {
    //Read and parse input file
    let data = fs::read_to_string("input-05.txt").expect("Unable to read file");

    let mut program: HashMap<i64, i64> = HashMap::new();
    for (i, num) in data.trim().split(",").enumerate() {
        program.insert(i as i64,num.parse().expect("Invalid number"));
    }

    //Part 1
    let mut machine = Intcode::new(program.clone());
    machine.push_input(1);
    /*
    let mut machine = Intcode {
        program: program.clone(),
        status: Status::Running,
        pc: 0,
        output: Vec::new(),
        input: vec![1],
        relative_base: 0
    };
    */

    machine.run();

    println!("{}", machine.last_output().unwrap());

    //Part 2
    machine = Intcode::new(program.clone());
    machine.push_input(5);

    machine.run();

    println!("{}", machine.last_output().unwrap());
}