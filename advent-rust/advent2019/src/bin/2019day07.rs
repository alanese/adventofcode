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

fn run_p2(program: &Vec<isize>, phases: &Vec<isize>, input: isize) -> isize {
    let mut amp_a = Intcode::create(program.clone());
    amp_a.input.push(phases[0]);
    amp_a.input.push(input);
    let mut amp_b = Intcode::create(program.clone());
    amp_b.input.push(phases[1]);
    let mut amp_c = Intcode::create(program.clone());
    amp_c.input.push(phases[2]);
    let mut amp_d = Intcode::create(program.clone());
    amp_d.input.push(phases[3]);
    let mut amp_e = Intcode::create(program.clone());
    amp_e.input.push(phases[4]);

    let mut final_output: isize = 0;

    while amp_a.status != Status::HALTED && amp_b.status != Status::HALTED && amp_c.status != Status::HALTED
        && amp_d.status != Status::HALTED && amp_e.status != Status::HALTED {
        amp_a.run();
        while amp_a.output.len() != 0 {
            amp_b.input.push(amp_a.output.remove(0));
        }
        amp_b.run();
        while amp_b.output.len() != 0 {
            amp_c.input.push(amp_b.output.remove(0));
        }
        amp_c.run();
        while amp_c.output.len() != 0 {
            amp_d.input.push(amp_c.output.remove(0));
        }
        amp_d.run();
        while amp_d.output.len() != 0 {
            amp_e.input.push(amp_d.output.remove(0));
        }
        amp_e.run();
        if amp_e.output.len() != 0 {
            final_output = *amp_e.output.last().unwrap();
        }
        while amp_e.output.len() != 0 {
            amp_a.input.push(amp_e.output.remove(0));
        }
    }

    return final_output;
}

fn main() {
    //Read and parse input data
    let data = fs::read_to_string("input-07.txt").expect("Unable to read file");

    let mut program: Vec<isize> = Vec::new();

    for num in data.split(",") {
        program.push(num.parse().expect("Malformed input"));
    }

    //Part 1
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

    max_out = 0;
    for phases in (5..=9).permutations(5) {
        let result = run_p2(&program, &phases, 0);
        if result > max_out {
            max_out = result;
        }
    }
    println!("{max_out}");
    
}