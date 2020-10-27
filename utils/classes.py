# Copyright (C) 2020 RW Bunney

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


class CPU_NODE:
	def __init__(self, cores, flops_per_cycle, ncycles, bandwidth):
		self.cores = cores
		self.flops_per_cycle = flops_per_cycle
		self.ncyles = ncycles
		self.bandwidth = bandwidth


class GPU_NODE:
	def __init__(self, memory, memory_bandwidth, single_pflops, double_pflops, cuda_cores):
		self.memory = memory
		self.memory_bandwidth = memory_bandwidth
		self.single_pflops = single_pflops
		self.double_pflops = double_pflops
		self.cuda_cores = cuda_cores
