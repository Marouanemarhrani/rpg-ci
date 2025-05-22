from character import Character
from combat import Combat

def main():
    name = input("Entrez le nom de votre personnage : ")
    player = Character(name=name)
    enemy = Character(name="Bot")

    fight = Combat(player, enemy)

    while not fight.is_over():
        print(f"\n{player.name}: {player.hp} HP — {enemy.name}: {enemy.hp} HP")

        if fight.turn % 2 == 0:
            action = input("Votre tour ! (attack/heal): ").strip().lower()
            if action == "attack":
                player.attack(enemy)
            elif action == "heal":
                player.heal()
            else:
                print("Action invalide, vous perdez votre tour.")
        else:
            # Tour du bot
            if enemy.hp < 5:
                enemy.heal()
                print(f"{enemy.name} se soigne !")
            else:
                enemy.attack(player)
                print(f"{enemy.name} vous attaque !")

        fight.turn += 1

    print("\nCombat terminé !")
    print(f"🏆 Vainqueur : {fight.winner().name}")

if __name__ == "__main__":
    main()
