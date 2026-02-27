pub struct Intcode {
    pub program: Vec<usize>,
    pub running: bool,
    pub pc: isize
}

impl Intcode {
    pub fn step(&mut self) {
        if self.pc < 0 || self.pc >= self.program.len() as isize || self.program[self.pc as usize] == 99 {
            self.running = false;
        }
        if !self.running {
            return
        }

        let op1 = self.program[(self.pc+1) as usize];
        let op2 = self.program[(self.pc+2) as usize];
        let op3 = self.program[(self.pc+3) as usize];
        match self.program[(self.pc) as usize] {
            1 => {
                self.program[op3] = self.program[op1] + self.program[op2];
                self.pc += 4;
            }
            2 => {
                self.program[op3] = self.program[op1] * self.program[op2];
                self.pc += 4;
            }
            _ => {
                panic!("Invalid opcode");
            }
        }
    }

    pub fn run(&mut self) {
        while self.running {
            self.step();
        }
    }
}