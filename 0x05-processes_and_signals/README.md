# Processes and signals

Project done during **Full Stack Software Engineering studies** at **Alx School**. It aims to learn about PID, processes and commands that handles them (`ps`, `pgrep`, `pkill`, `kill`, etc) in **Bash**.

## Technologies
* Scripts written in Bash 4.3.11(1)
* Tested on Ubuntu 20.04 LTS

## Files

| Filename | Description |
| -------- | ----------- |
| `0-what-is-my-pid` | Displays its own PID |
| `1-list_your_processes` | Displays a list of currently running processes |
| `2-show_your_bash_pid` | Displays lines contaning the `bash` word in a list of currently running processes |
| `3-show_your_bash_pid_made_easy` | Displays the PID, along with the process name, of processes whose name contain the word `Bash` |
| `4-to_infinity_and_beyond` | Displays `To infinity and beyond` indefinitely |
| `5-dont_stop_me_now` | Kills `4-to_infinity_and_beyond` process |
| `6-stop_me_now_if_you_can` | Kills `4-to_infinity_and_beyond` process |
| `7-highlander` | Displays `To infinity and beyond` indefinitely and displays `I am invincible!!!` when receiving a `SIGTERM` signal |
| `8-beheaded_process` | Kills the process `7-highlander` |
| `100-process_and_pid_file` | Prints some messages according to sended signals |
| `101-manage_my_process` | Init script that manages `manage_my_process` with `start`, `stop` and `restart` instructions |
| `102-zombie.c` | C program that creates 5 zombie processes |
