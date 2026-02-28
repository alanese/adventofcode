use std::fs;
use advent2019::{Intcode, Status};

fn main() {
    //Read and parse input file
    let data = fs::read_to_string("input-05.txt").expect("Unable to read file");

    let mut program: Vec<isize> = Vec::new();
    for num in data.trim().split(",") {
        program.push(num.parse().expect("Invalid number"));
    }

    //Part 1
    let mut machine = Intcode {
        program: program.clone(),
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: vec![1]
    };

    machine.run();

    println!("{}", machine.output.last().unwrap());

    //Part 2
    machine = Intcode {
        program: program,
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: vec![5]
    };

    machine.run();

    println!("{}", machine.output.last().unwrap());
}