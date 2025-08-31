from dotenv import load_dotenv
from pathlib import Path
from config.paths import LOG_DIR,ensure_dirs
from config.constants import OPEN_QUES,FEED_QUES
from core.agent import Ask_AI
from core.executor import execTask
from utils.PLI import splitResponse
import os
import typer 
import random
import datetime
import traceback

load_dotenv()
ensure_dirs()

API_KEY = os.getenv("OPENROUTER_API_KEY")

agent = typer.Typer()

def Ask_toWrite(typer, temp):
    permission = typer.prompt("Agent> Do you want me to run this code? (yes/no)")
    if permission.strip().lower() == "yes":
        flag, msg = execTask(temp['code'])
        if flag:
            msg = "Agent> "+msg
            typer.echo(msg)
    else:
        typer.echo("just follow the given step to run the code")

@agent.command()
def run():
        quesAsked = False
        try:
            typer.echo("Welcome to AiAgent!")

            while True:
                if quesAsked:
                    ques = "\nAgent> "+random.choice(FEED_QUES)+" (yes / issue)"
                else:
                    ques = "\nAgent> "+random.choice(OPEN_QUES)
                    quesAsked = True

                task = typer.prompt(ques)

                if task.lower() in ['exit', 'quit']:
                    typer.echo("Exiting..")
                    typer.echo("Bye!")
                    break
                elif task == "yes" and quesAsked:
                    quesAsked = False
                    continue
                else:
                    flag,response = Ask_AI(task)
                    print(f"{response}")
                    if flag:
                        temp = splitResponse(response)
                        for i, j in temp.items():
                            typer.echo("\n")
                            if i.lower() == 'plan':
                                typer.echo("## This is the plan for the given task! ##")
                            elif i.lower() == 'code':
                                typer.echo("## This is the Code for the given task! ##")
                            else:
                                typer.echo("## How to run manually! ##")
                            typer.echo("\n")
                            if i.lower()=='code':
                                typer.echo(j['content'])
                            else:
                                typer.echo(j)
                            typer.echo("\n\n")
                            str1 = "_"*30
                            typer.echo(str1+"\n\n")

                        Ask_toWrite(typer,temp)
                        
        except Exception as e:
            logfile = LOG_DIR / 'log.txt'
            with open(logfile, 'a') as myfile:  # Append mode
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_trace = traceback.format_exc()  # Full traceback
                myfile.write(f"[{timestamp}] Error: {str(e)}\n")
                myfile.write(f"[{timestamp}] Traceback:\n{error_trace}\n")
                myfile.write(f"[{timestamp}] File Location: {__file__}\n")
                myfile.write("-" * 60 + "\n")


if __name__ == "__main__":
    agent()