#!/usr/bin/env python3
import tcod
from engine import *
from input_handlers import EventHandler
from entity import Entity
from colors import *
from game_map import *


def main() -> None: 
    print("\n\nWelcome traveller!\n\n")
    # Setting up the initial variables, like screen size and the tileset.
    color = Color()

    # Screen resolution
    screen_w = 80
    screen_h = 50
    
    # Map size
    map_w = 80
    map_h = 45

    tileset = tcod.tileset.load_tilesheet("Game1/basic_symbols.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    # Creating the entities
    player = Entity(int(screen_w / 2), int(screen_h / 2), "@", color.green_lime)
    npc = Entity(int(screen_w / 2 - 5), int(screen_h / 2), "@", color.orange_gold)
    entities = {player, npc}

    game_map = GameMap(map_w, map_h)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # Game window
    with tcod.context.new_terminal(
        screen_w,
        screen_h,
        tileset=tileset,
        title="The Lonely Traveller",
        vsync=False,
    ) as context:
        root_console = tcod.console.Console(screen_w, screen_h, order="F")

        while True: # Game loop
            # Drawing the screen and everything on it.
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            
            engine.handle_events(events)


if __name__ == "__main__":
    main()
    
