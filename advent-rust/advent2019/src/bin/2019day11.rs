use std::collections::HashMap;
use std::fs;
use advent2019::{Intcode, Status};

#[derive(PartialEq, Copy, Clone)]
enum Direction {
    North,
    East,
    South,
    West
}

impl Direction {
    fn vector(&self) -> (i32, i32) {
        match self {
            Direction::North => (0, -1),
            Direction::East => (1, 0),
            Direction::South => (0, 1),
            Direction::West => (-1, 0)
        }
    }

    fn turn_left(&self) -> Direction {
        match self {
            Direction::North => Direction::West,
            Direction::East => Direction::North,
            Direction::South => Direction::East,
            Direction::West => Direction::South
        }
    }

    fn turn_right(&self) -> Direction {
        match self {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North
        }
    }
}

fn paint_id(program: &HashMap<i64, i64>, init_color: i64) ->  HashMap<(i32, i32), i64> {
    let mut machine = Intcode::new(program.clone());

    let (mut robot_x, mut robot_y) = (0,0);
    let mut robot_direction = Direction::North;
    let mut paint: HashMap<(i32, i32), i64> = HashMap::new();
    paint.insert((0,0), init_color);

    while machine.get_status() != Status::Halted {
        machine.push_input(*paint.get(&(robot_x, robot_y)).unwrap_or(&0));
        machine.run();
        if machine.has_output() {
            paint.insert((robot_x, robot_y), machine.pop_output().unwrap());
            match machine.pop_output().unwrap() {
                0 => robot_direction = robot_direction.turn_left(),
                1 => robot_direction = robot_direction.turn_right(),
                _ => panic!("Unexpected output")
            }
            let (dx, dy) = robot_direction.vector();
            robot_x += dx;
            robot_y += dy;
        }
    }

    paint
}

fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-11.txt").expect("Unable to read file");
    let mut program: HashMap<i64, i64>  = HashMap::new();
    for (i, num) in data.split(",").enumerate() {
        program.insert(i as i64, num.parse().expect("Bad parse"));
    }

    //Part 1
    let mut paint = paint_id(&program, 0);
    println!("{}", paint.len());

    //Part 2
    paint = paint_id(&program, 1);
    let mut min_x = std::i32::MAX;
    let mut min_y = std::i32::MAX;
    let mut max_x = std::i32::MIN;
    let mut max_y = std::i32::MIN;

    for (x,y) in paint.keys() {
        if *x < min_x {
            min_x = *x;
        }
        if *x > max_x {
            max_x = *x;
        }
        if *y < min_y  {
            min_y = *y;
        }
        if *y > max_y {
            max_y = *y;
        }
    }

    for y in min_y..=max_y {
        for x in min_x..=max_x {
            if *paint.get(&(x,y)).unwrap_or(&0) == 0 {
                print!(" ");
            } else {
                print!("#");
            }
        }
        println!();
    }

}