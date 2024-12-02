def main()
    print('')
    menu = '\n\n[g] Games\n[b] BoxScore\n[s] Standings\n' +\
    '\n[dis] Display\n[exit] Exit'
    
    while u_choice != 'exit':
        print(menu)
        u_choice = input('Enter your choice: ')

        if u_choice == 'g':
            if p.game == True:
                print(game)
            else:
                print('error for games')

        elif u_choice == 'b':
            if p.boxscore == True:
                print(new_boxscore)
            else:
                print('Error in boxscore')

        elif u_choice == 's'
            if p.standings == True:
                print(standings)

        elif u_choice =='dis':
            if p.display == True:
                print('---Display---')

        elif u_choice =='exit':
            print('exiting app')
            else:
                print('invalid exit to app')
