use std::fs;
use std::collections::HashMap;
use advent2019::{Intcode, Status};

fn update_screen(machine: &mut Intcode, screen: &mut HashMap<(i64, i64), i64>) {
    while machine.has_output() {
        let x = machine.pop_output().unwrap();
        let y = machine.pop_output().unwrap();
        let id = machine.pop_output().unwrap();
        screen.insert((x,y), id);
    }
}

/// Returns paddle x, ball x, score, block count
fn get_status(screen: &HashMap<(i64, i64), i64>) -> (i64, i64, i64, i32) {
    let mut paddle_x = 0;
    let mut ball_x = 0;
    let mut score = 0;
    let mut block_count = 0;
    for ((x,y), id) in screen {
        if *x == -1 && *y == 0 {
            score = *id;
        } else if *id == 2 {
            block_count += 1;
        } else if *id == 3 {
            paddle_x = *x;
        } else if *id == 4 {
            ball_x = *x
        }
    }

    (paddle_x, ball_x, score, block_count)
}

fn main() {
    let data = fs::read_to_string("input-13.txt").expect("Unable to open file");
    let mut program: HashMap<i64, i64> = HashMap::new();
    for (i, num) in data.split(",").enumerate() {
        program.insert(i as i64, num.parse().unwrap());
    }

    let mut screen: HashMap<(i64, i64), i64> = HashMap::new();
    //Part 1
    let mut machine = Intcode::new(program.clone());
    machine.run();

    update_screen(&mut machine, &mut screen);
    let (_, _, _, block_count) = get_status(&screen);
    println!("{block_count}");

    //Part 2
    screen.clear();
    program.insert(0, 2);
    machine = Intcode::new(program);

    let mut block_count = -1;
    let (mut ball_x, mut paddle_x);

    while machine.get_status() != Status::Halted && block_count != 0 {
        machine.run();
        update_screen(&mut machine, &mut screen);
        (paddle_x, ball_x, _, block_count) = get_status(&screen);
        
        if paddle_x < ball_x {
            machine.push_input(1);
        } else if paddle_x > ball_x {
            machine.push_input(-1);
        } else {
            machine.push_input(0);
        }
    }
    println!("{}", screen.get(&(-1, 0)).unwrap());
}