use std::fs;
use std::collections::{HashMap, HashSet};
use std::f64::consts::PI;

//Greatest common divisor, using the Euclidean algorithm
fn gcd(mut x: i32, mut y: i32) -> i32 {
    while y != 0 {
        (x,y) = (y,x%y);
    }

    return x.abs();
}

fn reduce(x: i32, y: i32) -> (i32, i32) {
    if x == 0 {
        (0, y.signum())
    } else if y == 0 {
        (x.signum(), 0)
    } else {
        let div = gcd(x, y);
        (x/div, y/div)
    }
}

fn angle_from_up(x: i32, y: i32) -> f64 {
                    //Remember up is negative!
    return ((x as f64).atan2(-y as f64) + (2.0*PI)) % (2.0*PI);
}
fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-10.txt").expect("Unable to read file");

    let mut asteroids: HashSet<(i32, i32)> = HashSet::new();

    for (y, row) in data.lines().enumerate() {
        for (x, chr) in row.chars().enumerate() {
            if chr == '#' {
                asteroids.insert((x as i32, y as i32));
            }
        }
    }

    //Part 1
    let (mut best_x, mut best_y) = (-1, -1);
    let mut most_seen = 0;

    for (cur_x, cur_y) in &asteroids {
        let mut visible: HashSet<(i32, i32)> = HashSet::new();
        for (other_x, other_y) in &asteroids {
            let off_x = other_x - cur_x;
            let off_y = other_y - cur_y;
            visible.insert(reduce(off_x, off_y));
        }
        if visible.len() > most_seen {
            most_seen = visible.len();
            (best_x, best_y) = (*cur_x, *cur_y);
        }
    }
    println!("{best_x},{best_y}: {}", most_seen-1);

    //Part 2
    let mut by_angle: HashMap<(i32, i32), Vec<(i32, i32)>> = HashMap::new();
    for (cur_x, cur_y) in asteroids {
        let (to_x, to_y) = reduce(cur_x - best_x, cur_y - best_y);
        if !by_angle.contains_key(&(to_x, to_y)) {
            by_angle.insert((to_x, to_y), vec![(cur_x, cur_y)]);
        } else {
            by_angle.get_mut(&(to_x, to_y)).unwrap().push((cur_x, cur_y));
        }
    }
    by_angle.remove(&(0,0)).unwrap();

    let mut angles: Vec<(i32, i32)> = Vec::new();
    for angle in by_angle.keys() {
        angles.push(*angle);

    }

    angles.sort_by(|(x1, y1), (x2, y2)| angle_from_up(*x1, *y1).total_cmp(&angle_from_up(*x2, *y2)));

    let mut found = 0;
    let mut cycle: usize = 0;
    let (target_x, target_y): (i32, i32);
    'outer: loop {
        for angle in &angles {
            if by_angle[angle].len() > cycle {
                found += 1;
            }
            if found == 200 {
                (target_x, target_y) = *angle;
                break 'outer;
            }

        }
        cycle += 1;
    }

    println!("{:?}, {cycle}", by_angle[&(target_x, target_y)]);


}