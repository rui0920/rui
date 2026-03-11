from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()



def main():
    lim = ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
    reponse = lim.invoke("6")
    print(reponse.content)


if __name__ == "__main__":
    main()
