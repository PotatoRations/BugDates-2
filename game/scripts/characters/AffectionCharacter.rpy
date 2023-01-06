init 1 python: # Must be initialised after CustomCharacter
    class AffectionCharacter(CustomCharacter):
        affection = 0

        def change_affection(amount: int):
            self.affection += amount
            # run fancy screen animation here