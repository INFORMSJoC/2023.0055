/**
 * MIT License
 * 
 * Copyright (c) 2020, Thibaut Vidal (HGS-CVRP)
 * Copyright (c) 2022, ORTEC (HGS-DIMACS)
 * Copyright (c) since 2022, PyVRP contributors
 */
#include "crossover.h"
#include "crossover_docs.h"

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_crossover, m)
{
    m.def("selective_route_exchange",
          &pyvrp::crossover::selectiveRouteExchange,
          py::arg("parents"),
          py::arg("data"),
          py::arg("cost_evaluator"),
          py::arg("start_indices"),
          py::arg("num_moved_routes"),
          DOC(pyvrp, crossover, selectiveRouteExchange));
}
