from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()



def main():
    llm = ChatOpenAI(
        model="gemma3:27b",
        base_url="http://203.71.78.31:8000/v1",
        api_key="sk-12345678",
        temperature=0.0,
    )

    messages=[]
    messages.append(SystemMessage(content="""【語氣風格 / Tone & Style】
冷靜、專業、極簡、技術導向。不帶任何情感修飾，追求最高的邏輯嚴謹度。
將以下規格內容轉成 JSON物件"""))
    messages.append(HumanMessage(content=""" 【角色設定 / Role】
你是一位精通資安與資料工程的 「高階系統架構師 (Senior System Architect)」。你具備極強的文本邏輯分析能力，能從非結構化的產品文案中精準識別關鍵技術規格，並將其轉化為標準化的機器讀取格式。
【情境說明 / Context】
目前我們正在進行電競筆電產品線的資料庫自動化錄入工作。我會提供一段中文的產品描述文本，這段文本包含了處理器、記憶體、儲存空間等硬體資訊。我需要你充當中間層，將這些人類語言轉換為結構化的 JSON 物件，以便後續系統對接。
【任務目標 / Task】
請讀取下方的「原始規格文本」，執行以下操作：
提取關鍵參數：識別核心數、時脈、容量、硬碟協議等資訊。
分類分層：將硬體資訊歸類至 processor (處理器), memory (記憶體), storage (儲存) 等對應物件中。
轉換為 JSON：產出一個完整、符合語法規範的 JSON 物件。
【格式規範 / Format】
Key 命名：一律使用英文小駝峰式（lowerCamelCase），例如 coreCount, transmissionEfficiency。
Value 語言：數值與描述請保留原始文本中的中文與單位（如 "3.5GHz", "16GB", "八核心"）。
嚴格限制：輸出的結果僅限 JSON 代碼區塊。嚴禁任何開場白（例如「好的，這是你要的...」）或結尾說明。
【範例參考 / Few-shot Example】
輸入：具備 16GB 記憶體與 512GB SSD 硬碟。
輸出：
JSON
{
  "memory": { "size": "16GB" },
  "storage": { "capacity": "512GB", "type": "SSD" }
}
【語氣風格 / Tone & Style】
冷靜、專業、極簡、技術導向。不帶任何情感修飾，追求最高的邏輯嚴謹度。
將以下規格內容轉成 JSON物件:
    
    這款針對電競玩家與內容創作者設計的高性能筆電，
    核心運算單元採用八核心架構，其最高運作頻率可達 3.5GHz，
    在效能與功耗之間取得平衡。
    系統記憶體總容量為 16GB，可支援高強度多工處理與大型遊戲執行。
    儲存部分則配置一顆 1TB 容量的 NVMe 規格固態硬碟，
    相較於傳統 SATA SSD 具備更快的資料傳輸效率與更低的延遲表現。"""
    ))
    for chunk in llm.stream(messages):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    main()
