use std::fs;

fn tree_count(grid: &Vec<Vec<char>>, dx: usize, dy: usize) -> u64 {
    let row_size = grid[0].len();
    let row_count = grid.len();
    let mut x: usize = 0;
    let mut y: usize = 0;
    let mut count: u64 = 0;

    while y < row_count {
        if grid[y][x] == '#' {
            count += 1;
        }
        x = (x + dx) % row_size;
        y += dy;
    }

    count
}
fn main() {
    //Read and parse data
    let data = fs::read_to_string("input-03.txt").expect("Unable to read file");

    let lines: Vec<Vec<char>> = data.lines().map(|x| x.chars().collect()).collect();

    //Part 1
    let result = tree_count(&lines, 3, 1);
    println!("{result}");

    //Part 2
    let r1 = tree_count(&lines, 1, 1);
    let r3 = tree_count(&lines, 5, 1);
    let r4 = tree_count(&lines, 7, 1);
    let r5 = tree_count(&lines, 1, 2);
    println!("{}", r1 * result * r3 * r4 * r5);
}