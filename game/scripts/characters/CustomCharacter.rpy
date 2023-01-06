init python:
    from enum import Enum
    from functools import partial #Used when implementing the beep stuff

    # Audio channel for bleeps
    renpy.music.register_channel('bleeps', mixer='bleeps', loop=False)

    ## Custom character object that handles all of the extra things we need characters to be able to do in a neat-ish package
    class CustomCharacter:
        # Enum representing voice beep types
        class VoiceMode(Enum):
            LOW = 0
            NORM = 1
            HIGH = 2

        bleep_dict = {
            VoiceMode.LOW: '<silence 0.05>',
            VoiceMode.NORM: '<silence 0.05>',
            VoiceMode.HIGH: '<silence 0.05>'
        }

        voice_mode = VoiceMode.NORM
        muted = False

        # Changes which beep this character's voice callback will use
        def change_voice_mode(mode: VoiceMode):
            self.voice_mode = mode

        def set_mute(mode: bool):
            self.muted = mode
        
        def set_voices(high: str, norm: str, low: str):
            self.bleep_dict[VoiceMode.HIGH] = high
            self.bleep_dict[VoiceMode.NORM] = norm
            self.bleep_dict[VoiceMode.LOW] = low

    ## Callback function for beeps
    def beep(char: CustomCharacter, event, interact=True, **kwargs):
        if not interact:
            return
        
        # Do not make beeps if character is mute
        if char.muted:
            return

        beep_audio = char.bleep_dict[char.voice_mode]

        if event == 'begin':
            renpy.sound.play('<silence 0.05>', channel='bleeps', loop=True) # Brief silence so that the continue sound can be heard
        if event == "show_done":
            renpy.sound.queue(beep_audio, channel='bleeps', loop=True)
        elif event == "slow_done":
            renpy.sound.stop(channel='bleeps')
        elif event =='end':
            renpy.sound.stop(channel='bleeps')
