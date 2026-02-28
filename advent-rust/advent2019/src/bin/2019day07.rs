use std::fs;
use advent2019::{Intcode, Status};
use itertools::Itertools;

fn get_signal(program: &Vec<isize>, phase: isize, input: isize) -> isize {
    let mut machine = Intcode {
        program: program.clone(),
        status: Status::RUNNING,
        pc: 0,
        output: Vec::new(),
        input: vec![phase, input]
    };

    machine.run();
    return *machine.output.last().unwrap();

}

fn main() {
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");

    let mut program: Vec<isize> = Vec::new();

    for num in data.split(",") {
        program.push(num.parse().expect("Malformed input"));
    }

    let mut max_out: isize = 0;

    for phases in (0..=4).permutations(5) {
        let a_out = get_signal(&program, phases[0], 0);
        let b_out = get_signal(&program, phases[1], a_out);
        let c_out = get_signal(&program, phases[2], b_out);
        let d_out = get_signal(&program, phases[3], c_out);
        let e_out = get_signal(&program, phases[4], d_out);
        if e_out > max_out {
            max_out = e_out;
        }        
    }

    println!("{max_out}");
    
}