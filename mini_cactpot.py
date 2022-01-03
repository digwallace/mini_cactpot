import pandas
import random
import tabulate

# TODO (1) - Add gambling option which scales earnings based on wager.
# TODO (2) - Convert earnings to scaled payouts based on wager or initial value.
# TODO (3) - Finalize a display output.
# TODO (4) - Create general class for hanlding output.
# TODO (5) - Create general error handling class.   
# TODO (6) - Add final row selection 'H'.
# TODO (7) - Add initial revealed tile.
class mini_cactpot:

    def __init__(self):
        self.grid_values    = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.valid_rows     = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.grid_display   = list()
        self.earnings = 0
        self.run = True
        
        self.new_game()
    
    
    def initialize(self):
        random.shuffle(self.grid_values)
        self.choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.remaining_choices = self.choices.copy()
        self.grid_display = self.choices.copy()
        self.payouts = {6:10000
            , 7:36
            , 8:720
            , 9:360
            , 10:80
            , 11:252
            , 12:108
            , 13:72
            , 14:54
            , 15:180
            , 16:72
            , 17:180
            , 18:119
            , 19:36
            , 20:306
            , 21:1080
            , 22:144
            , 23:1800
            , 24:3600
            }


    def new_game(self):
        while self.run:
            self.choices_remaining = 3
            self.sum = 0
            self.initialize()
            print("\nSTARTING NEW GAME!\n")
            
            while self.choices_remaining:
            
                self.print_hintbox()
                self.hint_prompt()
                self.print_divider()
            
            self.set_select_gamebox()
            self.print_selectbox()
            self.row_prompt()
            self.get_score()
            self.print_divider()
            self.print_divider()
            self.print_winbox()
            self.print_divider()
            
            self.print_payouts()
            self.play_again_prompt()
    
    
    def play_again_prompt(self):
        player_input = input("Play again? (Y/n)")
        
        if player_input.upper() == "Y":
            return
        elif player_input.upper() == "N":
            print("\nThanks for playing!")
            exit(0)
        else:
            print(" Invalid input! - Enter \"Y\" or \"y\" for Yes, \"N\" or \"n\" for no.")
    
    
    def hint_prompt(self):
        awaiting_input = True

        print("Input tile ("+str(self.choices_remaining)+" left):")
        while awaiting_input:
            player_input = input()
            
            if player_input == "quit":
                self.run = False
                
            elif player_input.upper() in self.remaining_choices:
                awaiting_input = False
                
                index = self.choices.index(player_input.upper())
                self.grid_display[index] = self.grid_values[index]
                self.remaining_choices.remove(player_input.upper())
                
                self.choices_remaining -= 1
                
            else:
                print("Invalid input! (remaining options: ", str(self.remaining_choices)[1:-1].replace("'",'') + ')')


    def print_hintbox(self):
        print(" -------------\n"\
        " | "+self.grid_display[0]+" | "+self.grid_display[1]+" | "+self.grid_display[2]+" |\n"\
        " |---|---|---|\n"\
        " | "+self.grid_display[3]+" | "+self.grid_display[4]+" | "+self.grid_display[5]+" |\n"\
        " |---|---|---|\n"\
        " | "+self.grid_display[6]+" | "+self.grid_display[7]+" | "+self.grid_display[8]+" |\n"\
        " -------------\n")
    
    
    def print_selectbox(self):
        print("\n\n D    E   F   G    H\n    -------------\n"\
        " C  | "+self.grid_display[0]+" | "+self.grid_display[1]+" | "+self.grid_display[2]+" |\n"\
        "    |---|---|---|\n"\
        " B  | "+self.grid_display[3]+" | "+self.grid_display[4]+" | "+self.grid_display[5]+" |\n"\
        "    |---|---|---|\n"\
        " A  | "+self.grid_display[6]+" | "+self.grid_display[7]+" | "+self.grid_display[8]+" |\n"\
        "    -------------")
    
    
    def row_prompt(self):
        awaiting_input = True
        
        while awaiting_input:
            player_input = input("\nSelect a row:")
        
            if player_input == "quit":
                self.run = False
            elif self.valid_row(player_input.upper()):
                self.sum_row(player_input.upper())
                awaiting_input = False
            else:
                print("Invalid input! (valid options: ", str(self.valid_rows)[1:-1].replace("'",'') + ')')
    
    
    def valid_row(self, row):
        if row in self.valid_rows:
            return True
    
    
    def get_score(self):
        self.print_divider()
        print("Your Payout: " + str(self.payouts[self.sum]))
    
    
    def print_winbox(self):
        print("\n\n D    E   F   G    H\n    -------------\n"\
        " C  | "+self.grid_values[0]+" | "+self.grid_values[1]+" | "+self.grid_values[2]+" |\n"\
        "    |---|---|---|\n"\
        " B  | "+self.grid_values[3]+" | "+self.grid_values[4]+" | "+self.grid_values[5]+" |\n"\
        "    |---|---|---|\n"\
        " A  | "+self.grid_values[6]+" | "+self.grid_values[7]+" | "+self.grid_values[8]+" |\n"\
        "    -------------")
        
    
    def set_select_gamebox(self):
        index = 0
        for entry in self.grid_display:
            if entry in self.choices:
                self.grid_display[index] = '*'
            index += 1
    
    
    def sum_row(self, row):
        if row == 'A':
            self.sum = int(self.grid_values[6]) + int(self.grid_values[7]) + int(self.grid_values[8])
        elif row == 'B':
            self.sum = int(self.grid_values[3]) + int(self.grid_values[4]) + int(self.grid_values[5])
        elif row == 'C':
            self.sum = int(self.grid_values[0]) + int(self.grid_values[1]) + int(self.grid_values[2])
        elif row == 'D':
            self.sum = int(self.grid_values[0]) + int(self.grid_values[4]) + int(self.grid_values[8])
        elif row == 'E':
            self.sum = int(self.grid_values[0]) + int(self.grid_values[3]) + int(self.grid_values[6])
        elif row == 'F':
            self.sum = int(self.grid_values[7]) + int(self.grid_values[4]) + int(self.grid_values[1])
        elif row == 'G':
            self.sum = int(self.grid_values[8]) + int(self.grid_values[5]) + int(self.grid_values[2])
        elif row == 'H':
            self.sum = int(self.grid_values[2]) + int(self.grid_values[4]) + int(self.grid_values[6])
            
     
    def print_divider(self):
        print("==========================")
        
    
    
    def print_payouts(self):
        print("\n =============== Payout ================"\
              "\n Sum     MGP    Sum    MGP   Sum    MGP "\
              "\n   6   10,000    12    108    18    119 "\
              "\n   7      36     13     72    19     36 "\
              "\n   8     720     14     54    20    306 "\
              "\n   9     360     15    180    21   1,080"\
              "\n  10      80     16     72    22    144 "\
              "\n  11     252     17    180    23   1,800"\
              "\n                              24   3,600")


def main():
    instance = mini_cactpot()
    return
    
    
if __name__ == "__main__":
    main()
    