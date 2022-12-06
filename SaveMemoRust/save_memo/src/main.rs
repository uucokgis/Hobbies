use console::Term;

fn main() {
    let stdout = Term::buffered_stdout();

    'game_loop: loop {
        if let Ok(character) = stdout.read_char() {
            match character {
                'w' => todo!("Up"),
                'a' => todo!("Left"),
                's' => todo!("Down"),
                'd' => todo!("Right"),
                _ => break 'game_loop,
            }
        }
    }
}