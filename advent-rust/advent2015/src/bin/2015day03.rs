use std::fs;
use std::collections::HashMap;



fn main(){
    let instructions = fs::read_to_string("input-03.txt").expect("Unable to read file");
    let mut x: i32 = 0;
    let mut y: i32 = 0;

    let mut seen = HashMap::new();
    for c in instructions.chars() {
        match c {
            '^' => y += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            '>' => x += 1,
            _ => ()
        }
        seen.insert((x,y), ());
    }
    println!("{}", seen.len());

    seen.clear();
    let mut santas_turn = true;
    x = 0;
    y = 0;
    let mut robo_x: i32 = 0;
    let mut robo_y: i32 = 0;
    for c in instructions.chars() {
        if santas_turn {
            match c {
                '^' => y += 1,
                'v' => y -= 1,
                '<' => x -= 1,
                '>' => x += 1,
                _ => ()
            }
            seen.insert((x,y), ());
        } else {
            match c {
                '^' => robo_y += 1,
                'v' => robo_y -= 1,
                '<' => robo_x -= 1,
                '>' => robo_x += 1,
                _ => ()
            }
            seen.insert((robo_x, robo_y), ());
        }
        santas_turn = !santas_turn
    }

    println!("{}", seen.len())
}