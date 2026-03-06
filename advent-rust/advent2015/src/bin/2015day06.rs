use std::fs;

enum Instruction {
    On,
    Off,
    Toggle
}

fn parse_coordinate(coords: &str) -> (usize, usize) {
    let split: Vec<_> = coords.split(",").collect();
    return (split[0].parse().unwrap(), split[1].parse().unwrap())
}

fn parse_line(line: &str) -> (Instruction, usize, usize, usize, usize) {
    let words: Vec<_> = line.split_whitespace().collect();

    if words[1] == "on" {
        let (x1, y1) = parse_coordinate(words[2]);
        let (x2, y2) = parse_coordinate(words[4]);
        return (Instruction::On, x1, y1, x2, y2);
    } else if words[1] == "off" {
        let (x1, y1) = parse_coordinate(words[2]);
        let (x2, y2) = parse_coordinate(words[4]);
        return (Instruction::Off, x1, y1, x2, y2);
    } else {
        let (x1, y1) = parse_coordinate(words[1]);
        let (x2, y2) = parse_coordinate(words[3]);
        return (Instruction::Toggle, x1, y1, x2, y2);
    }
}

const GRID_SIZE: usize = 1000;
fn main() {
    let data = fs::read_to_string("input-06.txt").expect("Unable to read file");
    let mut grid: Vec<i32> = vec![0; 1000000];
    let mut instructions: Vec<(Instruction, usize, usize, usize, usize)> = Vec::new();

    for line in data.lines() {
        instructions.push(parse_line(line));
    }

    //Part 1
    for (instruction, x1, y1, x2, y2) in instructions.iter() {
        for y in *y1..=*y2 {
            for x in *x1..=*x2 {
                match instruction {
                    Instruction::On => grid[x*GRID_SIZE + y] = 1,
                    Instruction::Off => grid[x*GRID_SIZE + y] = 0,
                    Instruction::Toggle => grid[x * GRID_SIZE + y] = 1 - grid[x * GRID_SIZE + y]
                }
            }
        }
    }

    let mut sum: i32 = grid.iter().sum();
    println!("{sum}");

    //part 2
    grid = vec![0;1000000];
    for (instruction, x1, y1, x2, y2) in instructions {
        for y in y1..=y2 {
            for x in x1..=x2 {
                match instruction {
                    Instruction::On => grid[x*GRID_SIZE + y] += 1,
                    Instruction::Off => grid[x*GRID_SIZE + y] = (grid[x*GRID_SIZE+y]-1).max(0),
                    Instruction::Toggle => grid[x * GRID_SIZE + y] += 2
                }
            }
        }
    }

    sum = grid.iter().sum();
    println!("{sum}")

    
}