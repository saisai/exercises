use std::process::Command;
use std::io::{Write, self};

fn main() {
    let output = Command::new("/bin/cat")
                    .arg("/etc/fstab")
                    .output()
                    .expect("failed to execute proecess");

    io::stdout().write(&output.stdout);
}

