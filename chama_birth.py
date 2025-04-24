from dotenv import load_dotenv
import os
from openai import OpenAI
import json

def model_response(conversation_history):

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
   
    response = client.responses.create(
        model="gpt-4.1-nano",
        input= conversation_history
    )

    return response.output_text

def user_history_manager(usrID, usrMessage):

    with open("behaviour_prompt_I.txt", "r") as bPrompt:
        behaviour_prompt = bPrompt.read()

    conversation_start = [
        {
            "role": "developer",
            "content": behaviour_prompt
        },
        {
            "role": "user",
            "content": "se apresente, diga quem é você e o que você faz."
        }
    ]


    try:
        with open("usrids.json", "r", encoding="utf-8") as idsJson:
            usrIDs_convDict = json.load(idsJson)
            
            if usrID in usrIDs_convDict.keys():
                conversation_history = usrIDs_convDict[usrID]
    
                return conversation_history
            else:
                
    except Exception as e:
        print("Sem arquivos para históricos de conversas", "\n", f"{e}")

        usrIDs_convDict = {usrID:conversation_start}

        with open("usrids.json", "w", encoding="utf-8") as idsjson:
            json.dump(usrIDs_convDict, idsjson, indent=4, ensure_ascii=False)



def main():

    with open("behaviour_prompt_I.txt", "r") as bPrompt:
        behaviour_prompt = bPrompt.read()

    conversation_history = [
        {
            "role": "developer",
            "content": behaviour_prompt
        },
        {
            "role": "user",
            "content": "se apresente, diga quem é você e o que você faz."
        }
    ]

    print("Este é um loop infinito de conversação, para sair digite: quit", "\n")

    assistant_welcoming = model_response(conversation_history)

    conversation_history.append({"role":"assistant", "content": assistant_welcoming})

    print(f"{conversation_history[2]["content"]}","\n")

    while True:

        most_recent_user_prompt = input("User: ")

        if most_recent_user_prompt == "quit":
            
            with open("conversation_histoy.json", "w", encoding="utf-8") as hFile:
                json.dump(conversation_history, hFile, indent=4, ensure_ascii=False) 

            break

        most_recent_user_state = {"role": "user", "content": most_recent_user_prompt}
        
        conversation_history.append(most_recent_user_state)
        
        most_recent_model_state = {"role": "assistant", "content": model_response(conversation_history)}

        conversation_history.append(most_recent_model_state)
        print("\n")
        print(f"Assistant: {most_recent_model_state["content"]}", "\n")

if __name__ == "__main__":
    main()

