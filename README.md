![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

# Port Management Simulation System

A Python-based simulation of a port management system that models truck cargo unloading and ship loading operations using object-oriented programming, CSV data processing, and heap queue scheduling.

## Features

- **Truck queue management** -- reads truck data from CSV and queues them using a min-heap
- **Ship queue management** -- reads ship data from CSV and queues them by ship number
- **Cargo unloading simulation** -- trucks arrive at the port and unload cargo into the staging area
- **Ship loading simulation** -- cargo from the staging area is loaded onto ships bound for matching destinations
- **Priority scheduling** -- heap queue ensures trucks and ships are processed in sorted order

## Tech Stack

| Component | Purpose |
|-----------|---------|
| **Python 3** | Core language |
| **OOP** | Class-based architecture (`Truck`, `Ship`, `Port`) |
| **csv** | Reading truck and ship data from CSV files |
| **heapq** | Min-heap priority queue for scheduling |

## Architecture

### Truck (`Tir`)

Represents a truck arriving at the port.

- `__init__(self, plate, country, twenty_ton, thirty_ton, cost)` -- initializes the truck with its license plate, origin country, container counts, and transport cost.
- `__lt__(self, other)` -- comparison method for heap ordering by license plate.

### Ship (`Gemi`)

Represents a cargo ship docked at the port.

- `__init__(self, number, capacity, destination_country)` -- initializes the ship with its ID number, cargo capacity, and destination country.
- `__lt__(self, other)` -- comparison method for heap ordering by ship number.

### Port (`Liman`)

Manages all port operations and orchestrates the simulation.

- `__init__(self)` -- initializes the port with empty queues and staging area.
- `read_truck_data(self)` -- reads truck records from `olaylar.csv` and enqueues them.
- `read_ship_data(self)` -- reads ship records from `gemiler.csv` and enqueues them.
- `unload_truck_cargo(self)` -- dequeues trucks, places cargo in the staging area.
- `load_ship_cargo(self)` -- loads staged cargo onto ships and tracks departures.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yavuzhankursun/Python-Liman-Otomasyon-Sistemi.git
   cd Python-Liman-Otomasyon-Sistemi
   ```
2. Make sure Python 3 is installed. If not, download it from [python.org](https://www.python.org/downloads/).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The simulation reads data from `olaylar.csv` (truck events) and `gemiler.csv` (ships), then runs the full port workflow:

```bash
python main.py
```
