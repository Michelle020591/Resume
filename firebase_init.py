import os
import json
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
# https://console.firebase.google.com/u/0/project/resume-92e7b/firestore/databases/-default-/data/~2Fresume~2Fadvantage


# init
cred_json = os.environ.get("firebase_cred")
cred_dict = json.loads(cred_json)
cred = credentials.Certificate(cred_dict)
# cred = credentials.Certificate("firebase_cred.json")
firebase_admin.initialize_app(cred)

# connect to database
db = firestore.client()

def load_data():
    # store data
    ## contact 
    user_info = db.collection("resume").document("user_info")
    user_info.set({
        'user_info':[{
        'id': 1,
        'ch_name': '李宣葇',
        'en_name': 'Michelle Lee', 
        'email': 'mimilee2733@gmail.com', 
        'phone': '0972009925', 
        'github': 'https://github.com/Michelle020591',
        'address': '台北市大安區'
        }]

    }
    )

    ## education
    education = db.collection("resume").document("education")
    education.set({
        'education':[
        {
            'id': 1,
            'user_id': 1,
            'start_date': '20210901', 
            'end_date': '20240530', 
            'school': '台灣大學 生命科學系', 
            'class': '商管程式設計, 統計學, 行銷管理'
        },
        {
            'id': 2,
            'user_id': 1,
            'start_date': '20170901', 
            'end_date': '20200530', 
            'school': '中山女高',
            'class': ''
        }
    ]})

    ## skill
    skill = db.collection("resume").document("skill")
    skill.set({
        'skill':[
        {
            'id': 1,
            'category': '程式語言',
            'category_id': 1,
            'user_id': 1,
            'tools': 'Python、Excel (VBA)'
        },
        {
            'id': 2,
            'category': '資料庫',
            'category_id': 2,
            'user_id': 1,
            'tools': 'SQL Server'
        },
        {
            'id': 3,
            'category': '版本控制',
            'category_id': 3,
            'user_id': 1,
            'tools': 'Git'
        },
        {
            'id': 4,
            'category': '數位設計', 
            'category_id': 4,
            'user_id': 1,
            'tools': 'Figma、Notion、Procreate'
        }
        ]
    }
    )



    ## language
    language = db.collection("resume").document("language")
    language.set({
        'language': [
        {
        'id': 1,
        'user_id': 1,
        'category': '中文',
        'test': '母語'
        },
        {
        'id': 2,
        'user_id': 1,
        'category': '英文',
        'test': 'TOEIC 935分'      
        },
        {
        'id': 3,
        'user_id': 1,
        'category': '日文',
        'test': 'JLPT 180分'   
        }
        ]

    }
    )

    ## advantage
    advantage = db.collection("resume").document("advantage")
    advantage.set({
        'advantage': [
            {
                'id': 1,
                'user_id': 1,
                'advantage': '跨領域背景', 
                'description': '對新領域始終保持高度好奇心與學習熱忱。不受限生科系背景，曾任數據分析與自動化開發實習生，亦有準備財金所考試經驗，累積金融與科技的基礎知識與實務經驗，具備跨部門溝通與團隊協作能力。'
            },
            {
                'id': 2,
                'user_id': 1,
                'advantage': '程式與資料處理能力', 
                'description': '於 IT 組實習期間，熟悉用Python撰寫自動化腳本將資料匯入DB，並用SQL梳理大量數據，以Excel進行視覺化分析，提升團隊工作效率。'
            },
            {
                'id': 3,
                'user_id': 1,
                'advantage': '靈活運用 AI 工具', 
                'description': '善於活用 ChatGPT 加速自學與解決問題，並搭配 GitHub Copilot 輔助程式開發，提升開發效率與程式品質。'        
            },
            {
                'id': 4,
                'user_id': 1,
                'advantage': '語言能力佳', 
                'description': '英文聽說讀寫流利，能勝任跨國溝通與閱讀英文技術文件。'        
            }        
        ]
    }
    )


    ## experience
    experience = db.collection("resume").document("experience")
    experience.set({
        'experience':
        [
            {
            'id': 1,
            'user_id': 1,
            'company': 'TAROBO 證券投資顧問公司',
            'role': 'IT組 數據分析實習生',
            'start_date': '20230118',
            'end_date': '20240924',
            },
            {
            'id': 2,
            'user_id': 1,
            'company': '',
            'role': '美術家教 ＆ 數位插畫創作者',
            'start_date': '20220501',
            'end_date': '20250401'
            }
        ]
    })


    ## work skill
    work_skill = db.collection("resume").document("work_skill")
    work_skill.set({
        'work_skill': [
            {
                'id': 1,
                'exp_id': 1,
                'category': '具備基金相關知識',
                'description': '能操作 MorningStar、Bloomberg 等金融終端，獲取基金資料' 
            },
            {
                'id': 2,
                'exp_id': 1,
                'category': '使用 Python 開發爬蟲程式',
                'description': '定期蒐集 經濟部報告、Reddit 討論串、iPhone 配貨狀態等數據'
            },
            {
                'id': 3,
                'exp_id': 1,
                'category': '串接 Bloomberg API 與 Wind API',
                'description': '擷取金融數據'
            },
            {
                'id': 4,
                'exp_id': 1,
                'category': '熟悉 SQL CRUD操作及撰寫Store Procedure',
                'description': '以梳理大量資料'
            },
            {
                'id': 5,
                'exp_id': 1,
                'category': '善用 Excel (VBA)',
                'description': '將數據整理與可視化，提供每週報告，優化決策流程'
            },
            {
                'id': 6,
                'exp_id': 1,
                'category': '熟悉 Git版本控制',
                'description': '使用 branching workflow 進行程式開發與協作'
            },
            {
                'id': 7,
                'exp_id': 2,
                'category': '擔任美術家教',
                'description': '教授色鉛筆繪畫，指導基礎技法、構圖、色彩運用'
            },
            {
                'id': 8,
                'exp_id': 2,
                'category': '使用 Procreate',
                'description': '設計並上架 LINE 貼圖'
            }
        ]
    }
    )


    ## project
    project = db.collection("resume").document("project")
    project.set({
        'project': [
            {
                'id': 1,
                'title': '個人專案 履歷網站',
                'skill': '運用前端技術（HTML、CSS、JavaScript）',
                'description': '設計履歷網頁'
            },
            {
                'id': 2,
                'title': '個人專案 履歷網站',
                'skill': '了解UI/UX',
                'description': '並自己設計AI小助理的形象'
            },
            {
                'id': 3,
                'title': '個人專案 履歷網站',
                'skill': '運用Python建構Flask Server',
                'description': '結合Gemini建立自己的ChatBot（AI小助理），使用者可與其對話，詢問關於我的問題，並部署到GCP'
            }        
        ]
    })


    ## main classifier
    main_class = db.collection("resume").document("main_class")
    main_class.set({
        'main_class': [
            {'class_id': 1, 'classifier': '自我介紹、關於我、介紹一下自己', 'description': '我是宣葇，畢業於台灣大學生命科學系，具備跨領域學習與實作能力。曾任數據分析與自動化開發實習生，熟悉撰寫腳本、資料清理與視覺化分析，提升團隊效率與決策品質。具備財金背景與程式能力，能跨部門協作。平時善用 ChatGPT、GitHub Copilot 等 AI 工具自學與開發，提升產出效率與程式品質。英文流利，能閱讀技術文件並勝任跨國溝通，期望持續在科技與數據領域中精進成長。'},
            {'class_id': 2, 'classifier': '教育背景', 'description': '宣葇畢業於台灣大學生命科學系，大學期間積極選修跨領域課程，如：商管程式設計、統計學、行銷管理，並透過課外專案與實習累積實戰經驗，建立跨領域整合與應用的能力。同時也有準備一年財務金融研究所的經驗，具備基礎的金融知識。'},
            #{'class_id': 3, 'classifier': '應徵原因', 'description': ''},
            {'class_id': 4, 'classifier': '離開上一份工作原因、空窗期', 'description': '宣葇當時正在準備財金所考試，因此決定離開實習公司，專心備考，那段期間他學習統計學、經濟學、財務管理學以及計量經濟等學科，對於金融領域具備基礎的了解。'},
            {'class_id': 5, 'classifier': '技術技能', 'description': '宣葇具備扎實的程式與資料處理能力，擅長使用 Python（含 Selenium、BeautifulSoup）進行自動化與網頁爬蟲，曾於 IT 組實習中整合跨平台資料（如Bloomberg、Wind），也會用Flask打造履歷網站。具備前端基礎（HTML/CSS/JS），可設計互動網頁與 UI，亦能結合Procreate設計小助理角色，展現跨域整合力。精通 SQL 操作與資料視覺化，並具備 Excel VBA 自動報表實務經驗。具備基金相關知識，能操作 MorningStar、Bloomberg 等金融終端，獲取基金資料。熟悉 Git/GitHub 協作流程。善用AI：1.會用ChatGPT、Copilot等工具加速開發品質與學習速度2.結合Gemini API建立自己的ChatBot（AI小助理），使用者可與其對話，詢問關於他的問題。雲端平台：將履歷網頁部署到GCP(Google Cloud Platform)'},
            {'class_id': 6, 'classifier': '個人特質', 'description': '宣葇面對陌生領域，始終保持高度好奇心與自學動力，透過 ChatGPT、GitHub Copilot 等 AI 工具提升學習、開發速度，會主動學習與持續優化。個性細心且具責任感，能在壓力下穩定完成任務；能同理使用者與前端需求，強化跨領域整合能力。'},
            {'class_id': 7, 'classifier': '優點與缺點', 'description': '宣葇的優點是邏輯思維清晰，具備主動解決問題的能力。在實習期間，他負責自動化開發與跨平台資料整合，遇到技術挑戰時會主動查資料，並善用 AI 工具輔助學習與除錯，加快開發效率。缺點是目前的實戰經驗尚有限，仍有許多技術需要學習與精進。不過他具備快速學習與實作能力，能在短時間內掌握新工具並應用於實務。'},
            {'class_id': 8, 'classifier': '語言能力', 'description': '宣葇的語言能力如下：中文為母語，英文能力優異，具 TOEIC 935 分證照，能以英文進行日常溝通與閱讀技術文件。日文方面亦通過 JLPT N3，具備基礎閱讀與對話能力，能勝任多語環境下的資訊處理與國際資料查詢。'},
            {'class_id': 9, 'classifier': '經驗題，關鍵字：曾經、有沒有、過去、做過、遇過、描述分享等', 'description': '第二層分類「經驗」'},
            {'class_id': 10, 'classifier': '情境題，關鍵字：如果、假設、會怎麼等', 'description': '請根據面試者詢問的情境題，回答一個能讓面試者滿意的答案，100字以內。若要列點，請用米字號將標題標記出來，例如：**標題**'},
            {'class_id': 11, 'classifier': '工作方式與態度，例如：工作優先順序、分工', 'description': '宣葇重視清晰目標與合理分工，任務開始前會先釐清需求與時程，並依據緊急與重要程度安排優先順序，確保關鍵任務如期完成。遇到變動時，他會主動與同事協調，避免重工與資源浪費。團隊合作時，他習慣初期明確分工，過程中根據專長彈性調整。實習期間曾使用 GitHub 進行任務追蹤與進度同步，有效協助團隊準時交付成果。對他而言，良好的工作方式是在穩定交付的同時，持續優化流程並創造更高團隊價值。'},
            {'class_id': 12, 'classifier': '職涯規劃、未來目標', 'description': '宣葇期望在未來持續深化後端開發與資料處理能力，扎實掌握系統架構設計、資料庫效能優化與 API 開發等核心技術。短期目標是能在實務專案中累積經驗，獨立負責功能開發與問題排查，逐步成為團隊中穩定可靠的工程師。中長期希望能參與更大型或跨部門的系統整合專案，提升技術廣度與團隊協作能力。同時，他也會持續關注 AI、雲端技術的應用，並將其融入實務工作中，提升開發效率與產品價值。對他而言，工程師不僅是解決問題的人，更是連結使用者需求與技術實現的橋樑，他希望未來能成為具有系統思維與整合能力的關鍵人才。'},
            {'class_id': 13, 'classifier': '預期薪資', 'description': '宣葇希望薪資能依照市場行情與自身能力水平進行評估，對於具挑戰性與學習機會的職務有高度興趣，亦重視團隊文化與成長空間。可配合公司制度進行試用期與薪資調整機制。'},
            {'class_id': 14, 'classifier': '工作條件，例如：加班、工時、遠端工作等', 'description': '宣葇可以配合公司需求在必要時加班，尤其在專案緊湊或時程較吃緊的情況下，他會以完成任務為優先。不過他也重視效率與工作規劃，會盡可能在上班時間內完成工作，確保工作與生活的平衡。'},
            {'class_id': 15, 'classifier': '聯絡資訊', 'description': '詳細的聯絡方式請參見履歷中的「Contact」'},
            #{'class_id': 16, 'classifier': '其他面試', 'description': '目前確實有幾個正在進行的面試，不過他對貴公司的職務內容與團隊文化特別感興趣，這也是他最投入準備、最期待的機會之一。'},
            {'class_id': 17, 'classifier': '匯出履歷', 'description': '連結'},
            {'class_id': 18, 'classifier': '對軟體相關工作是否有興趣，想應徵軟體相關工作的原因', 'description': '宣葇過去在實習累積許多程式相關的技能以及興趣，對軟體相關工作感興趣。宣葇對於撰寫程式有興趣，他期待在實際專案中累積更多開發經驗，學習如何設計穩定的系統架構與優化資料流程。透過與資深工程師協作，不斷精進技術細節與開發思維，也希望在團隊合作與跨部門溝通中，培養更完整的軟體工程素養。'},
            {'class_id': 19, 'classifier': '對非軟體相關工作是否有興趣', 'description': '請回答：「這是一個有趣的問題，但宣葇沒有告訴我，歡迎填寫回饋表單，留下您的問題！」'},
            {'class_id': 0, 'classifier': '其他', 'description': '第二層分類「其他」'}
        ]
    })


    ## experience classifier
    exp_class = db.collection("resume").document("exp_class")
    exp_class.set({
        'exp_class': [
            {'class_id': 1, 'classifier': '犯錯/失敗/挫折', 'description': '宣葇在實習初期還不熟悉流程或技術，常常去詢問前輩們的建議和幫助，當時因為負責一項資料自動化任務，對內部系統與資料結構還不夠熟悉，初期嘗試時屢屢遇到錯誤，甚至花了大量時間 debug 卻找不到問題所在。後來主動請教前輩，學習他們處理問題的邏輯與方式，也搭配查資料與紀錄筆記，逐步建立起解決問題的系統流程。這段經驗讓他理解遇到困難時，與其一個人硬撐，不如有效地尋求協助，並將學到的知識轉化成未來的解決能力。', 'main_class_id': 9},
            {'class_id': 2, 'classifier': '壓力/緊急情況', 'description': '宣葇在實習時曾遇過臨時的資料需求，且時限很短。他會先確認對方的需求是否和他的認知相同，並且在腦中順過資料處理流程，調整工作的優先順序，最終準時交付成果。這次經驗讓他學會在高壓下保持冷靜、理清重點，並善用時間與工具提升效率，是他在後續工作中反覆應用的能力。', 'main_class_id': 9},
            {'class_id': 3, 'classifier': '主動行動', 'description': '宣葇在實習時發現每週資料整合流程繁瑣且人工處理容易出錯，於是主動設計一套自動化腳本，大幅減少處理時間。主管採納並推廣至整個團隊使用。這讓他體會到主動觀察、提出改善方案不只能幫助團隊，也能累積成就感與實戰經驗', 'main_class_id': 9},
            {'class_id': 4, 'classifier': '意見不合', 'description': '之前主管建議宣葇可以如何優化他的串接平台資料程式，他和主管說明他現在程式撰寫的方式和他的優點，而這似乎和主管的意見不合，經過討論之後，他認為主管的建議確實有道理，因此作調整', 'main_class_id': 9},
            {'class_id': 5, 'classifier': '溝通不良', 'description': '宣葇剛開始實習接到新任務時，沒有向需求方確認他的需求是否和他的理解一致，因此導致結果不如預期，不過幸好他提早完成任務並且回報，因此有時間再作修改，不過這件事情讓他學會在開始任務之前，一定要和對方溝通清楚，以免產生誤會', 'main_class_id': 9},
            {'class_id': 6, 'classifier': '團隊合作/團隊貢獻', 'description': '宣葇在實習期間，常常需要和其他的實習生合作完成專案，他們會先安排工作進度及分工，並時常向團隊回報工作進度，若有困難，會先嘗試自己解決，再不行會盡快向團隊提出，想辦法解決，目標是要產出一個品質良好、符合需求的程式。他認爲自己在團隊中的貢獻是，會想辦法用程式幫忙處理繁瑣的流程，提升團隊效率，他也時常會針對他的疑惑提出問題，讓大家一起思考是否有需要改進的地方。', 'main_class_id': 9},
            {'class_id': 7, 'classifier': '領導與被領導', 'description': '雖然宣葇沒有領導經驗，但是他認爲自己在團隊中非常的積極，例如：實習時接受資深工程師指導，學會主動提問，釐清對方的需求，讓合作更有效率。這讓他體認到無論角色如何，關鍵是如何有效達成共同目標。', 'main_class_id': 9},
            {'class_id': 8, 'classifier': '無法準時完成工作/達不到工作目標', 'description': '宣葇曾因低估資料清理難度，導致進度延誤。他立刻調整時程安排並主動向主管說明狀況，爭取額外支援並提出後續改進方法。雖未如期完成，但他從中學會如何誠實面對進度風險，並預留彈性處理變數，讓未來的時程預估更精準。', 'main_class_id': 9},
            {'class_id': 9, 'classifier': '沒有經驗卻必須完成的任務', 'description': '工作中宣葇最大的挑戰是面對不熟悉的技術時，仍需在短時間內上手並應用於專案。為此他訓練自己快速學習與查找資料的能力，善用 AI 工具與技術文件自學，並在實作中不斷修正與優化。同時也很感謝團隊中經驗豐富的工程師前輩，在他遇到卡關時給予實用的建議與回饋，讓他能持續成長。', 'main_class_id': 9},
            {'class_id': 10, 'classifier': '工作/任務內容與工作角色', 'description': '（一）操作MorningStar、Bloomberg 等金融網站，獲取基⾦相關資訊（二）使用python開發爬蟲程式，定期蒐集經濟部報告、Reddit討論串、iPhone配貨狀態等數據，提升資料處理效率；串接SQL和Wind API，減少查詢資料時間（三）熟練 SQL 資料庫操作，能獨立完成資料串接、CRUD 操作與報表視覺化，並擁有使用 Excel VBA 進行自動化報表製作的實務經驗（四）在版本控制方面，熟悉 Git/GitHub 與 branching workflow，具備協作式開發經驗（五）善於運用 ChatGPT、GitHub Copilot 等 AI 工具加速開發與除錯流程（六）亦有兩年以上美術家教經驗，能以條理清晰方式進行知識傳遞。', 'main_class_id': 9},
            {'class_id': 11, 'classifier': '專案內容', 'description': '（一）曾獨立開發履歷網站，使HTML/CSS/JavaScript 架設前端，並透過 Flask 架構後端伺服器，結合 Gemini 建立 AI 對話助手，提供互動式使用體驗。此專案展示他對 UI/UX 設計的興趣與全端開發能力，也運用 Google Cloud Platform 完成部署，具備實戰技能與自學能力。（二）串接不同平台數據，例如：Wind, Bloomberg。（三）網頁爬蟲開發，蒐集經濟部報告、Reddit 討論串、iPhone 配貨狀態等數據', 'main_class_id': 9},
            {'class_id': 12, 'classifier': '挑戰', 'description': '工作中宣葇最大的挑戰是面對不熟悉的技術時，仍需在短時間內上手並應用於專案。為此他訓練自己快速學習與查找資料的能力，善用 AI 工具與技術文件自學，並在實作中不斷修正與優化。同時也很感謝團隊中經驗豐富的工程師前輩，在他遇到卡關時給予實用的建議與回饋，讓他能持續成長。', 'main_class_id': 9},
            {'class_id': 13, 'classifier': '學習', 'description': '從工作與專案中，宣葇學會了許多學校課程之外的重要能力。舉例來說，在實習中參與跨平台資料整合與自動化腳本開發，讓他學會如何系統性分析問題、拆解需求，並選擇合適的技術解法。面對技術卡關時，他也養成了查詢文件、善用 AI 工具輔助學習的習慣，提升解決問題的效率。此外，他從團隊合作中學會清楚溝通與彈性協作，透過使用 GitHub 等工具進行版本管理與任務追蹤，提升了專案的可控性與透明度。這些經驗讓他更具備實務能力，也建立了自學與持續成長的習慣。', 'main_class_id': 9},
            {'class_id': 0, 'classifier': '其他', 'description': '抱歉，目前還沒有相關的經驗～但您可以問他，如果今天發生這樣的事情，宣葇會如何處理', 'main_class_id': 9}
        ]
    })



    ## else classifier
    else_class = db.collection("resume").document("else_class")
    else_class.set({
        'else_class': [
            {'class_id': 1, 'classifier': '屬於HR/面試官會問的問題且和職位、公司、工作、個人意願有關，', 'description': '請回答：「這是一個有趣的問題，但宣葇沒有告訴我，歡迎填寫回饋表單，留下您的問題！」'},
            {'class_id': 2, 'classifier': '屬於HR/面試官會問的問題且和職位、公司、工作、個人意願無關，例：嗨、你好', 'description': '請簡單回覆'},
            {'class_id': 3, 'classifier': '其他', 'description': '請強調你是宣葇的AI小助手，並引導使用者問跟宣葇或工作相關的問題'}
        ]
    })




    print('Done! Successfully Store Data!')

#與履歷或應徵工作有關，例如：你對我們公司有什麼了解
if __name__ == "__main__":
    load_data()