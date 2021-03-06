#!/usr/bin/python
# This source file is part of Obozrenie
# Copyright 2015 Artem Vorotnikov

# For more information, see https://github.com/obozrenie/obozrenie

# Obozrenie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.

# Obozrenie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Obozrenie.  If not, see <http://www.gnu.org/licenses/>.


import json
import unittest
import xmltodict

from obozrenie import helpers, adapters, i18n, launch


class HelpersTests(unittest.TestCase):
    """Tests for helpers"""
    module = helpers
    @classmethod
    def unit_dict_to_list(cls):
        """Does helper convert dict table into a list table based on specified format correctly?"""
        spec_dict_table = [{'a': 'A1', 'b': 'B1', 'c': 'C1', 'd': 'D1', 'e': 'E1'}, {'d': 'D2', 'e': 'E2', 'a': 'A2'}]
        spec_key_list = ('a',
                         'e',
                         'd')

        func = cls.module.dict_to_list
        spec_args = {'dict_table': spec_dict_table, 'key_list': spec_key_list}
        spec_result = [['A1', 'E1', 'D1'], ['A2', 'E2', 'D2']]

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_dict_to_list(self):
        unit = self.unit_dict_to_list()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_flatten_dict_table(cls):
        """Does helper flatten dict based on specified format correctly?"""
        spec_dict_table = {'lead1': {'a': 'A1', 'b': 'B1', 'c': 'C1', 'd': 'D1', 'e': 'E1'}, 'lead2': {'a': 'A2', 'b': 'B2'}}
        spec_leading_key_spec = 'leading key'

        func = cls.module.flatten_dict_table
        spec_args = {'dict_table': spec_dict_table, 'leading_key_spec': spec_leading_key_spec}
        spec_result = [{'leading key': 'lead1', 'a': 'A1', 'b': 'B1', 'c': 'C1', 'd': 'D1', 'e': 'E1'}, {'leading key': 'lead2', 'a': 'A2', 'b': 'B2'}]

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_flatten_dict_table(self):
        unit = self.unit_flatten_dict_table()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_flatten_list(cls):
        """Does helper flatten list of iterable objects based on specified format correctly?"""
        spec_nested_list = ['a', ['b', ['c', 'd'], 'e'], 'f']

        func = cls.module.flatten_list
        spec_args = {'nested_list': spec_nested_list}
        spec_result = ['a', 'b', 'c', 'd', 'e', 'f']

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_flatten_list(self):
        unit = self.unit_flatten_list()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_sort_dict_table(cls):
        """Checks how helper function sorts dictionary tables"""
        spec_dict_table = [{'name': 'Olga', 'age': 32, 'gender': 'F'}, {'name': 'Marina', 'age': 25, 'gender': 'F'}, {'name': 'Nikolai', 'age': 40, 'gender': 'M'}]
        spec_sort_key = 'name'

        func = cls.module.sort_dict_table
        spec_args = {'dict_table': spec_dict_table, 'sort_key': spec_sort_key}
        spec_result = [{'name': 'Marina', 'age': 25, 'gender': 'F'}, {'name': 'Nikolai', 'age': 40, 'gender': 'M'}, {'name': 'Olga', 'age': 32, 'gender': 'F'}]

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_sort_dict_table(self):
        unit = self.unit_sort_dict_table()
        self.assertTrue(unit['expectation'] == unit['result'])


class LauncherTests(unittest.TestCase):
    module = launch
    """Tests for launcher"""
    @classmethod
    def unit_steam_launch_pattern(cls):
        """Check Steam launch pattern"""
        func = cls.module.steam_launch_pattern
        spec_args = {'game_settings': {'steam_path': 'steam'}, 'steam_app_id': '12345', 'host': 'localhost', 'port': '27960', 'password': 'abracadabra'}
        spec_result = ['steam', '-applaunch', '12345', '+connect', 'localhost:27960', '+password', 'abracadabra']

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_steam_launch_pattern(self):
        unit = self.unit_steam_launch_pattern()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_quake_launch_pattern(cls):
        """Check Quake launch pattern"""
        func = cls.module.quake_launch_pattern
        spec_args = {'path': 'quake', 'host': 'localhost', 'port': '27960', 'password': 'abracadabra'}
        spec_result = ['quake', '+connect', 'localhost:27960', '+password', 'abracadabra']

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_quake_launch_pattern(self):
        unit = self.unit_quake_launch_pattern()
        self.assertTrue(unit['expectation'] == unit['result'])


