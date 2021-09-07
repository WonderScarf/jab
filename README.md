# Jab (Discord Bot)

### Description
A general discord bot using discord.py made around the end of summer 2020 with a wide variety of functions made as a way to learn Python. Can do things ranging from translating to role management to banning and kicking users. It also includes a few smaller things like a dice roller, message mimicry and reading from text files.

### Setup
To setup Jab you will need to downlaod a few things:
<ol>
  <li> Python, tested working on version 3.97 as of time of writing but has worked with older versions of 3 in the past. You can get it at: 
     <ul>
          <li> https://www.python.org/downloads/ </li>
     </ul>
    
  <li> The discord.py, googletrans and dotenv packages. You can find the most modern versions of them in these places: 
    <ul>
        <li> https://pypi.org/project/discord.py/ </li>
        <li> https://pypi.org/project/googletrans/ </li>
        <li> https://pypi.org/project/python-dotenv/ </li>
    </ul>
  </li>
  
  <li> Next download or clone the repository and lauch it with your IDE of choice (In this example I will use visual studio code )  </li>
  
  <li> After that you need to create a '.env' file (with that exact name) and place it at the same level as bot.py as it will be needed to run the use the discrod.py API. We need to fill this file with 2 values the bot's token and your user id.</li>

  <li>Since it is against the API's terms of sevrvice to use my own bot's token and my accounts id you will need to make your own. I won't explain how to make a discord profile as it should be easy to find a guide online which is far better explained then I can write.</li>

  <li>You also need to create your own bot for and as such need to use the discord dev portal to get it's key for use. Login to the discord developer portal at the link bellow and follow the video placed bellow that to create your bot. I recomend giving it administrator permisions but the rest is to you (it doesn't even need to be called Jab if you want). Get your new bot's TOKEN and your user id (there is a guide bellow of how to find it). 
      <ul>
        <li> https://discord.com/developers/ </li>
        <li> https://www.youtube.com/watch?v=b61kcgfOm_4</li>
        <li>https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID- </li>
    </ul>
  </li>

  <li>Take your two values and place them where the .env.example says (like the name states it's an example of the .env you will replicate). After you place the values where they are meant to be save the .env and open the press the run button while on the bot.py page. If you already invited your bot to the server it should apear online and some messages will apear in the terminal bellow.</li>
  
  <li>Now you can use the bot's commands with the prefix "?" without the brackets and a command right after. type ?help to get a list of commands and look in the files for descriptions, paramaters and other such things. </li>

</ol>

Sorry for the length of the guide but due to the discord.py's restrictions of using my own bot and the fact I don't have my own way of always hosting it means that we must go through many loops for it to run but on the bright side doing this means now you can make the bot do whatever you specifically want with a steady base full of examples. Anyways hope you have some fun with it!

