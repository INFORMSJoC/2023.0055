> **Note**
> This static archive described version 0.5.0 of PyVRP, the version that was submitted to INFORMS Journal on Computing.
> Continued development on PyVRP takes place in [the PyVRP repository](https://github.com/PyVRP/PyVRP/), not here!

---

![PyVRP logo](docs/source/assets/images/logo.svg)

PyVRP is an open-source, state-of-the-art vehicle routing problem (VRP) solver.
It currently supports VRPs with:
- Client demands (capacitated VRP);
- Vehicles of different capacities;
- Time windows, client service durations, and release times (VRP with time windows and release times);
- Optional clients with prizes for visiting (prize collecting).

The implementation builds on Thibaut Vidal's [HGS-CVRP][8], but has been completely redesigned to be easy to use as a highly customisable Python package, while maintaining speed and state-of-the-art performance.
Users can customise various aspects of the algorithm using Python, including population management, crossover strategies, granular neighbourhoods and operator selection in the local search.
Additionally, for advanced use cases such as supporting additional VRP variants, users can build and install PyVRP directly from the source code.

PyVRP is available on the Python package index as `pyvrp`.
It may be installed in the usual way as
```
pip install pyvrp
```
This also resolves the few core dependencies PyVRP has.
The documentation is available [here][1].

> If you are new to vehicle routing or metaheuristics, you might benefit from first reading the [introduction to VRP][6] and [introduction to HGS][7] pages.

### Building PyVRP

Ensure you have a Python 3.8 to Python 3.11 installed on your system, along with a recent (C++20-compatible) compiler.
Future versions of Python might also work, but they have not been tested with PyVRP 0.5.0.
Then, install poetry:
```
pip install poetry
```
Thereafter, from the project root, simply run:
```
poetry install --with dev
```
This will install all dependencies from the Python package index, and compile the native extensions.
That could take a little while!
You may verify installation succeeds by typing:
```
poetry run pytest
```
You have a working installation of PyVRP if all tests pass.

### How to cite PyVRP

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs:

- https://doi.org/10.1287/ijoc.2023.0055

- https://doi.org/10.1287/ijoc.2023.0055.cd

Below is the BibTex for citing this snapshot of the respoitory.
```bibtex
@article{CacheTest,
  author =        {Niels A. Wouda and Leon Lan and Wouter Kool},
  publisher =     {INFORMS Journal on Computing},
  title =         {{PyVRP}},
  year =          {2023},
  doi =           {10.1287/ijoc.2023.0055.cd},
  url =           {https://github.com/INFORMSJoC/2023.0055},
}
```

### How to replicate the paper's experiments

Installing PyVRP makes the `pyvrp` script available within the poetry environment.
We use this script to solve benchmark instances from [CVRPLIB](http://vrp.atd-lab.inf.puc-rio.br/), particularly the X instances of Uchoa et al. (2017) [CVRP], and the Homberger and Gehring (1999) instances [VRPTW].
Assuming the `RC1_10_7` VRPTW instance is available in `data/VRPTW`, the `pyvrp` script can be ran as:
```
poetry run pyvrp data/VRPTW/RC1_10_7.txt \
  --seed 1 \ 
  --max_runtime 7200 \
  --round_func dimacs \
  --instance_format solomon
```
Make sure to use the runtimes as explained in the paper, adjusting for CPU performance.

By default, PyVRP is compiled for the VRPTW problem.
Compiling it for CVRP provides some free performance gains since time window checks are no longer needed.
This can be achieved by running:
```
poetry run python build_extensions.py --problem cvrp --build_type release
```
before executing the CVRP benchmarks.
Those can be solved using the following command, assuming the `X-n641-k35` instance is available in `data/CVRP`:
```
poetry run pyvrp data/CVRP/X-n641-k35.vrp \
  --seed 1 \ 
  --max_runtime 1538 \
  --round_func dimacs \
  --instance_format vrplib
```

### Support

If you have questions or run into issues using PyVRP, please [open an issue in our repository](https://github.com/PyVRP/PyVRP/issues).


[1]: https://pyvrp.org/

[2]: https://pyvrp.org/dev/contributing.html

[3]: https://pyvrp.org/setup/getting_help.html

[4]: https://pyvrp.org/examples/basic_vrps.html

[5]: https://pyvrp.org/examples/quick_tutorial.html

[6]: https://pyvrp.org/setup/introduction_to_vrp.html

[7]: https://pyvrp.org/setup/introduction_to_hgs.html

[8]: https://github.com/vidalt/HGS-CVRP/

[9]: https://pyvrp.org/examples/using_pyvrp_components.html
