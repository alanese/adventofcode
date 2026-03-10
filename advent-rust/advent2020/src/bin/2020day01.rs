use std::fs;

fn main() {
    //Read and parse input
    let data = fs::read_to_string("input-01.txt").expect("Unable to open file");

    let nums: Vec<i32> = data.lines().map(|x| x.parse().unwrap()).collect();

    let length = nums.len();

    //Part 1
    'outer: for i in 0..length {
        for j in i+1..length {
            if nums[i] + nums[j] == 2020 {
                println!("{}", nums[i] * nums[j]);
                break 'outer;
            }
        }
    }

    //Part 2
    'outer2: for i in 0..length {
        for j in i+1..length {
            for k in j+1..length {
                if nums[i] + nums[j] + nums[k] == 2020 {
                    println!("{}", nums[i] * nums[j] * nums[k]);
                    break 'outer2;
                }
            }
        }
    }
}