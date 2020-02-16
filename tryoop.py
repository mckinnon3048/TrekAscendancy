from os import name, system
class Player:

    ascendancy_level = 1
    culture = 3
    science = 3
    manufacturing = 5
    warp_level = 1
    ships = 3
    civic_centers = 1
    laboratories = 1
    factories = 1
    planets = 1
    
    player_count = 1

    def __init__(self, name, active=False):
        self.name = name
        self.active = active
        self.player_id = Player.player_count
        Player.player_count = Player.player_count + 1
        return
    
    def faction_active(self):
        if self.active == True:
            print('{} active.'.format(self.name))

    def add_culture(self):
        print("adding culture")
        self.culture = self.culture + 1
        return

    def add_science(self):
        self.science = self.science + 1
        return

    def add_manufacturing(self):
        self.manufacturing = self.manufacturing + 1
        return

    def add_warp(self):
        self.warp_level = self.warp_level + 1
        return
    
    def add_ascendancy(self):
        if self.culture >= 5:
            self.culture = self.culture - 5
            self.ascendancy_level = self.ascendancy_level + 1

            if self.ascendancy_level >= 5:
                print("{} Wins via culture victory").format(self.name)
                input(" press enter to close")
                SystemExit
            else:
                return
        else:
            print("You do not have enough culture to spend")
            input()
            return

    def build_ship(self):
        pass

    def build_civics(self):
        pass

    def build_lab(self):
        pass
    
    def build_factory(self):
        pass

    def display_values(self):
        if self.active == True:
            print(
                "The {} level {} has: \n{} culture \n{} science \n{} manufacturing  \n{} warp".format(
                self.name, self.ascendancy_level, self.culture, self.science, self.manufacturing, self.warp_level))
            return
        else:
            return

    def short_display(self):
        if self.active == True:
            print(
            "{} level {} -> culture {} -> science {} -> manufacturing {} ".format( self.name,
            self.ascendancy_level, self.culture, self.science, self.manufacturing))
        else:
            pass

    def menu_run(self):
        upkeep_loop = 1
        while upkeep_loop != 0:  
            system('cls')
            self.display_values()
            #print('PLEASE SELECT AN ACTION')
            print("""
            1: add culture 
            2: add science  
            3: add manufacturing
            4: add warp
            5: increase ascendancy level (-5 culture)
            0: quit
            """)
            menu_selection = input()
            if menu_selection == (''):
                choice = 99999
            else:
                choice = int(menu_selection)
            
            if choice == 1:
                self.add_culture()
            elif choice == 2:
                self.add_science()
            elif choice == 3:
                self.add_manufacturing()
            elif choice == 4:
                self.add_warp()
            elif choice == 5:
                self.add_ascendancy()

            elif choice == 0:
                upkeep_loop = 0
            else:
                print("Invalid selection \n") 
            

federation = Player('Federation',False)
klingons = Player('Klingons', False)
romulans = Player('Romulans', False)
cardassians = Player('Cardassians', False)
ferengi = Player('Ferengi', False)
andorians = Player('Andorians', False)
vulkans = Player('Vulkans', False)

def main():
    print('How many players are there?')
    player_count = count_players()
    while  player_count > 0:
        print("""
        1: Federation
        2: Klingon
        3: Romulin
        4: Cardassian
        5: Ferengi
        6: Andorian
        7: Vulkan
        """)
        menu_input = input()
        if menu_input.isdigit() == False:
            player_selection = 0
        else:    
            player_selection = int(menu_input)
        
        if player_selection == 1:
            if federation.active == False:
                federation.active = True
                player_count = player_count -1
            else:
                print("This faction has already been selected.")

        elif player_selection == 2:
            if klingons.active == False:
                klingons.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")

        elif player_selection == 3:
            if romulans.active == False:
                romulans.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")
        
        elif player_selection == 4:
            if cardassians.active == False:
                cardassians.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")

        elif player_selection == 5:
            if ferengi.active == False:
                ferengi.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")

        elif player_selection == 6:
            if andorians.active == False:
                andorians.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")

        elif player_selection == 7:
            if vulkans.active == False:
                vulkans.active = True
                player_count = player_count - 1
            else:
                print("This faction has already been selected.")
        else:
            print("That was not a valid selection.")


    confirm_active_players()
    print(
        """\n\n
        All players begin with {} ascendancy token, 
        {} culture, {} science, {} manufacturing, warp level {}, 
        their homeworld, with 1 of each structure, and {} ships. 
        \n\nPress Enter/Return to begin.""".format(
        Player.ascendancy_level, Player.culture, Player.science, Player.manufacturing,
        Player.warp_level, Player.ships)
        )
    input()
    system('cls')
    game()

def count_players():
    count_input = input()
    if count_input.isdigit() == True:
        player_count = int(count_input)
        return player_count
    else:
        print("You must input a number.")
        player_count = count_players()
        return player_count



def confirm_active_players():
    federation.faction_active()
    klingons.faction_active()
    romulans.faction_active()
    cardassians.faction_active()
    ferengi.faction_active()
    andorians.faction_active()
    vulkans.faction_active()
    return

def display_player_values():
    federation.short_display()
    klingons.short_display()
    romulans.short_display()
    cardassians.short_display()
    ferengi.short_display()
    andorians.short_display()
    vulkans.short_display()
    input()
    system('cls')
    return

def game():
    game_loop = 1 
    while game_loop != 0:
        system('cls')
        confirm_active_players()
        print("""Select a faction to take their turn.\n
        1: Federation turn
        2: Klingon turn
        3: Romulin turn
        4: Carassian turn
        5: Ferengi turn
        6: Andorian turn
        7: Vulkan turn
        8: All status
        1234: quit
        """)
        menu_input = input()
        if menu_input == (''):
            menu_choice = 0
        else:
            menu_choice = int(menu_input)
        if menu_choice == 1:
            if federation.active == True:
                federation.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 2:
            if klingons.active == True:
                klingons.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 3:
            if romulans.active == True:
                romulans.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 4:
            if cardassians.active == True:
                cardassians.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 5:
            if ferengi.active == True:
                ferengi.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 6:
            if andorians.active == True:
                andorians.menu_run()            
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()
        elif menu_choice == 7:
            if vulkans.active == True:    
                vulkans.menu_run()
            else:
                print("This faction is not in this game. Select a new option. Press enter to resume.")
                input()    
        elif menu_choice == 8:
            display_player_values()

        elif menu_choice == 1234:
            game_loop = 0        
        
        else:
            print("Invalid selection \n press enter to continue.")
            input()    

main()
print ("End game")
