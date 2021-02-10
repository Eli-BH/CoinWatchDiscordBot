<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/kTmv71j.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Coin Watch Discord Bot</h3>


---

<p align="center"> 🤖 Few lines describing what your bot does.
    <br> 
    The bot allows the user to query in discord for the price and the 24hr value change of most crypto-currencies. 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About <a name = "about"></a>](#-about-)
- [💭 How it works <a name = "working"></a>](#-how-it-works-)
- [🎈 Usage <a name = "usage"></a>](#-usage-)
  - [Example:](#example)
- [🏁 Getting Started <a name = "getting_started"></a>](#-getting-started-)
- [⛏️ Built Using <a name = "built_using"></a>](#️-built-using-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)
- [🎉 Acknowledgements <a name = "acknowledgement"></a>](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

The bot is primarily hosted using a flask web server and is being kept alive on repl.it by constant pings to the web server. 
The bot works by being invited into a discord server, it will them be automatically started up and will listen for commands that start
withe '%' character. The bot can tell the current price of the queried crypto currency and the percentage change for the last 24 hours. 


## 💭 How it works <a name = "working"></a>

The bot constantly listens for commands, and responds if the query starts with '%'. 
The queries are used to search using the Coingecko API which supplies the information of the crypto currency in question. 

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:

```
%price 'coin name'
```
The bot will then give you the price of the coin.

```
%change 'coin name'
```

The bot will then give you the percentage change of the coin for the last 24 hours.

### Example:

> %price bitcoin

**Price:**
The price of Bitcoin is $46,000.43


## 🏁 Getting Started <a name = "getting_started"></a>

Go to: [CoinWatch](https://discord.com/api/oauth2/authorize?client_id=808737231081701436&permissions=519232&scope=bot)
And add the bot to your server.


## ⛏️ Built Using <a name = "built_using"></a>

- [Repl](https://www.Repl.it/) - Online Code editor

## ✍️ Authors <a name = "authors"></a>

- [@EliBH](https://github.com/Eli-BH) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- FreeCodeCamp for great starter guides [FreeCodeCamp](https://www.freecodecamp.org/)
