#-*- coding: utf-8 -*-
# en.py
# English localization module
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

import textwrap

LOCALE = {

	# Global
	"root_only"          : "Only root can use this application",
	"note_unlisted_apps" : "Additionally to those process above, there are:",
	"note_unlisted_apps_short" : "There are:",
	"requires_session"  : "  - {0} processes requiring restart of your session (i.e. Logging out & Logging in again)",
	"requires_reboot"   : "  - {0} processes requiring reboot",
	"unsupported_distro" : ( "You are running unsupported linux distribution\n"
				"\n"
				"Please visit https://github.com/FrostyX/tracer/issues\n"
				"and create new issue called 'Unknown or unsupported linux distribution: {0} (v{1})' if there isn't such.\n"
				"\n"
				"Don't you have an GitHub account? Please report this issue on frostyx@email.cz" ),
	"path_not_found"     : ("Problem occurred - neither one of {0} paths doesn't exist\n"
				"Please contact maintainer of tracer package in your distribution."),
	"you_should_restart" : "You should restart:",
	"restart_using_helpers" : "* Some applications using:",
	"restart_manually"   : "* These applications manually:",
	"restart_session"    : "* These applications restarting your session:",
	"restart_rebooting"  : "* These applications rebooting your computer:",
	"for_more_informations": "For more information run:",
	"nothing_to_restart" : "Nothing needs to be restarted",
	"locked_database"    : "Package database is locked by another process",
	"database_permissions": "You can't open package database due to insufficient permissions",

	# Interactive
	"prompt_help"      : "Press application number for help or 'q' to quit",
	"press_enter"      : "-- Press enter to get list of applications --",
	"wrong_app_number" : "Wrong application number",

	# Helpers
	"app_not_running"   : "Application called {0} is not running",
	"not_known_restart" : "Sorry, It's not known",
	"session_restart"   : "You will have to log out & log in again",
	"static_restart"    : "You will have to reboot your computer",
	"affected_by"       : "Affected by",
	"how_to_restart"    : "How to restart",
	"helper"            : textwrap.dedent("""\
				* {app_name}
				    Package:     {pkg_name}
				    Description: {pkg_description}
				    Type:        {type}
				    State:       {app_name} has been started by {user} {time} ago. PID - {pid}
				    {affected_by}
				    How to restart:
				        {how_to_restart}
				"""),
	"affected_by_forbidden" : "You don't have enough permissions",
}
