from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    max_width: int = 1400
    canny_low: int = 50
    canny_high: int = 150
    approx_epsilon_ratio: float = 0.02
    min_contour_area_ratio: float = 0.12
    adaptive_block_size: int = 31
    adaptive_c: int = 11
