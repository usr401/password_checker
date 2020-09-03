import subprocess as subpro
import sys, time, random



def main():


    def exit_prompt():

        print('\n[1] Test another password\n[2] Exit\n   ')
        
        rerun = int(input('Enter choice: '))

        if rerun == 1:
            main()

        else:
            subpro.call('clear', shell=True)
            sys.exit(0)



    subpro.call('clear', shell=True)

    print('============================================')
    print('              PASSWORD CHECKER              ')
    print('============================================')
    print('                                            ')
    print('  [0] Exit                                  ')
    print('  [1] Check if in top 10,000 passwords      ')
    print('  [2] Evaluate strength of password         ')
    print('                                            ')
    print('============================================')

    try:
        init_choice = int(input('\n   Enter choice: '))

    except ValueError:
        print('\n   ERROR: Enter a number from the menu')
        time.sleep(1)
        main()

    if init_choice == 0:

        sys.exit(0)


    ### BRANCH 1 ###

    elif init_choice == 1:

        try:
            passwd = input('\n   Enter password: ')
            subpro.call('clear', shell=True)

        except KeyboardInterrupt:
            print('\n\nERROR: Keyboard interupt\n')
            time.sleep(0.5)
            sys.exit(0)

        with open("pass3000.csv") as pwords:
            pass_list = [ ]
            for item in pwords.readlines():
                item = item.rstrip()
                pass_list.append(item)

        del pass_list[42]
        del pass_list[-1]

        if passwd in pass_list:
            print('_' * (32 + len(passwd)))
            print(f'\nTRUE: "{passwd}" in top 10,000 passwords  ')
            print('_' * (32 + len(passwd)) + '\n')

        else:
            print('_' * (36 + len(passwd)))
            print(f'\nFALSE: "{passwd}" not in top 10,000 passwords')
            print('_' * (36 + len(passwd)) + '\n')

        exit_prompt()


    ### BRANCH 2 ###

    elif init_choice == 2:
         
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        upper = alpha.upper()
        special = ('~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',
                   ']','}','|','\\',';',':','"',"'",'<',',','>','.','?','/')
        numbers = str(random.randint(0,1000000000))

        try:
            passwd = input('\n   Enter password: ')
            subpro.call('clear', shell=True)

        except KeyboardInterrupt:
            print('\n\nERROR: Keyboard interupt\n')
            time.sleep(0.5)
            sys.exit(0)
       
        alp = [ ]
        upp = [ ]
        spe = [ ]
        num = [ ]

        for char in passwd:

            if char in alpha:
                alp.append(char)

            elif char in upper:
                upp.append(char)

            elif char in special:
                spe.append(char)

            else:
                num.append(char)

        length = len(passwd)
        alength = len(alp)
        ulength = len(upp)
        slength = len(spe)
        nlength = len(num)

        if length < 15: 
            strength='weak'.upper() 

        elif length >= 15 and length < 30 and ulength <= 2 and slength <= 2 and nlength <= 2: 
            strength='weak'.upper()

        elif length >= 15 and length < 30 and ulength > 2 and slength > 2 and nlength > 2:
            strength='medium'.upper()

        elif length >= 30 and length < 50 and ulength < 2 or slength < 2 or nlength < 2:
            strength='medium'.upper() 

        elif length >= 30 and length < 50 and ulength >= 2 and slength >= 2 and nlength >= 2:
            strength='strong'.upper()

        elif length >= 50 and ulength < 3 or slength < 3 or nlength < 3: 
            strength='strong'.upper()

        elif length >= 50 and ulength >= 3 and slength >= 3 and nlength >= 3:
            strength='very strong'.upper()

        else:
            strength=None

        subpro.call('clear', shell=True)

        print('=========================')
        print('    PASSWORD SECURITY    ')
        print('=========================')
        print('                         ')
        print(f' Lower case: {alength}  ')
        print('                         ')
        print(f' Upper case: {ulength}  ')
        print('                         ')
        print(f' Special: {slength}     ')
        print('                         ')
        print(f' Numbers: {nlength}     ')
        print('                         ')
        print(f' Total Length: {length} ')
        print('                         ')
        print('=========================')
        print('    PASSWORD STRENGTH    ')
        print('=========================')
        print(f'\n {strength}         \n')
        print('=========================')

        exit_prompt()

    
main()


