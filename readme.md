

# Final exam (June 2024; 103-2 Semester, Feng Chia University)

Friends 是 1994-2004 年盛行的美劇劇情，主要圍繞著一眾好友在紐約曼哈頓的生活展開。據估計在美國有 5110 萬人觀看了該劇的大結局。我們要做一個網站來介紹這個節目。下載此本版本，安裝執行; http://127.0.0.1:8000/seasons 會出現一個頁面，呈現 1-10 集的內容介紹

1. 目前點擊 HOME (http://127.0.0.1:8000) 會出現錯誤，請修正 urls.py 讓他導到 /seasons 的內容(30%)
2. 目前 models 中的 Cast 沒有提供男女性別與出生年（不用年月日）資料，請加上該資料，並在 /casts 上包含他們的姓名、出生年、簡介、照片等。（注意：性別應該用列舉的型態）。六個主角的資訊請參考 [wiki](https://en.wikipedia.org/wiki/Friends)。(30%)
3. 請修改 /seasons 列出季時，可以點擊該季呈現「該季」所有單集 (20%)
4. 目前 /seasons 列出的介紹都是文字，請修改其資料庫 (model), 使之可以在 admin 介面上傳照片，並在介紹頁可以呈現照片與文字。各季的代表照片放在 [season_img](episode/season_img) 下。(20%)


## new in browse
* next and previous of the episode