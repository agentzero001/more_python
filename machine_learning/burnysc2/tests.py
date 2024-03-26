from sc2.bot_ai import BotAI  # parent class we inherit from
from sc2.data import Difficulty, Race  # difficulty for bots, race for the 1 of 3 races
from sc2.main import run_game  # function that facilitates actually running the agents in games
from sc2.player import Bot, Computer  #wrapper for whether or not the agent is one of your bots, or a "computer" player
from sc2 import maps  # maps method for loading maps to play in.
from sc2.ids.unit_typeid import UnitTypeId
import sc2

class MyBot(BotAI):
    

    
    def __init__(self):
        BotAI.__init__(self)
        self.scout = True

    
    async def on_step(self, iteration: int):
        # Check if we have enough resources to train a Probe
        if self.can_afford(UnitTypeId.PROBE):
            # Select a random Nexus
            nexus = self.townhalls.random
            # Train a Probe from the selected Nexus
            await self.do(nexus.train(UnitTypeId.PROBE))
            
        if self.scout:
            self.scout_target_index = 0  # Initialize the index for scouting targets
            
            scout_probe = self.workers.random
            target_location = self.enemy_start_locations[self.scout_target_index]
            await self.do(scout_probe.move(target_location))
            
            if scout_probe.position.distance_to(target_location) < 10:
                self.scout_target_index = (self.scout_target_index + 1) % len(self.enemy_start_locations)
                if self.scout_target_index == 0:
                    self.scout = False
                    
            
        #print(self.enemy_start_locations[0])

        
        # print(f"{iteration}, n_workers: {self.workers.amount}, n_idle_workers: {self.workers.idle.amount},", \
		# 	f"minerals: {self.minerals}, gas: {self.vespene}, cannons: {self.units(UnitTypeId.PHOTONCANNON).amount}," \
		# 	f"pylons: {self.units(UnitTypeId.PYLON).amount}, nexus: {self.units(UnitTypeId.NEXUS).amount}", \
		# 	f"gateways: {self.units(UnitTypeId.GATEWAY).amount}, cybernetics cores: {self.units(UnitTypeId.CYBERNETICSCORE).amount}", \
		# 	f"stargates: {self.units(UnitTypeId.STARGATE).amount}, voidrays: {self.units(UnitTypeId.VOIDRAY).amount}, supply: {self.supply_used}/{self.supply_cap}")
        
        
       
sc2.run_game(
    sc2.maps.get("Flat48"),
    [Bot(sc2.Race.Protoss, MyBot()), Computer(sc2.Race.Zerg, sc2.Difficulty.Hard)],
    realtime=True,
    game_time_limit=1800
)
