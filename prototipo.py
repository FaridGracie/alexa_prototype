def get_command():
    command = input('Enter your command:\n')
    print('Your command is ' + command + '?')
    confirmation = input('yes/no\n')
    if confirmation == "yes":
        if command[0] == 'o':
            program = command[5]
            if command[5] == "c" and command[6] == 's' and command[7] == 'g' and command[8] == 'o':
                os.startfile('csgo.exe')
            elif command[5] == 'v' and command[6] == 'e' and command[7] == 'g' and command[8] == 'a' and command[9] == 's':
               os.startfile('vegas160.exe')
            elif command[5] == 'g' and command[6] == 'o' and command[7] == 'o' and command[8] == 'g' and command[9] == 'l' and command[10] == 'e' or 'c' and command[6] == 'h' and command[7] == 'r' and command[8] == 'o' and command[9] == 'm' and command[10] == 'e':
                os.startfile('chrome.exe')
            elif command[5] == 'c' and command[6] == 'l' and command[7] == 'i' and command[8] == 'p' and command[9] == 'e' and command[10] == 's':
                local_clipes = 'D:/fredg/Videos/Counter-strike  Global Offensive'
                webbrowser.open(local_clipes)
            else:
                print('Request not supported, sending request ideia to Farid.')
                command_suggestions = open('Command.txt', 'a')
                command_suggestions.write(command + '\n')
                command_suggestions.close()
        elif command[0] == 's':
            webbrowser.open('https://www.google.com/search?q=' + command.replace('search', ''))
        elif command[0] == 'a':
            if command[7] == 'a':
                task = input('What task do you want to add? When do you want to be remembered?')
                agenda =  open('Agenda.txt', 'a')
                agenda.write(task + '\n')
                agenda.close
            elif command[7] == 's':
                leragenda = open('Agenda.txt', 'r')
                print(leragenda.readline(1))
                leragenda.close
            elif command[7] == 'w':
                with open("Agenda.txt", "r") as file_input:
                    with open("Agenda.txt", "w") as output: 
                        for line in file_input:
                            if line.strip("\n") != 'remove':
                                output.write(line)
            elif command[7] == 'r':
                os.startfile('Agenda.txt')
            else:
                print('Request not supported, sending request ideia to Farid.')
                command_suggestions = open('Command.txt', 'a')
                command_suggestions.write(command + '\n')
                command_suggestions.close()
        else:
            print('Request not supported, sending request ideia to Farid.')
            command_suggestions = open('Command.txt', 'a')
            command_suggestions.write(command + '\n')
            command_suggestions.close()   
          
    else:
        get_command()

get_command()