# Copyright (C) 12/3/20 RW Bunney

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Contains the specifications and details for the hardware used in Pawsey's "Galaxy"
HPC facility. 
https://www.microway.com/knowledge-center-articles/detailed-specifications-intel-xeon-e5-2600v3-haswell-ep-processors/
Based on the above link, the Galaxy Ivy Bridge has 8FLOPs/Cycle
"""

from utils.constants import SI
from utils.classes import CPU_NODE, GPU_NODE


class PawseyGalaxy:

	XeonSandyBridge = CPU_NODE(
		cores=8,
		flops_per_cycle=8,
		ncycles=2.6 * SI.giga,
		bandwidth=1600 * SI.mega
	)  # ~240 giga flops

	XeonIvyBridge = CPU_NODE(  # Total flops ~ 480 gigaflops
		cores=10,
		flops_per_cycle=16,
		ncycles=3.0 * SI.giga,  # frequency e.g. 2.2GHz
		bandwidth=1866 * SI.mega  # megaherz
	)

	NvidiaKepler = GPU_NODE(
		memory=6 * SI.giga,
		memory_bandwidth=1300 * SI.mega,
		single_pflops=3.95 * SI.tera,
		double_pflops=1.3 * SI.tera,
		cuda_cores=2688
	)
	memory_per_cpu_node = 64
	memory_per_gpu_node = 32
	cpu_architecture = [
		(XeonIvyBridge, 50),
		(XeonSandyBridge, 100),
		(NvidiaKepler, 64)
	]
