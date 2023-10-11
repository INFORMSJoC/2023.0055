/**
 * MIT License
 * 
 * Copyright (c) 2020, Thibaut Vidal (HGS-CVRP)
 * Copyright (c) 2022, ORTEC (HGS-DIMACS)
 * Copyright (c) since 2022, PyVRP contributors
 */
#ifndef PYVRP_MOVETWOCLIENTSREVERSED_H
#define PYVRP_MOVETWOCLIENTSREVERSED_H

#include "LocalSearchOperator.h"

namespace pyvrp::search
{
/**
 * Inserts U -> X after V (as V -> X -> U), if that is an improving move.
 */
class MoveTwoClientsReversed : public LocalSearchOperator<Route::Node>
{
    using LocalSearchOperator::LocalSearchOperator;

public:
    Cost evaluate(Route::Node *U,
                  Route::Node *V,
                  CostEvaluator const &costEvaluator) override;

    void apply(Route::Node *U, Route::Node *V) const override;
};
}  // namespace pyvrp::search

#endif  // PYVRP_MOVETWOCLIENTSREVERSED_H
