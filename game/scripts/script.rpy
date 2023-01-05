# Script starts here

define n = Character("Nighten", image="nighten")

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label start:

    ac "hello ksjdfhkjsdfhjksdh"


    #nvl show
    pause
    nvl_narrator "Ace added you to the group"
    ac_nvl "It's ball snatching time"
    mc_nvl "Who's this?"
    nvl_narrator "Blair joined the group"
    b_nvl "I'm here too!"
    return
