# Subnet Identifier GUI

A Python-based subnet identifier with a graphical user interface (GUI) using Tkinter. This application allows users to calculate subnet information, split networks into subnets by prefix or by required number of hosts, and export the results to a CSV file. It supports both IPv4 and IPv6 networks.

## Features

* Calculate subnet information:

  * Network ID
  * Broadcast address
  * Subnet mask
  * First host
  * Last host
  * Total addresses
  * Usable hosts
* Split a network into smaller subnets by CIDR prefix.
* Calculate subnets based on the required number of hosts.
* Export subnet information to CSV.
* Clean GUI using Tkinter with a scrollable TreeView for output.
* MVC architecture for maintainable and extensible code.

## Project Structure

```
project/
│── main.py            # Application entry point
│── ui.py              # GUI layout
│── controller.py      # Application logic and event handling
│── subnet_logic.py    # Subnet calculations and CSV export
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/donmalya-tech/Subnet-Identfier.git
   cd Subnet-Identifier
   ```

2. Make sure you have Python 3.8+ installed.

3. Install any dependencies (Tkinter is included in standard Python):

   ```bash
   pip install -r requirements.txt  # Optional if you add extra packages
   ```

## Usage

Run the application:

```bash
python App.py
```

### How to Use

1. Enter the IP address and prefix.
2. Choose a new prefix or enter the number of required hosts.
3. Select the mode: `By Prefix` or `By Hosts`.
4. Click **Subnet Info** to see basic information.
5. Click **Calculate Subnets** to list all subnets.
6. Click **Export CSV** to save results.

## Screenshots
<img width="696" height="527" alt="image" src="https://github.com/user-attachments/assets/543c5078-984b-482c-b4c7-b6411fdde4a1" />

<img width="693" height="524" alt="image" src="https://github.com/user-attachments/assets/ce9d5fdc-20cf-441c-8e46-e74c140f9bd1" />


## Author

https://github.com/donmalya-tech
