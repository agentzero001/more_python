from sc2.bot_ai import BotAI  
from sc2.data import Difficulty, Race
from sc2.player import Bot, Computer  
from sc2 import maps  # maps method for loading maps to play in.
from sc2.ids.unit_typeid import UnitTypeId as ut
import sc2
import time

class MyBot(BotAI):
    
    def __init__(self):
        BotAI.__init__(self)
        #self.scout = 0

    async def on_step(self, iteration: int):
        await self.build_workers()
        await self.distribute_workers()
        await self.build_pylons()
        await self.build_assimilators()
        
        time.sleep(1)
        
    async def build_assimilators(self):
        for nexus in self.units(ut.NEXUS):
            vaspenes = self.state.vespene_geyser.closer_than(10.0, nexus)
            for vaspene in vaspenes:
                if not self.can_afford(ut.ASSIMILATOR):
                    break
                worker = self.select_build_worker(vaspene.position)
                if worker is None:
                    break
                if not self.units(ut.ASSIMILATOR).closer_than(1.0, vaspene).exists:
                    await self.do(worker.build(ut.ASSIMILATOR, vaspene))
                
                
        
    async def scout(self):
            pass
        
        # if not self.units(ut.NEXUS).exists:
        #     for worker in self.workers:
        #         await self.do(worker.attack(self.enemy_start_locations[0]))
        #     return
        # else:
        #     nexus = self.units(ut.NEXUS).first
            
        # if self.scout == 0:    
        #     scout_probe = self.workers.random
        #     await self.do(scout_probe.move(self.enemy_start_locations[0]))
        # # if scout_probe.position.distance_to(self.enemy_start_locations[0]) < 10:   
        #     await self.do(scout_probe.move(self.enemy_start_locations[1]))
            
    async def build_workers(self):
        for nexuses in self.units(ut.NEXUS).ready.noqueue:    #build and not producing
            if self.can_afford(ut.PROBE):
                await self.do(nexuses.train(ut.PROBE))
                
    async def build_pylons(self):
        if self.supply_left < 5 and not self.already_pending(ut.PYLON):
            nexuses = self.units(ut.NEXUS).ready
            if nexuses.exists:
                if self.can_afford(ut.PYLON):
                    await self.build(ut.PYLON, near=nexuses.first)
               
    
        
        
        print(self.supply_cap)       
        # print(f"{iteration}, n_workers: {self.workers.amount}, n_idle_workers: {self.workers.idle.amount},", \
		# 	f"minerals: {self.minerals}, gas: {self.vespene}, cannons: {self.units(ut.PHOTONCANNON).amount}," \
		# 	f"pylons: {self.units(ut.PYLON).amount}, nexus: {self.units(ut.NEXUS).amount}", \
		# 	f"gateways: {self.units(ut.GATEWAY).amount}, cybernetics cores: {self.units(ut.CYBERNETICSCORE).amount}", \
		# 	f"stargates: {self.units(ut.STARGATE).amount}, voidrays: {self.units(ut.VOIDRAY).amount}, supply: {self.supply_used}/{self.supply_cap}")
        
        
       
sc2.run_game(
    sc2.maps.get("Flat48"),
    [Bot(sc2.Race.Protoss, MyBot()), Computer(sc2.Race.Zerg, sc2.Difficulty.Hard)],
    realtime=True,
    game_time_limit=1800
)
