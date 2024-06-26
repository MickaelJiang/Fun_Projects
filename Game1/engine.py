from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from entity import *
from input_handlers import *
from game_map import * 


"""
Renders map, player, npcs and enemies
"""

class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map
    
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)
            
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console) # Call the GameMap’s render method to draw it to the screen.

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, entity.color)

        context.present(console)

        console.clear()
                