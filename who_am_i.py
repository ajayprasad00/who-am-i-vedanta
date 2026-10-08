"""
WHO AM I? - A guided inquiry based on Advaita Vedanta.

Not a scientific proof. A philosophical walk-through of the
central ideas of the Upanishadic / Advaita tradition.

Run:  python who_am_i.py
"""

import sys
from textwrap import dedent

WIDTH = 70

# Each section: (title, text, optional reflection question)
SECTIONS = [
    ("Am I the Body?", """
        I can say "this is my body".
        The body changes: childhood, youth, old age.
        Cells, appearance and strength all change.
        Yet a continuous sense of "I" seems to remain.

        The body is something I experience. It is "my body".
        Can it be the complete meaning of "I"?
     """, "Which part of you is the same as it was ten years ago?"),

    ("Am I the Mind?", """
        Thoughts, emotions, desires and memories appear and disappear.
        Fear comes and goes. Happiness comes and goes.

        I say "my thoughts", "my emotions", "my mind".
        These are things I experience, so the changing contents of
        the mind cannot simply be the whole meaning of "I".
     """, "Watch your next thought arrive. Who noticed it?"),

    ("Am I the Intellect?", """
        The intellect understands, compares, decides, and revises.
        Yesterday I believed one thing; today I may see it differently.

        Even the intellect can be observed and known.

        If body, thoughts, emotions and intellect are all known...
        WHO is the knower?
     """, None),

    ("The Witness", """
        Everything that changes can be observed.

            The changing is the object of experience.
            The knower of the changing is the Witness.

        In Vedanta this witnessing principle is called ATMAN.
        Atman is not another object to be seen.
        It is that by which experience is known.
     """, None),

    ("Consciousness", """
        A sound is known. A sight is known. A thought is known.
        Without awareness, none of these could be experienced.

        Consciousness is not one more object inside experience.
        It is the condition of knowing.

        Advaita calls it self-luminous: it does not need another
        consciousness to reveal it, the way an object needs a knower.

        (Debated point: Buddhist traditions question whether any
        such abiding self is found in experience.)
     """, "Can you find awareness as an object? Or only as the one aware?"),

    ("The Dream Analogy", """
        In a dream, a whole world appears: people, places, events,
        fear, happiness, even time.

        When the dream ends, it is recognised as an experience that
        appeared in consciousness.

        This does NOT claim the waking world is literally a dream.
        The question is only:

            In what does every experience appear?

        Advaita's answer: Consciousness.
     """, None),

    ("Space and Time", """
        We say "I exist in space and time".
        But space and time are themselves experienced.

        So Vedanta asks whether Consciousness is merely another
        object located inside space and time.

        The body has a birth. The Self, according to the Upanishadic
        teaching (shruti), is unborn.

        Note: this is a scriptural claim, not a logical proof.
     """, None),

    ("What About Death?", """
        The body is born, grows, ages and dies.

        The Vedantic question: is the Witness itself an object that
        is born and dies?

        The Upanishads answer: the Atman is unborn and imperishable.
        Birth and death belong to the body and the life-process,
        not to the ultimate Self.
     """, None),

    ("One Consciousness, Many People?", """
        There are many bodies, minds, personalities and memories.
        Advaita does not deny this empirical diversity.

        The claim is that fundamental Consciousness is not divided
        just because many minds appear.

            One sun, many windows.

        This does NOT mean all minds share the same memories.

        Other Vedanta schools (Dvaita, Vishishtadvaita) read this
        differently. They keep individual selves distinct from Brahman.
     """, None),

    ("Why Do I Think I Am Only the Body?", """
        If my deepest nature is Consciousness, why do I think:
        "I am this body", "I am the doer", "I am the sufferer"?

        Vedanta calls this basic error AVIDYA.

        It is not lack of information. It is mistaken identification:
        taking the changing to be the Self and overlooking the
        unchanging ground of awareness.
     """, None),

    ("The Rope and the Snake", """
        In darkness, a rope is mistaken for a snake.
        The fear is real, but the snake is not.

        The solution is not to fight the snake.
        The solution is to know the rope.

        Likewise, liberation is not destroying the world.
        It is removing mistaken identification through knowledge.
     """, None),

    ("The Ego", """
        The ego says: "I am the thinker, the doer, the experiencer.
        I must gain. I must avoid loss."

        It is a functional centre of individual experience.

        But if the ego itself can be observed,
        it cannot be the final Witness.
     """, "Can you observe your own ego in action today?"),

    ("The Atman", """
        The inquiry has moved:

            body -> mind -> thoughts -> emotions
                 -> intellect -> ego -> Witnessing Consciousness

        The deepest Self is ATMAN.
        Not a personality. Not a thought. Not an image of oneself.
        The innermost Self, understood as pure Consciousness.
     """, None),

    ("Brahman", """
        The Upanishads investigate the ultimate reality behind all
        changing names and forms. That reality is BRAHMAN.

        In Advaita, Brahman is non-dual ultimate reality, not just a
        powerful object inside the universe.

        The Mahavakyas point to it:

            Prajnanam Brahma   - Consciousness is Brahman
            Aham Brahmasmi     - I am Brahman
            Tat Tvam Asi       - That thou art
            Ayam Atma Brahma   - This Self is Brahman
     """, None),

    ("The Great Recognition", """
        The questions change:

            "Where is God?"
            "What is Consciousness?"
            "Who is aware of my body and mind?"
            "Who am I?"

        The inquiry reaches: the deepest Self is not separate from
        Brahman.

        This does not mean the individual ego created the universe.
        It means the Self's ultimate nature is non-different from
        ultimate reality.
     """, None),

    ("Karma and the Individual", """
        While I identify as a separate doer and experiencer,
        action and consequence keep turning:

            Identification -> "I am the doer" -> Action
            -> Consequence -> Desire / aversion -> Further action

        Merely repeating "I am Brahman" does not erase this.
        The knowledge must become clear and steady.
     """, None),

    ("How Does Ignorance End?", """
        The traditional process:

            Viveka        - discrimination: eternal vs changing
            Vairagya      - freedom from excess dependence on objects
            Shravana      - listening to the teaching
            Manana        - reasoning, removing doubts
            Nididhyasana  - steady contemplation and assimilation

        The Self is not manufactured. It is already what it is.
        Knowledge only removes the mistaken identification.
     """, None),

    ("Liberation (Moksha)", """
        Moksha is not travelling to a place.
        It is freedom from fundamental ignorance.

        Body and mind continue to function. Life goes on.
        But the conclusion changes from

            "I am only this limited body-mind"
        to
            "My deepest nature is the witnessing Consciousness,
             which Advaita holds to be non-different from Brahman."
     """, None),

    ("The Final Question", """
        So... who am I?

        Not merely the body, senses, thoughts, emotions,
        intellect or ego.

        I am the Consciousness in whose presence all of these
        are known.

            ATMAN IS BRAHMAN.
     """, None),

    ("The Search Comes Full Circle", """
        The seeker searched in the world, in knowledge, in philosophy,
        for God, for Consciousness.

        Finally he turned toward the one who was searching.

        The Self was never an object waiting to be found.
        The journey was not from one place to another.
        It was a movement from ignorance to recognition.
     """, None),
]

