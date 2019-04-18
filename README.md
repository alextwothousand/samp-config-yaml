# samp-config-yaml
SAMP now loads configs from server.yml instead of server.cfg! Perfect if you're absolutely done with how absurdly ugly server.cfg looks.

### How is this meant to be useful to me?
Probably won't be. Though, if you're a YAML lover or you just want a way of having a much neater server.cfg then this is the way to go.

### Okay, but does this support maddinator's discord connector?
Actually, yes it does! All you have to do, is add `discord_bot_token: YOUR_TOKEN_HERE` and samp-config-yaml will go ahead and load it in for you!

### What if there is a specific config that this doesn't support and I desperately need it?
Open up a issue! I am usually active most times of the day and I will work on implementing and testing it as soon as possible.

### Do you have a server package I can use to get me going right away?
Yep! Just `git clone https://github.com/infin1tyy/samp-config-yaml.git`/git clone this repository and you've got your server package. This is R2-2 though so if you want DL you'll have to update your server executables. In future, I will write an alternative to artconfig.txt that is YAML based.

### Ugh, but I don't really want to run a python file. Do you have any alternatives?
Unfortunately not, for the time being. I plan on either bringing out a .NET alternative or compiling the .py file as a .exe in the near future. For the time being, you should install Python (recommended version would be 3.7.3 from here > https://www.python.org/downloads/release/python-373/), then run `pip install pyyaml` in your terminal. That's all you need to get this going!
