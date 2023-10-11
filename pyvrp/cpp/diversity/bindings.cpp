/**
 * MIT License
 * 
 * Copyright (c) 2020, Thibaut Vidal (HGS-CVRP)
 * Copyright (c) 2022, ORTEC (HGS-DIMACS)
 * Copyright (c) since 2022, PyVRP contributors
 */
#include "diversity.h"
#include "diversity_docs.h"

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_diversity, m)
{
    m.def("broken_pairs_distance",
          &pyvrp::diversity::brokenPairsDistance,
          py::arg("first"),
          py::arg("second"),
          DOC(pyvrp, diversity, brokenPairsDistance));
}
