# --- CHARACTER & IMAGES ---
define m = Character("Miby", color="#ff6b6b")
define p = Character("You", color="#a5a5a5") # Her internal thoughts

image bg bedroom = "images/bg bedroom.jpg"
image miby dream_shadow = "images/miby dream_shadow.png" # A blurry or shadowy Miby for the dream
image miby waking_up = "images/miby waking_up.png"     # Her real, exhausted face in bed

# --- THE GAME STARTS HERE ---
label start:

    # Start in pitch blackness, slowly drifting into the nightmare
    scene black
    with fade
    
    "..."
    "The air feels heavy. Cold. You are running, but your feet aren't touching the ground."
    "Suddenly, a distorted reflection appears in the dark..."

    # Show her dream version smoothly fading in
    show miby dream_shadow at center
    with dissolve

    m "Ugh, Hahahahahaha... Can you really believe that I lost?! Nah, I won't. Never!"
    
    # The screen shakes violently on this line to show her pain exploding
    m "You can try to hurt me as much as you want, you can think I am dead. You get it?"
    with vpunch
    
    m "I have dead inside."

    m "Yeah I am stupid. Yes I am a silly girl. Yes, and I don't care about that! I am gonna fight back."
    
    m "Yes, you made me like that. Can you remember when we were friends? I always tried to help you, always followed you..." 
    
    m "You know what? I didn't believe that you would do that. Now I am not me anymore."
    
    m "I am not the same girl you knew. I am not the same girl that you fooled and hurt." 
    
    # A dramatic pause before the final sentence of the dream
    show miby dream_shadow at center
    with dissolve
    
    m "Thanks for a lesson. I am not gonna forget that."

    # --- THE AWAKENING ---
    "The darkness starts to collapse. You can't breathe."
    
    # Blinding flash of light as she gasps awake
    scene white
    with flash
    
    "¡Gasp!" with hpunch
    
    # Drop immediately into her real, messy room
    scene bg bedroom
    show miby waking_up at center
    with dissolve
    
    p "(My chest... it feels so tight.)"
    p "(My face is covered in cold sweat. What a horrible, strange feeling...)"
    
    "You look at your hands. They are trembling slightly. The morning sun hasn't even come up yet."
    "The heavy weight of all your school assignments is still waiting for you on your desk."

    p "(Was that just a dream? Or am I still trapped in what they did to me?)"
    
    # This is where your first real choice will happen!
    jump morning_choices