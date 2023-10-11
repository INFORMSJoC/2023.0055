/**
 * MIT License
 * 
 * Copyright (c) 2020, Thibaut Vidal (HGS-CVRP)
 * Copyright (c) 2022, ORTEC (HGS-DIMACS)
 * Copyright (c) since 2022, PyVRP contributors
 */
#include "CostEvaluator.h"

using pyvrp::Cost;
using pyvrp::CostEvaluator;

CostEvaluator::CostEvaluator(Cost capacityPenalty, Cost timeWarpPenalty)
    : capacityPenalty(capacityPenalty), timeWarpPenalty(timeWarpPenalty)
{
}
