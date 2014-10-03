#-*- coding: utf-8 -*-
# portage.py
# Module to work with portage package manager class
#
# Copyright (C) 2013 Jakub Kadlčík
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from __future__ import absolute_import
from .ipackageManager import IPackageManager
from tracer.resources.package import Package
from gentoolkit.helpers import FileOwner
from psutil import AccessDenied
import tracer.resources.memory as Memory
import os
import portage
import subprocess
import time


class Portage(IPackageManager):

	"""
	Package manager class - Portage
	"""

	# noinspection PyMissingConstructor
	def __init__(self):
		pass

	def packages_newer_than(self, unix_time):
		"""
		Returns list of packages which were modified between unix_time and present
		Requires root permissions.
		"""

		if not os.access('/var/log/emerge.log', os.R_OK):
			raise AccessDenied

		newer = []
		process = subprocess.Popen(['qlop', '-lC'], stdout=subprocess.PIPE)
		packages = process.communicate()[0]
		for package in packages.split('\n')[:-1]:
			package = package.split(" >>> ")

			# There actually should be %e instead of %d
			modified = time.mktime(time.strptime(package[0], "%a %b %d %H:%M:%S %Y"))
			if modified >= unix_time:
				pkg_name = package[1] # Package name with version, let's cut it off
				pkg_name = self._pkg_name_without_version(pkg_name)
				newer.append(Package(pkg_name, modified))

		return newer

	def package_files(self, pkg_name):
		"""Returns list of files provided by package"""
		vartree = portage.db[portage.root]['vartree']
		cpv = str(vartree.dep_bestmatch(pkg_name))

		contents = vartree.dbapi.aux_get(cpv, ['CONTENTS'])[0].split('\n')[:-1]
		return [x.split()[1] for x in contents]

	def package_info(self, app_name):
		"""Returns package object with all attributes"""
		description = None
		name = self.provided_by(app_name)
		if not name:
			return None

		category = name.split('/')[0]
		process = subprocess.Popen(['eix', '-e', name], stdout=subprocess.PIPE)
		out = process.communicate()[0]
		out = out.split('\n')

		for line in out:
			line = line.strip()
			if line.startswith("Description:"):
				description = line.split("Description:")[1].strip()

		package = Package(name)
		package.description = description
		package.category = category
		return package

	def provided_by(self, app_name):
		"""Returns name of package which provides given application"""
		process = Memory.processes_by_name(app_name)[0]  # @TODO Reimplement for all processes
		package = self._file_provided_by(process.exe)
		if package:
			if package.category == 'dev-lang':
				for arg in process.cmdline[1:]:
					if os.path.isfile(arg):
						package = self._file_provided_by(arg)
						return package.name if package else None
			return package.name
		return None

	def _file_provided_by(self, file):
		find_owner = FileOwner(early_out=True)
		packages = find_owner([file])
		if packages:
			package = packages[0][0]
			name = package.category + '/' + package.name
			p = Package(name)
			p.category = package.category
			return p
		return None
