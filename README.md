# Delivery Scheduler App

A Python GUI application for optimizing delivery task scheduling across multiple vehicles using tkinter.

## Features

- **Task Management**: Add delivery tasks with processing time and deadline
- **Smart Scheduling**: Automatically assigns tasks to vehicles based on:
  - Deadline constraints
  - Profit-to-time ratio optimization
  - Vehicle availability
- **Visual Interface**: Clean, dark-themed GUI with task overview
- **Multi-Vehicle Support**: Supports up to 30 vehicles
- **Profit Calculation**: Automatic profit calculation (Processing Time × ₨10)

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- For Linux users: `sudo apt install python3-tk`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/areekaraza/DeliveryScheduler.git
   cd DeliveryScheduler
   ```

2. Install required dependencies (if needed):
   ```bash
   # On Ubuntu/Debian
   sudo apt install python3-tk
   ```

## Usage

1. Run the application:
   ```bash
   python3 DeliverySchedulerApp.py
   ```

2. Add tasks by entering:
   - Processing Time (hours)
   - Deadline (hours)
   - Click "Add Task"

3. Click "Schedule Tasks" to see optimal vehicle assignments

## How It Works

The application uses a greedy algorithm that:
1. Sorts tasks by deadline (earliest first)
2. Prioritizes tasks with higher profit-to-time ratios
3. Assigns tasks to available vehicles while respecting deadline constraints

## Task Validation

- Processing time and deadline must be greater than 0
- Deadline cannot be less than processing time
- All inputs must be valid integers

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Author

Created by Areeka Raza

## Acknowledgments

- Built with Python's tkinter library
- Implements greedy scheduling algorithm for task optimization
