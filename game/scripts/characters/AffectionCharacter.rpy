init -1 python: # Must be initialised after CustomCharacter and before the rest of the scripts
    class AffectionCharacter(CustomCharacter):
        affection = 0

        def change_affection(amount: int):
            self.affection += amount
            # run fancy screen animation here