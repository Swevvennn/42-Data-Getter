_This project is made as a personnal project by swevvenn, or mosmond for the 42 network_

# 42 Data Getter
## Description
This project is an API caller that cache recents results and print them formatted depending of the desired data asked.

It's made fully in python by hand and for the use of tutors.

`uv` is used as package manager so make sure you have installed it before running. 

The goal of this project was to be able to get the data of the Pisciner during the piscine of july 2026 in 42 Le Havre.

## Usage
> First things first, let's setup the tool, just make sure that you have a /tmp available and then:
```bash
make setup
```
> After that you can check all the rules available in the makefile or check all the commands that the CLI take with:
```bash
make run # press q to quit
```
> Then don't forget to put your API keys in the `.env` file before running any other `make` rule.
>> If you're still having issue, check on your intra if your secret key hasn't changed.

> Finally, when you're done of working you can do a little
```bash
make clean
```
> To clean all the python cache and the virtual env made for the run of the tool, it will free some space without making you lose too much time.
> Next time you want to use the tool, just make to install the virtual env before running
```bash
make install
```
### :warning: DO NOT RUN `make fclean` UNINTENTIONALLY
> It will remove all the cached data and the .env file, making you forced to do all the setup again and to wait for all the API call instead of saving time by taking cached data. 

## Ressources

- Loading bars: `tqdm` => [doc](https://tqdm.github.io/)
- API: 42's API => [doc](https://api.intra.42.fr/apidoc)

### AI Usage
AI was used to help improving the tool by providing dependencies that helped improving the tool, such as `rich` for the print coloration.  
