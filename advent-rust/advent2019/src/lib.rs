use std::collections::{HashMap, VecDeque};

#[derive(Copy, Clone, PartialEq, Debug)]
pub enum Status {
    Running, //Program running normally
    Blocked, //Program awaiting input
    Halted   //Program completer
}

pub struct Intcode {
    program: HashMap<i64, i64>,
    status: Status,
    pc: i64,
    output: VecDeque<i64>,
    input: VecDeque<i64>,
    relative_base: i64
}

impl Intcode {
    //Create an Intcode object with the specified program
    pub fn create(program: HashMap<i64, i64>) -> Intcode {
        return Intcode{
            program: program,
            status: Status::Running,
            pc: 0,
            output: VecDeque::new(),
            input: VecDeque::new(),
            relative_base: 0
        };
    }

    //Push x into the input queue
    pub fn push_input(&mut self, x: i64) {
        self.input.push_back(x);
    }

    //Check whether the output queue contains a value
    pub fn has_output(&mut self) -> bool {
        return self.output.len() > 0;
    }

    //Pop and return the next value in the output queue, or None
    pub fn pop_output(&mut self) -> Option<i64> {
        return self.output.pop_front();
    }

    //Return most recently-added value from the output queue
    pub fn last_output(&mut self) -> Option<i64> {
        match self.output.back() {
            Some(x) => Some(*x),
            None => None
        }
    }

    pub fn get_status(&self) -> Status {
        return self.status;
    }

    fn get_ops(&self, num: u8, modes: i64) -> Vec<i64> {
        let mut ops: Vec<i64> = Vec::new();
        let mut next_mode = modes;

        for offset in 1..=num {
            match next_mode % 10 {
                0 => ops.push(*self.program.get(&(self.pc + offset as i64)).unwrap()),
                1 => ops.push(self.pc + offset as i64),
                2 => ops.push(*self.program.get(&(self.pc + offset as i64)).unwrap() + self.relative_base),
                _ => panic!("Invalid operator mode")
            }
            next_mode /= 10;
        }
        return ops;
    }

    pub fn get_mem(&mut self, addr: i64) -> i64 {
        if !self.program.contains_key(&addr) {
            self.program.insert(addr, 0);
        }
        self.program[&addr]
    }

    pub fn step(&mut self) {
        if self.status == Status::Halted {
            return;
        }

        let opcode = self.program[&self.pc] % 100;
        let modes = self.program[&self.pc] / 100;
        match opcode {
            1 => {
                //Add
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], op0 + op1);
                self.pc += 4;
            }
            2 => {
                //Multiply
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], op0 * op1);
                self.pc += 4;
            }
            3 => {
                //Input
                if self.input.len() == 0 {
                    self.status = Status::Blocked;
                    return;
                }
                let ops = self.get_ops(1, modes);
                self.program.insert(ops[0], self.input.pop_front().unwrap());
                self.pc += 2;
            }
            4 => {
                //Output
                let ops = self.get_ops(1, modes);
                let op0 = self.get_mem(ops[0]);
                self.output.push_back(op0);
                self.pc += 2;
            }
            5 => {
                //jump-if-true
                let ops = self.get_ops(2, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                if op0 != 0 {
                    self.pc = op1;
                } else {
                    self.pc += 3;
                }
            }
            6 => {
                //jump-if-false
                let ops = self.get_ops(2, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                if op0 == 0 {
                    self.pc = op1;
                } else {
                    self.pc += 3;
                }
            }
            7 => {
                //less than
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], if op0 < op1 {1} else {0});
                self.pc += 4;
            }
            8 => {
                //equals
                let ops = self.get_ops(3, modes);
                let op0 = self.get_mem(ops[0]);
                let op1 = self.get_mem(ops[1]);
                self.program.insert(ops[2], if op0 == op1 {1} else {0});
                self.pc += 4;
            }
            9 => {
                //Relative base offset
                let ops = self.get_ops(1, modes);
                let op0 = self.get_mem(ops[0]);
                self.relative_base += op0;
                self.pc += 2;
            }
            99 => {
                self.status = Status::Halted;
            }
            _ => {
                panic!("Invalid opcode");
            }
        }
    }

    //Run the machine until it either halts or blocks
    pub fn run(&mut self) {
        if self.status == Status::Blocked {
            self.status = Status::Running;
        }
        while self.status == Status::Running {
            self.step();
        }
    }
}