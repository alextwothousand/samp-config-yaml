SA-MP 0.3 Server Setup
----------------------

Once the configuration is complete, run samp.py to
launch the server process.

CONFIGURATION:

Example server.yml:
	echo: Executing Server Config...
	lanmode: 0
	rcon: 0
	rcon_password: changeme
	maxplayers: 50
	port: 7777
	hostname: SA-MP 0.3 Server
	gamemodes:
	- bare
	filterscripts:
	- vspawner
	announce: 0
	chatlogging: 0
	weburl: www.sa-mp.com
	onfoot_rate: 40
	incar_rate: 40
	weapon_rate: 40
	stream_distance: 300.0
	stream_rate: 1000
	maxnpc: 0
	logtimeformat: "[%H:%M:%S]"
	language: English
	mapname: San Andreas

To configure the server, you must edit the values in server.yml. They are explained below:
Note: More can be found on the SA-MP wiki or around the net.

hostname
--------
	Parameters:
		string
	
	Description:
		Specifies the hostname shown in the server browser
		
port
----
	Parameters:
		int
	
	Description:
		Specifies the port to listen on.
		This port is used for game connections, rcon connections, and for querying.
	
maxplayers
----------
	Parameters:
		int
	
	Description:
		Specifies the maximum amount of players.
		
announce
-------
	Parameters:
		int (0 or 1)
		
	Description:
		Announces your server to the 'Internet' server list in the SA:MP browser. On (1) or Off (0).

weburl
------
	Parameters:
		string
	
	Description:
		Specifies the URL shown in the server browser, which is associated to the server.
		
rcon_password
-------------
	Parameters:
		string
		
	Description:
		Specifies the password needed to connect to rcon, or login to rcon ingame.
		
gamemode0 - gamemode15
----------------------
	Parameters:
		string
		int
		
	Description:
		Specifies the rotation settings. The first parameter sets the game mode name. The second is the number of times it will repeat.
		You can use gamemode0 to specify the first gamemode, gamemode1 to specify the second, etc.
