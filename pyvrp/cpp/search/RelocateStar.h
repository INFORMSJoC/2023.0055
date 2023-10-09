/**
 * MIT License
 * 
 * Copyright (c) 2020, Thibaut Vidal (HGS-CVRP)
 * Copyright (c) 2022, ORTEC (HGS-DIMACS)
 * Copyright (c) since 2022, PyVRP contributors
 */
#ifndef PYVRP_RELOCATESTAR_H
#define PYVRP_RELOCATESTAR_H

#include "Exchange.h"
#include "LocalSearchOperator.h"

namespace pyvrp::search
{
/**
 * Performs the best (1, 0)-exchange move between routes U and V. Tests both
 * ways: from U to V, and from V to U.
 */
class RelocateStar : public LocalSearchOperator<Route>
{
    struct Move
    {
        Cost deltaCost = 0;
        Route::Node *from = nullptr;
        Route::Node *to = nullptr;
    };

    Exchange<1, 0> relocate;
    Move move;

public:
    Cost
    evaluate(Route *U, Route *V, CostEvaluator const &costEvaluator) override;

    void apply(Route *U, Route *V) const override;

    RelocateStar(ProblemData const &data)
        : LocalSearchOperator<Route>(data), relocate(data)
    {
    }
};
}  // namespace pyvrp::search

#endif  // PYVRP_RELOCATESTAR_H