FINAL_TEXT = """
    I AM NOT MERELY WHAT I EXPERIENCE.
    I AM THAT BY WHICH EXPERIENCE IS KNOWN.

    The body, mind, thoughts, emotions and personality change.
    The fact of awareness remains the ground of every experience.

    Vedanta calls this deepest Self ATMAN, and Advaita points to
    the identity:

                    ATMAN = BRAHMAN

    The discovery is not "I, the ego, have become God."
    It is "The ego was never the ultimate Self."

    Liberation is not acquiring something new.
    It is freedom from the ignorance that made the Self
    look like something else.

                    Tat Tvam Asi.
                    Aham Brahmasmi.
"""


def banner(text: str) -> None:
    print("\n" + "=" * WIDTH)
    print(text.upper().center(WIDTH))
    print("=" * WIDTH)


def show_section(index: int, total: int, title: str, text: str) -> None:
    banner(f"[{index}/{total}] {title}")
    print(dedent(text).rstrip())


def reflect(question: str) -> None:
    print(f"\n  >> Pause and reflect: {question}")
    input("     (Take a moment, then press Enter) ")


def wait() -> None:
    input("\nPress Enter to continue...")


def run() -> None:
    banner("Who Am I?")
    print(dedent("""
        This is not a scientific proof of Vedanta.
        It is a philosophical journey through the central insights
        of the Upanishadic and Advaita Vedanta tradition.

        It begins with one question:  WHO AM I?
    """))
    input("Press Enter to begin...")

    total = len(SECTIONS)
    for i, (title, text, question) in enumerate(SECTIONS, start=1):
        show_section(i, total, title, text)
        if question:
            reflect(question)
        wait()

    banner("Final Output")
    print(dedent(FINAL_TEXT))
    banner("End of the Inquiry")


def main() -> None:
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print("\n\nInquiry paused. Return whenever you like.")
        sys.exit(0)


if __name__ == "__main__":
    main()
