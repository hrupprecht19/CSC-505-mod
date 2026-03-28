"""developer_builder.py

Defines a Developer builder that collects traits and prints a formatted summary.
It randomly selects 3 traits from a predefined list.
Example output:
Brief Description: This program outlines the key steps required to build an excellent software engineer with specific personality traits.
Loading traits for developer...
Trait 1 loading...
Trait: Restorative - Excellent at problem-solving, immediately noticing what isn't working and persistent in resolving issues.
Trait 2 loading...
Trait: Analytical - Driven by a need for data and logic to find the root causes of problems, rather than simply accepting assumptions.
Trait 3 loading...
Trait: Achiever - Works hard, possesses a great deal of stamina, and takes satisfaction in being productive and busy.
Total traits included: 3

The traits are based on concepts from StrengthsFinder 2.0 by Tom Rath.
  References
 Rath, T. (2007). StrengthsFinder 2.0. Gallup Press.

"""

import time
import random
from typing import Dict

class Developer:
    def __init__(self):
        self.traits: Dict[str, str] = {}

    def add_trait(self, name: str, description: str) -> "Developer":
        """Add a trait to the developer and return self for fluent chaining."""
        self.traits[name] = description
        return self

    def build(self) -> "Developer":
        """Return the built developer object (keeps fluent API semantics)."""
        return self

    def display_traits(self) -> None:
        print("Building your ideal developer...")
        for name, description in self.traits.items():
            print(f"Trait: {name} - {description}")
        print(f"Total traits included: {len(self.traits)}")

    def display_traits_with_loading(self, delay: float = 1.0) -> None:
        """Display a brief description, then load each trait with a short delay and show descriptions."""
        print("Brief Description: This program outlines the key steps required to build an excellent software engineer with specific personality traits.\n")
        try:
            print("Loading traits for developer...")
            for idx, (name, description) in enumerate(self.traits.items(), start=1):
                print(f"Trait {idx} loading...")
                time.sleep(delay)
                print(f"Trait: {name} - {description}\n")
            print(f"Total traits included: {len(self.traits)}")
        except KeyboardInterrupt:
            print("\nLoading interrupted by user.")
        print()


if __name__ == "__main__":
    # Define available traits and pick 3 at random
    ALL_TRAITS = {
        "Restorative": "Excellent at problem-solving, immediately noticing what isn't working and persistent in resolving issues.",
        "Analytical": "Driven by a need for data and logic to find the root causes of problems, rather than simply accepting assumptions.",
        "Achiever": "Works hard, possesses a great deal of stamina, and takes satisfaction in being productive and busy.",
        "Empathy": "Understanding others' perspectives and considering their feelings in team settings.",
        "Learner": "Knowledge acquisition and adaptability and curiosity, deep dives."
    }

    selected = random.sample(list(ALL_TRAITS.items()), 3)
    dev = Developer()
    for name, desc in selected:
        dev.add_trait(name, desc)
    dev = dev.build()

    print("Selected traits:", ", ".join(name for name, _ in selected))

    # Show traits with a loading effect (0.8s between each by default)
    dev.display_traits_with_loading(delay=0.8)

    def display_developer_ascii() -> None:
        """Print ASCII-art developer."""
        ascii_man = r"""
          _
         /_\
        (o_o)
         /|\
         / \
        (developer)
        """
        print("\nShowing developer ASCII art:\n")
        print(ascii_man)

    # Show ASCII art
    display_developer_ascii()