class MinetestTests(unittest.TestCase):
    """Tests for minetest"""
    module = adapters.minetest
    @classmethod
    def unit_minetest_parse(cls):
        """Check Minetest backend parsing"""
        json_string = '{"ping": 0.09202814102172852, "clients_list": ["PlayerA", "PlayerB", "PlayerC"], "version": "0.4.13", "creative": false, "proto_max": 26, "total_clients": 807, "proto_min": 13, "pvp": true, "damage": true, "mapgen": "v7", "privs": "interact, shout, home", "address": "game.minetest-france.fr", "update_time": 1447351523.4476626, "uptime": 21600, "mods": ["potions", "item_drop", "irc", "irc_commands", "hudbars", "mana", "essentials_mmo", "efori", "denaid", "areas_gui", "areas", "worldedit", "worldedit_infinity", "worldedit_commands", "worldedit_shortcommands", "sethome", "screwdriver", "fire", "dye", "default", "mobs", "essentials", "encyclopedia", "economy", "xpanes", "wool", "farming", "stairs", "beds", "vessels", "tnt", "give_initial_stuff", "flowers", "doors", "creative", "unified_inventory", "u_skins", "worldedit_gui", "3d_armor", "hbarmor", "wieldview", "shields", "bucket", "hbhunger", "bones", "boats"], "rollback": false, "password": false, "game_time": 13680891, "lag": 0.1009900271892548, "description": "Serveur Survie / PvP", "can_see_far_names": false, "port": 30001, "start": 1447333508.1709588, "pop_v": 13.229508196721312, "clients_max": 50, "updates": 61, "name": "My Little Server", "url": "http://my-minetest-server.com", "clients_top": 23, "gameid": "minetest", "clients": 3, "dedicated": true, "ip": "12.34.56.789"}'
        json_result = {'password': False, 'host': '12.34.56.789:30001', 'player_count': 3, 'player_limit': 26, 'name': 'My Little Server', 'game_type': 'minetest', 'terrain': '', 'secure': False, 'rules': {}, 'players': [{'name': 'PlayerA'}, {'name': 'PlayerB'}, {'name': 'PlayerC'}]}

        func = cls.module.parse_json_entry
        spec_args = {"entry": json.loads(json_string)}
        spec_result = json_result

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_minetest_parse(self):
        unit = self.unit_minetest_parse()
        self.assertTrue(unit['expectation'] == unit['result'])


class QStatTests(unittest.TestCase):
    """Tests for QStat backend"""
    module = adapters.qstat
    @classmethod
    def unit_parse_master_entry(cls):
        """Check QStat output parsing - masters"""
        xml_string = '<server type="Q2M" address="localhost:12345" status="UP" servers="44"></server>'

        func = cls.module.adapt_qstat_entry
        spec_args = {"qstat_entry": xmltodict.parse(xml_string)['server'], "game": "q2", "master_type": "Q2M", "server_type": "Q2S"}
        spec_result = {'server_dict': None, 'debug_msg': i18n._('Queried Master. Address: localhost:12345, status: UP, server count: 44.')}

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_parse_master_entry(self):
        unit = self.unit_parse_master_entry()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_parse_server_entry(cls):
        """Check QStat output parsing - masters"""
        xml_string = '<server type="Q2S" address="localhost:12345" status="UP"><hostname>localhost</hostname><name>Gandalfehtgreen&apos;s Casino (R.I.P.)</name><gametype>action</gametype><map>locknload</map><numplayers>0</numplayers><maxplayers>15</maxplayers><numspectators>0</numspectators><maxspectators>0</maxspectators><ping>1126</ping><retries>1</retries><rules><rule name="*Q2Admin">2.0~3a63381</rule><rule name="actionversion">TNG 2.81~d504f0d</rule><rule name="allitem">0</rule><rule name="allweapon">0</rule><rule name="capturelimit">0</rule><rule name="cheats">0</rule><rule name="ctf">0</rule><rule name="deathmatch">1</rule><rule name="dmflags">8</rule><rule name="fraglimit">0</rule><rule name="game">action</rule><rule name="gamedate">Sep 15 2013</rule><rule name="gamedir">action</rule><rule name="gamename">action</rule><rule name="items">1</rule><rule name="matchmode">0</rule><rule name="needpass">0</rule><rule name="port">12345</rule><rule name="protocol">34</rule><rule name="q2a_mvd">1.6hau</rule><rule name="roundlimit">15</rule><rule name="roundtimelimit">5</rule><rule name="t1">0</rule><rule name="t2">0</rule><rule name="t3">0</rule><rule name="teamplay">1</rule><rule name="tgren">1</rule><rule name="timelimit">60</rule><rule name="use_3teams">0</rule><rule name="use_classic">0</rule><rule name="use_tourney">0</rule><rule name="uptime">297+0:09.46</rule></rules><players><player><name>PlayerA</name><score>0</score><ping>3</ping></player><player><name>PlayerB</name><score>0</score><ping>4</ping></player><player><name>PlayerC</name><score>0</score><ping>5</ping></player></players></server>'

        spec_server_dict = {'game_name': 'action', 'password': False, 'game_mod': '', 'player_count': 0, 'secure': False, 'ping': 1126, 'rules': {'gamedir': 'action', 'needpass': '0', 'uptime': '297+0:09.46', 'use_classic': '0', 'timelimit': '60', 'capturelimit': '0', 'game': 'action', 'tgren': '1', 'actionversion': 'TNG 2.81~d504f0d', 'allitem': '0', 'use_tourney': '0', 't1': '0', 'protocol': '34', 'port': '12345', 'cheats': '0', 'ctf': '0', 'deathmatch': '1', 'q2a_mvd': '1.6hau', '*Q2Admin': '2.0~3a63381', 'teamplay': '1', 'use_3teams': '0', 'gamedate': 'Sep 15 2013', 't2': '0', 'fraglimit': '0', 'matchmode': '0', 'dmflags': '8', 'allweapon': '0', 'roundlimit': '15', 'gamename': 'action', 'roundtimelimit': '5', 'items': '1', 't3': '0'}, 'players': [{'name': 'PlayerA', 'ping': 3, 'score': 0}, {'name': 'PlayerB', 'ping': 4, 'score': 0}, {'name': 'PlayerC', 'ping': 5, 'score': 0}], 'name': "Gandalfehtgreen's Casino (R.I.P.)", 'player_limit': 15, 'host': 'localhost', 'game_type': 'action', 'game_id': 'q2', 'terrain': 'locknload'}
        spec_debug_msg = None

        func = adapters.qstat.adapt_qstat_entry
        spec_args = {"qstat_entry": xmltodict.parse(xml_string)['server'], "game": "q2", "master_type": "Q2M", "server_type": "Q2S"}
        spec_result = {'server_dict': spec_server_dict, 'debug_msg': spec_debug_msg}

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_parse_server_entry(self):
        unit = self.unit_parse_server_entry()
        self.assertTrue(unit['expectation'] == unit['result'])


