# Twitter-Bot

This project uses https://repl.it and https://uptimerobot.com to create a Twitter Bot that is always running. You need these accounts as well as a Twitter account with API access to get started.

The python code is set for 1 keyword to search for and retweet, every 5 minutes. It will not retweet the same thing twice. This can always be changed to more then 1 keyword, or tweet however fast or slow you want. Twitter may block your API access if you abuse this feature. 

You can check out my bot here: https://twitter.com/btcbot9


Once you have your Twitter API, go ahead and upload main.py and keep_alive.py onto repl.it..

You then need to add your API key and access token to main.py on line 6 and 7

Run the file.

In the right hand side of the screen you will be given a URL from repl.it with your project name, this is needed for https://uptimerobot.com
On https://uptimerobot.com, add a new monitor. Choose HTTP(s), give it a name, and post your URL. You can choose the amount of time you want the server to ping that URL but I just kept it set at 5 minutes. Create monitor. 




