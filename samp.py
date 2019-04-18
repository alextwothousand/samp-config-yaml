import yaml
from os import path, remove, system, name

def program():
    with open("server.yml", 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            print(config)
            
        except yaml.YAMLError:
            print("server.yml was unable to be loaded. Maybe it's not been created?")

    if path.exists("server.cfg"):
        remove("server.cfg")

    with open("server.cfg", 'w') as f:
        try:
            f.write("echo {}\n".format(config['echo']))
        except KeyError:
            print('echo does not exist! Using default...')
            f.write("echo 0\n")

        try:
            f.write("lanmode {}\n".format(config['lanmode']))
        except KeyError:
            print('lanmode does not exist! Using default...')
            f.write("lanmode 0\n")

        try:
            f.write("rcon {}\n".format(config['rcon']))
        except KeyError:
            print('rcon does not exist! Using default...')
            f.write('rcon 0\n')

        try:
            f.write("rcon_password {}\n".format(config['rcon_password']))
        except KeyError:
            print('rcon_password does not exist! Using default...')
            f.write("rcon_password changeme\n")

        try:
            f.write("maxplayers {}\n".format(config['maxplayers']))
        except KeyError:
            print('maxplayers does not exist! Using default...')
            f.write("maxplayers 50\n")

        try:
            f.write("port {}\n".format(config['port']))
        except KeyError:
            print('port does not exist! Using default...')
            f.write("port 7777\n")

        try:
            f.write("hostname {}\n".format(config['hostname']))
        except KeyError:
            print('hostname does not exist! Using default...')
            f.write("hostname SA-MP 0.3 Server\n")
            
        try:
            #f.write("lanmode {}\n".format(config['lanmode']))
            count = 0
            f.write("gamemode0 ")

            for gamemode in config['gamemodes']:
                f.write("{} {} ".format(gamemode, count))
                count += 1

            f.write("\n")
        except KeyError:
            print('gamemodes do not exist! Using default...')
            f.write("bare 1\n")

        f.write("filterscripts ")
        try:
            for filterscript in config['filterscripts']:
                f.write("{} ".format(filterscript))
            f.write("\n")
        except KeyError:
            print('filterscripts do not exist! Using default...')
            f.write("\n")

        f.write("plugins ")
        try:
            if name == 'nt':
                for plugin in config['plugins']:
                    if '.dll' in plugin:
                        f.write("{} ".format(plugin))
                    else:
                        f.write("{}.dll ".format(plugin))
            elif name == 'posix':
                for plugin in config['plugins']:
                    if '.so' in plugin:
                        f.write("{} ".format(plugin))
                    else:
                        f.write("{}.so ".format(plugin))
            f.write("\n")
        except KeyError:
            print('plugins does not exist! Using default...')
            f.write("\n")

        try:
            f.write("announce {}\n".format(config['announce']))
        except KeyError:
            print('announce does not exist! Using default...')
            f.write('announce 0\n')

        try:
            f.write("chatlogging {}\n".format(config['chatlogging']))
        except KeyError:
            print('chatlogging does not exist! Using default...')
            f.write("chatlogging 0\n")

        try:
            f.write("weburl {}\n".format(config['weburl']))
        except KeyError:
            print('weburl does not exist! Using default...')
            f.write("weburl www.sa-mp.com\n")

        try:
            f.write("onfoot_rate {}\n".format(config['onfoot_rate']))
        except KeyError:
            print('onfoot_rate does not exist! Using default...')
            f.write("onfoot_rate 40\n")

        try:
            f.write("incar_rate {}\n".format(config['incar_rate']))
        except KeyError:
            print('incar_rate does not exist! Using default...')
            f.write("incar_rate 40\n")

        try:
            f.write("weapon_rate {}\n".format(config['weapon_rate']))
        except KeyError:
            print('weapon_rate does not exist! Using default...')
            f.write("weapon_rate 40\n")

        try:
            f.write("stream_distance {}\n".format(config['stream_distance']))
        except KeyError:
            print('stream_distance does not exist! Using default...')
            f.write("stream_distance 300.0\n")

        try:
            f.write("stream_rate {}\n".format(config['stream_rate']))
        except KeyError:
            print('stream_rate does not exist! Using default...')
            f.write("stream_rate 1000\n")

        try:
            f.write("maxnpc {}\n".format(config['maxnpc']))
        except KeyError:
            print('maxnpc does not exist! Using default...')
            f.write("maxnpc 0\n")

        try: 
            f.write("logtimeformat {}\n".format(config['logtimeformat']))
        except KeyError:
            print('logtimeformat does not exist! Using default...')
            f.write('logtimeformat [%H:%M:%S]\n')

        try:
            f.write("language {}\n".format(config['language']))
        except KeyError:
            print('language does not exist! Using default...')
            f.write('language English\n')

        try:
            f.write("mapname {}\n".format(config['mapname']))
        except KeyError:
            print('mapname does not exist! Using default...')
            f.write('mapname San Andreas\n')

        try:
            f.write("db_logging {}\n".format(config['db_logging']))
        except KeyError:
            print('db_logging does not exist! Using default...')
            f.write('db_logging 0\n')

        try:
            f.write("db_log_queries {}\n".format(config['db_log_queries']))
        except KeyError:
            print('db_log_queries does not exist! Using default...')
            f.write('db_log_queries 0\n')

        try:
            f.write("db_log_queries {}\n".format(config['db_log_queries']))
        except KeyError:
            print('db_log_queries does not exist! Using default...')
            f.write('db_log_queries 0\n')

        try:
            f.write("timestamp {}\n".format(config['timestamp']))
        except KeyError:
            print('timestamp does not exist! Using default...')
            f.write('timestamp 1\n')

        try:
            f.write("discord_bot_token {}\n".format(config['discord_bot_token']))
        except KeyError:
            print('No bot token! Continuing without...')

    print("\n\n")
    system('samp-server.exe')
    remove('server.cfg')

program()