from typing import Callable, Iterator, List, Tuple, Union, overload

class CostEvaluator:
    def __init__(
        self, capacity_penalty: int = 0, tw_penalty: int = 0
    ) -> None: ...
    def load_penalty(self, load: int, capacity: int) -> int: ...
    def tw_penalty(self, time_warp: int) -> int: ...
    def penalised_cost(self, solution: Solution) -> int: ...
    def cost(self, solution: Solution) -> int: ...

class DynamicBitset:
    def __init__(self, num_bits: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def count(self) -> int: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx: int) -> bool: ...
    def __setitem__(self, idx: int, value: bool) -> None: ...
    def __or__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __and__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __xor__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __invert__(self) -> DynamicBitset: ...

class Matrix:
    @overload
    def __init__(self, dimension: int) -> None: ...
    @overload
    def __init__(self, n_rows: int, n_cols: int) -> None: ...
    @overload
    def __init__(self, data: List[List[int]]) -> None: ...
    @property
    def num_cols(self) -> int: ...
    @property
    def num_rows(self) -> int: ...
    def max(self) -> int: ...
    def size(self) -> int: ...
    def __getitem__(self, idx: Tuple[int, int]) -> int: ...
    def __setitem__(self, idx: Tuple[int, int], value: int) -> None: ...

class Client:
    x: int
    y: int
    demand: int
    service_duration: int
    tw_early: int
    tw_late: int
    release_time: int
    prize: int
    required: bool
    def __init__(
        self,
        x: int,
        y: int,
        demand: int = 0,
        service_duration: int = 0,
        tw_early: int = 0,
        tw_late: int = 0,
        release_time: int = 0,
        prize: int = 0,
        required: bool = True,
    ) -> None: ...

class VehicleType:
    capacity: int
    num_available: int
    depot: int
    def __init__(self, capacity: int, num_available: int) -> None: ...

class ProblemData:
    def __init__(
        self,
        clients: List[Client],
        vehicle_types: List[VehicleType],
        distance_matrix: List[List[int]],
        duration_matrix: List[List[int]],
    ) -> None: ...
    def client(self, client: int) -> Client: ...
    def centroid(self) -> Tuple[float, float]: ...
    def vehicle_type(self, vehicle_type: int) -> VehicleType: ...
    def dist(self, first: int, second: int) -> int: ...
    def duration(self, first: int, second: int) -> int: ...
    @property
    def num_clients(self) -> int: ...
    @property
    def num_vehicles(self) -> int: ...
    @property
    def num_vehicle_types(self) -> int: ...

class Route:
    def __init__(
        self, data: ProblemData, visits: List[int], vehicle_type: int
    ) -> None: ...
    def __getitem__(self, idx: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def is_feasible(self) -> bool: ...
    def has_excess_load(self) -> bool: ...
    def has_time_warp(self) -> bool: ...
    def demand(self) -> int: ...
    def excess_load(self) -> int: ...
    def distance(self) -> int: ...
    def duration(self) -> int: ...
    def visits(self) -> List[int]: ...
    def time_warp(self) -> int: ...
    def start_time(self) -> int: ...
    def end_time(self) -> int: ...
    def slack(self) -> int: ...
    def service_duration(self) -> int: ...
    def travel_duration(self) -> int: ...
    def wait_duration(self) -> int: ...
    def release_time(self) -> int: ...
    def prizes(self) -> int: ...
    def centroid(self) -> Tuple[float, float]: ...
    def vehicle_type(self) -> int: ...

class Solution:
    def __init__(
        self,
        data: ProblemData,
        routes: Union[List[Route], List[List[int]]],
    ) -> None: ...
    @classmethod
    def make_random(
        cls, data: ProblemData, rng: RandomNumberGenerator
    ) -> Solution: ...
    def get_neighbours(self) -> List[Tuple[int, int]]: ...
    def get_routes(self) -> List[Route]: ...
    def has_excess_load(self) -> bool: ...
    def has_time_warp(self) -> bool: ...
    def distance(self) -> int: ...
    def excess_load(self) -> int: ...
    def time_warp(self) -> int: ...
    def prizes(self) -> int: ...
    def uncollected_prizes(self) -> int: ...
    def is_feasible(self) -> bool: ...
    def is_complete(self) -> bool: ...
    def num_routes(self) -> int: ...
    def num_clients(self) -> int: ...
    def __copy__(self) -> Solution: ...
    def __deepcopy__(self, memo: dict) -> Solution: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

class PopulationParams:
    generation_size: int
    lb_diversity: float
    min_pop_size: int
    nb_close: int
    nb_elite: int
    ub_diversity: float
    def __init__(
        self,
        min_pop_size: int = 25,
        generation_size: int = 40,
        nb_elite: int = 4,
        nb_close: int = 5,
        lb_diversity: float = 0.1,
        ub_diversity: float = 0.5,
    ) -> None: ...
    @property
    def max_pop_size(self) -> int: ...

class SubPopulation:
    def __init__(
        self,
        diversity_op: Callable[[Solution, Solution], float],
        params: PopulationParams,
    ) -> None: ...
    def add(
        self, solution: Solution, cost_evaluator: CostEvaluator
    ) -> None: ...
    def purge(self, cost_evaluator: CostEvaluator) -> None: ...
    def update_fitness(self, cost_evaluator: CostEvaluator) -> None: ...
    def __getitem__(self, idx: int) -> SubPopulationItem: ...
    def __iter__(self) -> Iterator[SubPopulationItem]: ...
    def __len__(self) -> int: ...

class SubPopulationItem:
    @property
    def fitness(self) -> float: ...
    @property
    def solution(self) -> Solution: ...
    def avg_distance_closest(self) -> float: ...

class TimeWindowSegment:
    def __init__(
        self,
        idx_first: int,
        idx_last: int,
        duration: int,
        time_warp: int,
        tw_early: int,
        tw_late: int,
        release_time: int,
    ) -> None: ...
    @overload
    @staticmethod
    def merge(
        duration_matrix: Matrix,
        first: TimeWindowSegment,
        second: TimeWindowSegment,
    ) -> TimeWindowSegment: ...
    @overload
    @staticmethod
    def merge(
        duration_matrix: Matrix,
        first: TimeWindowSegment,
        second: TimeWindowSegment,
        third: TimeWindowSegment,
    ) -> TimeWindowSegment: ...
    def total_time_warp(self) -> int: ...

class RandomNumberGenerator:
    def __init__(self, seed: int) -> None: ...
    @staticmethod
    def max() -> int: ...
    @staticmethod
    def min() -> int: ...
    def rand(self) -> float: ...
    def randint(self, high: int) -> int: ...
    def __call__(self) -> int: ...