class RigsofrodsTests(unittest.TestCase):
    module = adapters.rigsofrods
    @classmethod
    def unit_parse_server_entry(cls):
        spec_entry = [{'#text': '1 / 10', '@valign': 'middle'},
                      {'#text': 'password', '@valign': 'middle'},
                      {'@valign': 'middle', 'a': {'#text': 'My Little Server', '@href': 'rorserver://user:pass@localhost:12345/'}},
                      {'#text': 'any', '@valign': 'middle'}]
        spec_server_dict = {'player_count': 1, 'player_limit': 10, 'password': True, 'host': 'localhost:12345', 'name': 'My Little Server', 'terrain': 'any'}

        func = cls.module.parse_server_entry
        spec_args = {'entry': spec_entry}
        spec_result = spec_server_dict

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_parse_server_entry(self):
        unit = self.unit_parse_server_entry()
        self.assertTrue(unit['expectation'] == unit['result'])

    @classmethod
    def unit_adapt_server_list(cls):
        spec_html_string = "<table border='1'><tr><td><b>Players</b></td><td><b>Type</b></td><td><b>Name</b></td><td><b>Terrain</b></td></tr><tr><td valign='middle'>3 / 16</td><td valign='middle'>password</td><td valign='middle'><a href='rorserver://localhost:12345/'>My Little Server 1</a></td><td valign='middle'>Terrain A</td></tr><tr><td valign='middle'>1 / 9</td><td valign='middle'></td><td valign='middle'><a href='rorserver://localhost:54321/'>My Little Server 2</a></td><td valign='middle'>Terrain B</td></tr></table>"
        spec_server_list = [{'player_count': 3, 'player_limit': 16, 'password': True, 'secure': False, 'game_id': 'rigsofrods', 'game_type': 'rigsofrods', 'host': 'localhost:12345', 'name': 'My Little Server 1', 'terrain': 'Terrain A'},
                            {'player_count': 1, 'player_limit': 9, 'password': False, 'secure': False, 'game_id': 'rigsofrods', 'game_type': 'rigsofrods', 'host': 'localhost:54321', 'name': 'My Little Server 2', 'terrain': 'Terrain B'}]
        spec_game = 'rigsofrods'

        func = cls.module.adapt_server_list
        spec_args = {'game': spec_game, 'html_string': spec_html_string}
        spec_result = spec_server_list

        result = func(**spec_args)
        return {'expectation': spec_result, 'result': result}

    def test_parse_server_entry(self):
        unit = self.unit_adapt_server_list()
        self.assertTrue(unit['expectation'] == unit['result'])


if __name__ == "__main__":
    unittest.main()
